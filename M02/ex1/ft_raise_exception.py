def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise Exception(f"{temp}C is too hot for plants (max 40c)")
    if temp < 0:
        raise Exception(f"{temp}C is too cold for plants (min 0c)")
    return temp

def test_temperature() -> None:
    test_cases = ["25", "abc", "100", "-50"]
    
    for data in test_cases:
        print(f"Input data is {data}")

        try:
            input_temperature(data)
            print(f"Temperature is now {data}C\n")
        except Exception as e:
            print(f"Caught input_temperature error: {e}\n")
if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
