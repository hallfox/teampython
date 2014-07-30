prompt = "> "
# First room
print "It's been a hard day at work, and you lay down to sleep. Suddenly, you begin to dream."
print "In front of you there are 3 portals. Do you enter portal 1, 2, or 3?"

portal = raw_input(prompt)

if portal == "1":
	print "You find yourself within an abandoned tower. There are some stairs in the room, and an open doorway. The only window is boarded up, with beams of light shining through the cracks. What do you do?"
	print "1) Go down the stairs."
	print "2) Walk through the door."
	print "3) Look through the window cracks."
	
	abandoned1 = raw_input(prompt)

	if abandoned1 == "1":
		print "You walk down the stairs. It feels like an enternity before you reach the ground floor. There's a crack addict sitting in front of the entrance doorway. He notices your presence, and pulls out a gun. What do you do?"
		print "1) Try to dissuade the crack addict from killing you."
		print "2) Run towards the crack addict."

		crack_addict = raw_input(prompt)

		if crack_addict == "1":
			print "You try to talk, but it's no use. He unloads the entire gun into your body. You have died."
		elif crack_addict == "2":
			print "You try to rush the crack addict, but he gets a lucky shot off right before you tackle him. You have died."
		else:
			print "You wake up with cold sweats."

	elif abandoned1 == "2":
		print "As you walk through the doorway, the floor gives way beneath you. You have a split second to reach out somewhere before you tumble to your death. What do you do?"
		print "1) Grab to the right."
		print "2) Grab to the left."
		
		falling = raw_input(prompt)

		if falling == "1":
			print "There's nothing to grab to the right. You slam into wooden debris dozens of feet below, resulting in impaling. You have died."
		elif falling == "2":
			print "Thankfully, a small metal pipe is extruding to your left. You hang on for dear life onto this pipe. What do you do?"
			print "1) Hold on."
			print "2) Pull yourself up."
			
			pipe = raw_input(prompt)

			if pipe == "1" or pipe == "2":
				print "It doesn't work, and your hands lose grip. Right before slamming into the ground, you wake up screaming."
			else:
				print "You become the pipe."
		else:
			print "You wake up."

	elif abandoned1 == "3":
		print "Gazing into the cracks, you find yourself staring directly into the pupil of Cthulu's eye. Your mind is unable to comprehend the site, and melts into a slab of jello."
	else:
		print "Everything flashes a brilliant light, and you wake up. Unfortunately, you're now blind."

