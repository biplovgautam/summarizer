
# DjangoSummarizer

Welcome to **DjangoSummarizer**! This project is designed to make lengthy YouTube videos more digestible by transcribing audio into text and summarizing it. The transcription feature is fully functional, and future improvements will enhance the summarization capabilities.

---

## Features

### Current Features
- **Accurate Transcriptions**: Uses OpenAI's Whisper (base version) for high-quality speech-to-text conversion.
- **Summarization**: Automatically generate concise summaries from transcriptions or input text.

### Planned Features
- **YouTube Video Card**: Automatically generates a card with the title and video of the provided YouTube URL.
- **Enhanced UI**: A smoother, more intuitive user interface.
- **API Integration**: Access transcription and summarization services programmatically.

---

## Built With

- **Django**: A robust web framework for backend logic.
- **yt-dlp**: Downloads YouTube videos for processing.
- **Whisper (Base)**: A state-of-the-art model for audio transcription.
- **BERT**: A transformer-based model used for advanced text summarization.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Django 4.0+
- `yt-dlp` (to download video/audio)
- Whisper (`pip install openai-whisper`)
- FFmpeg (for audio/video processing)

---

## Installation

Follow the steps below to get the app up and running on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/biplovgautam/summarizer.git
   cd summarizer
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure FFmpeg**: Ensure FFmpeg is installed and added to your system's PATH.

5. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the App**: Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Usage

### For YouTube Transcription and Summarization:
1. Paste the URL of a YouTube video into the input box.
2. Click "Submit" to transcribe and summarize the audio.
3. View the transcription and download the summary if needed.

### For Text Summarization:
1. Enter the text you want to summarize into the input box.
2. Click "Submit" to view the concise summary of the entered text.

---

## Directory Structure

```
summarizer/
├── summarizer/        # Core project folder
├── ytvideosummarizer/ # youtube video summarizer app
├── textsummarizer/    # textsummarizer app folder
├── templates/         # HTML templates
├── static/            # Static files (CSS, JS, images)
├── media/             # Temporary storage for audio files
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

---

## Future Enhancements

- **Customizable Summary Length**: Choose between short, medium, or detailed summaries.
- **User Profiles**: Save and manage your transcriptions and summaries.
- **API Service**: Provide transcription and summarization capabilities via API.
- **Mobile App**: A dedicated app for easier accessibility.

---

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a brief description of the feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Acknowledgements

- **Django** for a robust backend framework.
- **yt-dlp** for seamless YouTube audio downloads.
- **Whisper** for state-of-the-art transcription capabilities.
- **Hugging Face Transformers** for powerful summarization models.

---

## Let’s make long videos and lengthy text easier to digest, together! 🎉
