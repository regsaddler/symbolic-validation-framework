"""
Symbolic Output Gatekeeper
Part of the SVN 1.2 Validation Framework
"""

import time
from typing import Callable, Any, Dict

# Basic decay model for symbolic lifespan
class Symbol:
    def __init__(self, name: str, value: Any, ttl: int = 600):
        self.name = name
        self.value = value
        self.created_at = time.time()
        self.ttl = ttl  # Time-to-live in seconds

    def is_expired(self) -> bool:
        return (time.time() - self.created_at) > self.ttl

# Entropy estimator for recursive loops
def semantic_entropy(text: str) -> float:
    return len(set(text.split())) / max(1, len(text.split()))

# Gatekeeper class with layered checks
class SymbolicGatekeeper:
    def __init__(self, reality_check: Callable[[str], bool], utility_check: Callable[[str], bool]):
        self.symbol_store: Dict[str, Symbol] = {}
        self.reality_check = reality_check
        self.utility_check = utility_check

    def validate_symbolic_output(self, label: str, output: str) -> bool:
        if label in self.symbol_store and self.symbol_store[label].is_expired():
            del self.symbol_store[label]  # Decay expired symbols

        entropy = semantic_entropy(output)
        if entropy > 0.85:
            print(f"[REJECTED] High entropy in '{label}' → Possible recursive drift.")
            return False

        if not self.reality_check(output):
            print(f"[REJECTED] Reality check failed for '{label}'.")
            return False

        if not self.utility_check(output):
            print(f"[REJECTED] Utility check failed for '{label}'.")
            return False

        # Passed all checks
        self.symbol_store[label] = Symbol(name=label, value=output)
        print(f"[ACCEPTED] Symbol '{label}' stored.")
        return True
