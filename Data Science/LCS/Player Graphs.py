import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
import pandas as pd

try:
    root = Tk()
    root.filename = filedialog.askopenfilename(
        initialdir="\\LCS\\Players", title = "Select Player",
                                               filetypes =(("Excel Workbook", "*.xlsx"), ("all files", "*")))
    df = pd.read_excel(root.filename)
except:
    print("Error you did not give a valid file")
    exit(0)
games = []
kill_part = []
damagetochampions = []
damageshare = []
csdiffat10=[]
csdiffat15 = []
golddiffat10 = []
golddiffat15 = []
visionscore=[]

x = 1
while(x<=df.shape[0]):
    games.append(x)
    x += 1

def kill_participation(final_df):
    iK = final_df.kills.values
    iA= final_df.assists.values
    num = list(zip(iK,iA))
    individual = []
    TK = final_df.teamkills.values

    for pairs in num: # zips up a players Kill and Assists
        KA = sum(pairs)
        individual.append(KA)
    values = list(zip(individual,TK))



    for game in values: # game is the first tuple so (sum of individuals KA, team Kills)
        calculation = game[0]/game[1]*100
        kill_part.append(calculation)
    return kill_part #returns it to the outside



def dmg_metrics(final_df):

    for i in final_df.damagetochampions:
        damagetochampions.append(i)

    for i in final_df.damageshare:
        damageshare.append(i*100)

    return damagetochampions,damageshare

def vision_metrics(final_df):

    for i in final_df.visionscore:
        visionscore.append(i)
    return visionscore

def lane_diff(final_df):
    for i in final_df.golddiffat10:
        golddiffat10.append(i)
    for i in final_df.golddiffat15:
        golddiffat15.append(i)
    for i in final_df.csdiffat10:
        csdiffat10.append(i)
    for i in final_df.csdiffat15:
        csdiffat15.append(i)
    return golddiffat10,golddiffat15,csdiffat10,csdiffat15


lane_diff(df)
dmg_metrics(df)
kill_participation(df)
vision_metrics(df)



plt.suptitle(df.player.values[0])
#small values
plt.subplot(4,1,1)
plt.plot(games, damageshare, label= "Damage Share", marker="o")
plt.plot(games, kill_part, label= "Participation %", marker="o")
plt.legend(loc= "best",fontsize = "small")


#mid sized values
plt.subplot(4,1,2)
plt.plot(games, visionscore, label= "Vision Score", marker=".")
plt.plot(games, csdiffat15, label= "CS Difference at 15", marker=".")
plt.plot(games, csdiffat10, label= "CS Difference at 10", marker=".")
plt.legend(loc= "best",fontsize = "small")

#100's values
plt.subplot(4,1,3)
plt.plot(games, golddiffat10, label= "Gold Difference at 10", marker=".")
plt.plot(games, golddiffat15, label= "Gold Difference at 15", marker=".")


plt.legend(loc= "best",fontsize = "small")


#high valued metrics

plt.subplot(4,1,4)
plt.bar(games,damagetochampions, label="DMG Output")
plt.xlabel("Game Number")
plt.legend(loc= "best",fontsize = "small")

plt.show()
