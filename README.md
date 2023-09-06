# Data-Analyzer-for-T7-Player-Displayer

Reads data from "Tekken Player List.txt" generated by https://github.com/ParadiseAigo/Tekken-7-Player-Displayer and analyzes it; displays various data in console.

## Example output:
(monospaced font recommended)
```
No duplicate IDs found in player list.

Total players VS'd: 163
(13/15) DLCs found
(33/36) base rosters found
(15/18) females+Leo found
(31/33) males found
27.0% VS females (35.3% expected)
21.5% VS DLC (29.4% expected)
(2/3) Laws had a bad connection
Cheaters/pluggers characters: ['Paul', 'King', 'Lee', 'Leroy Smith', 'Geese', 'Ganryu', 'Lei', 'Lars', 'Heihachi', 'Hwoarang']


Good%      Name          Freq
(1/8)--    Bryan         ********
(3/8)-     Heihachi      ********
(1/7)--    Hwoarang      *******
(0/7)--    Lucky Chloe   *******
(3/7)      Paul          *******
(1/6)--    Lee           ******
(1/6)--    Miguel        ******
(2/6)-     Lei           ******
(3/6)      Alisa         ******
(1/6)--    Bob           ******
(1/5)--    Dragunov      *****
(0/5)--    Lars          *****
(0/5)--    Asuka         *****
(1/5)--    King          *****
(1/5)--    Josie         *****
(2/5)-     Noctis        *****
(1/5)--    Lili          *****
(2/5)-     Armor King    *****
(2/4)      Devil Jin     ****
(0/4)--    Kazuya        ****
(3/4)+     Steve         ****
(0/4)--    Marduk        ****
(0/3)--    Julia         ***
(0/3)--    Jack-7        ***
(1/3)-     Zafina        ***
(0/3)--    Law           ***
(0/3)--    Fahkumram     ***
(0/2)--    Feng          **
(1/2)      Jin           **
(0/2)--    Gigas         **
(0/2)--    Geese         **
(0/2)--    Yoshimitsu    **
(0/2)--    Kazumi        **
(0/2)--    Xiaoyu        **
(0/1)--    Anna          *
(0/1)--    Ganryu        *
(0/1)--    Panda         *
(1/1)++    Lidia         *
(0/1)--    Nina          *
(0/1)--    Kuma          *
(0/1)--    Leroy Smith   *
(0/1)--    Eddy          *
(0/1)--    Shaheen       *
(1/1)++    Master Raven  *
(0/1)--    Katarina      *

Aight: 11
Okay: 3
Good: 11
Great: 8
No skip: 22
No re: 50
Lose quit: 28
Win quit: 4
Cheat: 3
Plug: 7
Connection: 22
Desync: 6
No comment: 6
```

## Setup
1) Put .py file in the same folder as Tekken-7-Player-Displayer.exe
2) Generate player data in-game using that ^ tool. Use the comments listed here in "Tekken Player List.txt" (case insensitive):
    * "No comment" (default)
    * "Connection" (for bad connections)
    * "Aight", "Okay", "Good", "Great" for overall set quality
    * "No skip", "No re" (rematch), "Lose quit", "Win quit"
    * "Cheat", "Plug"
    * "Connection", "Desync"
3) Open and run .py file and see the player/character analyses.
     * You may need to update charprops dict in .py file (line 5) with characters that aren't listed (I add them as I go)
     * "Good%" means how many players with the respective character are listed with any "good" comment, out of the total players with that character.
       * For example, (1/8) Bryan means that only one Bryan player was listed as "good" in their comment

## Notes
* Line 1 in the .txt file is skipped. This is because I don't want to include the default data provided by Tekken-7-Player-Displayer and because I deleted the second line.
* It helps to keep the .txt file in a monospaced font. Adding and removing tabs doesn't affect functionality the way I did it.
* Key comments can be changed easily in the code.
* The Python terminal should be monospaced in order to line up the Good% chart. Maybe you can format it so that this isn't required.
* The comments I left for "Win quit", "No re", and "Lose quit" are a bit inconsistent
* The data I got from the Player Displayer occurred while I was on Heihachi, around Fujin rank, with a wired connection, and I rematched most of the time and played honestly.
