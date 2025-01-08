
import sys
import logging
from src.logger import logging

def error_message_details(error,error_details:sys):
    _,_,tb=error_details.exc_info()
    file_name = tb.tb_frame.f_code.co_filename
    line_number = tb.tb_lineno
    error_message = f"file name: {file_name}, line number: {line_number}, error: {error}"
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
       super().__init__(error_message)
       self.error_message_details = error_message_details(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message_details
    
# if __name__ == "__main__":
#     try:
#        a=1/0
#     except Exception as e:
#         logging.info("Not Divisible by zero")
#         raise CustomException(e,sys)

