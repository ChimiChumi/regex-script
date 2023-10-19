import os

def get_directory():
    while True:
        dir_path = input("Please enter the directory path: ").strip()
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            return dir_path
        print("Invalid directory. Please try again.")

def get_file_path(prompt, default_file, directory):
    filename = input(prompt) or default_file
    return os.path.join(directory, filename)

def ensure_file_exists(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            pass

def main():
    directory = get_directory()

    input_filepath = get_file_path("Please enter the input filename (default is input.txt): ", "input.txt", directory)
    output_filepath = get_file_path("Please enter the output filename (default is output.txt): ", "output.txt", directory)

    ensure_file_exists(input_filepath)
    ensure_file_exists(output_filepath)

    print(f"Input file path: {input_filepath}")
    print(f"Output file path: {output_filepath}")
    print("Both files have been ensured to exist.")

if __name__ == "__main__":
    main()
