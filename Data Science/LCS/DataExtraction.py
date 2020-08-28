import pandas as pd
from tkinter import filedialog
from tkinter import *

try:
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir = "/Downloads", title = "Select origin source", filetypes =
    (("Excel Workbook","*.csv"),("all files","*")))

    print("The file "+root.filename +" has been loaded.")


    df = pd.read_csv(root.filename)

    #two drop lists are used to account for changes of the format of the raw dataset
    old_drop_list=["gameid", "url", "split", 'date', 'playerid','firedrakes','waterdrakes', 'airdrakes',
               'earthdrakes']
    new_drop_list = ["gameid", "url", "split", 'date', 'playerid','infernals','oceans', 'clouds',
               'mountains',"dragons (type unknown)"]
except:
    print("Origin Source not Found")
try:
    root1 = Tk()
    root1.filename = filedialog.askopenfilename(
        initialdir = "C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS",
        title = "Select parsed region file", filetypes =(("Excel Workbook","*.xlsx"),("all files","*")))

    new_df = pd.read_excel(root1.filename)
    print("The regional file of " + root1.filename+" has been selected.")
except:
    print("Parsed File not Found")

def info_parsing(df): #Initial filtering to obtain a hard coded region which is "LCS" in this case
    df.drop(new_drop_list, axis=1, inplace=True) #A list of columns to exclude was used as they are irrelevant columns
    df.player.fillna("Team") #repalces all n/a entries in the player column with the "team"
    df.fillna(0, inplace=True) #all values will be numeric values so we will associate "not applicable" as 0 (zero)

    league = df.loc[df['league'] == 'LCS'] #selects all of LCS from the league column which represents a region
    """
    selection = league.loc[(league['team']=='Team Liquid')] #varible "selection allows for flexibility on selecting 
    what to write to the excel file 
    """
    selection = league
    writer = pd.ExcelWriter('C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS\\LCS.xlsx',
                            engine='xlsxwriter')
    selection.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    return df







def grouping_team(new_df): #All teams in the LCS region are sent to the LCS folder
    for teams in new_df['team'].unique():
        team = new_df[new_df.team.str.match("%s"%(teams))]
        writer = pd.ExcelWriter(
            'C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS\\Teams (inlcuding players)\\%s.xlsx'%teams,
            engine='xlsxwriter')
        team.to_excel(writer)
        writer.save()
def grouping_team_stats(): #Sorting of unique Teams' overall stats into own excel file
    mod_df = pd.read_excel("C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS\\Positions\\"
                           "Team.xlsx")
    for teams in mod_df['team'].unique():
        team = mod_df[new_df.team.str.match("%s"%(teams))]
        writer = pd.ExcelWriter(
            'C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS\\Team (only team)\\%s.xlsx'%(teams)
            , engine='xlsxwriter')
        # create new folder then change LCS to another region
        team.to_excel(writer)
        writer.save()

def grouping_position(new_df): #creates a unique excel file by position
    drop_list = ["ban1", "ban2", "ban3", "ban4", "ban5"] #Removed all bans as this is relevant to whole teams not indivduals
    new_df.drop(drop_list, axis=1, inplace=True)
    for positions in new_df['position'].unique():
        position = new_df[new_df.position.str.match("%s"%(positions))]
        writer = pd.ExcelWriter('C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS'
                                '\\Positions\\%s.xlsx'%(positions), engine='xlsxwriter')
        position.to_excel(writer)
        writer.save()
def grouping_player(new_df): #creates a unique excel file for each player
    for players in new_df['player'].unique():
        player = new_df[new_df.player.str.match("%s"%(players),na=False)]
        writer = pd.ExcelWriter('C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\Data Science\\LCS'
                                '\\Players\\%s.xlsx'% (players), engine='xlsxwriter')
        player.to_excel(writer)
        writer.save()



info_parsing(df)
grouping_team(new_df)
grouping_position(new_df)
grouping_player(new_df)
grouping_team_stats()
print("Data preprocessing is done.")
