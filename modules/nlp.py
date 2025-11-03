"""
Central AI V2 - NLP Utilities
Basic text processing functions
"""

import re

def clean_text(text):
    """Clean and normalize text"""
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text.strip()

def extract_code_blocks(text):
    """Extract code blocks from markdown-style text"""
    pattern = r'```(\w+)?\n(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    
    code_blocks = []
    for match in matches:
        language = match[0] if match[0] else 'text'
        code = match[1].strip()
        code_blocks.append({
            'language': language,
            'code': code
        })
    
    return code_blocks

def detect_language(text):
    """Detect if text contains Indonesian or English"""
    indonesian_words = ['adalah', 'dengan', 'untuk', 'yang', 'ini', 'itu', 'dari', 'atau']
    english_words = ['is', 'are', 'the', 'and', 'for', 'with', 'this', 'that']
    
    text_lower = text.lower()
    
    indo_count = sum(1 for word in indonesian_words if word in text_lower)
    eng_count = sum(1 for word in english_words if word in text_lower)
    
    if indo_count > eng_count:
        return 'id'
    elif eng_count > indo_count:
        return 'en'
    else:
        return 'unknown'

def tokenize(text):
    """Simple word tokenization"""
    # Remove punctuation and split
    text = re.sub(r'[^\w\s]', ' ', text)
    tokens = text.lower().split()
    return tokens

def analyze_sentiment(text):
    """Basic sentiment analysis"""
    positive_words = ['bagus', 'baik', 'senang', 'suka', 'hebat', 'keren', 'mantap', 'good', 'great', 'happy', 'love', 'excellent']
    negative_words = ['buruk', 'jelek', 'sedih', 'benci', 'bad', 'terrible', 'hate', 'sad', 'awful']
    
    text_lower = text.lower()
    
    pos_count = sum(1 for word in positive_words if word in text_lower)
    neg_count = sum(1 for word in negative_words if word in text_lower)
    
    if pos_count > neg_count:
        return 'positive'
    elif neg_count > pos_count:
        return 'negative'
    else:
        return 'neutral'
