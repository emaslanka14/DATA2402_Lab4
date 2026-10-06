from classes1 import Team, Driver
import csv


def load_teams(filename: str) -> dict:
    teams = {}                                 

    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)                            # skip the header row

        for row in reader:
            driver_name = row[0]
            team_name = row[1]
            points = int(row[2])                # CSV values are strings

            if team_name not in teams:          # only one Team per name
                teams[team_name] = Team(team_name)

            teams[team_name].add_driver(Driver(driver_name, points))

    return teams


def main():
    teams = load_teams("f1_points.csv")
    print(len(teams), "teams loaded")           

    for team in sorted(teams.values()):         # Task 3: uses Team.__lt__
        print(team)


main()