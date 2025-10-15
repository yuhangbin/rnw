"""
Comprehensive unit tests for the calculator module.

This test suite demonstrates pytest best practices including:
- Organized test classes
- Descriptive test names
- Edge case testing
- Error condition testing
- Floating point precision handling
"""

import pytest
from src.rnw.calculator import add, subtract, multiply, divide, power


class TestAdd:
    """Test cases for the add function."""
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert add(2, 3) == 5.0
        assert add(1.5, 2.5) == 4.0
        
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert add(-2, -3) == -5.0
        assert add(-1.5, 2.5) == 1.0
        
    def test_add_zero(self):
        """Test addition with zero."""
        assert add(0, 5) == 5.0
        assert add(5, 0) == 5.0
        assert add(0, 0) == 0.0
        
    def test_add_floating_point_precision(self):
        """Test floating point precision with pytest.approx."""
        result = add(0.1, 0.2)
        assert result == pytest.approx(0.3)


class TestSubtract:
    """Test cases for the subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert subtract(5, 3) == 2.0
        assert subtract(10, 4) == 6.0
        
    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative number."""
        assert subtract(3, 5) == -2.0
        assert subtract(1.5, 2.5) == -1.0
        
    def test_subtract_zero(self):
        """Test subtraction with zero."""
        assert subtract(5, 0) == 5.0
        assert subtract(0, 5) == -5.0
        assert subtract(0, 0) == 0.0
        
    def test_subtract_same_numbers(self):
        """Test subtracting a number from itself."""
        assert subtract(7, 7) == 0.0
        assert subtract(-3, -3) == 0.0


class TestMultiply:
    """Test cases for the multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert multiply(3, 4) == 12.0
        assert multiply(2.5, 2) == 5.0
        
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert multiply(-2, 3) == -6.0
        assert multiply(-2, -3) == 6.0
        
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(5, 0) == 0.0
        assert multiply(0, 5) == 0.0
        assert multiply(0, 0) == 0.0
        
    def test_multiply_by_one(self):
        """Test multiplication by one."""
        assert multiply(7, 1) == 7.0
        assert multiply(1, 7) == 7.0
        
    def test_multiply_floating_point(self):
        """Test floating point multiplication."""
        result = multiply(0.1, 3)
        assert result == pytest.approx(0.3)


class TestDivide:
    """Test cases for the divide function."""
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert divide(10, 2) == 5.0
        assert divide(7, 2) == 3.5
        
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert divide(-6, 3) == -2.0
        assert divide(-6, -3) == 2.0
        assert divide(6, -3) == -2.0
        
    def test_divide_by_one(self):
        """Test division by one."""
        assert divide(5, 1) == 5.0
        assert divide(-3, 1) == -3.0
        
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0.0
        assert divide(0, -3) == 0.0
        
    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
            
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(-3, 0)
            
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(0, 0)
            
    def test_divide_floating_point_precision(self):
        """Test floating point division precision."""
        result = divide(1, 3)
        assert result == pytest.approx(0.3333333333333333)


class TestPower:
    """Test cases for the power function."""
    
    def test_power_positive_integers(self):
        """Test power with positive integers."""
        assert power(2, 3) == 8.0
        assert power(5, 2) == 25.0
        
    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        assert power(5, 0) == 1.0
        assert power(-3, 0) == 1.0
        
    def test_power_one_exponent(self):
        """Test power with exponent of one."""
        assert power(7, 1) == 7.0
        assert power(-4, 1) == -4.0
        
    def test_power_fractional_exponent(self):
        """Test power with fractional exponents."""
        assert power(4, 0.5) == 2.0
        assert power(27, 1/3) == pytest.approx(3.0)
        
    def test_power_negative_base(self):
        """Test power with negative base."""
        assert power(-2, 2) == 4.0
        assert power(-2, 3) == -8.0


class TestIntegration:
    """Integration tests combining multiple operations."""
    
    def test_calculator_operations_chain(self):
        """Test chaining calculator operations."""
        # (2 + 3) * 4 / 2 = 10
        result1 = add(2, 3)
        result2 = multiply(result1, 4)
        result3 = divide(result2, 2)
        assert result3 == 10.0
        
    def test_calculator_with_mixed_types(self):
        """Test calculator operations with mixed int/float types."""
        assert add(2, 3.5) == 5.5
        assert multiply(3, 2.5) == 7.5
        assert divide(7, 2) == 3.5