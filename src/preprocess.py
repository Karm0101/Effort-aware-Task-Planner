import re
import nltk
from nltk import PorterStemmer, WordNetLemmatizer

def lowercase(text):
    return text.lower()

def removeURLs(text):
    noURLs = re.compile(r'(http|https)://\S+')
    cleanedText = noURLs.sub('', text)
    return cleanedText

def removeNonWords(text):
    text = ' '.join(text)
    onlyWords = re.compile(r'[^\w\s]')
    cleanedText = onlyWords.sub('', text)

    cleanedText = cleanedText.split(' ')
    return cleanedText

def tokenizeText(text):
    return text.split(' ')

def removeStopWords(text):
    stopWords = ["a", "an", "the", "and", "but", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about"
                "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down"
                "in", "out", "over", "under", "further", "then", "once", "here", "there", "when", "where", "why", "how", "any",
                "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "can", "will", "just", "is", "now"]
    filteredWords = []

    for word in (text):
        if word not in stopWords:
            filteredWords.append(word)
    
    return filteredWords

def lemmatizeText(text):
    lemmatizer = WordNetLemmatizer()
    lemmatizedText = []

    for word in text:
        lemmatizedText.append(lemmatizer.lemmatize(word, 'v'))

    return lemmatizedText

def preprocessor(text):
    text = lowercase(text)
    text = removeURLs(text)
    text = tokenizeText(text)
    text = lemmatizeText(text)
    text = removeStopWords(text)
    text = removeNonWords(text)

    return ' '.join(text)