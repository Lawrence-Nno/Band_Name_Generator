def generate_band_name():
    """ This function generates a band name using the first syllable of the city you live in
    and the last syllable of your pet name """

    # A welcome message
    print("Welcome to the Band Name Generator.")

    # Stores your inputted city name to a variable named 'city_name'
    city_name = input("What is the name of the city you grew up in?\n")

    # Stores your inputted pet name to a variable named 'pet_name'
    pet_name = input("What is the name of your pet?\n")

    # Vowels to be used to split the entered names into syllables
    vowels = "aeiouAEIOU"

    # a list of the available syllables in the city_name
    city_name_syllables = [city_name[:index + 1] for index, char in enumerate(city_name) if char in vowels]

    # a list of the available syllables in the pet_name
    pet_name_syllables = [pet_name[index + 1:] for index, char in enumerate(pet_name) if char in vowels]

    # The first city_name syllable more than one letter to be used.
    for syllable in city_name_syllables:
        if len(syllable) > 1:
            city_first_syllable = syllable
            break
        else:
            city_first_syllable = city_name

    # The last pet_name syllable more than one letter to be used.
    for syllable in reversed(pet_name_syllables):
        if len(syllable) > 1:
            pet_last_syllable = syllable
            break
        else:
            pet_last_syllable = pet_name

    # The generated band name
    generated_band_name = city_first_syllable + pet_last_syllable

    # Prints out the generated band name to the console
    print(f"Your Band Name could be {generated_band_name}")

    # Returns the generated band name as an output of this function
    return generated_band_name


if __name__ == "__main__":
    generate_band_name()

