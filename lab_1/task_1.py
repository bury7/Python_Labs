from collections import Counter
from re import findall


def words_count(text: str) -> dict[str, int]:
    return dict(sorted(Counter(findall(r"\w+", text.lower())).items(), key=lambda item: item[1], reverse=True))


def get_words_above_frequency(words: dict[str, int], frequency_threshold: int = 3) -> list:
    return [word for word, count in words.items() if count > frequency_threshold]


def print_heading(title: str) -> None:
    print(f"\n{title}")
    print("-" * len(title))


def print_word_counts(word_counts: dict[str, int]) -> None:
    print_heading("Word Counts")
    if not word_counts:
        print("No words found.")
        return
    print(f"{'Word':<15} {'Count':>5}")
    print("-" * 22)
    for word, count in word_counts.items():
        print(f"{word:<15} {count:>5}")
    print()


def print_frequent_words(frequent_words: list[str]) -> None:
    print_heading("Words Above Frequency Threshold")
    if frequent_words:
        for word in frequent_words:
            print(f"- {word}")
    else:
        print("No words exceed the frequency threshold.")
    print()


def main() -> None:
    sample_text = """
The cat sat on the mat.
The cat saw a dog.
The dog saw the cat.
The dog barked at the cat.
The cat ran from the dog.
The dog chased the cat.
The cat climbed a tree.
The dog waited by the tree.
The cat meowed in the tree.
The dog barked at the tree.
The cat stayed in the tree.
The dog finally left.
The cat came down from the tree.
The cat returned to the mat.
    """

    print_heading("Sample Text")
    print(sample_text.strip())
    print()

    print("Counting words in the sample text...")
    word_counts = words_count(sample_text)
    print("=> Word counting completed.")
    print_word_counts(word_counts)

    frequency_threshold = 3
    print(f"Filtering words with counts above {frequency_threshold}...")
    frequent_words = get_words_above_frequency(word_counts, frequency_threshold)
    print("=> Filtering completed.")
    print_frequent_words(frequent_words)


if __name__ == "__main__":
    main()
