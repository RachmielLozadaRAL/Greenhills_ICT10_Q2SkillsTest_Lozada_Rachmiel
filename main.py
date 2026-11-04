# Skills Test2
from pyscript import display, document


non_metallic_elements = {
    'Hydrogen': 'H',
    'Carbon': 'C',
    'Nitrogen': 'N',
    'Oxygen': 'O',
    'Phosphorus': 'P',
    'Sulfur': 'S',
    'Selenium': 'Se',
    'Flourine': 'F',
    'Chlorine': 'Cl',
    'Bromine': 'Br',
    'Iodine': 'I',
    'Astatine': 'At',
    'Tennessine': 'Ts',
    'Helium': 'He',
    'Neon': 'Ne',
    'Argon': 'Ar',
    'Krypton': 'Kr',
    'Xenon': 'Xe',
    'Radon': 'Rn',
    'Oganesson': 'Og'
}

atomic_numbers = {
    'Hydrogen': 1,
    'Carbon': 6,
    'Nitrogen': 7,
    'Oxygen': 8,
    'Phosphorus': 15,
    'Sulfur': 16,
    'Selenium': 34,
    'Flourine': 9,
    'Chlorine': 17,
    'Bromine': 35,
    'Iodine': 53,
    'Astatine': 85,
    'Tennessine': 118,
    'Helium': 2,
    'Neon': 10,
    'Argon': 18,
    'Krypton': 36,
    'Xenon': 54,
    'Radon': 86,
    'Oganesson': 119
}

atomic_masses = {
    'Hydrogen': 1.008,
    'Carbon': 12.011,
    'Nitrogen': 14.007,
    'Oxygen': 15.999,
    'Phosphorus': 30.974,
    'Sulfur': 27.807,
    'Selenium': 78.96,
    'Flourine': 18.998,
    'Chlorine': 35.453,
    'Bromine': 79.904,
    'Iodine': 126.904,
    'Astatine': 210,
    'Tennessine': 294,
    'Helium': 4.002,
    'Neon': 20.180,
    'Argon': 39.948,
    'Krypton': 83.798,
    'Xenon': 131.293,
    'Radon': 222,
    'Oganesson': 294
}

# sym is the short form of symbol
symbol_lookup = {
    sym: f"Atomic Symbol: {sym}, Atomic Name: {name}, Atomic Number: {atomic_numbers[name]}, Atomic Mass: {atomic_masses[name]}"
    for name, sym in zip(non_metallic_elements.keys(), non_metallic_elements.values())
}

def check_symbol(event):
    user_input = document.getElementById('nonmetal').value.strip().capitalize() # capitalizes the symbols like cl to Cl
    
    result = symbol_lookup.get(user_input, "It is not found in the non-metallic elements list.") # Checks if the user input is either metal, metalloid, or nonmetal
    
    display(result, target='output', append=False)

document.getElementById('output').innerHTML = "Enter a non-metallic element symbol to get its details."