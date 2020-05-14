# This is a simple Python-based game imitating the classic game of Mad Libs. Follow the prompts, and get a funny story!

# Imports / Dependencies
import re
# Placeholder for full text story
story = "A vacation is when you take a trip to some [adjective1] place with your [adjective2] family. Usually you go to some place that is near a/an [noun1] or up on a/an [noun2]. A good vacation place is one where you can ride [noun_plural1] or play [game] or go hunting for [noun-plural]. I like to spend my time [verb_ing1] or [verb_ing2]. When parents go on a vacation, they spend their time eating three [noun_plural2] a day, and fathers play golf, and mothers sit around [verb_ing3]. Last summer, my little brother fell in a/an [noun3] and got poison [noun4] all over his [body1]. My family is going to go to (the) [place1], and I will practice [verb_ing4]. Parents need vacations more than kids because parents are always very [adjective3] and because they have to work [number1] hours every day all year making enough [noun_plural3] to pay for the vacation."
story2 = ""

def word_scan(): 
    story2 = story
    # wow = story2.count("[adjective" + str(1) + "]")
    # start = story2.find("[adjective") + len("[adjective")
    # end = story2.find("]")
    # substring = story2[start:end]
    # print(substring)
    
    regex = r"(?<=\[)(.*?)(?=\])"
    
    matches = re.findall(regex, story2)
    
    new = [] 
    
    # old = ['[adjective1]','[adjective2]','[verb_ing1]']

    for i in range(len(matches)):
        
        new.append(input(str(matches[i] + ": ")))
        story2 = story2.replace(matches[i],new[i])

    print("Blanks / Replacements: \n")    
    print(matches)  
    print("\n")
    print(story2)
    print("\n")
    
    # BELOW CODE ALLOWS FOR FORMATTING OF EACH MATCH
    # for matchNum, match in enumerate(matches, start=1):
        
        # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
        # for groupNum in range(0, len(match.groups())):
        #     groupNum = groupNum + 1
            
        #     print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    
word_scan()