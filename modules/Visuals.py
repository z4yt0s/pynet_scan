from rich.console import Console

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
        self.console = Console(color_system='256', theme=Visuals.type_msg)
    """
    This print the banner of the tool
    """
    def banner():
        pass

    """
    Its the charge print with colorized format all the output of the program
    Args:
        - text (str): the text to printed
        - color (str): color to set text
        - style (str): format of the font (bold, italic, etc)
        - type_text (str): type of message, this have predefined style options [default=None]
            - 'warning' or 'w'
            - 'error' or 'e'
            - 'info' or 'i'
    Explanation:
        If type_text its setted ignore the rest of the styles defined (style and color)
    """
    def colorized_print(self, text, style, color, type_text=None):
        if type_text is not None:
            style = None; color = None
            match type_text:
                case 'warning | w':
                    type_text = Visuals.type_msg['warning']
                case 'error | e':
                    type_text = Visuals.type_msg['error']
                case 'info | i':
                    type_text = Visuals.type_msg['info']
            for txt in text: 
                self.console.print(txt, style=type_text)
            return

        for txt in text:
            self.console.print(f'[{style} {color}]{txt}')