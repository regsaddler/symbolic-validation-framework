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

# Lexical diversity heuristic for repetitive loops
def lexical_diversity(text: str) -> float:
    return len(set(text.split())) / max(1, len(text.split()))


# Backward-compatible name retained for callers of the original prototype.
semantic_entropy = lexical_diversity


# Gatekeeper class with layered checks
class SymbolicGatekeeper:
    def __init__(
        self,
        reality_check: Callable[[str], bool],
        utility_check: Callable[[str], bool],
        min_word_diversity: float = 0.25,
    ):
        if not 0.0 <= min_word_diversity <= 1.0:
            raise ValueError("min_word_diversity must be between 0 and 1")
        self.symbol_store: Dict[str, Symbol] = {}
        self.reality_check = reality_check
        self.utility_check = utility_check
        self.min_word_diversity = min_word_diversity

    def validate_symbolic_output(self, label: str, output: str) -> bool:
        if label in self.symbol_store and self.symbol_store[label].is_expired():
            del self.symbol_store[label]  # Decay expired symbols

        diversity = lexical_diversity(output)
        if diversity < self.min_word_diversity:
            print(f"[REJECTED] Low word diversity in '{label}' → Possible repetitive drift.")
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
