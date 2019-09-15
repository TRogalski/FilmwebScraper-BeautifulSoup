from nose.tools import *
import sys, os
sys.path.append(os.path.abspath('..'))
from webScrapper.formatUtils import FormatUtils

def test_to_float_1():
    initial = '1.7'
    converted = FormatUtils.to_float(initial)
    expected = 1.7
    assert expected == converted
