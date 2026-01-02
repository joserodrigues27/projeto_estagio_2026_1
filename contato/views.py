from django.shortcuts import render
from django.urls import reverse
from .forms import MensagemForm


def landpage(request):
    form_action = reverse('landpage')

    if request.method == 'POST':
        form = MensagemForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'partials/_mensagem_sucesso.html')
        
        context = {
            'form': form,
            'form_action': form_action
        }

        return render(request, 'partials/_form.html', context)

    context = {
        'form': MensagemForm(),
        'form_action': form_action
    }

    if request.headers.get('HX-Request'):
        return render(request, 'partials/_form.html', context)

    return render(request, 'landpage.html', context)


def painel_mensagens(request):
    return render(request, 'painel.html')
