import os
import socket

DATA_DIR = os.environ.get("DATA_DIR", "/home/data")
OUTPUT_DIR = os.path.join(DATA_DIR, "output")
RESULT_FILE = os.path.join(OUTPUT_DIR, "result.txt")

CONTRACTIONS = {
    "it's": "it is",
    "that's": "that is",
    "i'm": "i am",
    "i'll": "i will",
    "you're": "you are",
    "can't": "can not",
    "won't": "will not",
    "don't": "do not",
    "couldn't": "could not",
}


def read_file(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower()
    for p in ",.;:!?-—‘":
        text = text.replace(p, " ")
    return text


def count_words(text):
    return len([w for w in text.split() if w.strip("’")])


def top_3_freq(text):
    word_dict = {c: text.split().count(c) for c in set(text.split())}
    top_3 = []
    for i in range(3):
        max_word = max(word_dict, key=word_dict.get)
        top_3.append((max_word, word_dict[max_word]))
        del word_dict[max_word]
    return top_3


def split_contractions(text):
    for contraction, expansion in CONTRACTIONS.items():
        text = text.replace(contraction, expansion)
    return text


# Read files
IF = read_file("IF.txt").lower()
ARUTW = read_file("AlwaysRememberUsThisWay.txt").lower()

# a) and b) Word counts
word_count = {
    "IF.txt": count_words(IF),
    "AlwaysRememberUsThisWay.txt": count_words(ARUTW),
}
total_words = sum(word_count.values())

# c) Top 3 in IF.txt
top_3_IF = top_3_freq(IF)

# d) Top 3 in AlwaysRememberUsThisWay.txt, contractions split
uncontracted_ARUTW = split_contractions(ARUTW)
top_3_ARUTW = top_3_freq(uncontracted_ARUTW)

# e) IP address
ip_address = socket.gethostbyname(socket.gethostname())

# f) Write result.txt
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(RESULT_FILE, "w", encoding="utf-8") as f:
    for i in word_count:
        f.write(f"{i}: {word_count[i]} words\n\n")
    f.write(f"Total words: {total_words}\n")

    f.write("\nTop 3 words in IF.txt \n")
    count = 1
    for i in top_3_IF:
        f.write(f"{count} - {i[0]} ({i[1]} occurrences)\n")
        count += 1

    f.write("\nTop 3 words in AlwaysRememberUsThisWay.txt \n")
    count = 1
    for i in top_3_ARUTW:
        f.write(f"{count} - {i[0]} ({i[1]} occurrences)\n")
        count += 1

    f.write(f"\nContainer IP address: {ip_address}\n")

# Print result.txt to the console
with open(RESULT_FILE, "r", encoding="utf-8") as f:
    print(f.read())
