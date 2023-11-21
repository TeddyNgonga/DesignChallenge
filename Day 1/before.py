def count_fruits(fruits: list[str]) -> dict[str, int]:
    fruit_count = {}
    for fruit in fruits:
        if type(fruit) != str:
            continue
        if fruit not in fruit_count:
            fruit_count[fruit] = 1
        else:
            fruit_count[fruit] += 1
    return fruit_count


def main() -> None:
    assert count_fruits(
        [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]
    ) == {"apple": 4, "banana": 3, "cherry": 4}
    assert count_fruits([]) == {}
    assert count_fruits(["apple", "pear", "orange", "pear", None]) == {"apple": 1, "pear": 2, "orange": 1}
    assert count_fruits([1, 3, 4, "pear", None, ["hi", "bye"]]) == {"pear": 1}
    # add more tests


if __name__ == "__main__":
    main()
