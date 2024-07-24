from summarizer import TransformerSummarizer

def Summary(text):

    
    # Initialize the summarizer
    summarizer = TransformerSummarizer()
    
    # Summarize the text
    summary = summarizer.summarize(text)
    
    # Print or use the summary as needed
    return summary

