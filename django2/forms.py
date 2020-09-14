from django import forms
from django.core import validators

class FormArticulo(forms.Form):

    title = forms.CharField(
            label='Titulo',
            max_length = 120,
            required= True,
            validators=[
                validators.MinLengthValidator(4,'titulo es muy corto'),
                validators.RegexValidator('^[A-Za-z0-9 ]*$', 'el titulo esta mal formado', 'invalid_title')
                ]
            )

    content = forms.CharField(
            label='Contenido',
            widget = forms.Textarea
            )

    options = [
            (1,'SI'),
            (0,'NO')
            ]

    public = forms.TypedChoiceField(
            label= "publicado",
            choices = options
            )


