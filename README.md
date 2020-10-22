# Multilingual Online Translator

This is a multilingual online translator which supports the following languages:

```
Welcome to the translator! Translator supports:

1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish
```

You can get translations of a word/phrase from one language to another or to all languages in the list. 
If you choose to translate to all languages, a file including the results is created as well. You can see a sample output file [here](https://github.com/kilicars/MultilingualOnlineTranslator/blob/master/how%20are%20you.txt)

Demo of the projects is below:

![translator](https://user-images.githubusercontent.com/37106831/96918086-6cfa2880-14b2-11eb-92f3-e5ee57610cec.gif)

Translations are fetched from [Reverso](https://context.reverso.net/translation/) website using web scraping.

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is used for web scraping and [Colorama](https://pypi.org/project/colorama/) is used to color the text.

The following packages are installed to the project in the beginning:

```pip install bs4 colorama requests```

You can run the project as:

```translator_manager.py```
