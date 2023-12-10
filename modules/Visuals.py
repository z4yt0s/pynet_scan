from time import sleep
from rich.console import Console, Group
from rich.table import Table
from rich.align import Align
from rich.theme import Theme
from rich.panel import Panel
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

    """
    This print the banner of the tool
    """
    def banner(self):
        name = [
            '                            __                           \n',
            '    ____  __  ______  ___  / /_     ______________ _____ \n',
            '   / __ \\/ / / / __ \\/ _ \\/ __/    / ___/ ___/ __ `/ __ \\\n',
            '  / /_/ / /_/ / / / /  __/ /_     (__  ) /__/ /_/ / / / /\n',
            ' / .___/\\__, /_/ /_/\\___/\\__/____/____/\\___/\\__,_/_/ /_/\n',
            '/_/    /____/              /_____/                       \n'
        ]
        logo = [
            '⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n',
            '⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀\n',
            '⠀⠀⠀⣠⣶⡿⣿⣿⡿⠋⠉⠀⠀⠉⠙⢿⣿⡿⣷⣦⡀⠀⠀⠀\n',
            '⠀⢀⣼⠟⠁⢠⣿⠏⠀⠀⢠⣤⣤⡀⠀⠀⢻⣿⡀⠙⢿⣦⠀⠀\n',
            '⣰⡟⠁⠀⠀⢸⣿⠀⠀⠀⢿⣿⣿⡟⠀⠀⠈⣿⡇⠀⠀⠙⣷⡄\n',
            '⠈⠻⣦⣄⠀⠸⣿⣆⠀⠀⠀⠉⠉⠀⠀⠀⣸⣿⠃⢀⣤⣾⠟⠁\n',
            '⠀⠀⠈⠻⣿⣶⣿⣿⣦⣄⠀⠀⠀⢀⣠⣾⣿⣿⣾⡿⠋⠁⠀⠀\n',
            '⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀\n',
            '⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
        ]
        text_name = Text()
        text_logo = Text()

        for line in name:
            text_name.append(f'{line}', style='bold dodger_blue3')
        for line in logo:
            text_logo.append(f'{line}', style='bold dodger_blue3')

        table_banner = Table.grid(padding=2)
        table_banner.add_column(no_wrap=True)
        table_banner.add_row(
            Align(text_name, vertical='middle'),
            text_logo
        )

        self.console.print(table_banner)

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


    """
    This return a Panel in base of the content recibed for 'renderable'.
    Args:
        - renderable (object): The content to be rendered inside the panel.
        - border_style (str): The style of the panel's border.
        - title (str): The title displayed at the top of the panel.
        - title_align (str): The alignment of the title ('center', 'left', 'right').
        - style (str): Additional styling for the panel.
        - expand (bool): Indicates if the panel should expand to fill available space.
        - dimensions (tuple of float or None): The dimensions (width, height) of the panel.
        - padding (tuple of int or None): The padding (vertical, horizontal) inside the panel.
    Returns:
        Panel: A Panel object created with the provided parameters.
    """
    def __panel(
            self, renderable, border_style='none', title=None, title_align='center',
            style='none', expand=False, padding=(0,0) #dimensions=(None, None), padding=(0,0)
        ):
        return Panel(
            renderable=renderable,
            border_style=border_style,
            title=title,
            title_align=title_align,
            style=style,
            expand=expand,
            #dimensions=dimensions,
            padding=padding
        )