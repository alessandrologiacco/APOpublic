import abc
from abc import ABC


class NutritionalElement(ABC):

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def calories(self) -> float:
        pass

    @property
    @abc.abstractmethod
    def proteins(self) -> float:
        pass

    @property
    @abc.abstractmethod
    def carbs(self) -> float:
        pass

    @property
    @abc.abstractmethod
    def fats(self) -> float:
        pass

    @property
    @abc.abstractmethod
    def per100g(self) -> bool:
        pass
