# from django.shortcuts import render


# # Create your views here.
# from django.http import JsonResponse
# def list_pizzas(request):
#     pizzas = [
#         {'id': 1, 'name': 'Margherita', 'ingredientes': ['Tomate', 'Mussarela', 'Manjericão']},
#         {'id': 2, 'name': 'Pepperoni', 'ingredientes': ['Pepperoni', 'Queijo']},
#         {'id': 3, 'name': 'Vegetariana', 'ingredientes': ['Tomate', 'Mussarela', 'Cogumelos', 'Espinafre']},
#     ]
#     return JsonResponse(pizzas, safe=False)
# aplicacao/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Dados estáticos para simular um banco de dados
pizzas = [
    {'id': 1, 'name': 'Margherita', 'ingredientes': ['Tomate', 'Mussarela', 'Manjericão']},
    {'id': 2, 'name': 'Pepperoni', 'ingredientes': ['Pepperoni', 'Queijo']},
    {'id': 3, 'name': 'Vegetariana', 'ingredientes': ['Tomate', 'Mussarela', 'Cogumelos', 'Espinafre']},
]

# Função para listar todas as pizzas (GET)
def list_pizzas(request):
    return JsonResponse(pizzas, safe=False)

# Função para criar uma nova pizza (POST)
@csrf_exempt  # Desabilitar CSRF apenas para simplificação (não usar em produção sem autenticação)
def create_pizza(request):
    if request.method == 'POST':
        # Obtém os dados enviados no corpo da requisição
        data = json.loads(request.body)
        new_id = max([pizza['id'] for pizza in pizzas]) + 1  # Gera um novo ID
        new_pizza = {'id': new_id, 'name': data['name'], 'ingredientes': data['ingredientes']}
        pizzas.append(new_pizza)  # Adiciona a nova pizza à lista
        return JsonResponse(new_pizza, status=201)  # Retorna a pizza criada com status 201 (Created)

# Função para atualizar uma pizza existente (PUT)
@csrf_exempt
def update_pizza(request, pizza_id):
    if request.method == 'PUT':
        # Obtém os dados enviados no corpo da requisição
        data = json.loads(request.body)
        for pizza in pizzas:
            if pizza['id'] == pizza_id:
                # Atualiza os dados da pizza
                pizza['name'] = data['name']
                pizza['ingredientes'] = data['ingredientes']
                return JsonResponse(pizza)  # Retorna a pizza atualizada
        return JsonResponse({'error': 'Pizza not found'}, status=404)  # Caso não encontre a pizza

# Função para deletar uma pizza existente (DELETE)
@csrf_exempt
def delete_pizza(request, pizza_id):
    if request.method == 'DELETE':
        global pizzas
        pizzas = [pizza for pizza in pizzas if pizza['id'] != pizza_id]  # Filtra a pizza pelo ID para deletar
        return JsonResponse({'message': 'Pizza deleted successfully'})  # Retorna uma mensagem de sucesso
