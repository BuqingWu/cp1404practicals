"""
Estimate time:45 mins
Actual time:75 mins
"""

class ProgrammingLanguage:
    """Represent a programming language object"""

    def __init__(self, name = "", typing = "", reflection = False, year = 0):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed, otherwise False."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a formatted string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"