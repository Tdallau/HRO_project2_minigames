from os import path

class HighScore:
    def __init__(self, amound):
        self.amound = self.getHighscore("highscore.txt")
        self.dir = ''

    def checkForHighScore(self, amound):
        if int(self.amound) == 0 or int(self.amound) > int(amound):
            print(str(self.amound) + "||||"+str(amound))
            self.amound = amound
            self.writeHighscore(amound)

    def writeHighscore(self, amound):
        with open(path.join(self.dir, "minigame6/highscore.txt"), 'r+') as f:
                        f.write(str(amound))

    def getHighscore(self,HS_file):
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, HS_file), 'r+') as f:
            try:
                return int(f.read())

            except:
                return  0

        
