OPENING = {"(": ")", "{": "}", "<": ">"}
CLOSING = {value: key for key, value in OPENING.items()}


def find_invalid_positions(text: str) -> list[int]:
    if not isinstance(text, str):
        raise TypeError("Очікується рядок")

    stack = []
    invalid = set()

    for index, char in enumerate(text):
        if char in OPENING:
            stack.append((char, index))
        elif char in CLOSING:
            if stack and stack[-1][0] == CLOSING[char]:
                stack.pop()
            elif stack:
                _, opening_index = stack.pop()
                invalid.add(opening_index)
                invalid.add(index)
            else:
                invalid.add(index)

    invalid.update(index for _, index in stack)
    return sorted(invalid)


def validate_brackets(text: str) -> bool:
    positions = find_invalid_positions(text)
    if positions:
        numbers = ", ".join(str(position + 1) for position in positions)
        raise ValueError(f"Дужки незбалансовані на позиціях {numbers}")
    return True


def highlight_invalid_brackets(text: str, positions: list[int]) -> str:
    markers = [" " for _ in text]
    for position in positions:
        if 0 <= position < len(text):
            markers[position] = "^"
    return text + "\n" + "".join(markers)


def main() -> None:
    text = input("Введіть строку: ")
    try:
        validate_brackets(text)
        print("Строка валідна")
    except ValueError as error:
        print(f"Помилка: {error}")
        print(highlight_invalid_brackets(text, find_invalid_positions(text)))


if __name__ == "__main__":
    main()
