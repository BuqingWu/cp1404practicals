class Guitar:
    """Represent a guitar object"""

    def __init__(self, name = "", year = 0, cost = 0):
        self.name = name
        self.year = year
        self.cost = cost
        """Initialize a Guitar instance."""

    def __str__(self):
        """Return a formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year=2022):
        """Return the age of the guitar based on the current year."""
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage (50 or more years old)."""
        return self.get_age() >= 50