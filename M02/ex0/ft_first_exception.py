def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    try:
        valid = "25"
        invalid = "abc"
        print(f"Input data is '{valid}'")
        valid_res = input_temperature(valid)
        print(f"Temperature is now {valid_res}\n")
        print(f"Input data is '{invalid}'")
        invalid_res = input_temperature(invalid)
        print(f"Temperature is now '{invalid_res}'\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("All tests completed - program didn't crash!")
