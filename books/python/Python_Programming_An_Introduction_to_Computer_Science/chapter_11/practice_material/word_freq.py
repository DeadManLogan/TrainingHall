def by_freq(pair):
    return pair[1]

def main():
    file = "chapter_11/practice_material/words.txt"
    reader = open(file, "r").read()
    reader = reader.lower()

    for ch in '! " #$%&()*+,-./:;<=>?<Q[\\]-_{|}~':
        reader = reader.replace(ch, " ")
    words = reader.split()

    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    items = list(counts.items())
    items.sort()
    items.sort(key=by_freq, reverse=True)

    for i in range(5):
        word, count = items[i]
        print(word, count)

main()