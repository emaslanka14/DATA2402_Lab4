
class Driver:

    def __init__(self, name: str, points: int):
        self.name = name
        self.points = points

    def __repr__(self) -> str:
        return(f"{self.name}, {self.points}")


class Team:

    def __init__(self, name: str):
       self.name = name
       self.drivers = []

    def add_driver(self, driver: Driver) -> None:   # append driver objects to list
        self.drivers.append(driver)

    def get_total_points(self) -> int:      # calculate points for each driver
        total = 0
        for driver in self.drivers:
            total += driver.points
        return total

    def __repr__(self) -> str:              # format string for team name, drivers and points
        names = []
        for driver in self.drivers:
            names.append(driver.name)
        return(f"{self.name} with drivers {", ".join(names)}. Total points: {self.get_total_points()}")
    
    def __lt__(self, other) -> bool:
        return self.get_total_points() < other.get_total_points()      # determines if one teams points are less than another