elif portal == "2":
	print "After seconds of portal travel, a bookstore materializes in front of you. What do you do?"
	print "1) Enter the bookstore."
	print "2) Turn around and walk across the street."
	print "3) Nothing."

	bookstore = raw_input(prompt)

	if bookstore == "1":
		print "The bookstore's name is \"Barnes & Noble\". Rows and rows of books fill the store, and a giant sign near the middle says 'Nook'. What do you do?"
		print "1) Go to the Science Fiction section."
		print "2) Look at the Nooks."
		print "3) Ask a Bookseller if they sell Amazon gift cards."

		books = raw_input(prompt)

		if books == "1":
			print "The Science Fiction section fills two entire aisles of bookshelves. A few books stand out. What do you do?"
			print "1) Look at 'Ubik' by Philip K. Dick."
			print "2) Look at 'Foundation' by Isaac Asimov."
			print "3) Look at 'Childhood's End' by Arthur C. Clarke."
			print "4) Try to steal a book."

			book = raw_input(prompt)

			if book == "1":
				print "You open up Ubik by Philip K. Dick. The book is incredibly strange, yet intriguing. The book involves telepathy, precognition, the afterlife, time reversal, regression of technology, and much more. After reading through it for a few hours, you decide that PKD is your new favorite author."
			elif book == "2":
				print "Foundation is the first in a long series of books. You've read it before, but this leather bound copy intrigues you. What do you do?"
				print "1) Eat the book."
				print "2) Buy the book."
				
				foundation = raw_input(prompt)

				if foundation == "1":
					print "The book is tough and crunchy. Halfway through your meal, a bookseller notices you. A manager comes over and removes you from the store, permamently banning re-entry. Suddenly there's a flash from the sky. You look up and see an asteroid streaking towards the parking lot. There's little time to run. The impact occurs in mere seconds, vaporizing you and everything within a mile radius. Your body convluses in your sleep, killing your real life self. You have died."
				elif foundation == "2":
					print "The checkout line moves quickly. Once it's your turn, the woman behind the counter cheerfully asks if you are a Barnes & Noble member. What do you do?"
					print "1) Pull out your Barnes & Noble membership."
					print "2) Scream at the bookseller for 'trying to con you into their scheming scams', slam the book on the counter, and vow to never shop here again."

					membership = raw_input(prompt)

					if membership == "1":
						print "You save 10%% off the price of the book! You finish paying, and walk outside the bookstore. Suddenly you hear an extremely loud alarm. Turns out its the alarm clock by your bed. You wake up and get ready for the day."
					elif membership == "2":
						print "Your face turns red as you begin to scream at the bookseller for trying to sell you a scam, and instead of slamming the book on the counter, you smash it into the face of the bookseller. A nearby customer tackles you, and the cops show up. You attempt to resist arrest and grab one of the officer's guns with quick reflexes. As you make an attempt to full the trigger at the cop, another officer shoots you in the face. You wake up."
					else:
						print "Lol okay. You wake up without legs."
				else:
					print "You place the book back on the shelf instead. It's best to save a little money every now and then. A few seconds later, the dream ends."
			elif book == "3":
				print "Partway through reading the back description of the book, a massive shadow covers everything outside. You can hear muffled screams through the windows. Rushing outside, you find the sky covered with a massive alien ship. From that moment onward, you realize life will never be the same. But alas, this is a dream. That dream ends, and you return to the boredom of reality."
			elif book == "4":
				print "Bad idea. After putting the book up your shirt, a loud klaxon sounds throughout the bookstore, and other customers drop to their stomachs. The ceiling tiles pop off, and armed men drop through the new openings. One of them lands behind you and slams his fist into your jaw, resulting in unconsciousness. You wake up."
			else:
				print "That works too, I guess. The dream abruptly ends as the serial killer in your house slits your throat as you sleep. You have died."

		elif books == "2":
			print "The nooks fill a significant section of the store. The tablets are cheaply priced, yet seem to be pretty high quality. A nookseller approaches and asks if you have any questions. What do you do?"
			print "1) Buy a Nook HD."
			print "2) Hug the nookseller."
			print "3) Rip a Nook demo unit off of the table and run."

			nooks = raw_input(prompt)

			if nooks == "1":
				print "The nookseller informs you that they're currently out of Nook HDs. A new nook comes out in August and they are preparing for the release. As a result, they cleared out stock of the new Nooks. You buy a Nook Glowlight instead. Unfortunately it's raining as you walk out, and you attempt to activate the device. A raindrop manages to reach some internal circuitry, and it blows up in your hands. You wake up in a panic."
			elif nooks == "2":
				print "You come up and give the Nookseller a tight hug, telling him everything will be alright. He bursts into tears, and says between sobs how you just made his day. He's been going through some tough times, since his wife and children just died in a car accident last month. You and him agree to meet for dinner later that night. You form a new friendship, and can't wait to see your friend next. Your real self enters a coma, and you spend the rest of your life dreaming with your new Nookseller buddy."
			elif nooks == "3":
				print "Pulling the Nook out of its holder snaps the wire, which triggers an old cold war era electric circuit. Turns out there's an old missile silo beneath the bookstore, filled with active nuclear weaponry. All of it detonates simultaneously. The entire city becomes one massive crater. You wake up in shock."
			else:
				print "You become a Nook. An elderly woman later buys you, yet she's mugged as she tries leaving the store and the Nook is taken. You're then given to an eBay reseller, and purchased by a strange man from rural India. Upon arriving to the destination, the man dismantles you for spare parts. You wake up, confused."

		elif books == "3":
			print "The bookseller rolls her eyes, telling you that Amazon is the main competitor of B&N and that they do not sell anything Amazon related. You walk away having learned some valuable new information, and then you wake up."
		else:
			print "That isn't an option, but unfortunately there's no way back. The bookstore vanishes around you, and you find yourself in hell. Turns out you died in your sleep. Have fun spending eternity on fire."

	elif bookstore == "2":
		print "You don't read much, so you decide to see what else is around. As you step into the street, a car comes tearing across the corner. You try to dodge it, but the driver swerves into you at the last second. An ambulance shows up within minutes, yet you're deemed dead on site. You wake up."
	else:
		print "You do nothing. Eventually you wake up."

elif portal == "3":
	print "This portal leads nowhere. Literally nowhere. You spend about an hour falling through the void before waking up. Most boring dream ever. You regret not choosing a different portal."

else:
	print "That isn't an option, so you stand around biding your time. A few people pass by and choose different portals. One guy comes over and mugs you for your shirt. The dream ends shortly after that."