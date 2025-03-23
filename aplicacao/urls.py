# from django.urls import path
# from . import views

# urlpatterns = [
#     path('pizzas/', views.list_pizzas, name='list_pizzas'),
# ]

# 'http://127.0.0.1:8000/aplicacao/pizzas'
from django.urls import path
from . import views

urlpatterns = [
    # Rota para listar todas as pizzas (GET)
    path('pizzas/', views.list_pizzas, name='list_pizzas'),

    # Rota para criar uma nova pizza (POST)
    path('pizzas/create/', views.create_pizza, name='create_pizza'),

    # Rota para atualizar uma pizza existente (PUT)
    path('pizzas/<int:pizza_id>/update/', views.update_pizza, name='update_pizza'),

    # Rota para deletar uma pizza existente (DELETE)
    path('pizzas/<int:pizza_id>/delete/', views.delete_pizza, name='delete_pizza'),
]