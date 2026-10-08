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
            try:
                points = int(row[2])               # CSV values are strings
            except ValueError:
                print(f"Invalid point value in row {row}")
                continue

            if team_name not in teams:          # only one Team per name
                teams[team_name] = Team(team_name)

            teams[team_name].add_driver(Driver(driver_name, points))

    return teams


def main():
    teams = load_teams("f1_points_error.csv")
    print(len(teams), "teams loaded")           

    for team in sorted(teams.values()):        
        print(team)


main()