# list of all possible sec teams
teams = ["LSU", "Arkansas", "Ole Miss", "Texas A&M", "Auburn", "Mississippi State", 
"South Carolina", "Vanderbilt", "Kentucky", "Missouri", "Oklahoma", "Florida", 
"Georgia", "Tennessee", "Alabama", "Texas"]
# list of all the possible sec last game schedule
games = ["Oklahoma on November 30 at LSU", "Missouri on November 30 at Missouri", 
"Mississippi State on November 29 at Ole Miss", "Texas Longhorns on November 30 at Texas A&M", 
"Alabama on November 30 at Alabama", "Ole Miss on November 29 at Ole Miss", 
"Clemson on November 30 at Clemson", "Tennessee on November 30 at Vanderbilt", 
"Louisville on November 30 at Kentucky", "Arkansas on November 30 at Missouri", 
"LSU on November 30 at LSU", "Florida State on November 30 at Florida", 
"Georgia Tech on November 29 at Georgia", "Vanderbilt on November 30 at Vanderbilt", 
"Auburn on November 30 at Alabama", "Texas A&M on November 30 at Texas A&M"]

# function to get the last game for the team the user inputs
def get_team_game(team_name):
    if team_name == "LSU":
        return games[0]
    elif team_name == "Arkansas":
        return games[1]
    elif team_name == "Ole Miss":
        return games[2]
    elif team_name == "Texas A&M":
        return games[3]
    elif team_name == "Auburn":
        return games[4]
    elif team_name == "Mississippi State":
        return games[5]
    elif team_name == "South Carolina":
        return games[6]
    elif team_name == "Vanderbilt":
        return games[7]
    elif team_name == "Kentucky":
        return games[8]
    elif team_name == "Missouri":
        return games[9]
    elif team_name == "Oklahoma":
        return games[10]
    elif team_name == "Florida":
        return games[11]
    elif team_name == "Georgia":
        return games[12]
    elif team_name == "Tennessee":
        return games[13]
    elif team_name == "Alabama":
        return games[14]
    elif team_name == "Texas":
        return games[15]
    else:
        return "Team not found enter a valid team name or check grammar" 
        #error message if team is not valid

# function to display all sec teams to the user
def display_available_teams():
    print("SEC football teams:")
    for team in teams:  
        print(team)  
# calls function to show teams
display_available_teams()  
# loop to continualy get user input for the team they choose
while True:
    selected_team = input("Enter a team name or type 'done' to exit): ")  # gets users team
    if selected_team == "done":  # option for user to leave
        print("Thank you for using the SEC football schedule app!")  # message for when they leave
        break  # exits loop

    last_game = get_team_game(selected_team)  # gets last game that corresponnse 
    # with what the user input

    print(last_game) # prints the schedule for selected team
    

    