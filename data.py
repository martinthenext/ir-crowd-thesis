from sklearn.externals import joblib

vectorizer = joblib.load('pickles/vectorizer.pkl')
topic_texts_relevances_variances = joblib.load('pickles/data.pkl')