#!/usr/bin/env python3
"""
Main demonstration script for the RNW calculator package.

This script demonstrates all the functionality of the calculator module
and serves as an example of how to use the package.
"""

from src.rnw.calculator import add, subtract, multiply, divide, power


def main():
    """Demonstrate calculator functionality with clear output."""
    print("=" * 50)
    print("RNW Calculator Package Demonstration")
    print("=" * 50)
    print()
    
    # Demonstrate addition
    print("Addition Examples:")
    print(f"  2 + 3 = {add(2, 3)}")
    print(f"  1.5 + 2.5 = {add(1.5, 2.5)}")
    print(f"  -1 + 1 = {add(-1, 1)}")
    print()
    
    # Demonstrate subtraction
    print("Subtraction Examples:")
    print(f"  5 - 3 = {subtract(5, 3)}")
    print(f"  1.5 - 2.5 = {subtract(1.5, 2.5)}")
    print(f"  0 - 5 = {subtract(0, 5)}")
    print()
    
    # Demonstrate multiplication
    print("Multiplication Examples:")
    print(f"  3 × 4 = {multiply(3, 4)}")
    print(f"  2.5 × 2 = {multiply(2.5, 2)}")
    print(f"  -2 × 3 = {multiply(-2, 3)}")
    print()
    
    # Demonstrate division
    print("Division Examples:")
    print(f"  10 ÷ 2 = {divide(10, 2)}")
    print(f"  7 ÷ 2 = {divide(7, 2)}")
    print(f"  -6 ÷ 3 = {divide(-6, 3)}")
    print()
    
    # Demonstrate power
    print("Power Examples:")
    print(f"  2³ = {power(2, 3)}")
    print(f"  4^0.5 = {power(4, 0.5)}")
    print(f"  5⁰ = {power(5, 0)}")
    print()
    
    # Demonstrate error handling
    print("Error Handling Example:")
    try:
        result = divide(5, 0)
        print(f"  5 ÷ 0 = {result}")
    except ValueError as e:
        print(f"  5 ÷ 0 → Error: {e}")
    print()
    
    # Demonstrate chained operations
    print("Chained Operations Example:")
    print("  Calculate: (2 + 3) × 4 ÷ 2")
    step1 = add(2, 3)
    print(f"    Step 1: 2 + 3 = {step1}")
    step2 = multiply(step1, 4)
    print(f"    Step 2: {step1} × 4 = {step2}")
    step3 = divide(step2, 2)
    print(f"    Step 3: {step2} ÷ 2 = {step3}")
    print(f"    Final result: {step3}")
    print()
    
    print("=" * 50)
    print("Demonstration complete!")
    print("Run 'pytest' to execute the test suite.")
    print("=" * 50)


if __name__ == "__main__":
    main()