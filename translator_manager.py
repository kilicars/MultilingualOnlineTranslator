from translator import Translator
from colorful import Colorful


class TranslatorManager:
    def __init__(self):
        self.languages = {"1": "Arabic", "2": "German", "3": "English", "4": "Spanish", "5": "French",
                          "6": "Hebrew", "7": "Japanese", "8": "Dutch", "9": "Polish", "10": "Portuguese",
                          "11": "Romanian", "12": "Russian", "13": "Turkish"}

    def print_languages(self):
        """
        Prints the supported languages to the screen
        """
        print(Colorful.color_text("blue", "\nWelcome to the translator! Translator supports:\n"))
        for number, lang in self.languages.items():
            print(Colorful.color_text("blue", f"{number}. {lang}"))

    @staticmethod
    def get_parameters():
        """
        Gets parameters from the user
        """
        from_lang_number = input("\nType the number of your language:\n")
        to_lang_number = input("Type the number of a language you want to translate to or '0' to translate to all languages:\n")
        word = input("Type the word/phrase you want to translate:\n")
        return from_lang_number, to_lang_number, word

    def check_parameters(self, from_lang_number, to_lang_number):
        """
        Checks the parameters got from the user
        """
        error = None
        if from_lang_number not in self.languages:
            error = "First language number is not in the supported languages list"
        elif to_lang_number not in self.languages and to_lang_number != "0":
            error = "Second language number needs to be in the supported languages list or it can be 0"
        return error

    @staticmethod
    def save_to_file(file_name, text):
        with open(file_name, "w", encoding="utf-8") as output_file:
            output_file.write(text)

    def translate_to_all(self, from_lang_number, word):
        """
        Translates the word to all languages in the list and
        prints the output to the screen and to the file
        :param from_lang_number: Original language
        :param word: Word to be translated
        """
        all_translations = ""
        for lang_number in self.languages:
            if from_lang_number != lang_number:
                response = self.get_translation_response(from_lang_number, lang_number, word)
                if response.error_code != 0:
                    translation_output = response.error_message
                    print(self.get_error_output(response.error_message))
                    # for these error codes, no need to try other languages
                    if response.error_code in [1, 2]:
                        break
                else:
                    translation_output = self.get_output_result(lang_number, response.translations, response.example_sentences, output_number=1)
                    print(translation_output)  # prints the colorful text
                    # this output will be added to the file
                    translation_output = self.get_output_result(lang_number, response.translations, response.example_sentences, output_number=1, colorful=False)

                # error message or translation output is appended to the result string
                all_translations += f"{translation_output}\n"
        if len(all_translations) > 0:
            file_name = f"{word}.txt"
            self.save_to_file(file_name, all_translations)
            print(Colorful.color_text("green", f"\nAll results saved to '{file_name}'\n"))

    def translate_to_one(self, from_lang_number, to_lang_number, word):
        """
        Translates the word and prints the output to the screen
        :param from_lang_number: Original language
        :param to_lang_number: Target language
        :param word: Word to be translated
        """
        response = self.get_translation_response(from_lang_number, to_lang_number, word)
        if response.error_message:
            print(self.get_error_output(response.error_message))
        else:
            print(self.get_output_result(to_lang_number, response.translations, response.example_sentences, output_number=5))

    def get_translation_response(self, from_lang_number, to_lang_number, word):
        """
        Gets the translation response for the word from the original language to the target language
        """
        from_language = self.languages[from_lang_number]
        to_language = self.languages[to_lang_number]
        return Translator(from_language, to_language).translate(word)

    @staticmethod
    def get_error_output(error):
        return Colorful.color_text("red", error)

    def get_output_result(self, lang_number, translations, example_sentences, output_number, colorful=True):
        """
        Prepares the formatted output for the given translations
        :param lang_number: Translation language number
        :param translations: Translations
        :param example_sentences: Example sentences
        :param output_number: Number of translations and example sentences to be shown
        :param colorful: Indicates if the output will be colorful
        """
        language = self.languages[lang_number]
        result = f"{language} translation cannot be found\n"
        if colorful:
            result = self.get_error_output(result)

        if translations:
            translations_count = min(output_number, len(translations))
            shown_translations = translations[0:translations_count]

            sentence_count = min(output_number * 2, len(example_sentences))
            shown_sentences = example_sentences[0:sentence_count]

            result = f"{language} Translations:\n"
            if colorful:
                result = Colorful.color_text("magenta", result)
            result += "\n".join(shown_translations) + "\n"
            if colorful:
                result += Colorful.color_text("magenta", f"\n{language} Examples:\n")
            else:
                result += f"\n{language} Examples:\n"
            for i in range(0, len(shown_sentences), 2):
                result += f"{shown_sentences[i]}\n"
                result += f"{shown_sentences[i + 1]}\n\n"

        return result

    def main(self):
        self.print_languages()
        from_lang_number, to_lang_number, word = self.get_parameters()
        error = self.check_parameters(from_lang_number, to_lang_number)
        if error:
            print(self.get_error_output(f"\n{error}\n"))
        else:
            if to_lang_number == "0":
                self.translate_to_all(from_lang_number, word)
            else:
                self.translate_to_one(from_lang_number, to_lang_number, word)


if __name__ == '__main__':
    answer = "y"
    while answer.lower() == "y":
        TranslatorManager().main()
        answer = input("Press 'Y' or 'y' to continue or any other key to exit: ")
