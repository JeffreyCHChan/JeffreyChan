import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
import pandas as pd

root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "\Documents\GitHub\\vigilant-telegram\Data Science\LCS",
                                           title = "Select file", filetypes =(("Excel Workbook","*.xlsx"),("all files","*")))
df = pd.read_excel(root.filename)

games = []
kill_part = []
average_game_time = []
dmg_done_to_champs = []
dmg_share = []
wards = []
csdat10=[]
csdat15 = []
gdat10 = []
gdat15 = []

x = 1
while(x<=df.shape[0]):
    games.append(x)
    x += 1

def kill_participation(final_df):
    iK = final_df.k.values
    iA= final_df.a.values
    num = list(zip(iK,iA))
    individual = []
    TK = final_df.teamkills.values



    for pairs in num: # zips up a players Kill and Assists
        KA = sum(pairs)
        individual.append(KA)
    values = list(zip(individual,TK))



    for game in values: # game is the first tuple so (sum of individuals KA, team Kills)
        calculation = game[0]/game[1]
        kill_part.append(calculation)
    return kill_part #returns it to the outside

def avgGameTime(final_df): #we need to access every team per week per day
    week = final_df.week
    game = final_df.game
    team = final_df.team
    time = final_df.gamelength
    avg_time = list(zip(week,game,team,time))
    for i in avg_time:
        average_game_time.append(i[3])
    return average_game_time

def dmg_metrics(final_df):

    for i in df.dmgtochamps:
        dmg_done_to_champs.append(i)

    for i in df.dmgshare:
        dmg_share.append(i)

    return dmg_done_to_champs,dmg_share

def vision_metrics(final_df):

    for i in df.wards:
        wards.append(i)
    return wards
def lane_diff(final_df):
    for i in df.gdat10:
        gdat10.append(i)
    for i in df.gdat15:
        gdat15.append(i)
    for i in df.csdat10:
        csdat10.append(i)
    for i in df.csdat15:
        csdat15.append(i)
    return gdat10,gdat15,csdat10,csdat15


lane_diff(df)
dmg_metrics(df)
kill_participation(df)
avgGameTime(df)
vision_metrics(df)



plt.suptitle(df.player.values[0])
#small values
plt.subplot(4,1,1)
plt.plot(games, dmg_share, label= "Damage Share")
plt.plot(games, kill_part, label= "Kill Participation")
plt.legend(loc= "best")


#mid sized values
plt.subplot(4,1,2)
plt.plot(games, wards, label= "Wards used (including vision)")
plt.plot(games, csdat15, label= "CS Difference at 15")
plt.plot(games, csdat10, label= "CS Difference at 10")
plt.legend(loc= "lower left")

#100's values
plt.subplot(4,1,3)
plt.plot(games, gdat10, label= "Gold Difference at 10")
plt.plot(games, gdat15, label= "Gold Difference at 15")


plt.legend(loc= "best")


#high valued metrics

plt.subplot(4,1,4)
plt.plot(games,dmg_done_to_champs, label = "Damage done in Game")
plt.legend(loc= "best")

plt.show()
