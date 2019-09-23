from nose.tools import *
from webScraper.utils.formatUtils import FormatUtils
from bs4 import BeautifulSoup

def test_to_float_1():
    initial = BeautifulSoup('1.7', 'html.parser')
    converted = FormatUtils.to_float(initial)
    expected = 1.7
    assert expected == converted


def test_to_float_2():
    initial = BeautifulSoup('1,7', 'html.parser')
    converted = FormatUtils.to_float(initial)
    expected = 1.7
    assert expected == converted


def test_to_float_3():
    initial = BeautifulSoup('20', 'html.parser')
    converted = FormatUtils.to_float(initial)
    expected = 20.0
    assert expected == converted

    
# not really what we want here, negative values should be handled somehow
def test_to_float_4():
    initial = BeautifulSoup('-15', 'html.parser')
    converted = FormatUtils.to_float(initial)
    expected = -15
    assert expected == converted


def test_to_float_5():
    initial = None
    converted = FormatUtils.to_float(initial)
    expected = "N/A"
    assert expected == converted


def test_to_float_6():
    initial = BeautifulSoup("String instead of number", 'html.parser')
    converted = FormatUtils.to_float(initial)
    expected = "error"
    assert expected == converted


def test_to_int_1():
    initial = BeautifulSoup('1000', 'html.parser')
    converted = FormatUtils.to_int(initial)
    expected = 1000
    assert expected == converted


def test_to_int_2():
    initial = BeautifulSoup('1,6', 'html.parser')
    converted = FormatUtils.to_int(initial)
    expected = "error"
    assert expected == converted


def test_to_int_3():
    initial = None
    converted = FormatUtils.to_int(initial)
    expected = "N/A"
    assert expected == converted


def test_to_int_4():
    initial = BeautifulSoup('1.2', 'html.parser')
    converted = FormatUtils.to_int(initial)
    expected = "error"
    assert expected == converted


def test_to_int_5():
    initial = BeautifulSoup('String instead of number', 'html.parser')
    converted = FormatUtils.to_int(initial)
    expected = "error"
    assert expected == converted

# just like in float_4, maybe negatives should be handled somehow
def test_to_int_6():
    initial = BeautifulSoup('-10', 'html.parser')
    converted = FormatUtils.to_int(initial)
    expected = -10
    assert expected == converted
