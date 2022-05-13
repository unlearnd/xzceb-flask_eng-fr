"""
    Simplifies translation of select languages
    via the IBM Watson language translation api.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']
VERSION_LT='2018-05-01'

# Initialize the IBM Watson translator service
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(\
    version=VERSION_LT,authenticator=authenticator)
language_translator.set_service_url(URL)

def english_to_french(english_text):
    """
    Translates the text provided from English to French.
    """
    response = language_translator.translate(\
        text=english_text, model_id='en-fr').get_result()
    french_text = response['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    """
    Translates the text provided from French to English.
    """
    response = language_translator.translate(\
        text=french_text, model_id='fr-en').get_result()
    english_text = response['translations'][0]['translation']

    return english_text
