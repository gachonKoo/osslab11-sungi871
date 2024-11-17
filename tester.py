# tester.py
from geo.utils import calculate_triangle_area

# Test the function
if __name__ == "__main__":
    base = 10
    height = 5
    area = calculate_triangle_area(base, height)
    print(f"Triangle area: {area}")  # Expected: 25.0
