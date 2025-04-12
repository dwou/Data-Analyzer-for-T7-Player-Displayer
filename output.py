
from sys import modules
import re

# Print character data line-by-line to verify groups
def verify_groups(groups):
    for i in groups:
        print(f"{i[0]:32}{i[1]:13}{i[2]:18}{i[3]}")

def get_groups(lines: list[str]) -> list[list[str]]:
    error_lines = []
    groups = []
    #            Username     Char               (ID    )     Comment
    pattern = r"^([^\t\n]+)\t+([a-zA-Z 7-]+?)\t+\((\d+)\)\t+?(.*)$"
    for line in lines:
        try:
            groups.append(re.match(pattern,line).groups())
        except:
            error_lines.append(line)
    if error_lines:
        print('Error lines:', error_lines, sep='\n')
    return groups

def main():

    with open("Tekken Player List.txt","r") as f:
        lines = f.readlines()[1:]
    
    # { name:(isfemale,isDLC) } Leo=female; robots/bears/DVJ are intended gender
    charprops = { 'Akuma':(0,0), 'Alisa':(1,0), 'Anna':(1,1), 'Armor King':(0,1), 'Asuka':(1,0), 'Bob':(0,0), 'Bryan':(0,0), 'Claudio':(0,0), 'Devil Jin':(0,0), 'Dragunov':(0,0), 'Eddy':(0,0), 'Eliza':(1,1), 'Fahkumram':(0,1), 'Feng':(0,0), 'Ganryu':(0,1), 'Geese':(0,1), 'Gigas':(0,0), 'Heihachi':(0,0), 'Hwoarang':(0,0), 'Jack-7':(0,0), 'Jin':(0,0), 'Josie':(1,0), 'Julia':(1,1), 'Katarina':(1,0), 'Kazumi':(1,0), 'Kazuya':(0,0), 'King':(0,0), 'Kunimitsu':(1,1), 'Kuma':(0,0), 'Lars':(0,0), 'Law':(0,0), 'Lee':(0,0), 'Lei':(0,1), 'Leo':(1,0), 'Leroy Smith':(0,1), 'Lidia':(1,1), 'Lili':(1,0), 'Lucky Chloe':(1,0), 'Marduk':(0,1), 'Master Raven':(1,0), 'Miguel':(0,0), 'Negan':(0,1), 'Nina':(1,0), 'Noctis':(0,1), 'Panda':(1,0), 'Paul':(0,0), 'Shaheen':(0,0), 'Steve':(0,0), 'Xiaoyu':(1,0), 'Yoshimitsu':(0,0), 'Zafina':(1,1) }
    mishimas = { 'Devil Jin', 'Heihachi', 'Jin', 'Kazuya'}

    males   = [i for i in charprops.keys() if charprops[i][0] == 0]
    females = [i for i in charprops.keys() if charprops[i][0] == 1]
    dlcs    = [i for i in charprops.keys() if charprops[i][1] == 1]
    base_r  = [i for i in charprops.keys() if charprops[i][1] == 0]

    # Case insensitive
    good_keys = ["Aight","Okay","Good","Great"]
    verybad_keys = ["Cheat","Plug","AFK","Boost","Custom"]
    bad_keys = ["No skip","No re","Lose quit","Win quit","Connection","Desync","Custom","BM","AFK","Noob"]
    comment_keys = good_keys + verybad_keys + bad_keys

    #global groups, chars, chars_nodupe
    print("Note: plugging is cheating")

    groups = get_groups(lines)
    #verify_groups(groups)
    
    # Exclude "NULL" character names
    groups = [ group for group in groups if group[1] != "NULL" ]

    # Extract features from groups
    names, chars, IDs, comments = zip(*groups)

    # Make comments lowercase
    comments = [ i.lower() for i in comments ]

    # Create map of players (by ID)
    IDs_m = { j[2] : dict(zip(['name','char','comment'],[j[0],j[1],j[3]])) for j in groups }

    # Find IDs with multiple entries
    if dupes := { j for i,j in enumerate(IDs) if j in IDs[i+1:] }:
        print(f'Duplicate IDs: {dupes}')
    else:
        print('No duplicate IDs found in player list.')

    # Calculate frequency of each character and the frequency of their 'goodness'
    chars_map = {} # { Char : ( pick_count, good_count, no_comments_count, verybad_count ) }
    for char,comment in zip(chars,comments):
        if char in chars_map:
            # count character
            chars_map[char][0] += 1
        else:
            # add character to the map
            chars_map[char] = [1,0,0,0]
        if comment == 'no comment yet':
            # add no_comment
            chars_map[char][2] += 1
        else:
            for j in good_keys:
                if j.lower() in comment:
                    chars_map[char][1] += 1
                    break # count both good and bad keys
            for j in verybad_keys:
                if j.lower() in comment:
                    chars_map[char][3] += 1
                    break
    
    # Calculate female, dlc set%
    total_chars, total_f, total_dlc = 0, 0, 0
    for i in chars_map.keys():
        if charprops[i][1]: total_dlc += chars_map[i][0]
        if charprops[i][0]: total_f += chars_map[i][0]
        total_chars += chars_map[i][0]

    # Print fun facts

    print("\n  ~Fun Facts~\n")
    print("Total players VS'd:",total_chars)
    if len(dlcs)==15 and len(base_r)==36:
        print("All characters found")
    else:
        if len(dlcs) != 15:
            print(f"({len(dlcs)}/15) DLCs found")
            print(f"({len(base_r)}/36) base rosters found")
        elif len(total_m) != 33:
            print(f"({len(males)}/33) males found")
            print(f"({len(females)}/18) females+Leo found")
    print(f"{100*total_f/total_chars:3.1f}% VS females (35.3% expected)")
    print(f"{100*total_dlc/total_chars:3.1f}% VS DLC (29.4% expected)")
    if mishimas_total := sum(1 for i in range(len(chars)) if chars[i] in mishimas):
        mishimas_bad_connection = sum(1 for i in range(len(chars)) if chars[i] in mishimas and 'connection' in comments[i])
        print(f"({mishimas_bad_connection}/{mishimas_total}) Mishimas had a bad connection")
    if 'Law' in chars_map:
        laws_total = chars_map['Law'][0]
        laws_bad_connection = sum(1 for i in range(len(chars)) if chars[i]=='Law' and 'connection' in comments[i])
        print(f"({laws_bad_connection}/{laws_total}) Laws had a bad connection")

    # List of cheaters' characters with duplicates
    cheater_chars = sorted([chars[i] for i in range(len(chars)) if any(j in comments[i] for j in ['cheat','boost','plug','duck'])])

    # { Character: quantity of cheaters }
    cheater_chars_m = { j:cheater_chars.count(j) for j in cheater_chars }

    s = ', '.join( [ name + ( f' x{q}' if q>1 else '' ) for name,q in cheater_chars_m.items() ] )
    print(f"Cheater chars ({len(cheater_chars)}): {s}")

    # Print character pickrate / good% etc.
    
    # This function tacks on a sign to quickly see good%, from -- to ++
    # Made to work with chars_map
    plus_minus_sign = lambda i: ['--','-','','+','++'][int((i[1][1]/(i[1][0]-i[1][2]))*5-.000001)] if i[1][0] - i[1][2] > 0 else ''

    # Chart
    # Get sizes of quantities for formatting
    max_num1 = len(str(max([ i[1][1] for i in chars_map.items() ])))
    max_num2 = len(str(max([ i[1][0]-i[1][2] for i in chars_map.items() ])))
    max_picks = max([ i[1][0] for i in chars_map.items() ])
    print("\n  ~Chart~\n")
    print("Note: Good% accounts for 'no comment yet', but freq does not\n")
    print(f"Tot {'Good%'.ljust(max_num1+max_num2+5)}  Name          Freq")
    for char in sorted(chars_map.items(),key=(lambda x:x[1][0]))[::-1]:
        symbols = '$'[:char[0] in dlcs] + 'M'[:char[0] in mishimas]
        good = 'g' * char[1][1]
        no_comm = '_' * char[1][2]
        verybad = 'B' * char[1][3]
        bad_q = char[1][0] - (char[1][1] + char[1][2] + char[1][3])
        bad = 'b' * bad_q
        total_withcomm = char[1][1] + bad_q + char[1][3]
        total = str(total_withcomm + char[1][2]).rjust(max(3,len(str(max_picks))))
        filler = f"{good}{no_comm}{bad}{verybad}".ljust(max(5,max_picks))
        #       total  (good                             /total_with_comment                   )sign                              char               filler   symbols
        print(f"{total} ({str(char[1][1]).rjust(max_num1)}/{str(total_withcomm).rjust(max_num2)}){(plus_minus_sign(char)).ljust(4)}{char[0].ljust(14)}{filler} {symbols}")

    total_good = sum(i[1][1] for i in chars_map.items())
    total_comm = total_good + sum(i[1][0] - (i[1][1] + i[1][2]) for i in chars_map.items())
    print(f"\n({total_good}/{total_comm}) Overall")

    # Print summary
    print("\n  ~Summary~\n")

    # { comment : frequency }
    comment_freq_m = { comment : len(
        [1 for i in comments if comment.lower() in i]
        ) for comment in comment_keys }

    # count of occurances of most frequent comment, for alignment
    max_comment = max( len(str(x)) for x in comment_freq_m.values() )

    # print comment frequencies
    for j,i in sorted(comment_freq_m.items(),key=lambda x:x[1])[::-1]:
        print(f'{str(i).rjust(max_comment)} ({100*i/total_chars:4.1f}%) {j}')

    # comments indicating an ability but unwillingness for opp to rematch
    quit_comments = ["No re","Lose quit","Win quit","Plug","Desync"]
    overlap = lambda comment, List : any( 1 for j in List if j.lower() in comment )
    quit_comment_occurances = [j for j in comments if overlap(j,quit_comments) and not overlap(j,good_keys) ]

    print(f"({100*len(quit_comment_occurances)/total_chars:4.1f}%) able but unwilling to rematch")

if __name__ == "__main__":
    main()
    if not "idlelib" in modules: input() #input if not in IDLE
