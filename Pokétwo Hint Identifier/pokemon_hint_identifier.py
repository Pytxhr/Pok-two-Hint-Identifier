import requests
import pyperclip
import os
import time

# Make an HTTP GET request to the PokéAPI to retrieve a list of Pokémon names
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10249")

# Get the list of Pokémon from the response
pokemon_list = response.json()["results"]

# Extract the names of the Pokémon from the list
pokemon_names = [pokemon["name"] for pokemon in pokemon_list]

while True:
    # Ask the user to enter a hint
    hint = input("Please enter a hint, to end the loop simply type exist: ")

    # Check if the user wants to exist the program
    if hint == "exist":
        break

    # If the hint is an empty string, print an error message and ask for input again
    if not hint:
        print("Invalid input. Please enter a non-empty string.")
        continue

    # If the first letter is not an underscore, then replace it with an underscore
    # have to do it this way because my dumbass doesn't know any other way to get it working
    if hint[0] != "_":
        hint = "_" + hint[1:]

    # Check each Pokémon name to see if it matches the hint
    matching_pokemon = []
    for name in pokemon_names:
        # Check if the length of the Pokémon name matches the length of the hint
        if len(name) == len(hint):
            # Check if the hint and the Pokémon name match at each character position
            for i in range(len(hint)):
                if hint[i] != "_" and hint[i] != name[i]:
                    break
            else:
                # Fill in the underscores with the missing letters from the Pokémon name
                full_name = ""
                hint_index = 0
                for i in range(len(name)):
                    if hint_index < len(hint) and name[i] == hint[hint_index]:
                        full_name += hint[hint_index]
                        hint_index += 1
                    else:
                        full_name += name[i]
                # Add the Pokémon name to the list of matching Pokémon
                matching_pokemon.append(full_name)
    else:
        # If no Pokémon names in pokeapi match the hint, search the pokes.txt file
        with open("pokes.txt", "r") as f:
            poke_names = f.read().splitlines()
    for name in poke_names:
        if len(name) == len(hint):
            for i in range(len(hint)):
                if hint[i] != "_" and hint[i] != name[i]:
                    break
            else:
                full_name = ""
                hint_index = 0
                for i in range(len(name)):
                    if hint_index < len(hint) and name[i] == hint[hint_index]:
                        full_name += hint[hint_index]
                        hint_index += 1
                    else:
                        full_name += name[i]
                # Only add the Pokémon name to the list if it's not already in the list
                if full_name not in matching_pokemon:
                    matching_pokemon.append(full_name)
                    
    # Print the list of matching Pokémon
    if matching_pokemon:
        if len(matching_pokemon) == 1:
            pyperclip.copy(matching_pokemon[0])
            print("Copied matching Pokémon to clipboard:", matching_pokemon[0])
            time.sleep(1.5)
            os.system("cls")
        else:
            print("There are more than one Pokémon that match this hint:")
            for i, name in enumerate(matching_pokemon):
                print(f"{i+1}. {name}")
            while True:
                try:
                    choice = int(input("Enter the number of the Pokémon name you want to copy to the clipboard: "))
                    
                    # Check if the choice is a valid index for the list of matching Pokémon
                    if choice < 1 or choice > len(matching_pokemon):
                        raise ValueError
                    pyperclip.copy(matching_pokemon[choice - 1])
                    print(f"Copied {matching_pokemon[choice - 1]} to clipboard.")
                    time.sleep(1.5)
                    os.system("cls")
                    break
                except ValueError:
                    print(
                        "Invalid input. Please enter a number between 1 and",
                        len(matching_pokemon),
                    )
    else:
        # If no Pokémon names match the hint, print an error message
        print("No Pokémon found with hint:", hint)