from django import forms
from phonenumber_field.formfields import PhoneNumberField
from . import models


class MensagemForm(forms.ModelForm):
    css_input = (
        'w-full bg-slate-600/50 border border-white/10 rounded-lg px-4 py-3 text-white placeholder-slate-300 '
        'focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-colors'
    ) 
    
    OPCOES = [('', 'Selecione o tipo de projeto')] + list(models.Mensagem.ASSUNTOS.items())

    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': css_input, 
                'placeholder': 'Seu nome completo'
            }
        )
    )
    telefone = PhoneNumberField(
        region="BR",
        widget=forms.TextInput(
            attrs={
                'class': css_input, 
                'placeholder': '(00) 00000-0000'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': css_input, 
                'placeholder': 'exemplo@email.com'
            }
        )
    )
    assunto = forms.ChoiceField(
        choices=OPCOES,
        widget=forms.Select(attrs={
            'class': css_input
        })
    )
    mensagem = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': css_input + ' resize-none', 
                'placeholder': 'Descreva sua necessidade...',
            }
        )
    )

    class Meta:
        model = models.Mensagem
        fields = ('nome', 'telefone', 'email', 'assunto', 'mensagem')
