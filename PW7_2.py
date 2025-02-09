def process_input():
    target_set = set("computer".lower())
    results = []

    while True:
        line = input("Введите строку слов (или 'HELLO' для завершения): ")

        if "HELLO" in line:
            break

        words = [word.strip() for word in line.split('-')]

        unique_words = set()

        for word in words:
            word_set = set(word.lower())
            common_letters = len(word_set.intersection(target_set))
            if common_letters <= 3:
                unique_words.add(word.strip())

        sorted_words = sorted(unique_words, key=lambda x: x.lower(), reverse=True)

        if sorted_words:
            index = process_input.counter
            if index % 3 == 0:
                results.append(' '.join(word.upper() for word in sorted_words))
            else:
                results.append(' '.join(sorted_words))

        process_input.counter += 1

    for result in results:
        print(result)


process_input.counter = 0

process_input()