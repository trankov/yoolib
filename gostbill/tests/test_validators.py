from .. import validators


def test_validator_max_len():
    assert validators.max_len('12345', 5)
    assert not validators.max_len('12345', 3)


def test_validator_min_max_len():
    assert validators.min_max_len('12345', 3, 5)
    assert not validators.min_max_len('12345', 3, 4)
    assert not validators.min_max_len('12345', 6, 7)


def test_validator_cast():
    assert validators.cast(1, str) == '1'
    assert validators.cast('1', str) == '1'
    assert validators.cast(1, int) == 1
    assert validators.cast('1', int) == 1


def test_validator_unstring_float():
    assert validators.unstring_float(1.1) == 1.1
    assert validators.unstring_float('1.1') == 1.1
    assert validators.unstring_float('1,1') == '1,1'


def test_validator_digits_only():
    assert validators.digits_only('1,1') == '11'
    assert validators.digits_only('11') == '11'
    assert validators.digits_only('ABC') == ''


def test_validator_make_non_empty():
    assert validators.make_non_empty('', 'default') == 'default'
    assert validators.make_non_empty('default') == 'default'
