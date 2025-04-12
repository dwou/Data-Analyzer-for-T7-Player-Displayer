# Data-Analyzer-for-T7-Player-Displayer

Reads data from "Tekken Player List.txt" generated by https://github.com/ParadiseAigo/Tekken-7-Player-Displayer and analyzes it; displays various data in the console.

I also linked my "Tekken Player list.txt", which includes, among others, ~19 cheaters/pluggers.

## Example output:
```
Note: plugging is cheating
No duplicate IDs found in player list.

  ~Fun Facts~

Total players VS'd: 752
All characters found
27.8% VS females (35.3% expected)
22.2% VS DLC (29.4% expected)
(47/112) Mishimas had a bad connection
(5/16) Laws had a bad connection
Cheater chars (49): Alisa, Armor King, Bryan x2, Eddy x2, Fahkumram, Feng x2, Ganryu x2, Geese x2, Gigas, Heihachi x4, Hwoarang x3, Jin x2, Josie x2, Kazumi, King x3, Lars x2, Law x2, Lee, Lei, Leroy Smith, Marduk, Master Raven, Miguel, Nina, Paul x4, Steve, Xiaoyu, Yoshimitsu x2, Zafina

  ~Chart~

Note: Good% accounts for 'no comment yet', but freq does not

Tot Good%      Name          Freq
 33 ( 2/30)--  Jin           gg___bbbbbbbbbbbbbbbbbbbbbbbbbbBB M
 33 ( 7/28)-   Bryan         ggggggg_____bbbbbbbbbbbbbbbbbbbBB 
 29 ( 4/23)--  Josie         gggg______bbbbbbbbbbbbbbbbBBB     
 29 (12/28)    Heihachi      gggggggggggg_bbbbbbbbbbbbBBBB     M
 29 ( 4/29)--  Hwoarang      ggggbbbbbbbbbbbbbbbbbbbbbbBBB     
 28 ( 6/26)-   Paul          gggggg__bbbbbbbbbbbbbbbBBBBB      
 27 ( 4/26)--  Kazuya        gggg_bbbbbbbbbbbbbbbbbbbbbb       M
 25 ( 2/24)--  Lei           gg_bbbbbbbbbbbbbbbbbbbbBB         $
 24 ( 7/23)-   Dragunov      ggggggg_bbbbbbbbbbbbbbbB          
 23 ( 4/21)--  Devil Jin     gggg__bbbbbbbbbbbbbbbbb           M
 23 ( 4/21)--  Miguel        gggg__bbbbbbbbbbbbbbbbB           
 23 ( 8/23)-   Steve         ggggggggbbbbbbbbbbbbBBB           
 23 ( 3/22)--  Lili          ggg_bbbbbbbbbbbbbbbbbbb           
 23 ( 9/21)    Armor King    ggggggggg__bbbbbbbbbbbB           $
 22 ( 2/22)--  King          ggbbbbbbbbbbbbbbbbbBBB            
 19 ( 3/18)--  Asuka         ggg_bbbbbbbbbbbbbbb               
 17 ( 4/16)-   Lee           gggg_bbbbbbbbbbbB                 
 17 ( 5/16)-   Alisa         ggggg_bbbbbbbbbbB                 
 17 ( 4/16)-   Noctis        gggg_bbbbbbbbbbbb                 $
 16 ( 0/16)--  Kunimitsu     bbbbbbbbbbbbbbbB                  $
 16 ( 1/16)--  Eddy          gbbbbbbbbbbbbbBB                  
 16 ( 3/15)--  Law           ggg_bbbbbbbbbbBB                  
 16 ( 3/15)--  Yoshimitsu    ggg_bbbbbbbbbBBB                  
 14 ( 0/12)--  Xiaoyu        __bbbbbbbbbbbB                    
 13 ( 2/13)--  Nina          ggbbbbbbbbbbB                     
 13 ( 2/13)--  Lucky Chloe   ggbbbbbbbbbbb                     
 12 ( 0/12)--  Feng          bbbbbbbbbbBB                      
 12 ( 1/11)--  Jack-7        g_bbbbbbbbbB                      
 12 ( 0/11)--  Kazumi        _bbbbbbbbbbB                      
 11 ( 1/11)--  Marduk        gbbbbbbbbbB                       $
 10 ( 1/ 9)--  Negan         g_bbbbbbbb                        $
 10 ( 1/ 9)--  Lars          g_bbbbbbBB                        
 10 ( 3/10)-   Julia         gggbbbbbbb                        $
 10 ( 1/10)--  Zafina        gbbbbbbbbB                        $
 10 ( 1/10)--  Geese         gbbbbbbbBB                        $
  9 ( 2/ 8)-   Fahkumram     gg_bbbbBB                         $
  9 ( 1/ 9)--  Bob           gbbbbbbbb                         
  8 ( 1/ 8)--  Leo           gbbbbbbB                          
  8 ( 2/ 8)-   Leroy Smith   ggbbbbbB                          $
  8 ( 1/ 8)--  Master Raven  gbbbbbBB                          
  7 ( 2/ 7)-   Gigas         ggbbbbB                           
  6 ( 0/ 5)--  Anna          _bbbbb                            $
  5 ( 3/ 5)    Akuma         gggbb                             
  5 ( 2/ 4)    Shaheen       gg_bb                             
  4 ( 2/ 4)    Eliza         ggbb                              $
  4 ( 0/ 4)--  Claudio       bbbb                              
  4 ( 0/ 4)--  Ganryu        bbBB                              $
  4 ( 1/ 4)-   Lidia         gbbb                              $
  3 ( 0/ 1)--  Kuma          __b                               
  2 ( 0/ 1)--  Katarina      _b                                
  1 ( 0/ 1)--  Panda         b                                 

(131/707) Overall

  ~Summary~

250 (33.2%) Lose quit
206 (27.4%) Connection
101 (13.4%) Noob
 92 (12.2%) No skip
 70 ( 9.3%) No re
 67 ( 8.9%) Aight
 50 ( 6.6%) Win quit
 32 ( 4.3%) Plug
 31 ( 4.1%) Good
 29 ( 3.9%) BM
 22 ( 2.9%) Great
 14 ( 1.9%) Desync
 14 ( 1.9%) Cheat
 11 ( 1.5%) Okay
  7 ( 0.9%) Custom
  6 ( 0.8%) AFK
  3 ( 0.4%) Boost
(52.8%) able but unwilling to rematch
```

