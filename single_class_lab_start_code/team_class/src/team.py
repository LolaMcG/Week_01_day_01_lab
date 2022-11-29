class Team:

    def __init__ (self, input_name, input_list_of_names, input_coach):
        self.name = input_name
        self.players = input_list_of_names
        self.coach = input_coach
        self.points = 0
        
    
    def add_player(self, player_name):
        self.players.append(player_name)

    def has_player(self, new_player):
        for player in self.players:
            if player == new_player:
                return True
        else:
            return False

    def team_has_points(self, team_points):
        self.points(team_points)
        
    def play_game(self, result):
        if result == True:
            self.points += 3