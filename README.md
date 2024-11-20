
# DjangoSummarizer

Welcome to **DjangoSummarizer**! This project is designed to make lengthy YouTube videos more digestible. By leveraging AI, it extracts the audio, transcribes it into text, and (in the future) will summarize the transcription into concise points. Currently, the transcription feature is fully functional.


## Features

### Current Features
- **Accurate Transcriptions**: Uses OpenAI's Whisper (base version) for high-quality speech-to-text conversion.
- **Summarization**: Automatically generate concise summaries from transcriptions.

### Planned Features
- **YT video card**: Automatically generates and update the card having title and video of that youtube url.
- **Enhanced UI**: A smoother, more intuitive interface for users.
- **API Integration**: Access transcription and summarization services programmatically.

---

## Built With

- **Django**: A robust web framework for backend logic.
- **yt-dlp**: Downloads YouTube videos for processing.
- **Whisper (Base)**: A state-of-the-art model for audio transcription.
- **BERT**: A transformer-based model used for advanced text summarization.

---

## Prerequisites

To get started, ensure you have the following:
- Python 3.8+
- Django 4.0+
- `yt-dlp` (to download video/audio)
- Whisper (install via `pip install openai-whisper`)

---

## Installation

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

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

---

## How It Works

1. Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
2. Paste a YouTube video URL into the input box.
3. Click **Submit**, and let the app transcribe the audio.
4. View the transcription results on the output page.

---

## Project Structure

```
djangosummarizer/
├── summarizer/        # Core project folder
├── templates/         # HTML files
├── ytvideosummarizer/ # Handles YouTube video processing
├── media/             # Temporary file storage
├── manage.py          # Django management script
├── requirements.txt   # Required libraries
└── README.md          # This file!
```

---

## What’s Coming Next?

- **User Profiles**: Save and revisit previous transcriptions and summaries.
- **Cloud Integration**: Store processed results for better scalability.
- **Frontend Enhancements**: Transition to React for a modern, dynamic user experience.

---

## Contributing

Want to help make DjangoSummarizer even better? Here’s how:

1. Fork the repo.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Describe your changes"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request!

---

## License

This project is licensed under the MIT License. Check out the [LICENSE](LICENSE) file for details.

---

## Special Thanks

- **Django** for the solid web framework.
- **yt-dlp** for making video and audio processing easy.
- **Whisper** for its groundbreaking transcription capabilities.
- **BERT** for its powerful capabilities in text summarization, making the process more efficient.

---

## Let’s Make Videos Easier to Understand Together!

This version emphasizes the use of Whisper for transcription and provides a friendly, approachable tone for readers.