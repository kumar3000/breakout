file_path = 'ingredients.txt'
bad_ings = [] # bad_ingredients

# Create a list of banned ingredients
with open(file_path, 'r') as file:
    for line in file:
        bad_ings.append(line)