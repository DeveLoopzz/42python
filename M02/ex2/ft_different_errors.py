def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        tmp = 10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "python" + 42
    else:
        return None

def test_error_types():
    for i in range(0, 5):
        try:
            print(f"Testing operation  {i}...")
            tmp = garden_operations(i)
            if tmp == None:
                print("Operation completed successfully!\n")
                return
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")

