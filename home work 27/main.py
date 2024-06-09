import json


def parse_json_files(filenames):
    parsed_data = {}
    for filename in filenames:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                parsed_data[filename] = data
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error parsing JSON in file '{filename}'.")
    return parsed_data


# Example usage
filenames = ["file1.json", "file2.json", "file3.json"]
parsed_results = parse_json_files(filenames)

for filename, data in parsed_results.items():
    print(f"Data from '{filename}':")
    print(json.dumps(data, indent=2))
    print("\n")

# You can replace the 'filenames' list with your actual file names.
