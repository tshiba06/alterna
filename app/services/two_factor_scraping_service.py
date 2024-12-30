from abc import ABC, abstractmethod


class TwoFactorService(ABC):
    @abstractmethod
    def initial_run(self):
        """
        返り値の型はbyteかもしれないし、stringの可能性もあるので一旦は定義せず
        """
        pass

    @abstractmethod
    def second_run(self) -> int:
        pass
