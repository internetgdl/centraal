class CustomError(Exception):
    def __init__(self, message):
        self.message = message

class AnotherError(Exception):
    def __init__(self,description, message):
        self.message = message
        self.description = description
