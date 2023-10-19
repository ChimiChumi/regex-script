import re
import timeit

text = """
example 1: here is an example.
This example is a tricky exampampamexampleexaapppleexampleEXamPLEEXAMPLExAmpleXexemplarexahexamplexample.
Are there five, six, seven... maybe ten eXaMpleS there? Oh sh*t, it's one more now.
example 2: Unreadable phone number: 5555551234. Also, another one: 4444445678
example 3: radar, level, deed, trumpet, xerox are words by randomizer.
example 4: --
example 5: [apple] and [pie], [hubbly-wobbly bubble-tea]
example 6: testing[++with++some++words++]
"""

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



text1 = "aaaaaaab"
text2 = "aaaaaaab"

# Basic (Greedy) Regex
greedy_pattern = r'a+.*b'
greedy_result = re.search(greedy_pattern, text1)

# Lazy Regex
lazy_pattern = r'a+?b'
lazy_result = re.search(pattern, text2)

# Possessive Regex (Python does not support possessive quantifiers)
# We will use an equivalent technique using negative lookahead
start_time = timeit.default_timer()
possessive_matches = re.findall(r"apple(?:(?!apple).)*", text)
possessive_runtime = timeit.default_timer() - start_time

print("\n\nOutput text:\n", replace_text)
print("\n\nThe following operations were made: \n")
print("\t\t- words with 2 neighboring 'b'-s: ")
for word in simple_matches:
    print("\t\t\t\t\t\t", word)
print("\n\t\t- occurance of the word 'example' with lookahead: ", len(lookahead_matches))
print("\t\t- verbose numbers replaced with numeric value")
print("\t\t- words with the same start-end letters: ")
for word in full_words:
    print("\t\t\t\t\t\t\t", word)
print("\n\t\t- phone number formatted with capturing group")

print("Basic (Greedy) Runtime:", greedy_result)
print("Lazy Runtime:", lazy_result)