from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell

def main() -> None:
    print("=== Circular Curse Breaking ===")
    
    print("Testing ingredient validation:")
    print(f"validate_ingredients(\"fire air\"): {validate_ingredients('fire air')}")
    print(f"validate_ingredients(\"dragon scales\"): {validate_ingredients('dragon scales')}")
    
    print("\nTesting spell recording with validation:")
    print(f"record_spell(\"Fireball\", \"fire air\"): {record_spell('Fireball', 'fire air')}")
    print(f"record_spell(\"Dark Magic\", \"shadow\"): {record_spell('Dark Magic', 'shadow')}")
    
    print("\nTesting late import technique:")
    print(f"record_spell(\"Lightning\", \"air\"): {record_spell('Lightning', 'air')}")
    
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")

if __name__ == "__main__":
    main()
