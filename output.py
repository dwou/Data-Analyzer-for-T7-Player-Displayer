
import sys
import re

# { name:(isfemale,isDLC) } Leo=female; robots/animals/DVJ are intended gender
charprops = { 'Alisa':(1,0), 'Anna':(1,1), 'Armor King':(0,1), 'Asuka':(1,0), 'Bob':(0,0), 'Bryan':(0,0), 'Devil Jin':(0,0), 'Dragunov':(0,0), 'Eddy':(0,0), 'Fahkumram':(0,1), 'Feng':(0,0), 'Ganryu':(0,1), 'Geese':(0,1), 'Gigas':(0,0), 'Heihachi':(0,0), 'Hwoarang':(0,0), 'Jack-7':(0,0), 'Jin':(0,0), 'Josie':(1,0), 'Julia':(1,1), 'Katarina':(1,0), 'Kazumi':(1,0), 'Kazuya':(0,0), 'King':(0,0), 'Kunimitsu':(1,1), 'Kuma':(0,0), 'Lars':(0,0), 'Law':(0,0), 'Lee':(0,0), 'Lei':(0,1), 'Leo':(1,0), 'Leroy Smith':(0,1), 'Lidia':(1,1), 'Lili':(1,0), 'Lucky Chloe':(1,0), 'Marduk':(0,1), 'Master Raven':(1,0), 'Miguel':(0,0), 'Negan':(0,1), 'Nina':(1,0), 'Noctis':(0,1), 'Panda':(1,0), 'Paul':(0,0), 'Shaheen':(0,0), 'Steve':(0,0), 'Xiaoyu':(1,0), 'Yoshimitsu':(0,0), 'Zafina':(1,1) }
mishimas = { 'Devil Jin', 'Heihachi', 'Jin', 'Kazuya'}


males   = [i for i in charprops.keys() if charprops[i][0] == 0]
females = [i for i in charprops.keys() if charprops[i][0] == 1]
dlcs    = [i for i in charprops.keys() if charprops[i][1] == 1]
base_r  = [i for i in charprops.keys() if charprops[i][1] == 0]

# Case insensitive
comkeys = ["Aight","Okay","Good","Great","No skip","No re","Lose quit","Win quit","Cheat","Plug","Connection","Desync","No comment"]
goods = ["Aight","Okay","Good","Great"]
bads = [i for i in comkeys if i not in goods]
#bads.remove("Desync")

with open("Tekken Player List.txt","r") as f:
    lines = f.readlines()[1:]

# Print character data line-by-line to verify groups
def verify_groups(groups):
    for i in groups:
        print(f"{i[0]:30}{i[1]:12}{i[2]:18}{i[3]}")


