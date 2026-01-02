from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Mensagem
from contato.forms import MensagemForm


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


def _get_mensagens_paginadas(request):
    q = request.GET.get('q', '')
    status = request.GET.get('status', '')
    
    queryset = Mensagem.objects.all().order_by('-data_envio')

    if q:
        queryset = queryset.filter(
            Q(nome__icontains=q) |
            Q(email__icontains=q) |
            Q(assunto__icontains=q)
        )
    
    if status == 'nao_lidas':
        queryset = queryset.filter(lida=False)
    elif status == 'lidas':
        queryset = queryset.filter(lida=True)

    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    mensagens = paginator.get_page(page_number)
    
    return mensagens, q, status


@login_required(login_url='login')
def painel_mensagens(request):
    mensagens, q, status = _get_mensagens_paginadas(request)

    context = {
        'site_title': 'Painel - ',
        'mensagens': mensagens, 
        'q': q,
        'status': status
    }

    return render(request, 'painel.html', context)


@login_required(login_url='login')
def painel_pesquisa(request):
    if not request.headers.get('HX-Request'):
        return redirect('painel')
    
    mensagens, q, status = _get_mensagens_paginadas(request)

    context = {
        'mensagens': mensagens,
        'q': q,
        'status': status
    }

    return render(request, 'partials/_lista_mensagens.html', context)


@login_required(login_url='login')
def detalhe_mensagem(request, mensagem_id):
    if not request.headers.get('HX-Request'):
        return redirect('painel')
    
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)

    if not mensagem.lida:
        mensagem.lida = True
        mensagem.save()
    
    response = render(request, 'partials/_detalhe_mensagem.html', {'msg': mensagem})
    
    response['HX-Trigger'] = 'atualizarLista'
    
    return response


@login_required(login_url='login')
@require_POST
def apagar_mensagem(request, mensagem_id):
    if not request.headers.get('HX-Request'):
        return redirect('painel')
    
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)
    mensagem.delete()
    return painel_pesquisa(request)


@login_required(login_url='login')
def confirmar_exclusao(request, mensagem_id):
    if not request.headers.get('HX-Request'):
        return redirect('painel')
    
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)
    return render(request, 'partials/_confirmar_exclusao.html', {'msg': mensagem})
