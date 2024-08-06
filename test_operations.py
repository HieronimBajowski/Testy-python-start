import operations
import math

def run_test(test_name, result, expected):
    if result == expected:
        print(f"{test_name} passed")
    else:
        print(f"{test_name} failed")

def test_add():
    run_test("Test 1", operations.add(2, 3), 5)

def test_subtract():
    run_test("Test 2", operations.subtract(5, 3), 2)

def test_multiply():
    run_test("Test 3", operations.multiply(4, 3), 12)

def test_divide():
    run_test("Test 4", operations.divide(10, 2), 5)
    try:
        operations.divide(10, 0)
    except ValueError:
        print("Test 5 passed")
    else:
        print("Test 5 failed")

def test_circle_area():
    run_test("Test 6", operations.circle_area(3), math.pi * 9)

def test_circle_circumference():
    run_test("Test 7", operations.circle_circumference(3), 2 * math.pi * 3)

def test_square_area():
    run_test("Test 8", operations.square_area(4), 16)

def test_square_perimeter():
    run_test("Test 9", operations.square_perimeter(4), 16)

def test_triangle_area():
    run_test("Test 10", operations.triangle_area(4, 3), 6)

def test_triangle_perimeter():
    run_test("Test 11", operations.triangle_perimeter(3, 4, 5), 12)

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_circle_area()
    test_circle_circumference()
    test_square_area()
    test_square_perimeter()
    test_triangle_area()
    test_triangle_perimeter()
