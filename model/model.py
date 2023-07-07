import pandas as pd
import numpy as np
from keras.models import load_model
import joblib

vectorizer = joblib.load('model/vectorizer.joblib')
train_min = joblib.load('model/train_min.joblib')
train_max = joblib.load('model/train_max.joblib')
encoder = joblib.load('model/encoder.joblib')
feature_names = joblib.load('model/feature_names.joblib')


model = load_model('model/language_detection_model.h5')
dict = {"deu": "German",
        "rus": "Russian",
        "fra": "French",
        "eng": "English",
        "spa": "Spanish",
        "ita": "Italian",
        "nld": "Dutch",
        "epo": "Esperanto",
        "por": "Portuguese",
        "jpn": "Japanese",
        "kor": "Korean",
        "bul": "Bulgarian",
        "swe": "Swedish",
        "ukr": "Ukrainian",
        "ces": "Czech",
        "ara": "Arabic",
        "ben": "Bengali",
        "hin": "Hindi",
        "mar": "Marathi",
        "ell": "Greek"
        }


def predict_language(sentence):
    preprocessed_sentence = vectorizer.transform([sentence])
    preprocessed_sentence = pd.DataFrame(data=preprocessed_sentence.toarray(), columns=feature_names)
    preprocessed_sentence = (preprocessed_sentence - train_min) / (train_max - train_min)

    predicted_probabilities = model.predict(preprocessed_sentence)

    predicted_label = encoder.inverse_transform(np.argmax(predicted_probabilities, axis=-1))

    return dict[predicted_label[0]]

