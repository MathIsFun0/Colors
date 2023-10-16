import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize

# Download the NLTK data (if not already downloaded)
nltk.download("punkt")

# Define a list of common color words
color_words = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
    "white",
    "gray",
    "grey",
    "gold",
    "silver",
    "cyan",
    "turquoise"
    "indigo",
    "magenta",
    "crimson",
    "azure",
    "maroon",
    "beige",
    "amber",
    "lilac",
]

# Read the text file
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().replace("\n", " ")
    return text

# Extract color words and their sentences from the text
def extract_color_words_and_sentences(text):
    sentences = sent_tokenize(text)
    color_sentences = {}

    for sentence in sentences:
        for color in color_words:
            pattern = r'\b{}\b'.format(re.escape(color))
            if re.search(pattern, sentence, re.IGNORECASE):
                if color in color_sentences:
                    color_sentences[color].append(sentence)
                else:
                    color_sentences[color] = [sentence]

    return color_sentences

if __name__ == "__main__":
    file_path = "ch3.txt"  # Replace with the path to your text file
    text = read_text_file(file_path)

    color_sentences = extract_color_words_and_sentences(text)

    for color, sentences in color_sentences.items():
        print(f"{color.capitalize()} sentences:")
        for sentence in sentences:
            print(f"- {sentence.strip()}")
        print()
