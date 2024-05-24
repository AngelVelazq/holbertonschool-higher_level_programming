from task_01_duck_typing import Circle


def test_circle_negative():
    try:
        circle_negative = Circle(-5)
    except ValueError as e:
        assert str(e) == "Radius cannot be negative"
        print("Test passed: ValueError raised for negative radius.")
    else:
        print("Test failed: ValueError not raised for negative radius.")


if __name__ == "__main__":
    test_circle_negative()
