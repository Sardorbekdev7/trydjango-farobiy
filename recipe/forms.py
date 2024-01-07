from django import forms
from .models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", 'image', 'author', 'description', 'tag']
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_title",
            "placeholder": "Title"
        })
        self.fields['image'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_image",
        })
        self.fields['description'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_description",
            "placeholder": "Description",
            "rows": "4"
        })

        self.fields['tag'].widget.attrs.update({
            "class": "form-select",
            "id": "recipe_tags",
        })

    def clean_title(self):
        title = self.cleaned_data['title']
        return title.capitalize()


class IngredientEditForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["title", "recipe", "quantity", "is_active", "unit"]
        exclude = ['recipe']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            "class": "form-control",
            "id": "ingredient_title",
            "placeholder": "Title"
        })
        self.fields['quantity'].widget.attrs.update({
            "class": "form-control",
            "id": "ingredient_quantity",
            "placeholder": "Quantity"
        })
        self.fields['unit'].widget.attrs.update({
            "class": "form-select",
            "id": "ingredient_unit",
        })
        self.fields['is_active'].widget.attrs.update({
            "id": "flexSwitchCheckChecked ",
            "class": "form-check-input",
            "type": "checkbox",
            "role": "switch",
        })


class IngredientForm(IngredientEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'].widget.attrs.update({
            "checked": "checked"
        })