from abc import ABC, abstractmethod


class Service(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def run(self) -> int:
        pass
