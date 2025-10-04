import sys
from networksecurity.logging import logger


class NetworkSecurityException(Exception):
    def __init__(self, error_message: str, error_details: sys, error_trace=None):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_details = error_details

        # Use provided traceback or fallback to sys.exc_info()
        exc_type, exc_obj, exc_tb = error_trace if error_trace else sys.exc_info()

        if exc_tb:
            self.script_name = exc_tb.tb_frame.f_code.co_filename
            self.lineno = exc_tb.tb_lineno
        else:
            # Fallback to caller frame
            try:
                import inspect
                caller_frame = inspect.stack()[2]
                self.script_name = caller_frame.filename
                self.lineno = caller_frame.lineno
            except Exception:
                self.script_name = "Unknown"
                self.lineno = "Unknown"

    def __str__(self):
        return f"Error occured in python script name [{self.script_name}] line number [{self.lineno}] error message [{self.error_message}]"

        
if __name__=='__main__':
    try:
        logger.logging.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
           raise NetworkSecurityException(str(e), sys, sys.exc_info())