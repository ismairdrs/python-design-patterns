from abc import ABC, abstractmethod


class PizzaFactory(ABC):
    @abstractmethod
    def create_veg_pizza(self):
        raise NotImplementedError

    @abstractmethod
    def create_non_veg_pizza(self):
        raise NotImplementedError


class IndianPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return DeluxVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_non_veg_pizza(self):
        return HamPizza()


class VegPizza(ABC):
    @abstractmethod
    def prepare(self, veg_pizza):
        raise NotImplementedError


class NonVegPizza(ABC):
    @abstractmethod
    def serve(self, veg_pizza):
        raise NotImplementedError


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Preparar", type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(type(self).__name__, "é servido com frango", type(veg_pizza).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Preparar", type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, "é servido com presunto", type(VegPizza).__name__)


class PizzaStore:
    def make_pizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.create_non_veg_pizza()
            self.VegPizza = self.factory.create_veg_pizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


if __name__ == "__main__":
    pizza = PizzaStore()
    pizza.make_pizzas()
