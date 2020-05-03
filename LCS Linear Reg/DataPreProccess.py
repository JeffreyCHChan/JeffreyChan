import pandas as pd
from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/Downloads", title = "Select file", filetypes =
(("Excel Workbook","*.csv"),("all files","*")))


df = pd.read_csv(root.filename)

ml_prep_list= ["gameid", "url", "split", 'date', 'playerid','infernals','oceans', 'clouds','team','champion',
           'mountains','side', 'position', 'player', 'patch', 'game', 'ban1','ban2','ban3','ban4', 'ban5',
            "dragons (type unknown)","elementaldrakes","opp_elementaldrakes","elders","opp_elders",
            "firstmidtower","firsttothreetowers"]

def ml_TrainData(df): # parses for a specific region
    df.drop(ml_prep_list, axis=1, inplace=True)
    df.fillna(0, inplace=True)
    league = df.loc[df['league'] != 'LCS']
    selection = league
    #selection = league.loc[(league['team']=='Team Liquid')] #can restrict to one team specifically
    writer = pd.ExcelWriter('C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\LCS Linear Reg\\Training.xlsx',
                            engine='xlsxwriter')
    selection.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    return df


def ml_TestData(df): # parses for a specific region
    #df.drop(ml_prep_list, axis=1, inplace=True)
    df.fillna(0, inplace=True)
    league = df.loc[df['league'] == 'LCS']
    selection = league
    #selection = league.loc[(league['team']=='Team Liquid')] #can restrict to one team specifically
    writer = pd.ExcelWriter('C:\\Users\\Jeff\\Documents\\GitHub\\JeffreyChan\\LCS Linear Reg\\Test.xlsx',
                            engine='xlsxwriter')
    selection.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    return df


ml_TrainData(df)
ml_TestData(df)
