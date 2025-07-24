#!/usr/bin/env python3
"""
Text Summarizer Tool Using NLP
===============================
A Python script that summarizes lengthy articles using Natural Language Processing techniques.

Author: Your Name
Date: 2024
"""

import re
import nltk
import heapq
from collections import defaultdict, Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

# Download required NLTK data (run once)
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    print("Downloading required NLTK data...")
    nltk.download('punkt')
    nltk.download('stopwords')

class TextSummarizer:
    """
    A comprehensive text summarizer using extractive NLP techniques.
    """
    
    def __init__(self):
        """Initialize the text summarizer with required components."""
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        
    def preprocess_text(self, text):
        """
        Clean and preprocess the input text.
        
        Args:
            text (str): Raw input text
            
        Returns:
            str: Cleaned text
        """
        # Remove extra whitespace and normalize
        text = re.sub(r'\s+', ' ', text.strip())
        
        # Remove special characters but keep sentence endings
        text = re.sub(r'[^\w\s\.\!\?]', '', text)
        
        return text
    
    def calculate_word_frequencies(self, text):
        """
        Calculate word frequencies excluding stop words.
        
        Args:
            text (str): Input text
            
        Returns:
            dict: Word frequencies
        """
        # Tokenize into words
        words = word_tokenize(text.lower())
        
        # Remove stop words and punctuation
        filtered_words = [
            self.stemmer.stem(word) for word in words 
            if word not in self.stop_words and word not in string.punctuation
            and len(word) > 2
        ]
        
        # Calculate frequencies
        word_freq = Counter(filtered_words)
        
        # Normalize frequencies
        max_freq = max(word_freq.values()) if word_freq else 1
        for word in word_freq:
            word_freq[word] = word_freq[word] / max_freq
            
        return word_freq
    
    def score_sentences(self, sentences, word_freq):
        """
        Score sentences based on multiple NLP factors.
        
        Args:
            sentences (list): List of sentences
            word_freq (dict): Word frequency dictionary
            
        Returns:
            dict: Sentence scores
        """
        sentence_scores = {}
        
        for i, sentence in enumerate(sentences):
            words = word_tokenize(sentence.lower())
            word_count = len([word for word in words if word not in string.punctuation])
            
            if word_count == 0:
                continue
                
            score = 0
            
            # 1. Word frequency score
            for word in words:
                stemmed_word = self.stemmer.stem(word)
                if stemmed_word in word_freq:
                    score += word_freq[stemmed_word]
            
            # 2. Position score (first and last sentences are important)
            position_score = 0
            if i == 0:  # First sentence
                position_score = 0.3
            elif i == len(sentences) - 1:  # Last sentence
                position_score = 0.2
            elif i < len(sentences) * 0.3:  # Early sentences
                position_score = 0.1
                
            # 3. Length score (prefer medium-length sentences)
            length_score = 0
            if 10 <= word_count <= 25:
                length_score = 0.2
            elif 5 <= word_count <= 35:
                length_score = 0.1
                
            # 4. Numerical data score
            numerical_score = 0.1 if re.search(r'\d', sentence) else 0
            
            # 5. Proper noun score
            proper_noun_score = 0.1 if re.search(r'[A-Z][a-z]+', sentence) else 0
            
            # 6. Question/exclamation bonus
            emphasis_score = 0.05 if re.search(r'[!?]', sentence) else 0
            
            # Combine all scores
            total_score = (score / word_count) + position_score + length_score + numerical_score + proper_noun_score + emphasis_score
            
            sentence_scores[i] = total_score
            
        return sentence_scores
    
    def extract_summary(self, text, summary_ratio=0.3, max_sentences=5):
        """
        Extract summary from text using NLP techniques.
        
        Args:
            text (str): Input text to summarize
            summary_ratio (float): Ratio of sentences to include (0.1 to 0.5)
            max_sentences (int): Maximum sentences in summary
            
        Returns:
            tuple: (summary_text, statistics)
        """
        # Preprocess text
        clean_text = self.preprocess_text(text)
        
        # Tokenize into sentences
        sentences = sent_tokenize(clean_text)
        
        if len(sentences) <= 2:
            return text, {"original_sentences": len(sentences), "summary_sentences": len(sentences), "compression_ratio": 0}
        
        # Calculate word frequencies
        word_freq = self.calculate_word_frequencies(clean_text)
        
        # Score sentences
        sentence_scores = self.score_sentences(sentences, word_freq)
        
        # Determine number of sentences for summary
        num_sentences = min(
            max_sentences,
            max(1, int(len(sentences) * summary_ratio))
        )
        
        # Select top sentences
        top_sentences = heapq.nlargest(num_sentences, sentence_scores.items(), key=lambda x: x[1])
        
        # Sort selected sentences by original order
        top_sentences.sort(key=lambda x: x[0])
        
        # Create summary
        summary_sentences = [sentences[i] for i, _ in top_sentences]
        summary_text = ' '.join(summary_sentences)
        
        # Calculate statistics
        original_words = len(word_tokenize(text))
        summary_words = len(word_tokenize(summary_text))
        compression_ratio = round((1 - summary_words / original_words) * 100, 1)
        
        statistics = {
            "original_sentences": len(sentences),
            "summary_sentences": len(summary_sentences),
            "original_words": original_words,
            "summary_words": summary_words,
            "compression_ratio": compression_ratio
        }
        
        return summary_text, statistics

