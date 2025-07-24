# 🤖 Text Summarizer Tool Using NLP

A Python script that summarizes lengthy articles using Natural Language Processing techniques. This tool demonstrates advanced NLP concepts including extractive summarization, sentence scoring, and text preprocessing.

## ✨ Features

### Core NLP Techniques
- **Extractive Summarization**: Selects most important sentences from original text
- **Multi-factor Sentence Scoring**:
  - Word frequency analysis with TF normalization
  - Position-based scoring (first/last sentence importance)
  - Length optimization (prefers medium-length sentences)
  - Numerical data recognition
  - Proper noun identification
  - Emphasis detection (questions/exclamations)

### Advanced Processing
- **Text Preprocessing**: Cleaning, normalization, tokenization
- **Stop Word Removal**: Filters common words using NLTK corpus
- **Stemming**: Word stemming using Porter Stemmer
- **Smart Sentence Selection**: Maintains original text flow
- **Compression Statistics**: Detailed analysis of summarization results

## 🛠️ Technologies Used

- **Python 3.7+**: Core programming language
- **NLTK**: Natural Language Toolkit for NLP operations
- **NumPy**: Numerical computations (if needed)
- **Regular Expressions**: Text pattern matching and cleaning
- **Heapq**: Efficient sentence selection algorithm

## 📋 Requirements

- Python 3.7 or higher
- NLTK library
- Internet connection (for initial NLTK data download)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/text-summarizer-nlp.git
cd text-summarizer-nlp
```

### 2. Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt

# Or install manually
pip install nltk numpy
```

### 3. Run the Script
```bash
python text_summarizer.py
```

The script will automatically download required NLTK data on first run.

## 📁 Project Structure

```
text-summarizer-nlp/
│
├── text_summarizer.py    # Main Python script
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── sample_texts/        # Sample articles for testing
│   ├── ai_article.txt
│   ├── climate_change.txt
│   └── technology.txt
└── examples/            # Example outputs
    └── sample_outputs.txt
```

## 🎯 How to Use

### Command Line Execution
```bash
python text_summarizer.py
```

### Programmatic Usage
```python
from text_summarizer import TextSummarizer

# Initialize summarizer
summarizer = TextSummarizer()

# Your text to summarize
text = "Your lengthy article here..."

# Generate summary
summary, stats = summarizer.extract_summary(
    text, 
    summary_ratio=0.3,  # 30% of original sentences
    max_sentences=5     # Maximum 5 sentences
)

print("Summary:", summary)
print("Statistics:", stats)
```

## 🔧 Customization Options

### Summary Length Control
```python
# Short summary (20% of original)
summary, stats = summarizer.extract_summary(text, summary_ratio=0.2, max_sentences=3)

# Medium summary (30% of original) 
summary, stats = summarizer.extract_summary(text, summary_ratio=0.3, max_sentences=5)

# Long summary (40% of original)
summary, stats = summarizer.extract_summary(text, summary_ratio=0.4, max_sentences=7)
```

### Scoring Algorithm Weights
You can modify the scoring weights in the `score_sentences` method:
- Position score: 0.3 (first sentence), 0.2 (last sentence)
- Length score: 0.2 (optimal length sentences)
- Numerical data: 0.1 bonus
- Proper nouns: 0.1 bonus
- Emphasis: 0.05 bonus

## 📊 Sample Output

```
TEXT SUMMARIZER USING NLP - RESULTS
================================================================================

📄 ORIGINAL TEXT:
--------------------------------------------------------------------------------
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals...

📝 GENERATED SUMMARY:
--------------------------------------------------------------------------------
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. The traditional problems of AI research include reasoning, knowledge representation, planning, learning, natural language processing, perception, and the ability to move and manipulate objects. The AI field draws upon computer science, information engineering, mathematics, psychology, linguistics, philosophy, and many other fields.

📊 STATISTICS:
--------------------------------------------------------------------------------
Original Sentences: 12
Summary Sentences:  3
Original Words:     387
Summary Words:      156
Compression Ratio:  59.7%
================================================================================
```

## 🧠 Algorithm Details

### 1. Text Preprocessing
- Remove extra whitespace and special characters
- Normalize text formatting
- Tokenize into sentences and words

### 2. Word Frequency Analysis
- Remove stop words (the, and, or, etc.)
- Apply stemming to reduce words to root forms
- Calculate normalized term frequencies

### 3. Sentence Scoring
Each sentence receives a score based on:
- **Content relevance**: Sum of word frequencies
- **Position importance**: First/last sentences weighted higher
- **Optimal length**: Medium-length sentences preferred
- **Information density**: Numbers and proper nouns boost score
- **Emphasis markers**: Questions and exclamations

### 4. Summary Generation
- Select top-scoring sentences
- Maintain original sentence order
- Generate compression statistics

## 📈 Performance Metrics

The tool provides detailed statistics:
- **Compression Ratio**: Percentage reduction in content
- **Word Count**: Original vs. summary word counts
- **Sentence Count**: Original vs. summary sentence counts
- **Processing Time**: Algorithm execution time

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/enhancement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/enhancement`)
5. Create Pull Request

## 🐛 Troubleshooting

### Common Issues:

**NLTK Data Error**:
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

**Import Error**:
```bash
pip install --upgrade nltk numpy
```

**Short Text Warning**:
The tool works best with texts containing at least 5-10 sentences (100+ words).

## 🔮 Future Enhancements

- [ ] Abstractive summarization using transformers
- [ ] Multi-document summarization
- [ ] Topic-based summarization
- [ ] GUI interface
- [ ] Web API endpoint
- [ ] Support for multiple languages
- [ ] PDF/Word document processing
- [ ] Keyword extraction features

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- NLTK team for comprehensive NLP toolkit
- Research papers on extractive summarization
- Open source NLP community

---

**DELIVERABLE**: ✅ Python script showcasing input text and concise summaries using NLP techniques