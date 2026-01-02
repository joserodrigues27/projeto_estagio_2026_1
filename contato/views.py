from django.shortcuts import render
from django.urls import reverse
from .forms import MensagemForm


def landpage(request):
    form_action = reverse('landpage')

    if request.method == 'POST':
        form = MensagemForm(request.POST)

        contexto = {'form': form, 'form_action': form_action,}

        if form.is_valid():
            form.save()
            return render(request, 'partials/_mensagem_sucesso.html')

        return render(request, 'partials/_form.html', contexto)

    contexto = {'form': MensagemForm(), 'form_action': form_action,}

    if request.headers.get('HX-Request'):
        return render(request, 'partials/_form.html', contexto)

    return render(request, 'landpage.html', contexto)
