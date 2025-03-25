from collections import Counter
from re import findall

from constants import SAMPLE_TEXT


def words_count(text: str) -> dict:
    return dict(sorted(Counter(findall(r"\w+", text.lower())).items(), key=lambda item: item[1], reverse=True))


def get_words_above_frequency(words: dict, frequency_threshold: int = 3) -> list:
    return [word for word, count in words.items() if count > frequency_threshold]


def main() -> None:
    word_counts = words_count(SAMPLE_TEXT)
    print(f"Dictionary of word counts:\n{word_counts}")

    frequent = get_words_above_frequency(word_counts)
    print(f"\nWords that appear more than 3 times:\n{frequent}")


if __name__ == "__main__":
    main()
