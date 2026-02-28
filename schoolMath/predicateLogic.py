# Define predicates as Python functions
def human(x: str) -> bool:
    return x in ["Socrates", "Plato"]

def mortal(x: str) -> bool:
    # In our model, every human is mortal
    return human(x)

def god(x: str) -> bool:
    return x == "Zeus"

# Logical implication: P -> Q
def implies(p: bool, q: bool) -> bool:
    return (not p) or q

# Universal quantifier ∀
def forall(domain: list, predicate) -> bool:
    return all(predicate(x) for x in domain)

# Existential quantifier ∃
def exists(domain: list, predicate) -> bool:
    return any(predicate(x) for x in domain)

# Domain of discourse
domain = ["Socrates", "Plato", "Zeus"]

# Universal formula: ∀x. Human(x) -> Mortal(x)
law_forall = forall(domain, lambda x: implies(human(x), mortal(x)))

# Existential formula: ∃x. Mortal(x)
law_exists = exists(domain, mortal)

# Detailed per-element check
def check_each(domain):
    for x in domain:
        print(f"Checking: {x}")
        print(f"  Human(x)  = {human(x)}")
        print(f"  Mortal(x) = {mortal(x)}")
        print(f"  Human(x) -> Mortal(x) = {implies(human(x), mortal(x))}")
        print(f"  God(x)    = {god(x)}\n")

# Main execution
if __name__ == "__main__":
    print("Universal quantifier check: ∀x. Human(x) -> Mortal(x)")
    print("------------------------------------------")
    check_each(domain)
    print(f"Is the universal formula true for the entire domain? {law_forall}\n")

    print("Existential quantifier check: ∃x. Mortal(x)")
    print("------------------------------------------")
    print(f"Is there at least one mortal? {law_exists}")