def check_strength(password: str):
    pw_points = len(password) / 2
    if len(password) < 10:
        print("Your password must be more than 10 characters")
        return

    special_characters = [
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
    ]  # worth 5 pts each

    if not any(char in password for char in special_characters):
        print("Passowrd must contain a special character")
        return

    for char in password:
        if char in special_characters:
            pw_points = pw_points + 5

    print(f"Your password scored {pw_points} points!")


def main():
    password = input("Enter a password: ")
    check_strength(password)


if __name__ == "__main__":
    main()
