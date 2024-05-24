from task_01_duck_typing import Circle


def test_circle_negative():
    try:
        Circle(-5)
    except ValueError as e:
        if str(e) == "Radius cannot be negative":
            print("Test passed: ValueError raised for negative radius.")
        else:
            print(f"Test failed: Unexpected ValueError message: {e}")
    else:
        print("Test failed: ValueError not raised for negative radius.")


if __name__ == "__main__":
    test_circle_negative()
