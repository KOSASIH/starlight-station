# natural_language_processing_module.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

nltk.download('punkt')
nltk.download('stopwords')

class NaturalLanguageProcessingModule:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.classifier = MultinomialNB()
        self.pipeline = Pipeline([
            ('vectorizer', self.vectorizer),
            ('classifier', self.classifier)
        ])

    def train(self, X_train, y_train):
        self.pipeline.fit(X_train, y_train)

    def predict(self, X_test):
        return self.pipeline.predict(X_test)

    def evaluate(self, X_test, y_test):
        return self.pipeline.score(X_test, y_test)

    def tokenize_text(self, text):
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token.isalpha()]
        tokens = [token for token in tokens if token not in stopwords.words('english')]
        return '.join(tokens)

    def sentiment_analysis(self, text):
        text_tokenized = self.tokenize_text(text)
        sentiment = self.pipeline.predict([text_tokenized])[0]
        return sentiment

    def topic_modeling(self, texts):
        vectorized_texts = self.vectorizer.transform(texts)
        topics = self.classifier.predict(vectorized_texts)
        return topics
