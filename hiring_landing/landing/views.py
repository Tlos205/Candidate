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
    return render(request, 'landing/index.html', {'form': form})

def success(request):
    return render(request, 'landing/success.html')