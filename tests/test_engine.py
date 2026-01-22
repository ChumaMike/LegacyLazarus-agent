import pytest
from legacy_lazarus.engine import process_code_string

# Mock input for testing (don't use real sensitive code)
SAMPLE_LEGACY_CODE = """
def old_function(x):
    print 'Hello World' # Python 2 syntax
    return x + 1
"""

def test_refactor_logic():
    """
    Test that the agent correctly identifies Python 2 syntax 
    and returns a valid Python 3 structure.
    """
    result = process_code_string(SAMPLE_LEGACY_CODE)
    
    # Assertions
    assert "refactored_code" in result
    assert result["complexity_score"] < 8
    assert "print(" in result["refactored_code"] # Checks if print statement was fixed
    assert not result["needs_human_escalation"]