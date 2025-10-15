# RNW Calculator Package

A simple Python calculator package demonstrating modern Python development practices including proper project structure, comprehensive testing, and clear documentation.

## Features

- **Basic Mathematical Operations**: Addition, subtraction, multiplication, division, and power operations
- **Type Safety**: Full type hints for better code clarity and IDE support
- **Comprehensive Testing**: Complete test suite using pytest with edge cases and error handling
- **Modern Python Packaging**: Uses pyproject.toml for configuration
- **Documentation**: Detailed docstrings and examples for all functions

## Installation

### Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd rnw
```

2. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

3. Install the package in development mode:
```bash
pip install -e .
```

## Usage

### Basic Calculator Operations

```python
from src.rnw.calculator import add, subtract, multiply, divide, power

# Basic operations
result = add(2, 3)        # 5.0
result = subtract(10, 4)  # 6.0
result = multiply(3, 4)   # 12.0
result = divide(10, 2)    # 5.0
result = power(2, 3)      # 8.0

# Error handling
try:
    result = divide(5, 0)
except ValueError as e:
    print(f"Error: {e}")  # Error: Cannot divide by zero
```

### Running the Demo

Execute the demonstration script to see all calculator functions in action:

```bash
python main.py
```

## Testing

Run the complete test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=src/rnw
```

Run tests with verbose output:

```bash
pytest -v
```

## Development Tools

This project includes configuration for several development tools:

- **pytest**: Testing framework with comprehensive test coverage
- **black**: Code formatting
- **flake8**: Code linting
- **mypy**: Static type checking

Run code formatting:
```bash
black src/ tests/ main.py
```

Run linting:
```bash
flake8 src/ tests/ main.py
```

Run type checking:
```bash
mypy src/
```

## Project Structure

```
rnw/
├── src/
│   └── rnw/
│       ├── __init__.py          # Package initialization
│       └── calculator.py        # Calculator functions
├── tests/
│   ├── __init__.py             # Test package initialization
│   └── test_calculator.py      # Comprehensive test suite
├── main.py                     # Demonstration script
├── pyproject.toml              # Project configuration
├── requirements.txt            # Runtime dependencies
├── requirements-dev.txt        # Development dependencies
└── README.md                   # This file
```

## API Reference

### Calculator Functions

#### `add(a: Number, b: Number) -> float`
Add two numbers and return the result.

#### `subtract(a: Number, b: Number) -> float`
Subtract the second number from the first.

#### `multiply(a: Number, b: Number) -> float`
Multiply two numbers and return the result.

#### `divide(a: Number, b: Number) -> float`
Divide the first number by the second. Raises `ValueError` if dividing by zero.

#### `power(a: Number, b: Number) -> float`
Raise the first number to the power of the second.

**Note**: `Number` is a type alias for `Union[int, float]`.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License.
