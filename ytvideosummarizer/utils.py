from pytube import YouTube
import whisper
import yt_dlp
import os
from django.conf import settings
import uuid


# Initialize Whisper model
model = whisper.load_model("base")  # You can use 'small', 'medium', or 'large' for different performance levels

def download_audio(video_url):
    print(f"Attempting to download from URL: {video_url}")
    user_uuid = str(uuid.uuid4()) 
    try:
        audio_directory = os.path.join(settings.MEDIA_ROOT, 'audio_files')
        # Generate a filename with UUID appended
        filename = f"{user_uuid}_audio.%(ext)s"  # The UUID will be appended to the file name
    
        # Path where the audio will be saved
        audio_path = os.path.join(audio_directory, filename)
        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': audio_path,
    }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            audio_file_path = info_dict.get("requested_downloads")[0]["filepath"]  # Get the downloaded file path
            print(f"Audio downloaded to {audio_file_path}")
            return audio_file_path
    except Exception as e:
        print(f"Error downloading audio: {e}")
        return None

def audio_to_text(audio_file_path):
    if not audio_file_path:
        print("No audio file found for transcription.")
        return ""
    
    print(f"Transcribing audio from {audio_file_path}")
    # Use Whisper to transcribe the audio to text
    result = model.transcribe(audio_file_path)
    
    # Extract the transcribed text
    text = result['text']
    print("Transcription complete:")
    print(text)
    return text


def delete_audio(audio_file_path):
    try:
        os.remove(audio_file_path)
        print(f"Deleted audio file: {audio_file_path}")
    except Exception as e:
        print(f"Error deleting audio file: {e}")
