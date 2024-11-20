# views.py
from django.shortcuts import render
from .forms import VideoURLForm
from .utils import download_audio, audio_to_text, delete_audio

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