def print_separator(char="=", length=80):
    """Print a separator line."""
    print(char * length)

def display_results(original_text, summary, stats):
    """
    Display the summarization results in a formatted way.
    
    Args:
        original_text (str): Original input text
        summary (str): Generated summary
        stats (dict): Summarization statistics
    """
    print_separator("=")
    print("TEXT SUMMARIZER USING NLP - RESULTS")
    print_separator("=")
    
    print("\n📄 ORIGINAL TEXT:")
    print_separator("-")
    print(f"{original_text}\n")
    
    print("📝 GENERATED SUMMARY:")
    print_separator("-")
    print(f"{summary}\n")
    
    print("📊 STATISTICS:")
    print_separator("-")
    print(f"Original Sentences: {stats['original_sentences']}")
    print(f"Summary Sentences:  {stats['summary_sentences']}")
    print(f"Original Words:     {stats['original_words']}")
    print(f"Summary Words:      {stats['summary_words']}")
    print(f"Compression Ratio:  {stats['compression_ratio']}%")
    print_separator("=")

def main():
    """Main function to demonstrate the text summarizer."""
    print("🤖 TEXT SUMMARIZER TOOL USING NLP")
    print("==================================")
    print("This tool summarizes lengthy articles using Natural Language Processing techniques.\n")
    
    # Initialize summarizer
    summarizer = TextSummarizer()
    
    # Sample text for demonstration
    sample_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of 'intelligent agents': any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. Colloquially, the term 'artificial intelligence' is often used to describe machines that mimic 'cognitive' functions that humans associate with the human mind, such as 'learning' and 'problem solving'.
    
    As machines become increasingly capable, tasks considered to require 'intelligence' are often removed from the definition of AI, a phenomenon known as the AI effect. For instance, optical character recognition is frequently excluded from things considered to be AI, having become a routine technology. Capabilities currently classified as AI include successfully understanding human speech, competing at the highest level in strategic game systems, autonomously operating cars, intelligent routing in content delivery networks, and military simulations.
    
    The traditional problems of AI research include reasoning, knowledge representation, planning, learning, natural language processing, perception, and the ability to move and manipulate objects. General intelligence is among the field's long-term goals. Approaches include statistical methods, computational intelligence, and traditional symbolic AI. Many tools are used in AI, including versions of search and mathematical optimization, artificial neural networks, and methods based on statistics, probability, and economics.
    
    The AI field draws upon computer science, information engineering, mathematics, psychology, linguistics, philosophy, and many other fields. The field was founded on the assumption that human intelligence 'can in principle be so precisely described that a machine can be made to simulate it'. This raises philosophical arguments about the mind and the ethics of creating artificial beings endowed with human-like intelligence.
    """
    
    print("Using sample text about Artificial Intelligence...\n")
    
    # Different summary lengths
    summary_types = [
        ("Short Summary (20%)", 0.2, 3),
        ("Medium Summary (30%)", 0.3, 5),
        ("Long Summary (40%)", 0.4, 7)
    ]
    
    for summary_name, ratio, max_sent in summary_types:
        print(f"\n🔍 {summary_name}")
        print("-" * 50)
        
        # Generate summary
        summary, stats = summarizer.extract_summary(
            sample_text, 
            summary_ratio=ratio, 
            max_sentences=max_sent
        )
        
        # Display results
        print(f"Summary ({stats['summary_sentences']} sentences):")
        print(f"{summary}\n")
        print(f"Compression: {stats['compression_ratio']}% | Words: {stats['original_words']} → {stats['summary_words']}")
        print_separator("-", 50)
    
    # Interactive mode
    print("\n" + "="*60)
    print("INTERACTIVE MODE")
    print("="*60)
    print("Enter your own text to summarize (or press Enter to exit):")
    
    while True:
        user_input = input("\n📝 Enter text to summarize: ").strip()
        
        if not user_input:
            print("👋 Thank you for using the Text Summarizer!")
            break
            
        if len(user_input) < 100:
            print("⚠️  Please enter at least 100 characters for better summarization.")
            continue
            
        # Generate summary
        summary, stats = summarizer.extract_summary(user_input)
        
        # Display results
        display_results(user_input, summary, stats)
        
        continue_choice = input("\nWould you like to summarize another text? (y/n): ").lower()
        if continue_choice != 'y':
            print("👋 Thank you for using the Text Summarizer!")
            break

if __name__ == "__main__":
    main()