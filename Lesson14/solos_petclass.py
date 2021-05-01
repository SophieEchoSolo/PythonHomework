"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 14 - OOP Pet Adoption
Description:  solos_petclass.py - This program will use OOP to create a pet adoption app
"""


class PetAdoption:
    """
    A class for the pet adoption process
    """

    def __init__(self, name, age, animal_type):
        self.__name = name
        self.__age = age
        self.__animal_type = animal_type

    def __str__(self):
        return (f"Name: {self.__name} Age: {self.__age} Type: {self.__animal_type}")

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_animal_type(self):
        return self.__animal_type


def main():
    cat = PetAdoption("Tapioca", 3, "cat")
    cat.__str__()


if __name__ == "__main__":
    main()
