import pandas as pd
from tkinter import filedialog
from tkinter import *


root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/Downloads", title = "Select file", filetypes =
(("Excel Workbook","*.csv"),("all files","*")))


df = pd.read_csv(root.filename)

old_drop_list=["gameid", "url", "split", 'date', 'playerid','firedrakes','waterdrakes', 'airdrakes',
           'earthdrakes']
new_drop_list = ["gameid", "url", "split", 'date', 'playerid','infernals','oceans', 'clouds',
           'mountains',"dragons (type unknown)"]


def info_parsing(df): # parses for a specific region
    df.drop(new_drop_list, axis=1, inplace=True) #drop list not used to maximize data
    df.player.fillna("Team")
    df.fillna(0, inplace=True)
    #df.loc[df['position']=='Team']
    #test= df[df.position.str.match('Team')] #limiting the search to just one thing for now
    league = df.loc[df['league'] == 'LCS'] #selects all of LCS
    #selection = league.loc[(league['team']=='Team Liquid')] #can restrict to one team specifically
    selection = league
    writer = pd.ExcelWriter('C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS\\LCS.xlsx',
                            engine='xlsxwriter')
    selection.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    return df



root1 = Tk()
root1.filename = filedialog.askopenfilename(initialdir = "C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science"
                                                    "\\LCS", title = "Select parsed region file", filetypes =
(("Excel Workbook","*.xlsx"),("all files","*")))

new_df = pd.read_excel(root1.filename)

'''team_list = {}
def teams(parsed_df):
    a_teams= parsed_df[parsed_df['team']]
    team_list=set(a_teams) #unique values of teams
    return team_list
 #work on one region first
'''

def grouping_team(new_df): #grouping of all teams
    for teams in new_df['team'].unique():
        team = new_df[new_df.team.str.match("%s"%(teams))]
        writer = pd.ExcelWriter('C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS' #create new folder then change LCS to another region
                                '\\Teams\\%s.xlsx'%(teams), engine='xlsxwriter')
        team.to_excel(writer)
        writer.save()
def grouping_team_stats(): #grouping of Team overall stats
    mod_df = pd.read_excel("C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS\\Positions\\"
                           "Team.xlsx")
    for teams in mod_df['team'].unique():
        team = mod_df[new_df.team.str.match("%s"%(teams))]
        writer = pd.ExcelWriter('C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS' #create new folder then change LCS to another region
                                '\\Team Stats\\%s.xlsx'%(teams), engine='xlsxwriter')
        team.to_excel(writer)
        writer.save()

def grouping_position(new_df): #grouping by position
    drop_list = ["ban1", "ban2", "ban3", "ban4", "ban5"] #Removed all bans from this point on
    new_df.drop(drop_list, axis=1, inplace=True)  # drop list not used to maximize data
    for positions in new_df['position'].unique():
        position = new_df[new_df.position.str.match("%s"%(positions))]
        writer = pd.ExcelWriter('C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS'
                                '\\Positions\\%s.xlsx'%(positions), engine='xlsxwriter')
        position.to_excel(writer)
        writer.save()
def grouping_player(new_df): #grouping by position
    #drop_list = ["ban1", "ban2", "ban3", "ban4", "ban5"]
    #new_df.drop(drop_list, axis=1, inplace=True)  # drop list not used to maximize data
    for players in new_df['player'].unique():
        player = new_df[new_df.player.str.match("%s"%(players),na=False)]
        writer = pd.ExcelWriter('C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS'
                                '\\Players\\%s.xlsx'%(players), engine='xlsxwriter')
        player.to_excel(writer)
        writer.save()


#remove side, position, player, patch, game, league, bans for the ML data and make two seperate datasets one with
# LCS and another with LCS removed
info_parsing(df)
grouping_team(new_df)
grouping_position(new_df)
grouping_player(new_df)
grouping_team_stats(new_df)
