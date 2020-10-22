from colorama import Fore


class Colorful:
    @staticmethod
    def color_text(color, text):
        colors = {
            "blue": Fore.BLUE,
            "green": Fore.GREEN,
            "magenta": Fore.MAGENTA,
            "red": Fore.RED,
            "yellow": Fore.YELLOW,
            "cyan": Fore.CYAN
        }
        return f"{colors[color]}{text}{Fore.RESET}"
