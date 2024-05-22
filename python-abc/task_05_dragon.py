#!/usr/bin/python3

"""The Mystical Dragon - Mastering Mixins"""


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")


if __name__ == "__main__":
    """Testing the Dragon's Abilities"""
    draco = Dragon()

    draco.swim()
    draco.fly()
    draco.roar()
