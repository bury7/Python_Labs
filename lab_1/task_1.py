from collections import Counter
from re import findall


def words_count(text: str) -> dict:
    return dict(sorted(Counter(findall(r"\w+", text.lower())).items(), key=lambda item: item[1], reverse=True))


def frequent_words(words: dict, min_count: int = 3) -> list:
    return [word for word, count in words.items() if count > min_count]


if __name__ == "__main__":
    sample_text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fringilla est vel libero suscipit ultricies.
    Mauris ut ligula diam. Nam ut porta urna. Cras tincidunt lobortis elementum. Pellentesque orci ligula,
    pellentesque nec diam et, pellentesque varius leo. Quisque et erat rhoncus, sollicitudin leo consectetur,
    bibendum elit. Ut at luctus orci. Sed luctus neque vitae placerat aliquet. Nullam condimentum sollicitudin
    justo non congue. Ut at magna sed erat sagittis scelerisque vel a sapien. In id facilisis lorem, quis
    consectetur tellus. Cras pellentesque dignissim nisl et tempus. Cras pulvinar purus libero, in fermentum
    libero imperdiet ut.

    Integer molestie nisl vitae quam tristique, non suscipit velit faucibus. Nullam interdum nisl ut justo
    dignissim congue. Etiam tempor neque ut nisi faucibus maximus. Aliquam erat volutpat. Proin auctor quam sed
    nulla ullamcorper laoreet. Duis lacinia et dolor eu tristique. Aenean in luctus massa. Morbi purus ligula,
    consectetur eget nisl et, ultricies blandit nibh. Integer sem ante, hendrerit mollis tempor non, feugiat
    non ante. Aenean convallis gravida turpis vel sollicitudin. Maecenas semper egestas molestie. Duis eget
    lorem diam. Praesent nec nulla rhoncus, interdum nisl id, consectetur augue. Maecenas in aliquet augue.
    Praesent gravida tincidunt tristique. Proin blandit nisl sed nibh vehicula, quis pellentesque felis volutpat.
    """

    word_counts = words_count(sample_text)
    print(word_counts)
    print("\nTop 10 most frequent words:")
    for i, (word, count) in enumerate(list(word_counts.items())[:10], 1):
        print(f"{i}. {word}: {count}")

    frequent = frequent_words(word_counts)
    print(f"\n{frequent}")
    print("\nWords appearing more than 3 times:")
    for word in frequent:
        print(f"- {word} ({word_counts[word]} times)")
