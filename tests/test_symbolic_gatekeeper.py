import unittest
from symbolic_gatekeeper import SymbolicGatekeeper

def dummy_reality_check(text):
    return "error" not in text

def dummy_utility_check(text):
    return len(text.split()) > 5

class TestSymbolicGatekeeper(unittest.TestCase):
    def test_validation(self):
        gk = SymbolicGatekeeper(dummy_reality_check, dummy_utility_check)
        result = gk.validate_symbolic_output("test_symbol", "This is a valid symbolic phrase for testing.")
        self.assertTrue(result)

    def test_rejection_entropy(self):
        gk = SymbolicGatekeeper(dummy_reality_check, dummy_utility_check)
        repetitive = "loop loop loop loop loop"
        result = gk.validate_symbolic_output("bad_entropy", repetitive)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
