import pytest

def test_exception_message():
    with pytest.raises(ValueError) as excinfo:
        int('hello')

    assert excinfo.value.args[0] == 'invalid literal for int() with base 10: "hello"'

test_exception_message()


