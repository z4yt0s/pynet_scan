import sys

class CustomError(Exception):
    def __init__(self, msg, code, prev_err_info=dict(), obj_err=None) -> None:
        super().__init__(msg)
        self.msg = msg
        self.code = code
        self.obj_err = obj_err
        self.prev_err_info = prev_err_info

    def detect_error_type(self):
        # setting info for 
        self.prev_err_info['class'] = self.__cause__.__class__.__name__
        self.prev_err_info['cause'] = self.__cause__
        try:
            # invalid ip address
            if self.code == 10:     
                raise ArgsError(self.msg, self.code, self.prev_err_info, self.obj_err, panic=True) from self

        except ArgsError as ae:
            ae.handler_panic()
        except NetworkError as ne:
            pass

    def __report_info(self):
        if self.prev_err_info['cause'] is not None:
            print(f'[!] From: {self.prev_err_info['class']} - {self.prev_err_info['cause']}')
        print(f'[!] Proc: {self.__cause__.__class__.__name__} - Code[{self.code}]')
        print(f'[!] Throw: {self.__class__.__name__} - {self.msg}')
            
class ArgsError(CustomError):
    def __init__(self, msg, code, prev_err_info, object_error=None, panic=True) -> None:
        super().__init__(msg, code, prev_err_info, object_error)
        self.panic = panic
        
    def handler_panic(self):
        self._CustomError__report_info()
        if self.panic: sys.exit(0)

class NetworkError(CustomError):
    pass 