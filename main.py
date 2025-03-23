import sys
from stats import get_word_count, get_character_count, sort_character_dict

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    file = get_book_text(book_path)
    word_count = get_word_count(file)
    character_count = get_character_count(file)
    sorted_characters = sort_character_dict(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for lookup in sorted_characters:
        print(f'{lookup["name"]}: {lookup["num"]}')

main()
