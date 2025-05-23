from django.shortcuts import render, redirect
from .forms import CandidateForm
from .utils import send_to_telegram
import asyncio



def candidate_form(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            # Отправляем данные в Telegram
            asyncio.run(send_to_telegram(form.cleaned_data))
            return redirect('success')
    else:
        form = CandidateForm()
    context = {
        'title': 'Оставьте заявку',
        'form': form,
        }
    return render(request, 'landing/index.html', context=context)

def success(request):
    context = {
        'title': 'Спасибо за заявку!',
    }
    return render(request, 'landing/success.html', context=context)

def conditions(request):
    context = {
        'title': 'Условия работы',
    }
    return render(request, 'landing/conditions.html', context=context)

def vacancies(request):
    context = {
        'title': 'Вакансии',
    }
    return render(request, 'landing/vacancies.html', context=context)