import string

def censor(input, output):
    censored_words = []
    with open(input, "r") as file:
        text = file.read()

    words = text.split()

    for w in words:
        clean = clean_word(w)
        if len(clean) == 4:
            censored_words.append("****")
        else:
            censored_words.append(clean)
    final_text = " ".join(censored_words)

    with open(output, "w") as file:
        file.write(final_text)

def clean_word(word):
    return word.strip(string.punctuation)

def main():
    file = "chapter_11/exercise_material/exercise_11/words.txt"
    file_o = "chapter_11/exercise_material/exercise_11/output.txt"

    censor(file, file_o)

main()