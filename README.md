# Pok-two-Hint-Identifier

This Python script uses the PokéAPI (https://pokeapi.co) to retrieve a list of Pokémon names and identify the Pokémon based on a hint. The user inputs a hint in the form of an underscore-filled version of the Pokémon name, and the script finds the closest match based on the hint. The script can then copy the matched Pokémon name to the system clipboard.

## Requirements

The following packages must be installed to run the script:
* requests
* pyperclip

To install the required packages, run the following command in your terminal/command prompt: pip install -r requirements.txt



## Usage

1. Clone the repository to your local machine.
2. Open a terminal/command prompt in the repository directory.
3. Run the script using the following command: python pokemon_hint_identifier.py
4. Enter a hint in the form of an underscore-filled version of the Pokémon name.
5. The script will return the closest matching Pokémon name and copy it to the system clipboard.

## Limitations

This script is limited by the data available in the PokéAPI, so it may not include all Pokémon names. However, it also searches a `pokes.txt` file that can be edited to include additional Pokémon names not found in the PokéAPI.

## Note
This script uses the os and time modules to clear the console, so it may not work on all operating systems.
