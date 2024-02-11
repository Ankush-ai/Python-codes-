import json

# Specify the correct path to the JSON file
json_file_path = 'data.json'

# Open the JSON file for reading
try:
    with open(json_file_path, 'r') as json_file:
        # Use json.load() to convert the JSON file content into a dictionary
        data_dict = json.load(json_file)
        # Print the resulting dictionary
        print(data_dict)
except FileNotFoundError:
    print(f"Error: File '{json_file_path}' not found.")
except json.JSONDecodeError:
    print(f"Error: Invalid JSON syntax in file '{json_file_path}'.")
