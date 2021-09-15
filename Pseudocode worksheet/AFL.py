#AFL
print("Enter a team's number of goals and behinds in the format 'goals.behinds'.")

for x in range(2):
    teamname = input("What is the team's name? ")
    score = input("Enter {}'s number of goals and behinds: ".format(teamname))

    if x == 0:
        team1 = teamname
        goals1, behinds1 = score.split('.')
        points1 = (int(goals1) * 6) + int(behinds1)

    if x == 1:
        team2 = teamname
        goals2, behinds2 = score.split('.')
        points2 = (int(goals2) * 6) + int(behinds2)

if points1 > points2:
    print("The winning team is {} with {} points. The losing team is {} with {} points.".format(team1, points1, team2, points2))
elif points2 > points1:
    print("The winning team is {} with {} points. The losing team is {} with {} points.".format(team2, points2, team1, points1))
else:
    print("It was a tie with both teams getting {} points.".format(points1))
