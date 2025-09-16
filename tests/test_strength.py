from password_gen.generator.strength import check_strength


def test_weak_password_short():
    """Слишком короткий пароль должен считаться слабым."""
    assert check_strength("abc") == "weak"
    assert check_strength("12!") == "weak"


def test_weak_password_no_variety():
    """Даже длинный, но однотипный пароль (например, только цифры) — слабый."""
    assert check_strength("12345678") == "weak"
    assert check_strength("aaaaaaaaaaaa") == "weak"


def test_fair_password_medium():
    """Средний уровень: длина достаточная, но разнообразие категорий не максимальное."""
    assert check_strength("abc12345") == "fair"  # буквы+цифры
    assert check_strength("abcdEFGH") == "fair"  # верхний+нижний регистр


def test_strong_password():
    """Сильный пароль: длина >= 12 и разнообразие >= 3 категорий."""
    assert check_strength("Abcdef12345!") == "strong"
    assert check_strength("Qwerty1234+-") == "strong"
