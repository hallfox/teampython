def begin():
	print "\n\n\nWelcome to the game!\n"
	print "-" * 90
	print "During the game type 'ls' to list available commands for the current room"
	print "-" * 90
	print "\nYou've been asleep for 5 years.  They told you your head would hurt when you awoke, but\n"
	print "you didn't think you would feel like cutting your head open to release the pressure.\n"
	print "It's all coming back to you... the economy on Earth is in shambles and the only way\n"
	print "you could get out of being a cutthroat at home was being one for a private military\n"
	print "contractor on Mars.\n"
	
	print "-" * 90
	raw_input('Hit Enter to continue')	
	print "-" * 90
	

def dead(how):
	print how + "\n"
	print "-" * 90
	print "GAME OVER!"
	print "-" * 90
	raw_input('\nHit Enter to replay\n')
	playGame()


def wake_up():
	print "A bright light begins to flash from the console.  Your reflexes kick in and you shield\n"
	print "your eyes.  Your brain waves were picked up from the headset the operator put on before\n"
	print "your long slumber.  The annoying rays of light, triggered by your renewed consciousness,\n"
	print "speak to you...\n"
	
	name = raw_input("Please enter your name >>> ")
	
	print "\nA calm, warm, and motherly voice welcomes you.  Welcome %s.  An operator shall be with you shortly.\n" % name
	print "As the capsule door opens you hear blood curdling screams.  Frozen in fear, you think of your next move.\n"
	
	
	while True:
	
		choice = raw_input("> ")
		
		if choice == "ls":
			print "You can 'sit up', 'peek', or 'stay put'"
		elif choice == "sit up":
			dead("\nYou sit up and see a streak of blood across the 'Welcome to Base 33' sign.  Before anything else can sink\nin,"
				"an alien that eerily looks like the one from that 1979 movie with Sigourney Weaver takes your head off.")
		elif choice == "peek":
			print "\nYou raise your head just enough to see someone impaled by an alien.  The sight makes you slap back"
			print "\ninto your capsule."
			arrival()
		elif choice == "stay put":
			print "\nYou keep your body laying low and wait for the screaming to stop.\n"
			arrival()
		else:
			print "I can't %s" % choice
	
	
def arrival():
	
	print "-" * 90
	raw_input('Hit Enter to continue')
	print "-" * 90
	
	print "After an eternity of silence you decide to look up from your capsule.  You see a hand streak of blood smeared" 
	print "across the 'Welcome to Base 3' sign.  It seems safe enough and the medication forcing your deep sleep is"
	print "wearing off.  Your stomach growls, and the only thing on your mind other than the alien killing every living"
	print "thing, is the gnawing pain in your stomach.\n"
	
	print "A woman covered in horrifying injuries lies on the floor. You kneel down and pull off a key card from her neck"
	print "While doing this you see it... an alien starts running at you from the only hallway in sight.  In a split second you...\n"
	
	while True:
	
		choice = raw_input("> ")
		
		if choice == "ls":
			print "You can 'shut door', 'hide', or 'run'"
		elif choice == "shut door":
			print "You jump, slip, and scramble for the door of the hallway.  As you fling your body toward the keypad your life flashes\n"
			print "before your eyes...  fortunately, you forced such thoughts from your mind and with your key card swipe closed the door\n"
			print "right as the alien reached the doorway.  You hear a large slam against the door, but don't stay long and run down\n"
			print "the hallway at the opposite side of the room."
			cafe()
		elif choice == "hide":
			dead("You run for your capsule and slam the door.  It doesn't take long for it to find you.  You don't even have time for a\n"
				"quick prayer.  There are no atheists in alien burrows")
		elif choice == "run":
			print "\nForget trying to lock the door to the hallway.  In the corner of your eye see another open doorway which you sprint for."
			print "The alien is fast, so fast it slips on the blood spread across the floor.  This slight disruption give you just enough\n"
			print "time to lock the door behind you.  You wait to catch you breath until you notice the alien starting to rip through\n"
			print "the door.  You have enough time to figure out where the cafeteria is." 
			cafe()
		else:
			print "I can't %s" % choice

			
