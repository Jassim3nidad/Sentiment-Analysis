# Sentiment Analysis Application
## VADER-Based Sentiment Analyzer with Web Interface

**Author:** Trinidad, Jassim Eman M.  
**Course:** Artificial Intelligence Laboratory  
**Date:** February 10, 2026  
**Project:** Sentiment Analysis App (VADER + User Inputs + Prompt Engineering)

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [What is VADER?](#what-is-vader)
3. [Labeling Rules and Thresholds](#labeling-rules-and-thresholds)
4. [Technology Stack](#technology-stack)
5. [Installation and Setup](#installation-and-setup)
6. [Usage Instructions](#usage-instructions)
7. [Testing Summary](#testing-summary)
8. [Observations and Analysis](#observations-and-analysis)
9. [Limitations and Improvements](#limitations-and-improvements)
10. [Prompt Engineering](#prompt-engineering)
11. [AI Assistance Reflection](#ai-assistance-reflection)

---

## Project Overview

This project implements a comprehensive sentiment analysis application using VADER (Valence Aware Dictionary and sEntiment Reasoner). The application consists of:

- **Baseline Script**: Command-line sentiment analyzer
- **Web Application**: Interactive Streamlit-based UI with analysis history
- **Testing Framework**: 25 test cases with accuracy measurement
- **Documentation**: Complete project documentation with prompt engineering analysis

The application analyzes user-provided text and returns:
- Sentiment label (Positive, Neutral, or Negative)
- Four sentiment scores: positive, neutral, negative, and compound
- Historical record of last 5 analyses

---

## What is VADER?

**VADER (Valence Aware Dictionary and sEntiment Reasoner)** is a lexicon and rule-based sentiment analysis tool specifically designed for social media text. Unlike machine learning models that require training data, VADER uses a pre-built dictionary of words with sentiment scores.

### Key Characteristics:

1. **Lexicon-Based**: Uses a dictionary of ~7,500 words with validated sentiment ratings
2. **Rule-Based**: Applies grammatical and syntactical rules to adjust scores
3. **Social Media Optimized**: Handles emoticons, slang, acronyms, and capitalization
4. **No Training Required**: Works out-of-the-box without training data
5. **Fast Performance**: Near-instantaneous analysis of text

### How VADER Works:

1. **Tokenization**: Breaks text into individual words
2. **Lexicon Lookup**: Each word is matched against the sentiment lexicon
3. **Score Calculation**: Computes intensity scores for positive, neutral, and negative sentiment
4. **Rule Application**: Adjusts scores based on:
   - Capitalization (e.g., "AMAZING" scores higher than "amazing")
   - Punctuation (e.g., "Good!!!" scores higher than "Good")
   - Negations (e.g., "not good" reverses polarity)
   - Boosters (e.g., "very good" increases intensity)
5. **Normalization**: Produces a compound score ranging from -1 (most negative) to +1 (most positive)

### VADER Advantages:

- No need for labeled training data
- Works well on short, informal text
- Interpretable results with explainable scores
- Lightweight and fast

### VADER Limitations:

- Struggles with sarcasm and irony
- May miss context-dependent sentiment
- Lexicon may not include newest slang
- Cannot understand complex linguistic nuances

---

## Labeling Rules and Thresholds

The sentiment classification uses the **compound score** from VADER with the following decision rules:

```python
if compound >= 0.05:
    label = "Positive"
elif compound <= -0.05:
    label = "Negative"
else:
    label = "Neutral"
```

### Threshold Justification:

- **Positive Threshold (≥ 0.05)**: Allows for slight positive sentiment while filtering noise
- **Negative Threshold (≤ -0.05)**: Symmetric with positive threshold for balanced classification
- **Neutral Range (-0.05 to 0.05)**: Captures truly neutral or ambiguous statements

These thresholds are VADER's recommended defaults based on extensive validation studies and have been shown to work well across diverse text types.

### Score Interpretation:

- **Compound Score**: Overall sentiment (-1.0 to +1.0)
  - `-1.0 to -0.05`: Negative sentiment
  - `-0.05 to 0.05`: Neutral sentiment
  - `0.05 to 1.0`: Positive sentiment

- **Individual Scores** (0.0 to 1.0 each):
  - **Positive (pos)**: Proportion of positive words
  - **Neutral (neu)**: Proportion of neutral words
  - **Negative (neg)**: Proportion of negative words
  - Note: pos + neu + neg = 1.0

---

## Technology Stack

### Core Technologies:

1. **Python 3.x**: Primary programming language
2. **vaderSentiment**: Sentiment analysis library
3. **Streamlit**: Web application framework

### Why Streamlit?

I chose **Streamlit** for the user interface because:

1. **Rapid Development**: Build interactive web apps with minimal code
2. **Python-Native**: No need for HTML/CSS/JavaScript knowledge
3. **Built-in Components**: Pre-built UI elements (text areas, buttons, metrics)
4. **Session State Management**: Easy history tracking and state persistence
5. **Real-time Updates**: Automatic re-rendering on user interaction
6. **Professional Appearance**: Clean, modern UI out-of-the-box
7. **Easy Deployment**: Simple to share and deploy

### Alternative Technologies Considered:

- **Flask**: More complex, requires HTML/CSS knowledge
- **Tkinter**: Desktop-only, less modern appearance
- **React + FastAPI**: Overkill for this project, steep learning curve
- **Command-line**: Limited user experience, no visual feedback

Streamlit provided the best balance of ease of development, functionality, and professional appearance for this academic project.

---

## Installation and Setup

### Prerequisites:

- Python 3.7 or higher
- pip package manager

### Step 1: Install Required Packages

```bash
pip install vadersentiment streamlit
```

### Step 2: Download Project Files

Ensure you have the following files:
- `sentiment_baseline.py` - Baseline CLI script
- `sentiment_app.py` - Streamlit web application
- `test_log.md` - Testing documentation
- `README.md` - This documentation file

### Step 3: Verify Installation

Test that VADER is installed correctly:

```bash
python -c "from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer; print('VADER installed successfully!')"
```

---

## Usage Instructions

### Option 1: Baseline Command-Line Script

Run the baseline script for simple text analysis:

```bash
python sentiment_baseline.py
```

**Features:**
- Interactive text input
- Displays all four scores (pos, neu, neg, compound)
- Shows sentiment label
- Continuous analysis until user types 'quit'

**Example Session:**
```
==============================================================
VADER Sentiment Analysis - Baseline Script
==============================================================

Enter text to analyze (or 'quit' to exit):

Text: I love this product!

------------------------------------------------------------
SENTIMENT ANALYSIS RESULTS:
------------------------------------------------------------
Positive Score: 0.746
Neutral Score:  0.254
Negative Score: 0.000
Compound Score: 0.6369

>>> SENTIMENT LABEL: POSITIVE <<<
------------------------------------------------------------
```

### Option 2: Streamlit Web Application (Recommended)

Launch the interactive web interface:

```bash
streamlit run sentiment_app.py
```

This will:
1. Start a local web server
2. Automatically open your browser to `http://localhost:8501`
3. Display the full-featured sentiment analysis application

**Web App Features:**
- Large text input area
- Real-time sentiment analysis
- Visual score display with progress bars
- Color-coded sentiment labels
- History of last 5 analyses
- Example texts in sidebar
- Responsive design

**How to Use the Web App:**
1. Enter or paste text in the text area
2. Click "🔍 Analyze Sentiment" button
3. View results: label, scores, and visualizations
4. Check the history panel for past analyses
5. Use example texts from the sidebar for testing

---

## Testing Summary

### Testing Methodology

A comprehensive test log was created with **25 manually entered test cases** to evaluate the VADER sentiment analyzer's performance across diverse text types.

### Test Distribution:

- **Regular Cases**: 15 straightforward examples
  - 5 clearly positive
  - 5 clearly negative
  - 5 neutral/factual

- **Tricky Cases**: 10 challenging examples
  - 3 sarcastic statements
  - 2 mixed sentiment statements
  - 3 modern slang expressions
  - 2 short/ambiguous phrases

### Results Summary:

| Metric | Value |
|--------|-------|
| Total Test Cases | 25 |
| Correct Predictions | 21 |
| Incorrect Predictions | 4 |
| **Overall Accuracy** | **84.00%** |

### Performance by Category:

1. **Regular Cases (15 tests)**: 15/15 correct (100%)
   - All straightforward positive, negative, and neutral statements were classified correctly

2. **Tricky Cases (10 tests)**: 6/10 correct (60%)
   - Struggled with sarcasm, modern slang, and complex mixed emotions
   - Performed well on some slang and short phrases

### Failed Test Cases Analysis:

1. **"Oh great, another meeting. Just what I needed."**
   - Expected: Negative (sarcasm)
   - Predicted: Positive
   - Reason: VADER detected "great" and missed sarcastic context

2. **"The movie was good but I'm disappointed with the ending."**
   - Expected: Neutral/Mixed
   - Predicted: Positive
   - Reason: "Good" weighted more heavily than "disappointed"

3. **"This is sick!"**
   - Expected: Positive (slang)
   - Predicted: Negative
   - Reason: "Sick" interpreted as illness, not as slang for "cool/awesome"

4. **Test #17** (mixed emotions case)
   - VADER focused on positive words, underweighted negative context

### Accuracy Calculation:

```
Accuracy = (Correct Predictions / Total Tests) × 100
Accuracy = (21 / 25) × 100
Accuracy = 84%
```

This 84% accuracy is **very good** for a lexicon-based tool on diverse text including challenging edge cases. For comparison, typical VADER accuracy on social media text ranges from 75-85%.

---

## Observations and Analysis

Based on testing with 25 diverse inputs, here are five key observations about VADER's behavior:

### 1. **Excellent Performance on Clear Statements**

VADER achieved 100% accuracy on straightforward positive, negative, and neutral statements. When text contains unambiguous sentiment words without sarcasm or irony, VADER's lexicon-based approach works exceptionally well.

**Example:**
- "I absolutely love this product!" → Correctly identified as Positive
- "This is terrible" → Correctly identified as Negative
- "The meeting is at 3 PM" → Correctly identified as Neutral

### 2. **Sarcasm Detection Remains a Challenge**

VADER struggles with sarcasm because it analyzes words independently without understanding contextual tone or speaker intent. Sarcastic statements often contain positive words used ironically.

**Example:**
- "Oh great, another meeting. Just what I needed." 
- Contains "great" (positive word) but is clearly sarcastic
- VADER predicted Positive when the actual sentiment is Negative

**Why This Happens:** Lexicon-based tools don't have contextual awareness or understanding of social cues that indicate sarcasm.

### 3. **Modern Slang Recognition is Inconsistent**

VADER's lexicon includes some slang (like "lit" which was correctly identified), but newer or context-dependent slang may be missed or misinterpreted.

**Successful Slang Detection:**
- "This app is lit! 🔥" → Correctly identified as Positive

**Failed Slang Detection:**
- "This is sick!" → Incorrectly identified as Negative (missed slang meaning)

**Implication:** The lexicon needs periodic updates to keep pace with evolving language.

### 4. **Capitalization and Punctuation Boost Intensity**

VADER's rules successfully detect emphasis from capitalization and exclamation marks, increasing the intensity of sentiment scores.

**Example:**
- "good" vs. "GOOD!!!" → The latter receives a higher positive score
- This helps capture emotional intensity in social media text

### 5. **Mixed Emotions Require Careful Interpretation**

When statements contain both positive and negative elements, VADER calculates a weighted compound score, but it may not always match human interpretation of "mixed" sentiment.

**Example:**
- "The movie was good but I'm disappointed with the ending"
- VADER weighted "good" more than "disappointed"
- Predicted: Positive (when expected was Neutral/Mixed)

**Consideration:** For applications requiring detection of mixed emotions, additional post-processing or alternative methods may be needed.

---

## Limitations and Improvements

### Current Limitations:

1. **Sarcasm and Irony**
   - Cannot detect sarcastic tone or ironic statements
   - Interprets words literally based on lexicon

2. **Context Independence**
   - Analyzes words in isolation without full sentence context
   - Misses nuanced meanings that depend on broader context

3. **Lexicon Currency**
   - May not include newest slang or evolving word meanings
   - Requires periodic updates to stay current

4. **Mixed Sentiment**
   - Provides a single compound score rather than detecting multiple emotions
   - May oversimplify complex emotional states

5. **Domain Specificity**
   - Optimized for social media text
   - May perform differently on formal text, academic writing, or specialized domains

6. **Language Limitation**
   - English-only (original VADER)
   - Other languages require different lexicons

### Suggested Improvements:

1. **Hybrid Approach**
   - Combine VADER with a transformer model (like BERT) for context understanding
   - Use VADER for speed, deep learning for accuracy on complex cases

2. **Sarcasm Detection Module**
   - Add a separate classifier to detect sarcastic patterns
   - Use contextual clues and punctuation patterns

3. **User Feedback Loop**
   - Allow users to correct misclassifications
   - Build a custom adjustment layer based on user corrections

4. **Domain Adaptation**
   - Create domain-specific lexicons for specialized fields
   - Fine-tune thresholds for different text types

5. **Multi-Label Classification**
   - Extend beyond positive/neutral/negative
   - Detect multiple emotions (joy, anger, sadness, fear, etc.)

6. **Continuous Lexicon Updates**
   - Regularly update with new slang from social media
   - Crowdsource word sentiment ratings

7. **Confidence Scores**
   - Add confidence metrics to indicate prediction reliability
   - Flag ambiguous cases for human review

8. **Batch Processing**
   - Add ability to analyze multiple texts at once
   - Export results to CSV for data analysis

---

## Prompt Engineering

This section documents the prompts used with AI coding assistants (GPT-5-Mini through VS Code Copilot) during development, following best practices in prompt engineering.

### Overview of AI Assistance

Throughout this project, I used GitHub Copilot with GPT-5-Mini to assist with coding, debugging, and documentation. The following prompts represent key interactions that helped shape the final implementation.

---

### Prompt 1: Core Sentiment Analysis Function

**Prompt Used:**
```
Create a Python function that uses the VADER SentimentIntensityAnalyzer to 
analyze a text input and return pos, neu, neg, and compound scores. Also 
return a sentiment label using these rules: Positive if compound >= 0.05, 
Negative if compound <= -0.05, Neutral otherwise. Include proper error 
handling for empty inputs.
```

**Intent:**
I needed the core analysis function that would be used in both the baseline script and the web app. I wanted to ensure it followed the exact labeling rules specified in the assignment and handled edge cases properly.

**AI Output (Accepted):**
```python
def analyze_sentiment(text):
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
        'pos': scores['pos'],
        'neu': scores['neu'],
        'neg': scores['neg'],
        'compound': compound,
        'label': label
    }
```

**What I Changed:**
- Added more descriptive docstring with parameter and return type documentation
- Added a timestamp field for history tracking in the web app version
- Modified the return structure to include the original text for logging purposes

**Evaluation:**
The AI-generated code provided a solid foundation. The logic was correct, and the threshold implementation matched requirements perfectly. However, it needed enhancements for production use (better documentation, additional metadata).

---

### Prompt 2: Streamlit UI with History Feature

**Initial Prompt:**
```
Create a Streamlit web interface for sentiment analysis with a text input, 
analyze button, and display of results.
```

**Refinement Process:**

This prompt was too vague and produced a basic UI without the required history feature. I refined it:

**Refined Prompt:**
```
Create a Streamlit web interface for VADER sentiment analysis that includes:
1. A text area for input
2. An analyze button
3. Display of sentiment label (Positive/Neutral/Negative) with color coding
4. Display of all four scores (pos, neu, neg, compound) in metric cards
5. A history panel showing the last 5 analyses with expandable details
6. Use Streamlit session state to persist history across interactions
```

**Intent:**
The assignment specifically required tracking the last 5 analyses. My initial prompt was too general, so I refined it to be more specific about all UI requirements.

**AI Output (Partially Accepted):**

The AI generated the basic structure with session state and history tracking. I accepted:
- Session state initialization
- History data structure
- Layout with columns
- Metric display for scores

**What I Changed/Added:**
- Added color coding based on sentiment label
- Implemented progress bars for score visualization
- Added a sidebar with example texts
- Improved the history display with expandable sections
- Added a "Clear History" button
- Enhanced CSS styling for better visual appeal

**Prompt Refinement Lesson:**
Being specific about requirements (especially features like "last 5 analyses") dramatically improved the output quality. The refined prompt saved significant debugging time.

---

### Prompt 3: Test Case Generation

**Prompt Used:**
```
Generate a diverse set of 25 test cases for VADER sentiment analysis including:
- 15 straightforward cases (positive, negative, neutral)
- 10 tricky cases including sarcasm, mixed emotions, modern slang, and short phrases
- Format as a markdown table with columns: Text, Expected Label, Predicted Label, Correct?
- Include at least 5 cases where VADER might struggle
```

**Intent:**
The assignment required 20+ test cases with at least 5 "tricky" ones. I wanted a diverse set that would thoroughly test VADER's capabilities and limitations.

**AI Output (Partially Accepted):**

The AI generated good examples for straightforward cases but the "tricky" cases weren't challenging enough initially.

**What I Changed:**
- Manually added more nuanced sarcasm examples
- Included context-dependent slang ("sick" as positive slang)
- Added edge cases with conflicting sentiment words
- Ran each test case through VADER and updated the "Predicted Label" column with actual results (AI had guessed at predictions)
- Added a "Notes" column to explain why certain cases failed

**Evaluation:**
The AI was helpful for generating initial test case ideas, but I needed to verify all predictions by actually running the tests. The AI's guesses about VADER's behavior weren't always accurate.

---

### Prompt 4: Debugging Empty Input Handling

**Prompt Used:**
```
This sentiment analysis function crashes when given an empty string. 
Show me how to safely handle empty input, whitespace-only input, and 
None values without throwing exceptions. Return a meaningful error 
message instead.
```

**Intent:**
During testing, I discovered the baseline script crashed on empty input. I needed robust error handling.

**AI Output (Accepted with Minor Changes):**
```python
if not text or text.strip() == "":
    return {
        'error': 'Empty input provided',
        'pos': 0.0,
        'neu': 0.0,
        'neg': 0.0,
        'compound': 0.0,
        'label': 'Neutral'
    }
```

**What I Changed:**
- For the web app version, I used Streamlit's `st.warning()` instead of returning an error dict
- Added user-friendly messaging: "⚠️ Please enter some text to analyze."

**Evaluation:**
The AI provided exactly what I needed. The error handling pattern was clean and comprehensive.

---

### Prompt 5: Documentation Generation

**Prompt Used:**
```
Write a comprehensive README section explaining what VADER is, how it works, 
its advantages and limitations, and why it's useful for sentiment analysis. 
Use clear academic language suitable for an AI course laboratory report.
```

**Intent:**
I needed to explain VADER's methodology for the documentation requirement but wanted to ensure accuracy and appropriate depth.

**AI Output (Heavily Edited):**

The AI provided a good overview, but it was too technical in some areas and too brief in others.

**What I Accepted:**
- Basic definition of VADER
- Explanation of lexicon-based approach
- List of features (emoticon handling, etc.)

**What I Rewrote:**
- Simplified the technical explanation of the algorithm
- Added concrete examples for each rule (capitalization, punctuation)
- Expanded the limitations section based on my actual testing results
- Added the "How VADER Works" step-by-step breakdown
- Included specific accuracy ranges from validation studies

**Evaluation:**
AI-generated documentation needed significant human oversight. While it provided a good starting point, domain knowledge and project-specific insights were essential for quality documentation.

---

### Prompt 6: Explaining VADER Limitations

**Prompt Used:**
```
Explain why lexicon-based sentiment analysis like VADER struggles with 
sarcasm, mixed emotions, and modern slang. Provide simple examples that 
a first-year AI student would understand. Focus on the technical reasons 
related to how VADER processes text.
```

**Intent:**
For the "Observations and Analysis" section, I needed to explain why certain test cases failed. I wanted technically accurate but accessible explanations.

**AI Output (Accepted with Examples Added):**

The AI explained:
- Lexicons analyze words independently → cannot detect sarcasm
- No contextual awareness → misses irony
- Static lexicon → doesn't update with new slang

**What I Added:**
- Specific failed examples from my test log
- Comparison to how humans understand sarcasm through context
- Discussion of why this is expected behavior, not a flaw
- Suggestions for hybrid approaches

**Evaluation:**
The AI provided good theoretical explanations, but connecting them to concrete test failures required human analysis.

---

### Prompt 7: Accuracy Calculation Verification

**Prompt Used:**
```
I have 25 test cases with 21 correct predictions. Show me the correct 
formula for calculating accuracy percentage and verify my calculation.
```

**Intent:**
I wanted to ensure my accuracy calculation was correct and properly formatted.

**AI Output (Accepted):**
```
Accuracy = (Correct Predictions / Total Tests) × 100
Accuracy = (21 / 25) × 100
Accuracy = 84%
```

**Evaluation:**
Simple and correct. This was a good use of AI for verification.

---

### Summary of Prompt Engineering Insights

**What Worked Well:**
1. **Specific, detailed prompts** produced better results than vague requests
2. **Iterative refinement** improved outputs significantly
3. **Requesting explanations** helped me understand the generated code
4. **Verification prompts** were useful for checking my work

**What Required Human Judgment:**
1. **Testing accuracy** - AI guessed at VADER behavior; I had to verify
2. **Code integration** - Combining AI-generated pieces into a cohesive app
3. **Documentation quality** - AI drafts needed significant editing for clarity
4. **Design decisions** - Choosing Streamlit, color schemes, layout

**Key Lesson:**
AI coding assistants are powerful tools for:
- Generating boilerplate code
- Providing initial implementations
- Explaining concepts
- Debugging specific issues

However, they **cannot replace**:
- Testing and verification
- Understanding project requirements
- Making architectural decisions
- Ensuring code quality and correctness

---

## AI Assistance Reflection

### How Copilot GPT-5-Mini Helped Me

1. **Rapid Prototyping**
   - Quickly generated baseline implementations of functions
   - Provided starting points that I could refine and customize
   - Saved time on boilerplate code (imports, basic structure)

2. **Learning Resource**
   - Explained Streamlit features I wasn't familiar with
   - Showed me how session state works in Streamlit
   - Demonstrated best practices for error handling

3. **Debugging Assistant**
   - Helped identify why empty input was causing crashes
   - Suggested improvements for code organization
   - Provided alternative approaches when my initial approach had issues

4. **Documentation Support**
   - Generated initial drafts of technical explanations
   - Helped structure the README with appropriate sections
   - Provided templates for test log formatting

### What I Learned from Reviewing AI Suggestions

1. **Critical Evaluation is Essential**
   - Not all AI-generated code is correct or optimal
   - Always test AI suggestions before accepting them
   - AI may not understand specific project requirements

2. **AI Excels at Patterns, Struggles with Novelty**
   - Good at generating standard functions and common patterns
   - Less effective for unique requirements or creative solutions
   - Needs clear, specific prompts to produce good results

3. **Verification is Mandatory**
   - AI "hallucinated" some VADER predictions in test cases
   - Generated documentation sometimes contained inaccuracies
   - Testing actual behavior is crucial

4. **Iterative Prompting Improves Results**
   - First attempt rarely produces perfect output
   - Refining prompts with more specificity yields better results
   - Breaking complex tasks into smaller prompts works better

### Why Human Understanding is Still Required

1. **Requirements Interpretation**
   - AI doesn't understand assignment rubrics or grading criteria
   - Only humans can ensure all requirements are met
   - Need human judgment for "what makes a good test case"

2. **Quality Assurance**
   - AI can't test its own output effectively
   - Humans must verify correctness, not just assume it
   - Edge cases and error handling need human consideration

3. **Integration and Architecture**
   - Combining separate AI-generated pieces requires understanding
   - Overall system design needs human planning
   - Trade-off decisions (Streamlit vs Flask) require domain knowledge

4. **Domain Expertise**
   - Understanding why VADER fails on sarcasm requires NLP knowledge
   - Explaining limitations requires understanding of the field
   - Connecting theory to practice is a human skill

5. **Ethical Responsibility**
   - Humans are accountable for the final code
   - Cannot blame AI for errors or shortcomings
   - Academic integrity requires understanding what you submit

6. **Creative Problem Solving**
   - AI suggests common solutions
   - Novel approaches to unique problems require human creativity
   - Adapting general solutions to specific contexts needs human insight

### Conclusion on AI Assistance

GitHub Copilot with GPT-5-Mini was an incredibly valuable tool for this project, significantly accelerating development and providing learning opportunities. However, it was a **tool to augment my abilities**, not a replacement for understanding and effort.

The most successful interactions involved:
- Me having a clear goal
- Providing specific, detailed prompts
- Critically evaluating AI output
- Testing and verifying suggestions
- Modifying and improving generated code

This project reinforced that effective use of AI coding assistants requires strong foundational knowledge. Without understanding sentiment analysis, Python, and web development, I wouldn't have been able to effectively guide, evaluate, and improve the AI's suggestions.

**Key Takeaway:** AI is a powerful assistant that makes developers more productive, but understanding, judgment, and responsibility remain fundamentally human tasks.

---

## Conclusion

This sentiment analysis project successfully implemented a complete VADER-based application with both command-line and web interfaces. The system achieved **84% accuracy** on a diverse test set, demonstrating strong performance on straightforward text while revealing expected limitations with sarcasm and modern slang.

The project fulfilled all requirements:
- ✅ Functional VADER implementation
- ✅ Clear labeling rules with proper thresholds
- ✅ Interactive web UI with history feature
- ✅ 25+ test cases with accuracy calculation
- ✅ Comprehensive documentation
- ✅ Detailed prompt engineering analysis
- ✅ Responsible AI use disclosure

Through this project, I gained hands-on experience with:
- Lexicon-based NLP techniques
- Web application development with Streamlit
- Systematic software testing and evaluation
- Effective prompt engineering
- Responsible use of AI coding assistants

The combination of traditional programming skills and modern AI assistance tools proved powerful when used thoughtfully and critically.

---

## References

- Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14).
- VADER GitHub Repository: https://github.com/cjhutto/vaderSentiment
- Streamlit Documentation: https://docs.streamlit.io
- Python vaderSentiment Library: https://pypi.org/project/vaderSentiment/

---

**End of Documentation**
