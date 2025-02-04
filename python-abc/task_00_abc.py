#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


def main():
    dog = Dog()
    cat = Cat()
    print(dog.sound())
    print(cat.sound())


if __name__ == "__main__":
    main()
