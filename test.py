import os
import uuid
from pytube import YouTube
import whisper

def generate_unique_filename():
    return f"temp_audio_{uuid.uuid4().hex}.wav"

def download_audio(url, audio_path):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(output_path=os.path.dirname(audio_path), filename=os.path.basename(audio_path))

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    transcript = result["text"]
    print("Transcription: ", transcript)
    return transcript

def process_youtube_video(url):
    audio_path = generate_unique_filename()
    download_audio(url, audio_path)
    transcription = transcribe_audio(audio_path)
    if os.path.exists(audio_path):
        os.remove(audio_path)
        print(f"Deleted the audio file: {audio_path}")
    else:
        print("Audio file not found for deletion.")
        return transcription

video_url = "https://www.youtube.com/watch?v=kPhpHvnnn0Q"
transcription = process_youtube_video(video_url)
print(transcription)