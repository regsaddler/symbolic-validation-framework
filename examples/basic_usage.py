from symbolic_gatekeeper import SymbolicGatekeeper

# Mock validators
def reality_check(output: str) -> bool:
    return "unicorn" not in output.lower()

def utility_check(output: str) -> bool:
    return len(output.split()) > 5

gatekeeper = SymbolicGatekeeper(reality_check, utility_check)

symbolic_idea = "The team shall rise like the phoenix from the ashes of deadlines."
gatekeeper.validate_symbolic_output("team_rebirth_myth", symbolic_idea)
