nlp_module = NaturalLanguageProcessingModule()

# Train the model
X_train = [
    "This product is amazing!",
    "I love this product!",
    "This product is terrible.",
    "I hate this product.",
    "This product is okay.",
    "I'm neutral about this product."
]
y_train = [1, 1, 0, 0, 0.5, 0.5]  # 1: positive, 0: negative, 0.5: neutral

nlp_module.train(X_train, y_train)

# Predict sentiment
text = "This is a great product!"
sentiment = nlp_module.sentiment_analysis(text)
print("Sentiment:", sentiment)

# Predict topics
texts = [
    "I love playing basketball.",
    "The new iPhone is amazing.",
    "I'm so excited for the summer.",
    "This restaurant serves great food.",
    "I'm feeling sad today."
]
topics = nlp_module.topic_modeling(texts)
print("Topics:", topics)
