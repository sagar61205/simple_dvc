import pytest

class NotinRange(Exception):
    def __init__(self, message='Value not in range'):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a = 5
    with pytest.raises(NotinRange):
         if a not in range(15,20):
            raise NotinRange

def test_something():
    a=5
    b=5
    assert True