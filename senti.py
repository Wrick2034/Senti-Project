import nltk
nltk.download('all')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.util import mark_negation

# # Function to detect negation words in the text
# def detect_negation_words(text):
    
#     tokenized_text = word_tokenize(text.lower())
#     negation_detected = False
#     negation_scope = []

#     for word in tokenized_text:
#         if word in negation_words:
#             negation_detected = True
#             negation_scope.append(word)
#         else:
#             if negation_detected:
#                 negation_scope.append(word)

#     return " ".join(negation_scope)

def textPreprocessor(text):
  # Tokenization
  tokens =  word_tokenize(text.lower())

  negation_words= ["not", "no", "never","don't","would'nt"]
  for i in tokens:
    if i in negation_words:
      i+="_"

  # Remove stopwords
  filtered_tokens=[token for token in tokens if token not in stopwords.words('english') and negation_words]

  # Lemmanize the tokens
  lemmatizer = WordNetLemmatizer()
  lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

  # Join the tokens back into a string
  processed_text = ' '.join(lemmatized_tokens)

  return processed_text

def sentiment_analyzer(text):
  analyzer = SentimentIntensityAnalyzer()
  scores = analyzer.polarity_scores(text)
  sentiment = 'POSITIVE' if scores['pos']>0 else 'NEGATIVE'
  return sentiment

review=input("\n\n\n\nEnter a statement to see its sentiment : ")
print("Predicted Sentiment :",sentiment_analyzer(textPreprocessor(review)))
# print("Sentiment Analysis Model Accuracy :", accuracy)
