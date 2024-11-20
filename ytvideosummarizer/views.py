# views.py
from django.shortcuts import render
from .forms import VideoURLForm
from .utils import download_audio, audio_to_text, get_video_details
from django.http import JsonResponse



def ytvideosummarizerhome(request):
    if request.method == 'POST':
        form = VideoURLForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data['video_url']
            # Download audio and convert it to text
            audio_path = download_audio(video_url)
            text = audio_to_text(audio_path)
            # text = "testing is going on for downloading audio"
            return render(request, 'ytsummarizer/ytvideosummarizerhome.html', {'form': form, 'text': text})
    else:
        form = VideoURLForm()
    return render(request, 'ytsummarizer/ytvideosummarizerhome.html', {'form': form})

def get_video_details_ajax(request):
    if request.method == 'GET':
        url = request.GET.get('url', '')
        if url:
            try:
                title, thumbnail_url = get_video_details(url)
                return JsonResponse({'title': title, 'thumbnail_url': thumbnail_url})
            except Exception as e:
                return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Invalid request'})