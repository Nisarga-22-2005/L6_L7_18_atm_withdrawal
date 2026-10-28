import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup


def test_simple_withdrawal():
    assert withdraw(5000, 1000, "savings", True) == 4000


def test_current_account_withdrawal():
    assert withdraw(60000, 2000, "current", True) == 58000


def test_unknown_account():
    with pytest.raises(ValueError, match="unknown account"):
        withdraw(5000, 1000, "student", True)


def test_zero_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 0, "savings", True)


def test_negative_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, -100, "savings", True)


def test_amount_not_multiple_of_100():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 150, "savings", True)


def test_savings_limit_exceeded():
    assert withdraw(50000, 25100, "savings", True) == "limit exceeded"


def test_current_limit_exceeded():
    assert withdraw(60000, 50100, "current", True) == "limit exceeded"


def test_other_bank_withdrawal():
    assert withdraw(5000, 1000, "savings", False) == 3980


def test_other_bank_high_amount_fee():
    assert withdraw(20000, 11000, "current", False) == 8970


def test_insufficient_funds_own_bank():
    assert withdraw(500, 1000, "savings", True) == "insufficient funds"


def test_insufficient_funds_other_bank():
    assert withdraw(1000, 1000, "savings", False) == "insufficient funds"


def test_correct_pin():
    assert pin_check(1234, 1234, 0) == "ok"


def test_wrong_pin_retry():
    assert pin_check(1111, 1234, 0) == "retry"


def test_wrong_pin_last_attempt():
    assert pin_check(1111, 1234, 2) == "card blocked"


def test_card_already_blocked():
    assert pin_check(1234, 1234, 3) == "card blocked"


def test_note_breakup_with_500_notes():
    assert note_breakup(1200) == (2, 1, 0)


def test_note_breakup_with_200_notes():
    assert note_breakup(400) == (0, 2, 0)


def test_note_breakup_with_100_notes():
    assert note_breakup(300) == (0, 1, 1)


def test_note_breakup_invalid_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        note_breakup(150)

def test_note_breakup_remaining_below_200():
    assert note_breakup(600) == (1, 0, 1)