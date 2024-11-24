import os
from datetime import datetime

from log.base_logger import BaseLogger
from log import FatalLoggingException


class FileLogger(BaseLogger):
    """
    Logger that prints to the console and also appends to a given log file
    """

    def __init__(self, directory: str, filename: str) -> None:
        self.directory = directory
        self.filename = filename
        self.full_path = f"{self.directory}/{self.filename}"

        try:
            if not os.path.exists(directory):
                os.mkdir(directory)

            if not os.path.exists(self.full_path):
                with open(self.full_path, "x") as outfile:
                    outfile.write(
                        f"Begin Log: {datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}\n"
                    )
            else:
                with open(self.full_path, "a") as outfile:
                    outfile.write(
                        f"Begin Log: {datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}\n"
                    )
        except IOError as e:
            raise FatalLoggingException(f"Could not initialize logs: {e}")

    def create_entry(self, message):
        print(message)
        with open(self.full_path, "a") as outfile:
            timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
            outfile.write(f"{timestamp}: {message}\n")
