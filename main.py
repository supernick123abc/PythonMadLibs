# This is a simple Python-based game imitating the classic game of Mad Libs. Follow the prompts, and get a funny story!
# Directions:
# In the same directory as this script, place a "story.txt" file. Inside of this file, have blanks as follows: [adjective], [noun], etc.
# Modified story (story2) is printed and then writen to "story_modified.txt"
# This file will be created if it doesn't exist, and will be overwritten if it does exist

# Imports / Dependencies
import re

# Variables for original story with blanks
story_file = open("story.txt","r")
story = story_file.read()
story2 = ""

# Main function for reading and modifiying labels
def word_scan(): 
    # Creating another variable to work with rather than directly modifying
    story2 = story
    
    # Search for labels with []
    regex = r"(?<=\[)(.*?)(?=\])"
    
    matches = re.findall(regex, story2)
    
    # Make blank list in preperations for appending changes below
    new = [] 

    # Utilize range and i variable to keep appending changes until end of matches
    for i in range(len(matches)):
        
        new.append(input(str(matches[i] + ": ")))
        story2 = story2.replace(matches[i],new[i])

    # Printing output
    print("Blanks / Replacements: \n")    
    print(matches)  
    print("\n")
    print(story2)
    print("\n")
    
    # Writing to new file and closing files
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

# Calling the function to do the stuff :)
word_scan()