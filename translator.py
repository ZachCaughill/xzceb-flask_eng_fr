from deep_translator import MyMemoryTranslator
"""
This module translates text between French and English using MyMemoryTranslator.
"""
def english_to_french(english_text):
    '''
    Input text in English to return the French translation.
    '''
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    '''
    Input text in French to return the English translation
    '''
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
