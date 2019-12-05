class SipuniException(Exception):
    def __init__(self, error_code, error_message, error_description, *args):
        super().__init__(*args)
        self.error_code = error_code
        self.error_message = error_message
        self.error_description = ''

    def __str__(self):
        return f"code: {self.error_code}, detail: {self.error_message}, description: {self.error_description}"