if 1: # analysis
    #                        Username     Char                ID         Comment
    groups = [ re.findall(r"^([^\t\n]+)\t+([a-zA-Z 7-]+?)\t+\((\d+)\)\t+?(.*)$",i)[-1] for i in lines ]
    if 0: verify_groups(groups)
    names, chars, IDs, comments = [ [row[i] for row in groups] for i in range(4)]
    comments = [ i.lower() for i in comments ]
    chars_nodupe = sorted([j for i,j in enumerate(chars) if j not in chars[i:]])


    # Find IDs with multiple entries
    if (dupes := { j for i,j in enumerate(IDs) if j in IDs[i+1:] }):
        print(f'Duplicate IDs: {dupes}')
    else:
        print('No duplicate IDs found in player list.')

    
    # Calculate frequency of each character and the frequency of their goodness
    chars_map = {} # { Char : (picks,goods,no_comments) }
    for char,comment in zip(chars,comments):
        if char in chars_map:
            chars_map[char][0] += 1
        else:
            chars_map[char] = [1,0,0]
        if comment == 'no comment yet':
            #print(f'No comment: {char}') # print chars with 'no comment yet'
            chars_map[char][2] += 1
        else:
            for j in goods:
                if j.lower() in comment:
                    chars_map[char][1] += 1
                    break


    # Calculate female, dlc set%
    total, total_f, total_dlc = 0, 0, 0
    for i in chars_map.keys():
        if charprops[i][1]: total_dlc += chars_map[i][0]
        if charprops[i][0]: total_f += chars_map[i][0]
        total += chars_map[i][0]


    # Print fun facts
    print("\n  ~Fun Facts~\n")
    print("Total players VS'd:",total)
    print(f"({len(dlcs)}/15) DLCs found")
    print(f"({len(base_r)}/36) base rosters found")
    print(f"({len(females)}/18) females+Leo found")
    print(f"({len(males)}/33) males found")
    print(f"{100*total_f/total:3.1f}% VS females (35.3% expected)")
    print(f"{100*total_dlc/total:3.1f}% VS DLC (29.4% expected)")
    print(f"({sum([1 for i in range(len(chars)) if chars[i]=='Law' and 'connection' in comments[i]])}/{chars_map['Law'][0]}) Laws had a bad connection")
    cheater_chars = sorted([chars[i] for i in range(len(chars)) if 'cheat' in comments[i] or 'plug' in comments[i]])
    print(f"Cheat/plug ({len(cheater_chars)}): {', '.join(cheater_chars)}")

    # This function tacks on a sign to quickly see good%, from -- to ++
    # Made to work with chars_map
    plus_minus_sign = lambda i: ['--','-','','+','++'][int((i[1][1]/(i[1][0]-i[1][2]))*5-.000001)] if i[1][0] - i[1][2] > 0 else ''
    # Print character pickrate / good% etc.

    max_num1 = len(str(max([ i[1][1] for i in chars_map.items() ])))
    max_num2 = len(str(max([ i[1][0]-i[1][2] for i in chars_map.items() ])))
    max_picks = max([ i[1][0] for i in chars_map.items() ])
    print("\n  ~Chart~\n")
    print("Note: Good% accounts for 'no comment yet', but freq does not\n")
    print("Good%      Name          Freq")
    for i in sorted(chars_map.items(),key=(lambda x:x[1][0]))[::-1]:
        symbols ='$'[:i[0] in dlcs] + 'M'[:i[0] in mishimas]
        #symbols = ' '.join(list(symbols)) #'♂♀'
        gender_sign = ':*'[i[0] in females]
        print(f"({str(i[1][1]).ljust(max_num1)}/{str(i[1][0]-i[1][2]).ljust(max_num2)}){(plus_minus_sign(i)).ljust(5)}{i[0].ljust(14)}{(gender_sign*i[1][0]).ljust(max_picks)} {symbols}")

    # print comment frequencies
    print("\n  ~Summary~\n")
    # { comment : frequency }
    comment_freq_m = { j:len([1 for i in comments if j.lower() in i]) for j in comkeys }
    comment_freq_m
    max_comment = max(map(lambda x:len(str(x)),comment_freq_m.values()))
    for j,i in sorted(comment_freq_m.items(),key=lambda x:x[1])[::-1]:
        print(f'{str(i).ljust(max_comment)} ({100*i/total:4.1f}%) {j}')
    quit_comments = ["No re","Lose quit","Win quit","Plug"] # Desync OK
    total_quits = [j for j in comments if any(1 for i in quit_comments if i.lower() in j) ]
    print(f"({100*len(total_quits)/total:4.1f}%) total No re, Lose quit, Win quit, Plug")
    viable_comments = [i for i in comments if not any(['connection' in i, 'cheat' in i, 'No comment' in i, 'Desync' in i])]
    total_quits2 = [i for i in viable_comments if i in total_quits]
    print(f'({100*len(total_quits2)/len(viable_comments):4.1f}%) total no rematch, excluding connection, cheating, "no comment", desync')

if not "idlelib" in sys.modules: input() #input if not in IDLE; works now; Python, huh?





