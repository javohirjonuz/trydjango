from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q

from .models import Recipe, Tag, Ingredient
from .forms import RecipeForm, IngredientForm


def recipe_list(request):
    recipes = Recipe.objects.order_by('-id')
    tag = request.GET.get('tag')
    if tag:
        recipes = Recipe.objects.order_by('-id').filter(tags__title=tag)

    context = {
        'object_list': recipes

    }
    return render(request, 'recipe/index.html', context)


def my_recipe_list(request):
    recipes = Recipe.objects.filter(author_id=request.user.id).order_by('-id')
    # print(recipes.user.id)
    tag = request.GET.get('tag')
    if tag:
        recipes = recipes.filter(tags__title=tag)
    context = {
        'object_list': recipes
    }
    return render(request, 'recipe/index.html', context)


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    is_author_lookup = Q(is_active=False)
    if request.user == recipe.author:
        is_author_lookup = Q(is_active=True)

    ingredients = Ingredient.objects.filter(Q(recipe_id=recipe.id) & is_author_lookup)
    is_author = request.user == recipe.author
    # print(is_author)
    context = {
        'object': recipe,
        'ingredients': ingredients,
        'is_author': is_author

    }
    return render(request, 'recipe/detail.html', context)


def recipe_create(request):
    if not request.user.is_authenticated:
        messages.info(request, "You should log in first.")
        return redirect("auth:login")
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, files=request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)

        obj.author.id = request.user.id
        obj.save()
        obj.save_m2m()
        detail_url = reverse('recipe:detail ', args=[obj.slug])
        return redirect(detail_url)

    context = {
        "form": form,

        ' header': "Recipe Update",
    }

    return render(request, 'recipe/create.html', context)


def recipe_update(request, slug):
    instance = get_object_or_404(Recipe, slug=slug)
    form = Recipe(instance=instance)
    if request.method == 'POST':
        form = RecipeForm(data=request.POST, files=request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            form.save_m2m()
            detail_url = reverse('recipe:detail ', kwargs={"slug": instance.slug})
            return redirect(detail_url)

    ctx = {
        'form': form

    }
    return render(request, 'recipe/create.html', ctx)


def recipe_delete(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == 'POST':
        if not request.user == recipe.author:
            messages.warning(request, "You have no enough permission to delete.")
            return redirect(reverse('recipe:detail ', args=[recipe.slug]))
        recipe.delete()
        return redirect('recipe:list ')
    ctx = {
        'object': recipe
    }
    return render(request, 'recipe/delete.html', ctx)


def recipe_ingredient_create(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    form = IngredientForm()
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.recipe = recipe
            obj.save()
            reverse_url = reverse('recipe:detail ', args=[recipe.slug])
            return redirect(reverse_url)

    ctx = {
        'form': form
    }
    return render(request, 'recipe/ingredient_create.html', ctx)


def recipe_ingredient_edit(request, slug, pk, *args, **kwargs):
    recipe = get_object_or_404(Recipe, slug=slug)
    instance = get_object_or_404(Ingredient, id=pk)
    form = IngredientForm(instance=instance)
    if request.method == 'POST':
        form = IngredientForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            reverse_url = reverse('recipe:detail ', args=[slug])
            return redirect(reverse_url)
        ctx = {
            'form':form,
            'recipe': recipe,
            'title': "Change ingredient belong to",
        }
        return render(request, 'recipe/ingredient_create.html', ctx)
