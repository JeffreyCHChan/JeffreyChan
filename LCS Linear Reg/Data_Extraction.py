import pandas as pd
from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/Downloads", title = "Select file", filetypes =
(("Excel Workbook","*.xlsx"),("all files","*")))


df = pd.read_excel(root.filename)
new_df = pd.read_excel('C:\\Users\\Jeff\\Desktop\\LCS.xlsx')

drop_list=["gameid", "url", "split", 'date', 'patchno','player','ban1','ban2','ban3','ban4','ban5', 'firedrakes',
           'waterdrakes', 'earthdrakes','airdrakes', 'champion', 'elders','oppelders',
           'visiblewardclearrate','invisiblewardclearrate','heraldkills','oppheraldkills', 'week', 'game', 'playerid']#'league'
def info_parsing(df):
    df.drop(drop_list, axis=1, inplace=True)
    df.fillna(-9999999, inplace=True)
    #df.loc[df['position']=='Team']
    test= df[df.position.str.match('Team')] #limiting the search to just one thing for now
    #league = df.loc[df['league'] == 'LCS'] #not used currently since we want to maximize the amount of data
    Team = test.loc[(test['team']=='Team Liquid')]
    writer = pd.ExcelWriter('C:\\Users\\Jeff\\Desktop\\LCS.xlsx', engine='xlsxwriter')
    Team.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    return df

info_parsing(df)


