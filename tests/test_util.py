import unittest
import warnings
import pytest
from util import rename_decorator

def test_deprecated():
    """If there is no function specified in the pydoc comment, the 
    function does not have a replacement"""
    warnings.simplefilter('always')
    with pytest.deprecated_call() as w:
        rename_decorator(deprecated_function)
    # pytest.deprecated_call(rename_decorator(deprecated_function))
    assert(len(w) == 1)
    assert("instead" in w[0].message.args[0])
        
def test_warning_with_input():
    """Tests the behaviour when a function is correctly marked as deprecated"""
    warnings.simplefilter('always')
    with pytest.deprecated_call() as w:
        rename_decorator(faulty_deprecated_function)
    assert(len(w) == 1)
    assert("no replacement" in w[0].message.args[0])
        
def deprecated_function():
    """not_deprecated_function"""
    return not_deprecated_function()
    
def not_deprecated_function():
    return 0

def faulty_deprecated_function():
    return not_deprecated_function()
