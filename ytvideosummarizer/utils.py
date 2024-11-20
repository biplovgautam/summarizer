import whisper
import yt_dlp
import os
from django.conf import settings
import uuid
from transformers import pipeline
import requests
from bs4 import BeautifulSoup


# Initialize Whisper model
transcripter = whisper.load_model("base")  # You can use 'small', 'medium', or 'large' for different performance levels
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # or "t5-small" for T5

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
    result = transcripter.transcribe(audio_file_path)  # This returns a dictionary
    delete_audio(audio_file_path)
    # Extract the transcribed text
    transcribed_text = result['text']  # Get the text field
    # generate the summary from it
    print("transcription completed sumarizing it!!!")
    text = ttsummarizer(transcribed_text)
    return text
    

def delete_audio(audio_file_path):
    try:
        os.remove(audio_file_path)
        print(f"Deleted audio file: {audio_file_path}")
    except Exception as e:
        print(f"Error deleting audio file: {e}")


def ttsummarizer(input_text):
    chunk_size = 1024  # You can adjust this based on the model's token limit
    chunks = [input_text[i:i+chunk_size] for i in range(0, len(input_text), chunk_size)]
    summaries = []
    try:
        for chunk in chunks:
            summary = summarizer(chunk)  # Summarize each chunk
            summaries.append(summary[0]['summary_text'])  # Append the summary for each chunk
        # Combine the summaries
        final_summary = ' '.join(summaries)
        return final_summary
    except Exception as e:
        print(f"Error while generating summary: {e}")
        return e


def get_video_details(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title
        title = soup.find('meta', property='og:title')
        if title:
            title = title.get('content')
        else:
            title = "Title not found"

        # Extract thumbnail URL
        thumbnail_url = soup.find('meta', property='og:image')
        if thumbnail_url:
            thumbnail_url = thumbnail_url.get('content')
        else:
            thumbnail_url = "Thumbnail not found"

        return title, thumbnail_url
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return "Error retrieving details", None
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error retrieving details", None