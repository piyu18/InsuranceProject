import os
import sys

class InsuranceException(Exception):
    def __init__(self, error_message: Exception, error_details:sys):
        super().__init__(error_message)
        self.error_message = InsuranceException.error_message_detail(error_message, error_details=error_details)

    @staticmethod
    def error_message_detail(error:Exception, error_details:sys)->str:
        _, _, exe_tb = error_details.exc_info()

        line_number = exe_tb.tb_frame.f_lineno

         # extracting filename from exception traceback
        filename = exe_tb.tb_frame.f_code.co_filename

        # error message
        error_message = f"Error occuurred in python script {filename}" \
                        f"and line number {line_number} error is {error}"
        return error_message

    def __str__(self):
        return InsuranceException.__name__.__str__()
