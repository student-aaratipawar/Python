# spam_detector.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Step 1: Load Dataset
# Download this file from: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
# Rename to spam.csv and put it in the same folder as this script
df = pd.read_csv("spam.csv", encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']

# Step 2: Convert Labels to Numbers (ham = 0, spam = 1)
df['label_num'] = df.label.map({'ham': 0, 'spam': 1})

# Step 3: Split into Train and Test
X = df['message']
y = df['label_num']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Convert Text to TF-IDF Features
vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Step 5: Train Naive Bayes Model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Step 6: Predict
y_pred = model.predict(X_test_tfidf)

# Step 7: Show Accuracy and Report
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Optional: Predict your own message
while True:
    msg = input("\nEnter a message to check (or type 'exit'): ")
    if msg.lower() == 'exit':
        break
    msg_tfidf = vectorizer.transform([msg])
    prediction = model.predict(msg_tfidf)
    print("Prediction:", "SPAM" if prediction[0] == 1 else "HAM")
