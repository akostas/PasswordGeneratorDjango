import random
import string


def generate_password(length=12, use_numbers: bool = True, use_symbols: bool = True) -> str:
    """
    A utility function that generates a password.

    :param length: int: The number of characters that the password will have.
    :param use_numbers: bool: Whether the generated password will include numbers.
    :param use_symbols: bool: Whether the generated password will include symbols.
    :return:
    """
    chars = string.ascii_letters

    if use_numbers:
        chars += string.digits

    if use_symbols:
        chars += string.punctuation

    if not chars:
        return ""

    return "".join(random.choice(chars) for _ in range(length))
