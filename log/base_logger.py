from abc import ABCMeta, abstractmethod


class BaseLogger(metaclass=ABCMeta):
    @abstractmethod
    def create_entry(self, message: str):
        raise NotImplementedError

    def handle_error(self, error: Exception, message: str = "Error"):
        self.create_entry(f"{message}: {error}".replace("\n", ": "))


