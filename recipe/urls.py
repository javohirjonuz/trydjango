from django.urls import path

from .views import (
    recipe_list,
    recipe_detail,
    my_recipe_list,
    recipe_create,
    recipe_update,
    recipe_delete,
    recipe_ingredient_create,
    recipe_ingredient_edit

)

app_name = 'recipe'

urlpatterns = [
    path('list/', recipe_list, name='list '),
    path('list/my/ ', my_recipe_list, name='my-list'),
    path('detail/<slug:slug>/', recipe_detail, name='detail '),
    path('create/', recipe_create, name='create '),
    path('update/<slug:slug>/', recipe_update, name='update '),
    path('delete/<slug:slug>/', recipe_delete, name='delete '),
    path('<slug:slug>/ingredinrt/create/', recipe_ingredient_create, name='ingredient-create '),
    path('<slug:slug>/ingredinrt/edit/<int:pk>/', recipe_ingredient_edit, name='ingredient-edit '),

]
