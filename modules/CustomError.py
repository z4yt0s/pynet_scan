import sys
from traceback import print_tb

"""
CustomError: A custom error class for handling specific error types and format data
Atributes:
    - debug (bool): Indicates whether debug mode is enable or not [default=False]
"""
class CustomError(Exception):
    debug = False
    """
    Args:
        - msg (str): its the message for the error
        - code (int): its the status code of the error
        - prev_err_info (dict): store the attributes and methods of instance Exeption, to keep
          track of the error infomation, like: __cause__, __traceback__, etc [default=dict()].
    Explanation:
        The super().__init__() method calls the constructor of the base Exception class to 
        initialize the error message for this custom error class
    """
    def __init__(self, msg, code, prev_err_info=dict()) -> None:
        super().__init__(msg)
        self.msg = msg
        self.code = code
        self.prev_err_info = prev_err_info

    """
    Detect in based code the subtype of exception and decided if its panic or not
    Errors Codes:
        - 10: INVALID IP ADDRESS [Panic!]
    """
    def detect_error_type(self):
        if CustomError.debug:
            self.prev_err_info['traceback'] = self.__cause__.__traceback__
        self.prev_err_info['class'] = self.__cause__.__class__.__name__
        self.prev_err_info['cause'] = self.__cause__

        try:
            if self.code == 10:
                raise ArgsError(self.msg, self.code, self.prev_err_info, panic=True) from self
        except ArgsError as ae:
            ae.handler_panic()
        except NetworkError as ne:
            pass

    """
    Prepare the data recolected about error and show information
    """
    def __report_info(self):
        # if exeption its throw for other classes show original exeption error
        if self.prev_err_info['cause'] is not None:
            print(f'[!] From: {self.prev_err_info['class']} - {self.prev_err_info['cause']}')
        print(f'[!] Proc: {self.__cause__.__class__.__name__} - Code[{self.code}]')
        print(f'[!] Throw: {self.__class__.__name__} - {self.msg}')
        # traceback option: only if flag --debug its set
        if CustomError.debug:
            print_tb(self.prev_err_info['traceback'])
            
"""
ArgsError: A specific error class representing argsparse errors.
"""
class ArgsError(CustomError):
    """
    Args:
        - *args: Arguments inherited from the parent class CustomError
        - paninc (bool): Indicates whether to stop program execution [default=False]
    """
    def __init__(self, msg, code, prev_err_info, panic=False) -> None:
        super().__init__(msg, code, prev_err_info)
        self.panic = panic

    """
    Print report and decide if program has to be stopped
    """
    def handler_panic(self):
        self._CustomError__report_info()
        if self.panic: sys.exit(0)

"""
NetworkError: A specific error class representing network error
"""
class NetworkError(CustomError):
    pass