import os, re

def get_directory():
    while True:
        dir_path = input("Please enter the directory path: ").strip()
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            return dir_path
        print("\nInvalid directory. Please try again.\n")

def get_file_path(prompt, default_file, directory):
    filename = input(prompt) or default_file
    return os.path.join(directory, filename)

def file_exists(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            pass

def main():
    directory = get_directory()

    input_filepath = get_file_path("Please enter the input filename (default is input.txt): ", "input.txt", directory)
    output_filepath = get_file_path("Please enter the output filename (default is output.txt): ", "output.txt", directory)

    file_exists(input_filepath)
    file_exists(output_filepath)

    with open(input_filepath, 'r') as input_file:
        text = input_file.read()
        text2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"


    print(f"Input file path: {input_filepath}")
    print(f"Output file path: {output_filepath}")
    print("\nBoth files have been ensured to exist.")

        # Mapping of words to numbers
    word_to_num = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "ten": "10"
    }

    # Simple match
    pattern = re.compile(r"\b\w*bb\w*\b", re.IGNORECASE)
    simple_matches = pattern.findall(text)

    # Lookahead
    pattern = re.compile(r"(?=(example))", re.IGNORECASE)
    lookahead_matches = pattern.findall(text)

    # Conversion
    def format_phone_number(match):
        return f"({match.group(1)})-{match.group(2)}-{match.group(3)}"

    text = re.sub(r"(\d{3})(\d{3})(\d{4})", format_phone_number, text)

    # Capturing group & Processing
    def replace_word_with_number(match):
        return word_to_num[match.group(0).lower()]

    pattern = r"\b(one|two|three|four|five|six|seven|eight|nine|ten)\b"
    replace_text = re.sub(pattern, replace_word_with_number, text, flags=re.IGNORECASE)

    # Backreference
    words_same_start_end = re.findall(r"\b(\w)(\w*\1)\b", text, re.IGNORECASE)
    full_words = [start + rest for start, rest in words_same_start_end]

    # Lazy and Greedy matching
    lazy_match = re.search(r'(a+?)a+b', text2)
    greedy_match = re.search(r'(a+)a+b', text2)

    with open(output_filepath, 'w') as output_file:

        output_file.write(replace_text)
        output_file.write("\n\nThe following operations were made: \n")
        output_file.write("\t\t- words with 2 neighboring 'b'-s: \n")
        for word in simple_matches:
            output_file.write("\t\t\t\t\t\t" + word + '\n')
        output_file.write("\n\t\t- occurrence of the word 'example' with lookahead: " + str(len(lookahead_matches)) + '\n')
        output_file.write("\n\t\t- verbose numbers replaced with numeric value\n")
        output_file.write("\n\t\t- words with the same start-end letters: \n")
        for word in full_words:
            output_file.write("\t\t\t\t\t\t\t" + word + '\n')
        output_file.write("\n\t\t- phone number formatted with capturing group\n")
        if lazy_match:
            output_file.write("\n\t\t- lazy match (shortest match): " + lazy_match.group(1) + '\n')
        if greedy_match:
            output_file.write("\n\t\t- greedy match (longest match): " + greedy_match.group(1) + '\n')

    print(f"\nOutput has been written to {output_filepath}\n")

if __name__ == "__main__":
    main()
