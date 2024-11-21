from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # or "t5-small" for T5


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
