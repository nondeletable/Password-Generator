import pytest

from password_gen.policies.policies import POLICIES
from password_gen.ui import handlers


class FakeSession(dict):
    def set(self, key, value):
        self[key] = value


class FakePage:
    def __init__(self):
        self.session = FakeSession()
        self.updated = False
        self.overlay = []

    def update(self):
        self.updated = True


class FakeControl:
    def __init__(self, value=None):
        self.value = value


@pytest.mark.parametrize("policy_name", ["Standard", "Admin", "NIST"])
def test_on_policy_change_applies_policy(policy_name):
    page = FakePage()
    policy_selector = FakeControl(policy_name)
    length_selector = FakeControl("0")
    letters_switch = FakeControl(False)
    digits_switch = FakeControl(False)
    symbols_switch = FakeControl(False)

    handlers.on_policy_change(
        None,
        page,
        policy_selector,
        length_selector,
        letters_switch,
        digits_switch,
        symbols_switch,
    )

    policy = POLICIES[policy_name]
    assert length_selector.value == str(policy["length"])
    assert letters_switch.value == policy["letters"]
    assert digits_switch.value == policy["digits"]
    assert symbols_switch.value == policy["symbols"]
    assert page.session["exclude_ambiguous"] == policy["exclude_ambiguous"]
    assert page.updated


def test_on_policy_change_custom_does_nothing():
    page = FakePage()
    policy_selector = FakeControl("Custom")
    length_selector = FakeControl("10")
    letters_switch = FakeControl(True)
    digits_switch = FakeControl(True)
    symbols_switch = FakeControl(True)

    handlers.on_policy_change(
        None,
        page,
        policy_selector,
        length_selector,
        letters_switch,
        digits_switch,
        symbols_switch,
    )

    # Значения остались прежними
    assert length_selector.value == "10"
    assert letters_switch.value is True
    assert digits_switch.value is True
    assert symbols_switch.value is True
    assert page.updated
