class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        self.message = message


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def check_plant(name: str, health: int) -> None:
    if health < 50:
        raise PlantError(f"The {name} is wilting!")

def check_water(level: int) -> None:
    if level < 10:
        raise WaterError(f"Not enough water in the tank!")

def test_error_cases() -> None:
    print("Testing PlantError...")
    try:
        check_plant("tomato", 20)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
       check_water(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    fail = [
        lambda: check_plant("tomato", 10),
        lambda: check_water(5)
    ]
    for action in fail:
        try:
            action()
        except GardenError as e:
            print(f"Caught GardenError:{e}")
            
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_error_cases()
