import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
import pandas as pd

root = Tk()
root.filename = filedialog.askopenfilename(
    initialdir = "\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS\\Team (only team)",
    title = "Select Team from Team (only team)", filetypes =(("Excel Workbook","*.xlsx"),("all files","*")))
df = pd.read_excel(root.filename)

games = []
average_game_time = []
firstDrake = []
firstDrakeCounter = [0, 0]

x = 1
while(x<=df.shape[0]):
    games.append(x)
    x += 1

def avgGameTime(final_df): #we need to access every team per week per day

    game = final_df.game
    team = final_df.team
    time = final_df.gamelength/60
    avg_time = list(zip(game,team,time))
    for i in avg_time:
        average_game_time.append(i[2])
    return average_game_time

def first_drake(final_df):

    for i in final_df.firstdragon:
        firstDrake.append(i)
    fDrakeYes = 0
    fDrakeNo = 0
    for i in firstDrake:

        if (firstDrake[i] == 1):
            fDrakeYes +=1
        else:
            fDrakeNo +=1
    firstDrakeCounter[0] = fDrakeNo
    firstDrakeCounter[1] = fDrakeYes
    return firstDrake, firstDrakeCounter

avgGameTime(df)
first_drake(df)

#small values

fig, ax = plt.subplots(2, 1, constrained_layout=True)
fig.suptitle(df.team.values[0])
ax[0].set_title('First Dragon %% (%s games)' % (str(sum(firstDrakeCounter))))
ax[0].pie(firstDrakeCounter, labels=["no","yes"], autopct='%1.1f%%')
#The no label corresponds to the [0] of the firstDrakeCounter array



#mid sized values
ax[1].plot(games,average_game_time, label="Game Time", marker="o")
plt.ylabel("Time (minutes)")
ax[1].legend(loc= "best",fontsize = "small")
plt.xlabel("Game Number")
plt.legend(loc= "best",fontsize = "small")
plt.show()
