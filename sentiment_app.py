"""
Sentiment Analysis Web Application
Author: [Your Name]
Date: February 10, 2026

A Streamlit-based web interface for sentiment analysis using VADER.
Features include real-time analysis and history of last 5 analyses.
"""

import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime


# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state.history = []


def analyze_sentiment(text):
    """
    Analyze sentiment of given text using VADER.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Dictionary containing scores and sentiment label
    """
    if not text or text.strip() == "":
        return None
    
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    
    compound = scores['compound']
    if compound >= 0.05:
        label = 'Positive'
    elif compound <= -0.05:
        label = 'Negative'
    else:
        label = 'Neutral'
    
    return {
        'text': text,
        'pos': scores['pos'],
        'neu': scores['neu'],
        'neg': scores['neg'],
        'compound': compound,
        'label': label,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def add_to_history(result):
    """
    Add analysis result to history (maintain last 5).
    
    Args:
        result (dict): Analysis result to add
    """
    st.session_state.history.insert(0, result)
    # Keep only last 5
    if len(st.session_state.history) > 5:
        st.session_state.history = st.session_state.history[:5]


def get_sentiment_color(label):
    """
    Get color for sentiment label.
    
    Args:
        label (str): Sentiment label
        
    Returns:
        str: Color code
    """
    colors = {
        'Positive': '#28a745',
        'Negative': '#dc3545',
        'Neutral': '#6c757d'
    }
    return colors.get(label, '#000000')


# Page configuration
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="😊",
    layout="wide"
)

# Main title
st.title("🎭 VADER Sentiment Analysis App")
st.markdown("### Analyze the sentiment of any text in real-time")
st.markdown("---")

# Create two columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Enter Text to Analyze")
    
    # Text input area
    user_text = st.text_area(
        "Type or paste your text here:",
        height=150,
        placeholder="Enter text to analyze its sentiment...",
        key="text_input"
    )
    
    # Analyze button
    analyze_button = st.button("🔍 Analyze Sentiment", type="primary", use_container_width=True)
    
    # Process analysis
    if analyze_button:
        if user_text and user_text.strip():
            result = analyze_sentiment(user_text)
            if result:
                add_to_history(result)
                
                # Display current analysis
                st.markdown("---")
                st.subheader("📊 Analysis Results")
                
                # Sentiment label with color
                label_color = get_sentiment_color(result['label'])
                st.markdown(
                    f"<h1 style='text-align: center; color: {label_color};'>{result['label'].upper()}</h1>",
                    unsafe_allow_html=True
                )
                
                # Scores display
                st.markdown("#### Detailed Scores")
                
                # Create columns for scores
                score_col1, score_col2, score_col3, score_col4 = st.columns(4)
                
                with score_col1:
                    st.metric("Positive", f"{result['pos']:.3f}")
                
                with score_col2:
                    st.metric("Neutral", f"{result['neu']:.3f}")
                
                with score_col3:
                    st.metric("Negative", f"{result['neg']:.3f}")
                
                with score_col4:
                    st.metric("Compound", f"{result['compound']:.4f}")
                
                # Progress bars for visualization
                st.markdown("#### Score Breakdown")
                st.progress(result['pos'], text=f"Positive: {result['pos']:.1%}")
                st.progress(result['neu'], text=f"Neutral: {result['neu']:.1%}")
                st.progress(result['neg'], text=f"Negative: {result['neg']:.1%}")
                
        else:
            st.warning("⚠️ Please enter some text to analyze.")

with col2:
    st.subheader("📜 Analysis History")
    st.markdown("*Last 5 analyses*")
    
    if st.session_state.history:
        for i, item in enumerate(st.session_state.history):
            with st.expander(f"#{i+1} - {item['label']} ({item['timestamp']})", expanded=(i == 0)):
                st.markdown(f"**Text:** {item['text'][:100]}{'...' if len(item['text']) > 100 else ''}")
                st.markdown(f"**Label:** {item['label']}")
                st.markdown(f"**Compound:** {item['compound']:.4f}")
                st.markdown(f"**Pos:** {item['pos']:.3f} | **Neu:** {item['neu']:.3f} | **Neg:** {item['neg']:.3f}")
        
        # Clear history button
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.history = []
            st.rerun()
    else:
        st.info("No analysis history yet. Start analyzing text!")

# Footer with information
st.markdown("---")
st.markdown("""
### ℹ️ About This App
This application uses **VADER (Valence Aware Dictionary and sEntiment Reasoner)** for sentiment analysis.

**Labeling Rules:**
- **Positive**: Compound score ≥ 0.05
- **Negative**: Compound score ≤ -0.05
- **Neutral**: Compound score between -0.05 and 0.05

**Score Ranges:** All scores range from 0.0 to 1.0 (except compound: -1.0 to 1.0)
""")

# Sidebar with examples
with st.sidebar:
    st.header("💡 Example Texts")
    st.markdown("""
    **Try these examples:**
    
    **Positive:**
    - "I absolutely love this product! It's amazing!"
    - "What a wonderful day! Everything is perfect."
    
    **Negative:**
    - "This is terrible. I hate it so much."
    - "Worst experience ever. Never again."
    
    **Neutral:**
    - "The meeting is scheduled for 3 PM."
    - "I went to the store yesterday."
    
    **Tricky (Sarcasm):**
    - "Oh great, another meeting. Just what I needed."
    - "Yeah, right. Like that's going to work."
    """)
    
    st.markdown("---")
    st.markdown("**Note:** VADER works best with social media text and may struggle with sarcasm or complex contexts.")
