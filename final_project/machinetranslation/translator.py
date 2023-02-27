import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']
VERSION='2018-05-01',

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(URL)


def english_to_french(english_text):
    """
    Translates the input English text to French using the IBM Watson Language Translator service.

    Args:
        english_text (str): The English text to be translated.

    Returns:
        str: The French translation of the input English text.
    """
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        #Getting the pure translation string
        french_text = translation['translations'][0]['translation']
        return french_text
    except Exception as error:
        text=english_text
        if text == "" :
            return ""
        else :
            print(error)
            return None


def french_to_english(french_text):
    """
    Translates the input French text to English using the IBM Watson Language Translator service.

    Args:
        french_text (str): The French text to be translated.

    Returns:
        str: The English translation of the input French text.
    """
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        #Getting the pure translation string
        english_text = translation['translations'][0]['translation']
        return english_text
    except Exception as error:
        text=french_text
        if text == "" :
            return ""
        else :
            print(error)
            return None
