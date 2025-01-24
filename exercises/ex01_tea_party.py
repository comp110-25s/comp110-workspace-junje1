"""Exercise 01 for COMP 110!"""

__author__: str = "730719886"


def main_planner(guests: int) -> None:
    """Main Planner"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """The number of tea bags we need to prepare"""
    return people * 2


def treats(people: int) -> int:
    """The number of treats we need to prepare"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """The cost for the tea party"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
