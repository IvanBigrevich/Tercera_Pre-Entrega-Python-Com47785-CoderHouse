from django import forms


class CursoForm(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()


class BusquedaCursoForm(forms.Form):
    nombre = forms.CharField()
