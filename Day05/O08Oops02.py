
class Player:

    def __init__(self, name):         # Constructor
        print("Player Initialized.......")

    def get_runs(self):
        print("runs")

sachin = Player()       # ojbect of class
sourav = Player()
sachin.__init__()

print("-" * 60)
sachin.get_runs()
sourav.get_runs()