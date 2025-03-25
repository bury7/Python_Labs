from collections import Counter
from re import findall

from constants import SAMPLE_TEXT


def words_count(text: str) -> dict:
    return dict(sorted(Counter(findall(r"\w+", text.lower())).items(), key=lambda item: item[1], reverse=True))


def frequent_words(words: dict, min_count: int = 3) -> list:
    return [word for word, count in words.items() if count > min_count]


def main() -> None:
    word_counts = words_count(SAMPLE_TEXT)
    print(f"Dictionary of word counts:\n{word_counts}")

    frequent = frequent_words(word_counts)
    print(f"\nWords that appear more than 3 times:\n{frequent}")


if __name__ == "__main__":
    main()
