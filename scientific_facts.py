
scientific_facts = [

    "Physics: The law of conservation of energy states that energy cannot be created or destroyed, only transformed from one form to another.",

    "Biology: DNA, or deoxyribonucleic acid, is a molecule that carries most of the genetic instructions used in the development, functioning, and reproduction of all known living organisms.",

    "Chemistry: Water, with the chemical formula H2O, is a polar molecule, which means it has a partial negative charge near the oxygen atom and partial positive charges near the hydrogen atoms.",

    "Sports Science: The Cori cycle is a metabolic pathway where the liver converts lactate into glucose during intense exercise, allowing for sustained energy production.",

    "Geology: Plate tectonics is the scientific theory explaining the movement of the Earth's lithosphere on the underlying, more fluid asthenosphere, leading to the formation of continents, earthquakes, and volcanic activity."

]

length_of_elements = [len(i) for i in scientific_facts]
print(length_of_elements)

add_fact = input("Enter a fact to add to the fact factory (or FACTory haha): ")
scientific_facts.append(add_fact)
print(scientific_facts)

user_word = input("Enter a word that might be in one of the facts: ")
for word in scientific_facts:
    if ((user_word.lower() + ':') in word.lower()) or (' ' + (user_word.lower() + ' ') in word.lower()) or ((user_word.lower() + '.') in word.lower()) :
        print("Your word was find in the following fact... ", word)
        break
    else:
        print("Your word was not found in any of the facts..... ahhhhhhh!!!")
        
# Provide 3 examples of tuples, sets, and dictionaries