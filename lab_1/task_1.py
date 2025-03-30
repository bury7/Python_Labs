from collections import Counter
from re import findall

SAMPLE_TEXT = """
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


def words_count(text: str) -> dict:
    return dict(sorted(Counter(findall(r"\w+", text.lower())).items(), key=lambda item: item[1], reverse=True))


def get_words_above_frequency(words: dict, frequency_threshold: int = 3) -> list:
    return [word for word, count in words.items() if count > frequency_threshold]


def main() -> None:
    print(f"Used text:{SAMPLE_TEXT}")

    word_counts = words_count(SAMPLE_TEXT)
    print(f"Dictionary of word counts:\n{word_counts}")

    frequent = get_words_above_frequency(word_counts)
    print(f"\nWords that appear more than 3 times:\n{frequent}")


if __name__ == "__main__":
    main()
