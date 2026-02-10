# Quick Start Guide

## Installation

1. **Install Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

   OR install individually:
   ```bash
   pip install vadersentiment streamlit
   ```

## Running the Application

### Option 1: Baseline Command-Line Script
```bash
python sentiment_baseline.py
```
- Interactive text analysis
- Type text and press Enter
- Type 'quit' to exit

### Option 2: Web Application (Recommended)
```bash
streamlit run sentiment_app.py
```
- Opens automatically in browser at http://localhost:8501
- Full featured UI with history
- Visual score displays

## Files Included

- `sentiment_baseline.py` - CLI sentiment analyzer
- `sentiment_app.py` - Streamlit web application
- `test_log.md` - Testing results (25 test cases)
- `README.md` - Complete documentation
- `requirements.txt` - Python dependencies
- `INSTRUCTIONS.md` - This file

## Testing

All test cases are documented in `test_log.md` with:
- 25 total test cases
- Expected vs predicted labels
- 84% accuracy achieved
- Analysis of failures

## Documentation

See `README.md` for:
- Complete project documentation
- VADER explanation
- Prompt engineering section
- AI assistance reflection
- Observations and limitations

## Submission Format

Create ZIP file:
```
Lastname_Firstname_AI_Sentiment_Project.zip
```

Contents:
- All .py files
- test_log.md
- README.md
- requirements.txt
- PDF with screenshots (convert README.md to PDF and add screenshots)

**Note:** Do NOT zip the PDF file, submit it separately.

## Screenshots to Include in PDF

1. Baseline script running with sample output
2. Streamlit app main interface
3. Analysis results display
4. History panel with 5 analyses
5. Test case examples

## Grading Checklist

- [x] VADER implementation (25 pts) - sentiment_baseline.py
- [x] User interface (25 pts) - sentiment_app.py with history
- [x] Testing log (20 pts) - 25 test cases in test_log.md
- [x] Code quality (15 pts) - Clean, modular code
- [x] Documentation (10 pts) - Comprehensive README.md
- [x] AI disclosure (5 pts) - Prompt engineering section included

**Total: 100 points**
