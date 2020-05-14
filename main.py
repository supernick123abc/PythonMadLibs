# This is a simple Python-based game imitating the classic game of Mad Libs. Follow the prompts, and get a funny story!

# Imports / Dependencies
import re
# Placeholder for full text story
story_file = open("story.txt","r")
story = story_file.read()
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
    
    story_file2 = open("story_modified.txt", "w+")
    story_file2.write(story2)
    story_file.close
    story_file2.close
    
    # BELOW CODE ALLOWS FOR FORMATTING OF EACH MATCH
    # for matchNum, match in enumerate(matches, start=1):
        
        # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
        # for groupNum in range(0, len(match.groups())):
        #     groupNum = groupNum + 1
            
        #     print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    
word_scan()