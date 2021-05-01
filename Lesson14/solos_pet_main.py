"""
Author:  Sophie Solo
Course:  CSC 121
Assignment:  Lesson 14 - OOP Pet Adoption
Description:  solos_pet_main.py - This program will use OOP to create a pet adoption app
"""
from solos_petclass import PetAdoption as pa


def main():
    pet_list = []

    for i in range(10):
        name = (input("Enter a pet name: "))
        age = int(input("Enter the pet's age: "))
        animal_type = input("What type of pet is it? ")

        pet_list.append(pa(name, age, animal_type))

    for index, pet in enumerate(pet_list):
        print(str(index+1) + "- " + pet.__str__())

    print("Welcome to Echo's Pet Adoption Agency!")

    adopt_choice = int(input("Our pets are all fostered by members of the community, and not housed at a shelter. "
                             "Which "
                             "pet would you like to meet (or 0 for none right now)? "))

    if adopt_choice == 0:
        print("Thank you for vising Echo's Pet Adoption Agency!")
    else:
        print(
            f"Ahh, {pet_list[adopt_choice-1].get_name()} a lovely {pet_list[adopt_choice-1].get_age()} year old {pet_list[adopt_choice-1].get_animal_type()}")
        print(
            f"{pet_list[adopt_choice-1].get_name()}'s foster will email you soon with more details.")
        print("Thank you for vising Echo's Pet Adoption Agency!")


if __name__ == "__main__":
    main()
