
import re

# { name:(isfemale,isDLC) } Leo=female; robots/animals/DVJ are intended gender
charprops = { 'Alisa':(1,0), 'Anna':(1,1), 'Armor King':(0,1), 'Asuka':(1,0), 'Bob':(0,0), 'Bryan':(0,0), 'Devil Jin':(0,0), 'Dragunov':(0,0), 'Eddy':(0,0), 'Fahkumram':(0,1), 'Feng':(0,0), 'Ganryu':(0,1), 'Geese':(0,1), 'Gigas':(0,0), 'Heihachi':(0,0), 'Hwoarang':(0,0), 'Jack-7':(0,0), 'Jin':(0,0), 'Josie':(1,0), 'Julia':(1,1), 'Katarina':(1,0), 'Kazumi':(1,0), 'Kazuya':(0,0), 'King':(0,0), 'Kuma':(0,0), 'Lars':(0,0), 'Law':(0,0), 'Lee':(0,0), 'Lei':(0,1), 'Leroy Smith':(0,1), 'Lidia':(1,1), 'Lili':(1,0), 'Lucky Chloe':(1,0), 'Marduk':(0,1), 'Master Raven':(1,0), 'Miguel':(0,0), 'Negan':(0,1), 'Nina':(1,0), 'Noctis':(0,1), 'Panda':(1,0), 'Paul':(0,0), 'Shaheen':(0,0), 'Steve':(0,0), 'Xiaoyu':(1,0), 'Yoshimitsu':(0,0), 'Zafina':(1,1) }

males   = [i for i in charprops.keys() if charprops[i][0] == 0]
females = [i for i in charprops.keys() if charprops[i][0] == 1]
dlcs    = [i for i in charprops.keys() if charprops[i][1] == 1]
base_r  = [i for i in charprops.keys() if charprops[i][1] == 0]


with open("Tekken Player List.txt","r") as f:
    lines = f.readlines()


if 1: # analysis
    #                        Username     Char                ID         Comment
    groups = [ re.findall(r"^([^\t\n]+)\t+([a-zA-Z 7-]+?)\t+\((\d+)\)\t+?(.*)$",i)[-1] for i in lines ]

    # Print character data line-by-line to verify groups
    #for i in groups:
    #    print(f"{i[0]:30}{i[1]:13}{i[2]:18}{i[3]}")
    
    names,chars,IDs,comments = [ [row[i].lower() for row in groups] for i in range(4)]
    chars = [ i.title() for i in chars ]
    chars_nodupe = sorted([j for i,j in enumerate(chars) if j not in chars[i+1:]])
    
    comkeys = ["Aight","Okay","Good","Great","No skip","No re","Lose quit","Win quit","Cheat","Plug","Connection","Desync","No comment"]
    goods = ["Aight","Okay","Good","Great"]
    chars_map = {} # { Char : (picks,goods) }

    # One ID with multiple entries
    if (dupes := { j for i,j in enumerate(IDs) if j in IDs[i+1:] }):
        print(f'Dupes: {dupes}')
    else:
        print('No duplicate IDs found in player list.')
    
    # Calculate frequency of each character and the frequency of their goodness
    for i in range(len(groups)):
        char,comment = chars[i], comments[i]
        if char not in chars_map.keys():
            chars_map[char] = [1,0]
        else:
            chars_map[char][0] += 1
        for j in goods:
            if j.lower() in comment:
                chars_map[char][1] += 1
    
    
    # Calculate female, dlc set%
    total,total_f,total_dlc = 0,0,0
    for i in chars_map.keys():
        if charprops[i][1]: total_dlc += chars_map[i][0]
        if charprops[i][0]: total_f += chars_map[i][0]
        total += chars_map[i][0]

    # Print fun facts
    print("")
    print("Total players VS'd:",total)
    print(f"({len(dlcs)}/15) DLCs found")
    print(f"({len(base_r)}/36) base rosters found")
    print(f"({len(females)}/18) females+Leo found")
    print(f"({len(males)}/33) males found")
    print(f"{int(1000*total_f/total+.5)/10}% VS females (35.3% expected)")
    print(f"{int(1000*total_dlc/total+.5)/10}% VS DLC (29.4% expected)")
    print(f"({sum([1 for i in range(len(chars)) if chars[i]=='Law' and 'connection' in comments[i]])}/{chars_map['Law'][0]}) Laws had a bad connection")
    print(f"Cheaters/pluggers characters: {[chars[i] for i in range(len(chars)) if 'cheat' in comments[i] or 'plug' in comments[i]]}")

    # This function tacks on a sign to quickly see good%, from -- to ++
    plus_minus_sign = lambda i: ['--','-','','+','++'][int((i[1][1]/i[1][0])*5-.000001)]
    # Print character pickrate / good% etc.
    print("\n\nGood%      Name          Freq")
    for i in sorted(chars_map.items(),key=(lambda x:x[1][0]))[::-1]:
        print(f"({i[1][1]}/{i[1][0]}){(plus_minus_sign(i)).ljust(6)}{i[0].ljust(14)}{'*'*i[1][0]}")
    print('')

    # print comment frequencies
    for j in comkeys:
        print(j,": ",len([i for i in comments if j.lower() in i]),sep="")


#if not "idlelib" in sys.modules: input() #input if not in IDLE; broken






