import Tkinter
from Tkinter import *
import tkMessageBox
import string

def randf(seed):
	newseed = seed # hehe
	newseed *= 0x41C64E6D
	newseed += 0x00006073
	newseed &= 0xFFFFFFFF
	return newseed # nice
def getgv():	# Get Game Value
	return GD[cgame.get()]  
def gethv():	# Get Help Value
	return HD[helpstr.get()]  
def update():
	root.after(100, update)
	iseedl.set(ISEED[getgv()])
	cseedl.set(CSEED[getgv()])
	help_label1.set(LABEL1[gethv()])
	help_label2.set(LABEL2[gethv()])
def getdelay():
	delayvalue.set("%d - year" % (int(initialseed.get(),16)&0xFFFF))
def calculateresult():

	if len(initialseed.get()) > 8:
		resultvalue.set('Too Many Chars: 1')
		delayvalue.set('')
		return
	
	if len(currentseed.get()) > 8:
		resultvalue.set('Too Many Chars: 2')
		return

	try:
		a = int(initialseed.get(),16)
		pass
	except ValueError:
		resultvalue.set('Invalid FirstEntry')
		delayvalue.set('')
		return
		
	getdelay()
		
	try:
		a = int(currentseed.get(),16)
		pass
	except ValueError:
		resultvalue.set('Invalid SecondEntry')
		return

	if gethv() == 0: # Find Frame
		tempseed  = int(initialseed.get(),16)
		cs = int(currentseed.get(),16)
		iteration = 0
		while (tempseed != cs) and iteration < 10000:	# Prevent Large Loops.
			tempseed   = randf(tempseed)
			iteration += 1
			
		if iteration < 2000:
			resultvalue.set(iteration)
		else: 
			resultvalue.set(">10000")
	
	else:			 # Find Seed
		try:
			a = int(currentseed.get(),10)
			pass
		except ValueError:
			resultvalue.set('Invalid SecondEntry')
			return
		tempseed = int(initialseed.get(),16)
		frames = int(currentseed.get(),10)
		if frames < 10000: # Prevent Large Loops
			for i in range(0,frames):
				tempseed = randf(tempseed)
			resultvalue.set("%08X" % tempseed)
		else:
			resultvalue.set("Target Frame Too High.")
	return
def PopAbout():
	button_title = "About RNG Helpyr"
	button_text  = "RNG Helpyr Version 1.0a\nProgrammed by Kaphotics.\nBased on KazoWAR's RNG Helper.\nSpecial thanks to all those involved in the RNG scene."
	tkMessageBox.showinfo(button_title,button_text)
	
# GUI 	
root=Tkinter.Tk()
root.title("RNG Helpyr")

# Tables and Dictionaries

# Mode Selections
GAMES =		["Diamond/Pearl","Platinum","HGSS","Ruby/Sapphire","Emerald","FR/LG","Emerald [JP]"]
HELP =		["Frame Finder", "Seed Finder"]

# Converter Tables
GD =		{"Diamond/Pearl": 0, "Platinum": 1, "HGSS": 2, "Ruby/Sapphire": 3, "Emerald": 4, "FR/LG": 5, "Emerald [JP]": 6}
HD = 		{"Frame Finder": 0, "Seed Finder": 1}

# Spitout Tables
ISEED  =	["021C4D4C","021BFB18","021D15AC","RTC: 03000460","New Game: 02020000","Timer1: 02020000","NewGame: 02020000",]
CSEED  =	["021C4D48","021BFB14","021D15A8","03004818","03005D80","03005000","03005AE0"]
LABEL1 =	["Current Seed", "Target Frame"]
LABEL2 =	["Current Frame", "Desired Seed"]

# Dynamic Update String Variables
cgame   = StringVar()
iseedl  = StringVar()
cseedl  = StringVar()
helpstr = StringVar()
help_label1 = StringVar()
help_label2 = StringVar()
initialseed = StringVar()
currentseed = StringVar()
resultvalue = StringVar()
delayvalue  = StringVar()

# Set Default Game (D/P EN)
cgame.set(GAMES[0])
helpstr.set(HELP[0])

# Row 1 : Game Selection
game__label = Tkinter.Label(root, text="Game Version:")
gameversion = apply(OptionMenu, (root, cgame) + tuple(GAMES))
gameversion.pack(expand="yes", fill="x")
game__label.grid(row=0, column=0)
gameversion.grid(row=0, column=1)

# Row 2 : Initial Seed Location
iseed_label = Tkinter.Label(root, text="Initial Seed Location:")
iseed_value = Tkinter.Entry(root,justify=CENTER,state="readonly",textvariable=iseedl)
iseed_label.grid(row=1, column=0)
iseed_value.grid(row=1, column=1)

# Row 3 : Current Seed Location
cseed_label = Tkinter.Label(root, text="Current Seed Location:")
cseed_value = Tkinter.Entry(root,justify=CENTER,state="readonly",textvariable=cseedl)
cseed_label.grid(row=2, column=0)
cseed_value.grid(row=2, column=1)

# Row 4 : Help Selection
help_label = Tkinter.Label(root, text="Help Type:")
help__type = apply(OptionMenu, (root, helpstr) + tuple(HELP))
help__type.pack(expand="yes", fill="x")
help_label.grid(row=3, column=0)
help__type.grid(row=3, column=1)

# Row 5 : Initial Seed
init_label = Tkinter.Label(root, text="Initial Seed:")
init_value = Tkinter.Entry(root,justify=CENTER,textvariable=initialseed)
init_label.grid(row=5, column=0)
init_value.grid(row=5, column=1)

# Row 6 : Current Seed Location
cstf_label = Tkinter.Label(root, textvariable=help_label1)
cstf_value = Tkinter.Entry(root,justify=CENTER,textvariable=currentseed)
cstf_label.grid(row=6, column=0)
cstf_value.grid(row=6, column=1)

# Row 7 : Current Seed Location
cfds_label = Tkinter.Label(root, textvariable=help_label2)
cfds_value = Tkinter.Entry(root,justify=CENTER,state="readonly",textvariable=resultvalue)
cfds_label.grid(row=7, column=0)
cfds_value.grid(row=7, column=1)

# Row 8 : Delay
delay_label = Tkinter.Label(root, text="Initial's Delay")
delay_value = Tkinter.Entry(root,justify=CENTER,state="readonly",textvariable=delayvalue)
delay_label.grid(row=8, column=0)
delay_value.grid(row=8, column=1)

# Row 9 : About & Calculate Buttons
about_btn = Tkinter.Button(root, text ="About", command = PopAbout)
about_btn.pack()
about_btn.grid(row=9, column=0)
calculate_btn = Button(root, text="Calculate", command=calculateresult)
calculate_btn.pack()
calculate_btn.grid(row=9, column=1)


# Prompt : Update Loop
root.after(1, update)
root.mainloop()