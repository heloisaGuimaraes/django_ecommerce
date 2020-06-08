from django import forms

class ContactForm(forms.Form):
    nome_completo = forms.CharField()
    email = forms.Email.Field()
    conteudo = forms.CharField()