# This is a simple Python-based game imitating the classic game of Mad Libs. Follow the prompts, and get a funny story!
# Directions:
# In the same directory as this script, place a "story.txt" file. Inside of this file, have blanks as follows: [adjective], [noun], etc.
# Modified story (story2) is printed and then writen to "story_modified.txt"
# This file will be created if it doesn't exist, and will be overwritten if it does exist

# Imports / Dependencies
import re
from PyQt5 import QtCore, QtGui, QtWidgets

# Variables for original story with blanks
story_file = open("story.txt","r")
story = story_file.read()
story2 = ""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(260, 20, 284, 52))
        self.title.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.frame = QtWidgets.QTextEdit(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 761, 411))
        self.frame.setBaseSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QTextEdit.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QTextEdit.Raised)
        self.frame.setObjectName("frame")
        self.frame.setReadOnly(True)
        self.frame.setText(story)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 490, 761, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.open = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.open.setObjectName("open")
        self.horizontalLayout.addWidget(self.open)
        self.quit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.quit.setObjectName("quit")
        self.horizontalLayout.addWidget(self.quit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "PythonMadLibs"))
        self.save.setText(_translate("MainWindow", "Save Modified Story"))
        self.open.setText(_translate("MainWindow", "Open Modified Story"))
        self.quit.setText(_translate("MainWindow", "Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



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

# Prevent window from closing
input("Press Enter to Exit: ")