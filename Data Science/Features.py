import pandas as pd
from tkinter import filedialog
from tkinter import *
import matplotlib.pyplot as plt

root2 = Tk()
root2.filename = filedialog.askopenfilename(initialdir = "\Documents\GitHub\\vigilant-telegram\Data Science\LCS\Positions",
                                            title = "Select parsed file", filetypes =
(("Excel Workbook","*.xlsx"),("all files","*")))
final_df = pd.read_excel(root2.filename)

'''we are going to need many roots so we can do many things'''




#list of variables we will use to make graphs
kill_part = []
number_of_games = []
average_game_time = []

def num_games(final_df):#gets total number of games
    count = 0
    while (count< final_df.shape[0]):
        number_of_games.append(count)
        count+=1
    return number_of_games

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









num_games(final_df)
kill_participation(final_df)
avgGameTime(final_df)


plt.plot(number_of_games, kill_part,average_game_time)
plt.legend("Kill Participation", "Average Game Time")
plt.show()


