from django import forms

class ContactForm(forms.Form):
    nome_completo = forms.CharField(error_messages={'required': 'Campo obrigatório.'},
        widget = forms.TextInput(
        attrs = {
            "class": "form-control", 
            "placeholder": "Digite seu nome completo."}))
    
    email = forms.EmailField(error_messages={'required': 'Campo obrigatório'},
        widget = forms.EmailInput(
        attrs = {"class": "form-control", 
                 "placeholder": "Digite seu e-mail."}))
    
    conteudo = forms.CharField(error_messages={'required': 'Campo obrigatório'},
        widget = forms.Textarea(
        attrs = {"class": "form-control", 
                 "placeholder": "Digite sua mensagem."}))
    def clean_email(self):
        
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("O E-mail deve ser do gmail.com")
        return email