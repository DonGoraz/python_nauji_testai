from newcalc.calc import Calculator
import pytest

@pytest.fixture
def answer():
    return 6


def test_sudetis(answer):
    calc = Calculator()
    assert calc.add(4, 2) == answer


def test_sudetis_su_raidemis_exception():
    calc = Calculator()
    with pytest.raises(Exception):
        assert calc.add("fouras", 2)


def test_atimtis():
    calc = Calculator()
    assert calc.substract(2, 3) == -1


def test_daugyba(answer):
    calc = Calculator()
    assert calc.multiply(2, 3) == answer


def test_dalyba():
    calc = Calculator()
    assert calc.divide(18, 3) == 6


def test_kelimas_laipsniu():
    calc = Calculator()
    assert calc.power(2, 3) == 8
