from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
figlet_list = figlet.getFonts()

if len(sys.argv) == 1 :
    theChosen = random.choice(figlet.getFonts())
elif len(sys.argv) == 3 :
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        theChosen = sys.argv[2]
else :
    sys.exit("Invalid Usage")

figlet.setFont(font=theChosen)

Input = input("Input: ")

print(figlet.renderText(Input))
