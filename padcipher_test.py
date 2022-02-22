"""""test module in pytest"""

from padcipher import *

def test_generatepad():
    assert newnumpad == random.randint(65,91)

def test_encipher_0():
    assert encipher("A", 0) == "A"

def test_encipher_3():
    assert encipher("A", 3) == "C"

def test_decipher_0():
    assert decipher(65, 0) == "A"

def test_decipher_3():
    assert decipher(65, 3) == "X"
