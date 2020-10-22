from bs4 import BeautifulSoup


class Parser:
    @staticmethod
    def parse_page(content, element_id, css_class):
        result = []
        soup = BeautifulSoup(content, "html.parser")
        elements = soup.find(attrs={"id": element_id})
        if elements:
            names = elements.findAll(attrs={"class": css_class})
            for name in names:
                result.append(name.text.strip())
        return result
