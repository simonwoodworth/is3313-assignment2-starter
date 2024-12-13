class Calculator:
    def add(self, a, b):
        """Adds two numbers and returns the result."""
        return a + b  # Fixed from a * b to a + b

    def subtract(self, a, b):
        """Subtracts the second number from the first and returns the result."""
        return a - b  # Fixed from a / b to a - b

    def multiply(self, a, b):
        """Multiplies two numbers and returns the result."""
        return a * b  # Fixed from a - 55 to a * b

    def divide(self, a, b):
        """Divides the first number by the second and returns the result.
        Raises a ValueError if the second number is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b  # Fixed from returning b to a / b

    def power(self, base, exponent):
        """Raises the base to the power of the exponent and returns the result."""
        return base ** exponent  # Fixed from self / base to base ** exponent

    def modulus(self, a, b):
        """Calculates the modulus of two numbers and returns the result."""
        return a % b  # Fixed from self * base to a % b
