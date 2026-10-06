from classes1 import Driver, Team


def main():
    filename = "f1_points.csv"

    teamsDict = {}

    with open(filename, "r") as f:

        for line in f: #Iterate through file until we find the header row
            if line.find(',') != -1:
                break

        for line in f:
            data = line.strip().split(",")

            if len(data) < 3:
                continue

            try:
                driver = str(data[0])
                teamName = str(data[1])
                points = int(data[2])

                DriverObj = Driver(driver, points)
                if teamName not in teamsDict:
                    teamsDict[teamName] = Team(teamName)
                    teamsDict[teamName].add_driver(DriverObj)
                else:
                    teamsDict[teamName].add_driver(DriverObj)
            


            except ValueError:
                print(f"Error: Invalid data in line: {line.strip()}")
                continue
            except IndexError:
                print(f"Error: Missing data in line: {line.strip()}")
                continue
            except Exception as e:
                print(f"Error: {e} in line: {line.strip()}")
                continue
    listOfTeams = list(teamsDict.values())

    sortedTeams = sorted(listOfTeams, key=lambda team: team.get_total_points(), reverse=True) #convert dict to list

    print("Teams and their drivers sorted by total points:")
    for team in sortedTeams:
        print(team)



if __name__ == "__main__":
    main()  