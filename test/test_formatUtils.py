from nose.tools import *
from webScrapper.utils.formatUtils import FormatUtils
from bs4 import BeautifulSoup

def test_to_float_1():
    initial = BeautifulSoup('1.7','html.parser')
    converted = FormatUtils.to_float(initial)
    expected = 1.7
    assert expected == converted
    
def test_to_float_2():
    initial = BeautifulSoup('1,7','html.parser')
    converted = FormatUtils.to_float(initial)
    expected = 1.7
    assert expected == converted

def test_to_float_3():
    initial = BeautifulSoup('20','html.parser')
    converted = FormatUtils.to_float(initial)
    expected = 20.0
    assert expected == converted
    
    # not really what would we want - revise function so negative scores are handled if they
    # ever appear
def test_to_float_4():
    initial = BeautifulSoup('-15','html.parser')
    converted = FormatUtils.to_float(initial)
    expected = -15
    assert expected == converted

def test_to_float_5():
    initial = None
    converted = FormatUtils.to_float(initial)
    expected = "N/A"
    assert expected == converted
