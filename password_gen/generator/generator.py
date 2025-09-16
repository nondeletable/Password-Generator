import secrets
import string

from password_gen.constants import AMBIGUOUS, SYMBOLS


def generate_password(
    length, use_letters=True, use_digits=True, use_symbols=True, exclude_ambiguous=False
):
    categories = []
    if use_letters:
        categories.append(string.ascii_letters)
    if use_digits:
        categories.append(string.digits)
    if use_symbols:
        categories.append(SYMBOLS)

    if not categories:
        raise ValueError("At least one category must be selected")

    # 🔍 Проверка: длина меньше числа категорий
    if length < len(categories):
        raise ValueError(
            "Password length must be at least the number of selected categories"
        )

    all_chars = "".join(categories)

    if exclude_ambiguous:
        all_chars = "".join(ch for ch in all_chars if ch not in AMBIGUOUS)

    if not all_chars:
        raise ValueError("No characters available for generation")

    # Генерация
    password_chars = []
    for cat in categories:
        filtered = [c for c in cat if (not exclude_ambiguous or c not in AMBIGUOUS)]
        if filtered:
            password_chars.append(secrets.choice(filtered))

    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)
