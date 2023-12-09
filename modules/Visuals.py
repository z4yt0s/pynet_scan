from time import sleep
from rich.console import Console
from rich.theme import Theme
from rich.text import Text

"""
Visuals: is in charge of setting, preparing and rendering all the visual elements of 
the tool (tables, alignments, colours, banners, etc).
"""
class Visuals:
    type_msg = {
        'info': 'bold dodger_blue3',
        'warning': 'bold gold3',
        'error': 'bold red3'
    }
    """
    (Constructor)
    """
    def __init__(self, type_msg='default') -> None:
        # i think this has been result a error check more later (dict bad theme)
        # i think need early return check later
        #if type_msg == 'default':
            #self.type_msg = Visuals.type_msg
        self.console = Console(color_system='256', theme=Theme(Visuals.type_msg))
        self.text = Text()

    """
    This print the banner of the tool
    """
    def banner(self):
        name = [
            '                            __                           ',
            '    ____  __  ______  ___  / /_     ______________ _____ ',
            '   / __ \\/ / / / __ \\/ _ \\/ __/    / ___/ ___/ __ `/ __ \\',
            '  / /_/ / /_/ / / / /  __/ /_     (__  ) /__/ /_/ / / / /',
            ' / .___/\\__, /_/ /_/\\___/\\__/____/____/\\___/\\__,_/_/ /_/ ',
            '/_/    /____/              /_____/                       '
        ]
        logo = [
            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
            '⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀',
            '⠀⠀⠀⣠⣶⡿⣿⣿⡿⠋⠉⠀⠀⠉⠙⢿⣿⡿⣷⣦⡀⠀⠀⠀',
            '⠀⢀⣼⠟⠁⢠⣿⠏⠀⠀⢠⣤⣤⡀⠀⠀⢻⣿⡀⠙⢿⣦⠀⠀',
            '⣰⡟⠁⠀⠀⢸⣿⠀⠀⠀⢿⣿⣿⡟⠀⠀⠈⣿⡇⠀⠀⠙⣷⡄',
            '⠈⠻⣦⣄⠀⠸⣿⣆⠀⠀⠀⠉⠉⠀⠀⠀⣸⣿⠃⢀⣤⣾⠟⠁',
            '⠀⠀⠈⠻⣿⣶⣿⣿⣦⣄⠀⠀⠀⢀⣠⣾⣿⣿⣾⡿⠋⠁⠀⠀',
            '⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀',
            '⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀'
        ]
        # maybe 0.04 sleep
        self.colorized_print(name, type_text='i')
        self.colorized_print(logo, type_text='e')

    """
    Its the charge print with colorized format all the output of the program
    Args:
        - text_arr (arr or str): the text to printed
        - color (str): color to set text
        - style (str): format of the font (bold, italic, etc)
        - type_text (str): type of message, this have predefined style options [default=None]
            - 'warning' or 'w'
            - 'error' or 'e'
            - 'info' or 'i'
    Explanation:
        If text_arr is list this print all lines with the style setted, but if is str the 
        method become this str in list. And if type_text its setted ignore the rest of the
        styles defined (style and color)
    """
    def colorized_print(self, text_arr, style=None, color=None, type_text=None):
        if isinstance(text_arr, str):
            text = text_arr
            text_arr = list()
            text_arr.append(text)

        if type_text is not None:
            match type_text:
                case 'warning' | 'w':
                    type_text = Visuals.type_msg['warning']
                case 'error' | 'e':
                    type_text = Visuals.type_msg['error']
                case 'info' | 'i':
                    type_text = Visuals.type_msg['info']

            for txt in text_arr:
                self.console.print(txt, style=type_text)
            return
        for txt in text_arr:
            self.console.print(f'[{style} {color}]{txt}')