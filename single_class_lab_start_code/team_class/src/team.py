class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.__points = {
            "lose": 0,
            "win": 3
        }

    def team_has_name(self):
        return self.team.name

    def team_has_players(self):
        return self.team.players
    
    def team_has_coach(self):
        return self.team.coach
    
    def coach_can_be_changed(self):
        self.team.coach = "John Candy"
        return self.team.coach
    
    def add_player(self, new_player):
        self.players.append(new_player)
        return self.players
    
    def has_player(self, player):
        result = player in self.players
        return result
    
    def play_game(self, game):
        self.__points = 0
        if game == True:
            self.__points += self.points["win"]
        elif game == False:
            self.__points += self.__points["lose"]


            
    
