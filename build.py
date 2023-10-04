import os

# Define the top-level directory where your .loc files are located
game_directory = "game/"

# Function to read the contents of a .loc file and generate JavaScript code
def generate_js_code(folder, filename):
    with open(os.path.join(folder, filename), 'r') as file:
        content = file.read().replace("\n",'<br>')
    folder = folder.replace("game/",'')
    # Generate JavaScript code to populate HTML elements with the content

    js_code = f'div = document.createElement("div");'
    js_code += f'div.id = "{folder}/{filename.replace(".loc","")}";'
    js_code += f'div.innerHTML = `{content}`;'
    js_code += 'document.getElementById("game-container").appendChild(div);\n'
    return js_code

# Function to recursively process folders and files
def process_directory(folder):
    js_code_list = []

    # Get a list of .loc files in the current directory
    loc_files = [filename for filename in os.listdir(folder) if filename.endswith(".loc")]

    # Generate JavaScript code for each .loc file in the current directory
    for filename in loc_files:
        js_code_list.append(generate_js_code(folder, filename))

    # Recursively process subdirectories
    subdirectories = [subdir for subdir in os.listdir(folder) if os.path.isdir(os.path.join(folder, subdir))]
    for subdir in subdirectories:
        subfolder = os.path.join(folder, subdir)
        js_code_list.extend(process_directory(subfolder))

    return js_code_list

# Start processing from the top-level directory
js_code_list = process_directory(game_directory)

# Combine the generated JavaScript code into a single string
combined_js_code = '\n'.join(js_code_list)

# Write the combined JavaScript code to index.js
with open("src/index.js", 'w') as js_file:
    js_file.write(f"//this script was generate automaticaly, do not modify it manualy, rebuild the code after changing something\n\n{combined_js_code}")

print("index.js generated successfully.")