## Setup
1) Put .py file in the same folder as Tekken-7-Player-Displayer.exe
2) Generate player data in-game using that ^ tool. Use the comments listed here in "Tekken Player List.txt" (case insensitive):
    * "no comment yet" (default)
    * "Connection" (for bad connections), "Desync"
    * "Aight", "Okay", "Good", "Great" for overall set quality (good-only)
    * "No skip", "No re" (rematch), "Lose quit", "Win quit"
    * "Cheat", "Plug", "Boosted"
    * "Custom", "BM"
3) Open and run .py file and see the player/character analyses.
     * You may need to update charprops dict in .py file (line 5) with characters that aren't listed (I add them as I go)
     * "Good%" means how many players with the respective character are listed with any "good" comment, out of the total players with that character.
       * For example, (1/8) Bryan means that only one Bryan player was listed as "good" etc. in their comment

## Notes
* Line 1 in the .txt file is skipped. This is because I don't want to include the default data provided by Tekken-7-Player-Displayer and because I deleted the second line.
* It helps to keep the .txt file in a monospaced font. Adding and removing tabs doesn't affect functionality the way I did it.
* The Python terminal should be monospaced in order to line up the Good% chart.
* The comments I left for "Win quit", "No re", and "Lose quit" are a bit inconsistent
* The data I got from the Player Displayer occurred while I was mostly on Heihachi/Dragunov/Noctis/Paul/Jack, mostly around Fujin rank and player match (~400 onwards), with a wired connection, and I rematched most of the time and played honestly. I play from the Midwest.
