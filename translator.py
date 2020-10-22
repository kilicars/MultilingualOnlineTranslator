import requests
from html_parser import Parser


class TranslationResponse:
    def __init__(self, translations, example_sentence, error_code, error_message):
        self.translations = translations
        self.example_sentences = example_sentence
        self.error_code = error_code
        self.error_message = error_message


class Translator:
    def __init__(self, from_language, to_language):
        self.from_language = from_language
        self.to_language = to_language
        self.word = None

    def get_url(self):
        translation_host = "https://context.reverso.net/translation"
        translate_from_to = f"{self.from_language.lower()}-{self.to_language.lower()}"
        return f"{translation_host}/{translate_from_to}/{self.word}"

    @staticmethod
    def get_translations(page_content):
        return Parser.parse_page(page_content, "translations-content", "translation")

    @staticmethod
    def get_example_sentences(page_content):
        return Parser.parse_page(page_content, "examples-content", ["ltr", "rtl"])

    def translate(self, word):
        translations = None
        example_sentences = None
        error_code = 0  # success
        error = None
        self.word = word
        try:
            response = requests.get(self.get_url(), headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200:
                translations = self.get_translations(response.content)
                example_sentences = self.get_example_sentences(response.content)
            elif response.status_code == 404:
                error_code = 1
                error = f"\nSorry, unable to find {word}\n"
        except requests.exceptions.ConnectionError:
            error_code = 2
            error = "\nSomething wrong with your internet connection\n"

        return TranslationResponse(translations, example_sentences, error_code, error)
