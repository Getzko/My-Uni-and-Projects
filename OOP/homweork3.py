class Player:
    def __init__(self,name,position):
        self.name=name
        self.position=position

class Coach:
    def __init__(self,name,years_of_experience):
        self.name=name
        self.years_of_experience=years_of_experience

class Team:
    def __init__(self,name):
        self.name=name
        self.players=[]
        self.coach=None
    
    def add_player(self,name,position):
        new_player=Player(name,position)
        self.players.append(new_player)
    
    def assign_coach(self,coach):
        self.coach=coach
    
    def printteam(self):
        print(f"Team: {self.name}")
        for player in self.players:
            print(f"{player.name} - {player.position}")
        if self.coach:
            print(f"Coach: {self.coach.name} {self.coach.years_of_experience}")
        else:
            print("None assigned")

team=Team("Hamk hackers")
team.add_player("john","front")
team.add_player("donald","back")
team.add_player("mr phone","support")
coach1=Coach("michael jordan",20)
team.assign_coach(coach1)
team.printteam()