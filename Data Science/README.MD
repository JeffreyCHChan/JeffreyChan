# Data Science

## Datasets
For the purposes of testing and demonstration the following files can be used and are found in the LCS Folder. 

Origin Source: 2020_LoL_esports_match_data.csv
Test Parsed File: LCS.xlsx

## Scripts
####DataExtraction.py
Extracts, transfer and loads raw data into 4 categories/folders (Players, Positions, Team (only team), Teams (including players)).
The source of the origin file (.csv) was downloaded from https://oracleselixir.com/tools/downloads.
The output file uses the extension .xlsx where the file name is the name of the regional league they belong to.

#### Player Graphs.py
Generates the visualization of 8 metrics: 
<ul>
<li>Damage Share: Measure of total contribution to the overall damage output of the team.</li>
<li>Participation %: Measure of the player's tracked contribution to the overall kills on a team. </li>
<li>Vision Score: Measure that depicts the sum of minutes where a ward (item that gives vision) is active and sum of minutes where enemy vision is denied.

A rough estimation is the following VISION SCORE = (1 point per minute of ward lifetime provided) + (1 point per minute of ward lifetime denied).</li>
<li>CS Difference at 10/CS Difference at 15: These are a numerical difference between the player's creep score (the number of creeps executed) compared to the oppenent's creep score. 
A rough calulation is Player's creep score - oppenent's creep score.</li>
<li>Gold Difference at 10/Gold Difference at 15: These are a numerical difference between the player's gold (currency used to purchase items that increase a player's attribute and/or grant new abilities for the duration of the game) compared to the oppenent's amount of gold. 
A rough calulation is Player's gold amount - oppenent's gold amount.</li>

<li>DMG Output: Metric using the numerical value of damage produced by the player to the opponent's characters</li>
</ul>

#### Team Graphs.py
Generates the visualization of 2 metrics: 
<ul>
<li>First Dragon %: Measure of matches where they obtained the first dragon over the opposing team.</li>
<li>Average Game time: Measure of the time it takes for a team to defeat their opponent. </li>
</ul>
