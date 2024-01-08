from django import forms
from .models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image', 'author', 'description', 'tags']
        exclude = ['author']

    def __int__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_title",
            "placeholder": "Title   "
        })

        self.fields['image'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_title",
        })

        self.fields['description'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_description",
            "rows": "4",
            "placeholder": "Description"

        })
        self.fields['tags'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_tags",
            "rows": "4",

        })

    def clean_title(self):
        title = self.clean_title['title']
        return title.capitalize()


class IngredientForm():
    class Meta:
        model = Ingredient
        fields = ['recipe', 'title', 'quantity', ' unit', 'is_active']
        exclude = ['recipe']

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            "class": "form-control",
            "id": "ingredient_title",
            "placeholder": "Title   "
        })
        self.fields['quantity'].widget.attrs.update({
            "class": "form-control",
            "id": "ingredient_quantity",
            "placeholder": "Quantity"
        })
        self.fields['unit'].widget.attrs.update({
            "class": "form-control",
            "id": "ingredient_unit",

        })
        self.fields['is_active'].widget.attrs.update({
            "class": "form-control",
            "id": "ingredient_is_active",
            "role": "switch",
            "type": "сheckbox",
            "checked": "checked"
        })
