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
        else:#you can delete this 'else'! You can just have 'return False', in line with the 'for' loop.
            return False
    # an alternative way of doing the above, lines 13 - 18
    # def has_player(self, player):
        # return self.players.count(player) > 0 .  OR return new_player in self.players

    def team_has_points(self, team_points):
        self.points(team_points)
        
    def play_game(self, result):
        if result == True:  #you don't need the '== True' bit. You can just say 'if result:' because you are ALREADY passing in a boolean value.
            self.points += 3