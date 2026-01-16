from password_gen.blacklist.blacklist import (
    check_blacklist,
    has_repeated_chars,
    is_blacklisted,
    is_too_short,
)


def test_is_blacklisted_true():
    assert is_blacklisted("password")
    assert is_blacklisted("PASSWORD")  # регистр не должен влиять
    assert is_blacklisted("123456")
    assert is_blacklisted("qwerty")


def test_is_blacklisted_false():
    assert not is_blacklisted("securePass123!")


def test_has_repeated_chars_true():
    assert has_repeated_chars("aaaaaa")  # один символ повторяется
    assert has_repeated_chars("1111xyz")  # цифра повторяется
    assert has_repeated_chars("abc!!!!")  # спецсимвол повторяется


def test_has_repeated_chars_false():
    assert not has_repeated_chars("abcd123!")
    assert not has_repeated_chars("AaBbCcDd")


def test_is_too_short_true():
    assert is_too_short("123")  # слишком короткий
    assert is_too_short("abcdefg")  # ровно 7 символов


def test_is_too_short_false():
    assert not is_too_short("abcdefgh")  # ровно 8 символов
    assert not is_too_short("longsecurepassword")


def test_check_blacklist_common():
    assert check_blacklist("password") == "This password is too common."


def test_check_blacklist_repeats():
    assert (
        check_blacklist("aaaaaa") == "This password has too many repeated characters."
    )


def test_check_blacklist_short():
    assert check_blacklist("123") == "Password is too short."


def test_check_blacklist_secure():
    assert check_blacklist("Xyz123!@") is None
