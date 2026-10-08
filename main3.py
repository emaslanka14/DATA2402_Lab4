from classes1 import Driver, Team


def main():
    filename = "f1_points.csv"

    teams = {}

    with open(filename, "r") as f:

        for line in f: #Iterate through file until we find the header row
            if line.find(',') != -1:
                break

        for line in f:
            data = line.strip().split(",")
            try:
                driver = str(data[0])
                teamName = str(data[1])
                points = int(data[2])

                DriverObj = Driver(driver, points)
                if teamName not in teams:
                    teams[teamName] = Team(teamName)
                    teams[teamName].add_driver(DriverObj)
                else:
                    teams[teamName].add_driver(DriverObj)

            except Exception as e:
                print(f"Error: {e} in line: {line.strip()}")
                continue

    listOfTeams = list(teams.values())
    sortedTeams = sorted(listOfTeams, reverse=True) #convert dict to list

    print("Teams and their drivers sorted by total points:")
    for team in sortedTeams:
        print(team)

if __name__ == "__main__":
    main()  