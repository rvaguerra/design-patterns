from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    pass


class AbstractProductB(ABC):
    pass


class AbstractFactory(ABC):

    @abstractmethod
    def createProductA(self) -> AbstractProductA:
        pass

    @abstractmethod
    def createProductB(self) -> AbstractProductB:
        pass


class ConcreteFactoryAProductA(AbstractProductA):
    pass


class ConcreteFactoryAProductB(AbstractProductB):
    pass


class ConcreteFactoryA(AbstractFactory):

    def createProductA(self) -> AbstractProductA:
        return ConcreteFactoryAProductA()

    def createProductB(self) -> AbstractProductB:
        return ConcreteFactoryAProductB()


class ConcreteFactoryBProductA(AbstractProductA):
    pass


class ConcreteFactoryBProductB(AbstractProductB):
    pass


class ConcreteFactoryB(AbstractFactory):

    def createProductA(self) -> AbstractProductA:
        return ConcreteFactoryBProductA()

    def createProductB(self) -> AbstractProductB:
        return ConcreteFactoryBProductB()


factory = ConcreteFactoryB()

productA = factory.createProductA()
productB = factory.createProductB()

print(isinstance(productA, AbstractProductA))
print(isinstance(productB, AbstractProductB))
