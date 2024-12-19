from abc import ABC, abstractmethod


class TwoFactorService(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def initial_run(self):
        """
        返り値の型はbyteかもしれないし、stringの可能性もあるので一旦は定義せず
        """
        pass

    def second_run(self) -> int:
        pass