def cafe():

	print "-" * 90
	raw_input('Hit Enter to continue')
	print "-" * 90
	
	print "Whoever designed the base knew whoever arrived here was going to be very hungry or the cafeteria was placed in a"
	print "convenient location for your current situation.  Noticing a refrigerator in the kitchen, you jump the counter and"
	print "proceed to rummage through it's contents.  Many MREs stack the shelves, but you don't complain.  Sitting right"
	print "where you are, you begin your feast.  While chowing down you hear something approaching around the corner.\n"
	
	print "You decide to..."
	
	while True:
	
		choice = raw_input("> ")
		
		if choice == "ls":
			print "You can 'run', 'keep eating', or 'ambush'"
		elif choice == "run":
			print "As you sprint toward the cafeteria exit something black is seen momentarily.  Just as you are about to reach the"
			print "exit you slip and sprain your ankle.  Something approaches, yet speaks to you.  \"I thought I was the only one\""
			print "left alive.  As the man stands in the door frame between the hallway and cafeteria an alien slices through his"
			print "body.\n"		
			dead("Unable to run, ironically, you become the meal in the cafeteria.")
		elif choice == "keep eating":
			print "Alien around the corner?  Sheeit.  I don't care if it's Armageddon on Earth, this MRE is going to be eaten now."
			print "With a mouth full of food something turns the corner and you await your death.  Instead a man begins to laugh"
			print "and asks you if you are enjoying your meal.  You open one eye and smile knowing now you're not alone."
			security()
		elif choice == "ambush":
			print "You grab a nearby knife thinking you can surprise the poor creature rounding the corner.  As you stab into"
			print "the oncoming mass you find your weapon useless.  Someone, not something, retaliates with a shot from a laser gun"
			dead("Sadly, a fellow human looks into your eyes as you pass away into eternity")
		else:
			print "I can't %s" % choice
	
def security():
	
	print "Your new friend explains that some soldiers are locked up in the security room a few rooms away."
	print "They have kept the alien at bay, but every time it attacks it takes at least one person with it"
	print "He proposes you grab some MREs and try to convince them to let you guys in.  You think it's a good idea and"
	print "decide to take the risk of confronting some spooked soldiers for possible refuge.  After making it to the"
	print "security station you hear, \"I can't believe it, how are you guys alive?\" You explain your situation and they"
	print "agree to let you in in exchange for some of the MREs.  When they open the door an alien pops out from the above"
	print "duct work.  You decide to..."
	
	while True:
	
		choice = raw_input("> ")
		
		if choice == "ls":
			print "You can 'scram' or 'fight'"
		elif choice == "scram":
			print "Instead of staying and helping your new friend and the other soldiers you try and dash down the"
			print "hallway."
			dead("As you begin your run the alien swipes it's tail across your neck.  Another one bites the dust")
		elif choice == "fight":
			print "You and your friend stumble inside the security room and hit the ground.  The soldiers begin"
			print "firing what weapons they have, but the alien is fast and swiftly makes his way toward the"
			print "soldiers firing their weapons.  Your friend gets up and gets you to your feet and you rush"
			print "out of the room"
			finale()
		else:
			print "I can't %s" % choice
	
	
def finale():
	print "On the way out your buddy grabbed a pistol one of the soldiers dropped as he was impaled during"
	print "the onslaught.  He explains there are some pods used for evacuation just around the corner."
	print "He explains how it works on the way there, which is good because the alien was unknowingly right"
	print "on your tails.  He holds the creature off while you escape to bring back help."
	
	print "\n\nGood job, you won!"
	
	exit(1)
	
def playGame():
	begin()
	wake_up()
	arrival()
	cafe()
	security()
	finale()	
	
	
playGame()
	