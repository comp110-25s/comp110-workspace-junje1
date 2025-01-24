"""My first exercise in COMP110!"""

__author__ = "730719886"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello," + name + "!"


if __name__ == "__main":
    print(greet(name=input("What is your name?")))


def main() -> None:
    """asdfds"""
    print(perimenter(radius=1.0))
    print(area(radius=1.0))
    return None


def say_hello(name: str) -> None:
    """This function prints a greeting"""
    print str(("Hello," + name + "!"))
