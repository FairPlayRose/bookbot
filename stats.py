def get_word_count(file: str) -> int:
    return len(file.split())

def get_character_count(file: str) -> int:
    character_count = {}
    file = file.lower()
    for character in file:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_on(dict):
    return dict["num"]

def sort_character_dict(character_count: dict[str, int]) -> dict[str, int]:
    characters_and_counts = [{"name": k, "num": v} for k, v in character_count.items() if k.isalpha()]
    characters_and_counts.sort(reverse=True, key=sort_on)
    return characters_and_counts