"""
Calculator module providing basic mathematical operations.

This module demonstrates basic Python functionality with proper documentation,
type hints, and error handling. It serves as an example of good Python
coding practices.
"""

from typing import Union

# Type alias for numeric types
Number = Union[int, float]


def add(a: Number, b: Number) -> float:
    """
    Add two numbers and return the result.
    
    Args:
        a: First number to add
        b: Second number to add
        
    Returns:
        The sum of a and b as a float
        
    Examples:
        >>> add(2, 3)
        5.0
        >>> add(2.5, 1.5)
        4.0
        >>> add(-1, 1)
        0.0
    """
    return float(a + b)


def subtract(a: Number, b: Number) -> float:
    """
    Subtract the second number from the first and return the result.
    
    Args:
        a: Number to subtract from
        b: Number to subtract
        
    Returns:
        The difference of a and b as a float
        
    Examples:
        >>> subtract(5, 3)
        2.0
        >>> subtract(1.5, 2.5)
        -1.0
        >>> subtract(0, 5)
        -5.0
    """
    return float(a - b)


def multiply(a: Number, b: Number) -> float:
    """
    Multiply two numbers and return the result.
    
    Args:
        a: First number to multiply
        b: Second number to multiply
        
    Returns:
        The product of a and b as a float
        
    Examples:
        >>> multiply(3, 4)
        12.0
        >>> multiply(2.5, 2)
        5.0
        >>> multiply(-2, 3)
        -6.0
    """
    return float(a * b)


def divide(a: Number, b: Number) -> float:
    """
    Divide the first number by the second and return the result.
    
    Args:
        a: Dividend (number to be divided)
        b: Divisor (number to divide by)
        
    Returns:
        The quotient of a and b as a float
        
    Raises:
        ValueError: If b is zero (division by zero)
        
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
        >>> divide(-6, 3)
        -2.0
        >>> divide(5, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return float(a / b)


def power(a: Number, b: Number) -> float:
    """
    Raise the first number to the power of the second and return the result.
    
    Args:
        a: Base number
        b: Exponent
        
    Returns:
        a raised to the power of b as a float
        
    Examples:
        >>> power(2, 3)
        8.0
        >>> power(4, 0.5)
        2.0
        >>> power(5, 0)
        1.0
    """
    return float(a ** b)