def validate_ingredients(ingredients: str) -> str:
    valid_elements = ["earth", "air", "water", "fire"]
    if any(element in ingredients for element in valid_elements):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
