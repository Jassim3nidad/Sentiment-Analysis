"""
Sentiment Analysis Baseline Script using VADER
Author: [Your Name]
Date: February 10, 2026

This script performs sentiment analysis on text input using VADER
(Valence Aware Dictionary and sEntiment Reasoner).
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def analyze_sentiment(text):
    """
    Analyze sentiment of given text using VADER.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Dictionary containing scores and sentiment label
    """
    # Handle empty or whitespace-only input
    if not text or text.strip() == "":
        return {
            'error': 'Empty input provided',
            'pos': 0.0,
            'neu': 0.0,
            'neg': 0.0,
            'compound': 0.0,
            'label': 'Neutral'
        }
    
    # Initialize VADER analyzer
    analyzer = SentimentIntensityAnalyzer()
    
    # Get sentiment scores
    scores = analyzer.polarity_scores(text)
    
    # Determine sentiment label based on compound score
    compound = scores['compound']
    if compound >= 0.05:
        label = 'Positive'
    elif compound <= -0.05:
        label = 'Negative'
    else:
        label = 'Neutral'
    
    # Return results
    return {
        'pos': scores['pos'],
        'neu': scores['neu'],
        'neg': scores['neg'],
        'compound': compound,
        'label': label
    }


def main():
    """
    Main function to run the sentiment analyzer interactively.
    """
    print("=" * 60)
    print("VADER Sentiment Analysis - Baseline Script")
    print("=" * 60)
    print("\nEnter text to analyze (or 'quit' to exit):\n")
    
    while True:
        # Get user input
        user_input = input("\nText: ")
        
        # Check for exit command
        if user_input.lower() == 'quit':
            print("\nExiting sentiment analyzer. Goodbye!")
            break
        
        # Analyze sentiment
        result = analyze_sentiment(user_input)
        
        # Display results
        if 'error' in result:
            print(f"\nError: {result['error']}")
        else:
            print("\n" + "-" * 60)
            print("SENTIMENT ANALYSIS RESULTS:")
            print("-" * 60)
            print(f"Positive Score: {result['pos']:.3f}")
            print(f"Neutral Score:  {result['neu']:.3f}")
            print(f"Negative Score: {result['neg']:.3f}")
            print(f"Compound Score: {result['compound']:.4f}")
            print(f"\n>>> SENTIMENT LABEL: {result['label'].upper()} <<<")
            print("-" * 60)


if __name__ == "__main__":
    main()
