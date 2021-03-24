def sort_words(input):
    words = input.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w) // 2:] for w in words]
    return ' '.join(words)