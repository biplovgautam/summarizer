from django.shortcuts import render
from .forms import textForm
from django.http import JsonResponse
from .utils import ttsummarizer



def textsummarizerhome(request):
    if request.method == 'POST':
        form = textForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            text = ttsummarizer(input_text)
            return render(request, 'textsummarizer/textsummarizerhome.html', {'form': form, 'text': text})
    else:
        form = textForm()
    return render(request, 'textsummarizer/textsummarizerhome.html', {'form': form})