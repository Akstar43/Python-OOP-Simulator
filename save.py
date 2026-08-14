import csv
import os
class Save:
    def __init__(self):
        pass
    def saveparameter(self,blockname, max, resource, durabilitytaken, playername, toolname):
        file_path = "n.txt"
        if not os.path.exists(file_path):
            with open("n.txt", "a") as countinitialize:
                icount = 0
                countinitialize.write(str(icount))
        else:
            pass
        with open("n.txt", "r") as Counter:
            count = int(Counter.read())
        with open("saveparameter.csv","a",newline="") as File:
            writer = csv.writer(File)
            writer.writerow([count,blockname,max,resource,durabilitytaken,playername, toolname])
            count += 1
        with open("n.txt", "w") as updatedcount:
            updatedcount.write(str(count))
    def savegame(self,player,block,tool):
        file_path = "c.txt"
        if not os.path.exists(file_path):
            with open("c.txt", "a") as countinitialize:
                icount = 0
                countinitialize.write(str(icount))
        else:
            pass
        with open("c.txt", "r") as Counter:
            count = int(Counter.read())
            with open("savedgames.csv", "a", newline="") as File:
                writer = csv.writer(File)
                writer.writerow([count,player,block, tool])
                count += 1
            with open("c.txt", "w") as updatedcount:
                updatedcount.write(str(count))

