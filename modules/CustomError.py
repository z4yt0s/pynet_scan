import sys
from traceback import print_tb

class CustomError(Exception):
    debug = False

    def __init__(self, msg, code, prev_err_info=dict()) -> None:
        super().__init__(msg)
        self.msg = msg
        self.code = code
        self.prev_err_info = prev_err_info

    """ Detect in based code the subtype of exeption and decided if its panic or not"""
    def detect_error_type(self):
        # setting info for 
        if CustomError.debug: 
            self.prev_err_info['traceback'] = self.__cause__.__traceback__
        self.prev_err_info['class'] = self.__cause__.__class__.__name__
        self.prev_err_info['cause'] = self.__cause__
        # throws error based on the code
        try:
            # invalid ip address
            if self.code == 10:     
                raise ArgsError(self.msg, self.code, self.prev_err_info, panic=True) from self

        except ArgsError as ae:
            ae.handler_panic()
        except NetworkError as ne:
            pass

    """Prepare the data recolected and show info"""
    def __report_info(self):
        # if exeption its throw for other classes show original exeption error
        if self.prev_err_info['cause'] is not None:
            print(f'[!] From: {self.prev_err_info['class']} - {self.prev_err_info['cause']}')
        # normal info output
        print(f'[!] Proc: {self.__cause__.__class__.__name__} - Code[{self.code}]')
        print(f'[!] Throw: {self.__class__.__name__} - {self.msg}')
        # traceback option: only if flag --debug its set 
        if CustomError.debug:
            print('\n')
            print_tb(self.prev_err_info['traceback'])
            
class ArgsError(CustomError):
    def __init__(self, msg, code, prev_err_info, panic=True) -> None:
        super().__init__(msg, code, prev_err_info)
        self.panic = panic
        
    """Print report and decide if program has to be stopped"""
    def handler_panic(self):
        self._CustomError__report_info()
        if self.panic: sys.exit(0)

class NetworkError(CustomError):
    pass 