from log.base_logger import BaseLogger


class NullLogger(BaseLogger):
    """
    Logger that only prints to the console, used when creating the log file fails
    """
    def create_entry(self, message: str):
        print(message)