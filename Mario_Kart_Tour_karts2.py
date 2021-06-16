import weakref

class race_tool:
	_instances = set()

	def __init__(self, name, rarity, three_items = {}, two_items = {}, lv3_courses = {}, lv6_courses = {}):
		self.name = name
		self.rarity = rarity
		self._instances.add(weakref.ref(self))
		self.three_items = three_items
		self.two_items = two_items
		self.lv3_courses = lv3_courses
		self.lv6_courses = lv6_courses
	@classmethod
	def getinstances(cls):
		dead = set()
		for ref in cls._instances:
			obj = ref()
			if obj is not None:
				yield obj
			else:
				dead.add(ref)
		cls._instances -= dead


#Blue_Badwagon_
# https://game8.co/games/mariokarttour/archives/270470

Blue_Badwagon__TWO_x_Bonus_Points = ['Rock Rock Mountain T', 'Shy Guy Bazaar T', 'SNES Rainbow Road T', 'Mario Circuit 3', 'Los Angeles Laps R', 'New York Minute 3T', 'New York Minute 3R/T', 'Berlin Byways 2T', 'Berlin Byways 2R/T']

Blue_Badwagon__ONEoFIVE_x_Bonus_Points = ['New York Minute R/T', 'Rock Rock Mountain', 'Shy Guy Bazaar', 'Daisy Hills R', 'Daisy Hills', 'Neo Bowser City R', 'SNES Rainbow Road R', "Luigi's Mansion R", 'Ghost Valley 1', 'Mario Circuit 3T', 'Paris Promenade T', "Bowser's Castle 2R/T", 'Los Angeles Laps T', 'Los Angeles Laps', 'New York Minute 3', 'New York Minute 3R', 'Berlin Byways 2', 'Berlin Byways 2R', 'DK Summit T']

Blue_Badwagon__lv3_courses = ['Daisy Hills R', 'SNES Rainbow Road R']

Blue_Badwagon__lv6_courses = ['Neo Bowser City R', "Bowser's Castle 2R/T"]

Blue_Badwagon_ = race_tool('Blue_Badwagon_', 'High-End', Blue_Badwagon__TWO_x_Bonus_Points, Blue_Badwagon__ONEoFIVE_x_Bonus_Points, Blue_Badwagon__lv3_courses, Blue_Badwagon__lv6_courses)


#Badwagon_
# https://game8.co/games/mariokarttour/archives/270469

Badwagon__TWO_x_Bonus_Points = ['Rock Rock Mountain R', 'Yoshi Circuit R', 'Shy Guy Bazaar', 'Daisy Hills R', "Bowser's Castle 1", 'Kalimari Desert', 'Neo Bowser City R', 'RMX Rainbow Road 2R', 'Donut Plains 2R']

Badwagon__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain T', "Bowser's Castle 1R", 'Tokyo Blur 2R/T', 'Toad Circuit R/T', 'Choco Island 1', 'Choco Island 1R', 'Choco Mountain R', 'Choco Mountain T', 'Sunset Wilds R/T', 'RMX Rainbow Road 2', 'RMX Rainbow Road 2T', 'Donut Plains 2T']

Badwagon__lv3_courses = ['Rock Rock Mountain T', 'Toad Circuit R/T']

Badwagon__lv6_courses = ['Choco Island 1R', 'Choco Mountain T']

Badwagon_ = race_tool('Badwagon_', 'High-End', Badwagon__TWO_x_Bonus_Points, Badwagon__ONEoFIVE_x_Bonus_Points, Badwagon__lv3_courses, Badwagon__lv6_courses)


#Yellow_Taxi_
# https://game8.co/games/mariokarttour/archives/270468

Yellow_Taxi__TWO_x_Bonus_Points = ['Mario Circuit 1T', 'New York Minute', 'Toad Circuit R', 'New York Minute T', 'Waluigi Pinball', 'DS Rainbow Road T', 'Tokyo Blur 2R/T', 'Shy Guy Bazaar R/T', 'London Loop 2R/T']

Yellow_Taxi__ONEoFIVE_x_Bonus_Points = ['New York Minute R', 'New York Minute R/T', 'Yoshi Circuit T', 'Yoshi Circuit R', 'Toad Circuit T', 'Mario Circuit 2T', 'Mario Circuit R', 'Neo Bowser City T', "Luigi's Mansion R", 'New York Minute 2', 'DS Rainbow Road', 'New York Minute 2R/T', 'DK Pass R/T', 'London Loop 2', 'London Loop 2R', "Bowser's Castle 2", "Bowser's Castle 2R", 'New York Minute 3T', 'New York Minute 3R/T']

Yellow_Taxi__lv3_courses = ['Toad Circuit T', "Bowser's Castle 2"]

Yellow_Taxi__lv6_courses = ['Mario Circuit R', 'DS Rainbow Road']

Yellow_Taxi_ = race_tool('Yellow_Taxi_', 'High-End', Yellow_Taxi__TWO_x_Bonus_Points, Yellow_Taxi__ONEoFIVE_x_Bonus_Points, Yellow_Taxi__lv3_courses, Yellow_Taxi__lv6_courses)


#Black_B_Dasher_
# https://game8.co/games/mariokarttour/archives/270467

Black_B_Dasher__TWO_x_Bonus_Points = ['New York Minute R', 'New York Minute R/T', 'Yoshi Circuit T', 'Yoshi Circuit', 'Mario Circuit T', 'Neo Bowser City T', 'Donut Plains 1R', 'Tokyo Blur 3T']

Black_B_Dasher__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 1T', 'Cheep Cheep Lagoon R', 'Daisy Hills T', 'Daisy Hills R', 'Toad Circuit T', 'Toad Circuit R', 'Mario Circuit 1', 'New York Minute T', 'Neo Bowser City', 'Frappe Snowland R', 'DK Pass R/T', 'Choco Island 2R/T', 'London Loop 2R', 'Donut Plains 1T', 'Tokyo Blur 3', 'Tokyo Blur 3R']

Black_B_Dasher__lv3_courses = ['Daisy Hills T', 'Daisy Hills R']

Black_B_Dasher__lv6_courses = ['Toad Circuit R', 'Neo Bowser City']

Black_B_Dasher_ = race_tool('Black_B_Dasher_', 'High-End', Black_B_Dasher__TWO_x_Bonus_Points, Black_B_Dasher__ONEoFIVE_x_Bonus_Points, Black_B_Dasher__lv3_courses, Black_B_Dasher__lv6_courses)


#B_Dasher_
# https://game8.co/games/mariokarttour/archives/270466

B_Dasher__TWO_x_Bonus_Points = ['Cheep Cheep Lagoon T', 'Daisy Hills', 'Toad Circuit R', 'Toad Circuit', 'Mario Circuit 1', 'Mario Circuit', 'Mario Circuit 3R/T', 'Tokyo Blur 3R', 'RMX Rainbow Road 2R']

B_Dasher__ONEoFIVE_x_Bonus_Points = ['New York Minute R', 'New York Minute R/T', 'Yoshi Circuit T', 'Mario Circuit 1T', 'Mario Circuit 1R', 'Donut Plains 1T', 'RMX Mario Circuit 1R/T', 'Tokyo Blur 3', 'Tokyo Blur 3T', 'RMX Rainbow Road 2T']

B_Dasher__lv3_courses = ['Mario Circuit 1T', 'Mario Circuit 1R']

B_Dasher__lv6_courses = ['Yoshi Circuit T', 'RMX Mario Circuit 1R/T']

B_Dasher_ = race_tool('B_Dasher_', 'High-End', B_Dasher__TWO_x_Bonus_Points, B_Dasher__ONEoFIVE_x_Bonus_Points, B_Dasher__lv3_courses, B_Dasher__lv6_courses)


#Black_Circuit_
# https://game8.co/games/mariokarttour/archives/270712

Black_Circuit__TWO_x_Bonus_Points = ['Yoshi Circuit', 'Neo Bowser City', 'SNES Rainbow Road R', 'Neo Bowser City T', 'Waluigi Pinball R', 'Tokyo Blur 3R', 'New York Minute 3T']

Black_Circuit__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 1T', 'Shy Guy Bazaar T', 'Cheep Cheep Lagoon T', 'Tokyo Blur', 'Mario Circuit 2T', 'Mario Circuit T', 'Tokyo Blur R/T', 'Waluigi Pinball', 'Ghost Valley 1T', 'Mario Circuit 3', "Bowser's Castle 2T", "Bowser's Castle 2R/T", 'Tokyo Blur 3', 'Tokyo Blur 3T', 'Maple Treeway R']

Black_Circuit__lv3_courses = ['Mario Circuit 1T', "Bowser's Castle 2T"]

Black_Circuit__lv6_courses = ['Cheep Cheep Lagoon T', 'Waluigi Pinball']

Black_Circuit_ = race_tool('Black_Circuit_', 'High-End', Black_Circuit__TWO_x_Bonus_Points, Black_Circuit__ONEoFIVE_x_Bonus_Points, Black_Circuit__lv3_courses, Black_Circuit__lv6_courses)


#Circuit_Special_
# https://game8.co/games/mariokarttour/archives/270711

Circuit_Special__TWO_x_Bonus_Points = ['Yoshi Circuit T', 'Mario Circuit 1T', 'Toad Circuit R', 'Mario Circuit 2T', 'Mario Circuit 2', 'Mario Circuit', 'Waluigi Pinball T', 'Mario Circuit 3R', 'Vancouver Velocity T']

Circuit_Special__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit R', 'Mario Circuit 1R', 'Toad Circuit', 'Tokyo Blur R', 'Mario Circuit 2R', 'Mario Circuit R', 'Waluigi Pinball R', 'Vancouver Velocity', 'RMX Mario Circuit 1R/T']

Circuit_Special__lv3_courses = ['Mario Circuit 1R', 'Waluigi Pinball R']

Circuit_Special__lv6_courses = ['Yoshi Circuit R', 'Mario Circuit R']

Circuit_Special_ = race_tool('Circuit_Special_', 'High-End', Circuit_Special__TWO_x_Bonus_Points, Circuit_Special__ONEoFIVE_x_Bonus_Points, Circuit_Special__lv3_courses, Circuit_Special__lv6_courses)


#Kabuki_Dasher_
# https://game8.co/games/mariokarttour/archives/270710

Kabuki_Dasher__TWO_x_Bonus_Points = ['Mario Circuit 1R', 'Shy Guy Bazaar R', 'Daisy Hills T', 'Toad Circuit T', 'SNES Rainbow Road', 'Mario Circuit R', 'Tokyo Blur R/T', 'Ghost Valley 1T', 'Shy Guy Bazaar R/T', 'Donut Plains 1T', 'RMX Mario Circuit 1R/T', 'Tokyo Blur 3T', 'New York Minute 3']

Kabuki_Dasher__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit T', 'Mario Circuit 1T', 'Mario Circuit 1', 'Tokyo Blur R', 'Tokyo Blur T', 'Mario Circuit 3R', 'Choco Island 2R/T', 'Donut Plains 1', 'Donut Plains 1R', 'Tokyo Blur 3R', 'New York Minute 3R', 'New York Minute 3T', 'RMX Rainbow Road 2R', 'RMX Rainbow Road 2T']

Kabuki_Dasher__lv3_courses = ['Yoshi Circuit T', 'Mario Circuit 1T']

Kabuki_Dasher__lv6_courses = ['Mario Circuit 1', 'Mario Circuit 3R']

Kabuki_Dasher_ = race_tool('Kabuki_Dasher_', 'High-End', Kabuki_Dasher__TWO_x_Bonus_Points, Kabuki_Dasher__ONEoFIVE_x_Bonus_Points, Kabuki_Dasher__lv3_courses, Kabuki_Dasher__lv6_courses)


#Quickshaw_
# https://game8.co/games/mariokarttour/archives/270709

Quickshaw__TWO_x_Bonus_Points = ['Dino Dino Jungle', 'Toad Circuit', 'Tokyo Blur', 'Choco Island 2T', 'Mario Circuit T', 'Paris Promenade R', 'Mario Circuit 3R', 'DS Rainbow Road', 'Tokyo Blur 2', 'Tokyo Blur 2R', 'Tokyo Blur 2T', 'London Loop 2R/T', 'New York Minute 3', 'New York Minute 3R']

Quickshaw__ONEoFIVE_x_Bonus_Points = ['Tokyo Blur R', 'Mario Circuit 2R', 'Mario Circuit R', 'Mario Circuit', 'Neo Bowser City T', 'Tokyo Blur T', 'Tokyo Blur R/T', "Luigi's Mansion R", 'Ghost Valley 1T', 'DS Rainbow Road T', 'Tokyo Blur 2R/T', 'Vanilla Lake 1R/T', 'Tokyo Blur 3R', 'Tokyo Blur 3T', 'Los Angeles Laps T', 'Los Angeles Laps R', 'New York Minute 3R', 'New York Minute 3R/T', 'RMX Choco Island 2']

Quickshaw__lv3_courses = ['Neo Bowser City T', 'Vanilla Lake 1R/T']

Quickshaw__lv6_courses = ['Mario Circuit', "Luigi's Mansion R"]

Quickshaw_ = race_tool('Quickshaw_', 'High-End', Quickshaw__TWO_x_Bonus_Points, Quickshaw__ONEoFIVE_x_Bonus_Points, Quickshaw__lv3_courses, Quickshaw__lv6_courses)


#Bumble_V_
# https://game8.co/games/mariokarttour/archives/271639

Bumble_V__TWO_x_Bonus_Points = ['Dino Dino Jungle R', 'Daisy Hills', 'Mario Circuit 2R', 'Waluigi Pinball', 'Waluigi Pinball T', 'Mario Circuit 3', 'SNES Rainbow Road R/T', 'Paris Promenade 2T', 'Paris Promenade 2R/T', 'Waluigi Pinball R/T']

Bumble_V__ONEoFIVE_x_Bonus_Points = ['Dino Dino Jungle T', 'London Loop', 'London Loop R', 'Paris Promenade 2R', 'Paris Promenade 2', 'Donut Plains 1R/T', 'Choco Island 1T', 'Airship Fortress R', 'Airship Fortress T', 'Los Angeles Laps T', 'Los Angeles Laps R/T', "Rosalina's Ice World R", "Rosalina's Ice World T"]

Bumble_V__lv3_courses = ['Dino Dino Jungle T', 'Donut Plains 1R/T']

Bumble_V__lv6_courses = ['Choco Island 1T', 'Airship Fortress R']

Bumble_V_ = race_tool('Bumble_V_', 'High-End', Bumble_V__TWO_x_Bonus_Points, Bumble_V__ONEoFIVE_x_Bonus_Points, Bumble_V__lv3_courses, Bumble_V__lv6_courses)


#Queen_Bee_
# https://game8.co/games/mariokarttour/archives/271638

Queen_Bee__TWO_x_Bonus_Points = ['Koopa Troopa Beach R', 'Daisy Hills T', 'Daisy Hills R', 'Toad Circuit R', "Luigi's Mansion T", 'Ghost Valley 1T', 'Paris Promenade R/T', 'Mario Circuit R/T', 'RMX Choco Island 1R', 'Donut Plains 2R']

Queen_Bee__ONEoFIVE_x_Bonus_Points = ['Dino Dino Jungle R', "Luigi's Mansion", 'Ghost Valley 1', 'Ghost Valley 1R', 'Mario Circuit 3', 'RMX Choco Island 1T', 'Donut Plains 2T']

Queen_Bee__lv3_courses = ['Ghost Valley 1', 'Ghost Valley 1R']

Queen_Bee__lv6_courses = ["Luigi's Mansion", 'Mario Circuit 3']

Queen_Bee_ = race_tool('Queen_Bee_', 'High-End', Queen_Bee__TWO_x_Bonus_Points, Queen_Bee__ONEoFIVE_x_Bonus_Points, Queen_Bee__lv3_courses, Queen_Bee__lv6_courses)


#Trickster_
# https://game8.co/games/mariokarttour/archives/271637

Trickster__TWO_x_Bonus_Points = ['Shy Guy Bazaar', 'Choco Island 2R', "Luigi's Mansion", "Luigi's Mansion R", 'Ghost Valley 1', 'Ghost Valley 1R', "Bowser's Castle 2R/T", 'New York Minute 3R', 'Maple Treeway R']

Trickster__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain T', 'Rock Rock Mountain R', 'SNES Rainbow Road T', 'SNES Rainbow Road T', "Luigi's Mansion T", 'Ghost Valley 1T', 'DK Pass R', 'New York Minute 3T', 'New York Minute 3R/T', 'Sunset Wilds R/T']

Trickster__lv3_courses = ['Rock Rock Mountain T', 'SNES Rainbow Road T']

Trickster__lv6_courses = ['Rock Rock Mountain R', "Luigi's Mansion T"]

Trickster_ = race_tool('Trickster_', 'High-End', Trickster__TWO_x_Bonus_Points, Trickster__ONEoFIVE_x_Bonus_Points, Trickster__lv3_courses, Trickster__lv6_courses)


#Ghost_Ride_
# https://game8.co/games/mariokarttour/archives/271636

Ghost_Ride__TWO_x_Bonus_Points = ['Neo Bowser City', 'Neo Bowser City T', "Luigi's Mansion R", "Bowser's Castle 2R", "Bowser's Castle 2R/T", 'RMX Choco Island 1R']

Ghost_Ride__ONEoFIVE_x_Bonus_Points = ["Luigi's Mansion", "Luigi's Mansion T", 'Ghost Valley 1', 'Ghost Valley 1T', 'Paris Promenade T', 'Paris Promenade', 'Paris Promenade R', 'DK Pass', 'DK Pass T', "Bowser's Castle 2", "Bowser's Castle 2T", 'RMX Choco Island 1', 'RMX Choco Island 1T', 'Maple Treeway T']

Ghost_Ride__lv3_courses = ["Luigi's Mansion", "Bowser's Castle 2T"]

Ghost_Ride__lv6_courses = ['Ghost Valley 1T', 'RMX Choco Island 1T']

Ghost_Ride_ = race_tool('Ghost_Ride_', 'High-End', Ghost_Ride__TWO_x_Bonus_Points, Ghost_Ride__ONEoFIVE_x_Bonus_Points, Ghost_Ride__lv3_courses, Ghost_Ride__lv6_courses)


#Macharon_
# https://game8.co/games/mariokarttour/archives/272262

Macharon__TWO_x_Bonus_Points = ['Koopa Troopa Beach', 'Tokyo Blur', 'Paris Promenade', 'Paris Promenade R/T', 'Daisy Hills R/T', 'London Loop T', 'Cheep Cheep Lagoon R/T', 'Paris Promenade 2R', 'Frappe Snowland R/T', 'Choco Island 1R', 'Choco Island 1T', 'Maple Treeway R', 'Maple Treeway T', 'DK Summit R']

Macharon__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit', 'Daisy Hills T', 'Mario Circuit 1', 'Tokyo Blur R', 'Mario Circuit 3T', 'Paris Promenade T', 'SNES Rainbow Road R/T', 'London Loop R/T', 'Yoshi Circuit R/T', 'DS Rainbow Road T', 'Paris Promenade 2T', 'Paris Promenade 2', 'Paris Promenade 2R/T', 'Vancouver Velocity R', 'Donut Plains 1R/T', 'Choco Island 1', 'RMX Rainbow Road 2R']

Macharon__lv3_courses = ['Mario Circuit 1', 'SNES Rainbow Road R/T']

Macharon__lv6_courses = ['Yoshi Circuit', 'Choco Island 1']

Macharon_ = race_tool('Macharon_', 'High-End', Macharon__TWO_x_Bonus_Points, Macharon__ONEoFIVE_x_Bonus_Points, Macharon__lv3_courses, Macharon__lv6_courses)


#Carrot_Kart_
# https://game8.co/games/mariokarttour/archives/272263

Carrot_Kart__TWO_x_Bonus_Points = ['Toad Circuit T', 'Paris Promenade T', 'Paris Promenade R', 'New York Minute 2R/T', 'Mario Circuit 1R/T', 'Choco Island 2R/T', 'Paris Promenade 2R', 'Paris Promenade 2R/T', 'Mario Circuit 3R/T', 'Donut Plains 1T', 'New York Minute 3R']

Carrot_Kart__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 1', 'SNES Rainbow Road T', 'Mario Circuit 3', 'Mario Circuit 3T', 'Paris Promenade', 'Mario Circuit 3R', 'Mario Circuit R/T', 'Daisy Hills R/T', 'London Loop R', "Luigi's Mansion R/T", 'New York Minute 2T', 'Paris Promenade 2T', 'Dino Dino Jungle R/T', 'Vancouver Velocity', 'Vancouver Velocity R', 'RMX Mario Circuit 1R/T', 'Kalimari Desert 2', 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'New York Minute 3', 'New York Minute 3R/T']

Carrot_Kart__lv3_courses = ['SNES Rainbow Road T', 'Dino Dino Jungle R/T']

Carrot_Kart__lv6_courses = ['Mario Circuit 3R', 'Kalimari Desert 2R']

Carrot_Kart_ = race_tool('Carrot_Kart_', 'High-End', Carrot_Kart__TWO_x_Bonus_Points, Carrot_Kart__ONEoFIVE_x_Bonus_Points, Carrot_Kart__lv3_courses, Carrot_Kart__lv6_courses)


#Gold_Train_
# https://game8.co/games/mariokarttour/archives/272264

Gold_Train__TWO_x_Bonus_Points = ['Dino Dino Jungle T', 'Choco Island 2', 'Kalimari Desert', 'SNES Rainbow Road R', 'Paris Promenade', 'DK Pass R', "Luigi's Mansion R/T", 'Donut Plains 1R/T', 'Vanilla Lake 1R/T', 'Kalimari Desert 2T', 'New York Minute 3R', 'Merry Mountain R', 'RMX Rainbow Road 2R']

Gold_Train__ONEoFIVE_x_Bonus_Points = ['Dino Dino Jungle', 'SNES Rainbow Road', 'Waluigi Pinball', 'Waluigi Pinball R', 'Paris Promenade R/T', 'Paris Promenade R', 'SNES Rainbow Road R/T', 'Daisy Hills R/T', 'Paris Promenade 2', 'Choco Island 1R', 'Choco Island 1T', 'Kalimari Desert 2', 'Kalimari Desert 2R', 'New York Minute 3T', 'New York Minute 3R/T', 'Merry Mountain', 'Merry Mountain T', 'RMX Rainbow Road 2']

Gold_Train__lv3_courses = ['SNES Rainbow Road', 'SNES Rainbow Road R/T']

Gold_Train__lv6_courses = ['Choco Island 1T', 'Kalimari Desert 2']

Gold_Train_ = race_tool('Gold_Train_', 'High-End', Gold_Train__TWO_x_Bonus_Points, Gold_Train__ONEoFIVE_x_Bonus_Points, Gold_Train__lv3_courses, Gold_Train__lv6_courses)


#Cheermellow_
# https://game8.co/games/mariokarttour/archives/273759

Cheermellow__TWO_x_Bonus_Points = ['SNES Rainbow Road', 'Choco Island 2T', 'DK Pass', 'DK Pass T', 'Mario Circuit 2R/T', 'Toad Circuit R/T', 'Vanilla Lake 1', 'DK Pass R/T', 'RMX Mario Circuit 1T', 'RMX Choco Island 1R', 'New York Minute 3', 'New York Minute 3T', 'New York Minute 3R/T', 'Merry Mountain T']

Cheermellow__ONEoFIVE_x_Bonus_Points = ['Choco Island 2R', 'Yoshi Circuit R/T', "Luigi's Mansion R/T", 'Tokyo Blur 2', 'Frappe Snowland T', 'Vanilla Lake 1R', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1R', 'RMX Choco Island 1', 'New York Minute 3R', 'Merry Mountain', 'Merry Mountain R', "Rosalina's Ice World R"]

Cheermellow__lv3_courses = ["Luigi's Mansion R/T", 'Vanilla Lake 1R']

Cheermellow__lv6_courses = ['Frappe Snowland T', 'RMX Choco Island 1']

Cheermellow_ = race_tool('Cheermellow_', 'High-End', Cheermellow__TWO_x_Bonus_Points, Cheermellow__ONEoFIVE_x_Bonus_Points, Cheermellow__lv3_courses, Cheermellow__lv6_courses)


#Wild_Wing_
# https://game8.co/games/mariokarttour/archives/273760

Wild_Wing__TWO_x_Bonus_Points = ['Rock Rock Mountain R', "Bowser's Castle 1R", 'Mario Circuit R', 'Neo Bowser City T', 'DK Pass R', 'Daisy Hills R/T', 'Tokyo Blur 2R/T', 'Dino Dino Jungle R/T', 'RMX Mario Circuit 1R', 'London Loop 2R', 'London Loop 2R/T', "Bowser's Castle 2T", 'Kalimari Desert 2']

Wild_Wing__ONEoFIVE_x_Bonus_Points = ["Bowser's Castle 1T", 'DK Pass', 'DK Pass T', 'London Loop T', "Bowser's Castle 1R/T", 'Mario Circuit 2R/T', 'Neo Bowser City R/T', 'RMX Mario Circuit 1T', 'London Loop 2', "Bowser's Castle 2", "Bowser's Castle 2R", 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'RMX Rainbow Road 1R', 'Berlin Byways 2T', 'Berlin Byways 2R/T']

Wild_Wing__lv3_courses = ["Bowser's Castle 2", "Bowser's Castle 2R"]

Wild_Wing__lv6_courses = ['DK Pass T', 'Kalimari Desert 2R']

Wild_Wing_ = race_tool('Wild_Wing_', 'High-End', Wild_Wing__TWO_x_Bonus_Points, Wild_Wing__ONEoFIVE_x_Bonus_Points, Wild_Wing__lv3_courses, Wild_Wing__lv6_courses)


#Radish_Rider_
# https://game8.co/games/mariokarttour/archives/273761

Radish_Rider__TWO_x_Bonus_Points = ['Mario Circuit 1', 'Waluigi Pinball T', 'Mario Circuit 3', 'Mario Circuit 3T', 'DK Pass T', 'DK Pass T', 'Royal Raceway R', 'Royal Raceway', 'Merry Mountain R']

Radish_Rider__ONEoFIVE_x_Bonus_Points = ['Mario Circuit', 'DK Pass R', 'London Loop', 'London Loop T', 'Mario Circuit 1R/T', 'Paris Promenade 2T', 'Paris Promenade 2', 'Waluigi Pinball R/T', 'Ghost Valley 1R/T', 'Vancouver Velocity T', 'Vancouver Velocity R', 'Donut Plains 1R/T', 'Sunset Wilds']

Radish_Rider__lv3_courses = ['Mario Circuit', 'Mario Circuit 1R/T']

Radish_Rider__lv6_courses = ['DK Pass R', 'Waluigi Pinball R/T']

Radish_Rider_ = race_tool('Radish_Rider_', 'High-End', Radish_Rider__TWO_x_Bonus_Points, Radish_Rider__ONEoFIVE_x_Bonus_Points, Radish_Rider__lv3_courses, Radish_Rider__lv6_courses)


#Wildfire_Flyer_
# https://game8.co/games/mariokarttour/archives/273762

Wildfire_Flyer__TWO_x_Bonus_Points = ['Paris Promenade R/T', 'Paris Promenade R', 'DK Pass R', "Bowser's Castle 1R/T", 'Tokyo Blur 2R', 'Neo Bowser City R/T', 'Shy Guy Bazaar R/T', 'Paris Promenade 2T', 'RMX Mario Circuit 1R', 'RMX Choco Island 1', 'Royal Raceway R', 'Royal Raceway T']

Wildfire_Flyer__ONEoFIVE_x_Bonus_Points = ['Choco Island 2', "Luigi's Mansion R", 'Paris Promenade', 'DK Pass', 'DK Pass T', 'London Loop R', 'Tokyo Blur 2T', 'Tokyo Blur 2R/T', 'Vanilla Lake 1T', 'Paris Promenade 2R', 'Paris Promenade 2R/T', 'RMX Mario Circuit 1T', "Bowser's Castle 2R/T", 'RMX Choco Island 1R', 'RMX Choco Island 1T']

Wildfire_Flyer__lv3_courses = ['DK Pass', 'DK Pass T']

Wildfire_Flyer__lv6_courses = ['Vanilla Lake 1T', 'RMX Choco Island 1T']

Wildfire_Flyer_ = race_tool('Wildfire_Flyer_', 'High-End', Wildfire_Flyer__TWO_x_Bonus_Points, Wildfire_Flyer__ONEoFIVE_x_Bonus_Points, Wildfire_Flyer__lv3_courses, Wildfire_Flyer__lv6_courses)


#Double_Decker_
# https://game8.co/games/mariokarttour/archives/274707

Double_Decker__TWO_x_Bonus_Points = ["Bowser's Castle 1T", 'Neo Bowser City R', "Luigi's Mansion", 'Waluigi Pinball R', 'London Loop R', 'London Loop R/T', 'Mario Circuit 1R/T', 'London Loop 2T', 'London Loop 2R/T', 'Donut Plains 1T', 'Berlin Byways 2R/T', 'Donut Plains 2R']

Double_Decker__ONEoFIVE_x_Bonus_Points = ['Waluigi Pinball T', 'DK Pass T', 'London Loop', 'London Loop T', 'New York Minute 2R', 'DS Rainbow Road R', 'Tokyo Blur 2T', 'Tokyo Blur 2R/T', 'Vanilla Lake 1', 'DK Pass R/T', 'London Loop 2', 'London Loop 2R', 'Donut Plains 1', 'Donut Plains 1R', "Bowser's Castle 2", "Bowser's Castle 2R", 'Berlin Byways 2', 'Berlin Byways 2T', 'Donut Plains 2T']

Double_Decker__lv3_courses = ['DK Pass R/T', "Bowser's Castle 2"]

Double_Decker__lv6_courses = ['Donut Plains 1', 'Donut Plains 1R']

Double_Decker_ = race_tool('Double_Decker_', 'High-End', Double_Decker__TWO_x_Bonus_Points, Double_Decker__ONEoFIVE_x_Bonus_Points, Double_Decker__lv3_courses, Double_Decker__lv6_courses)


#Ribbon_Rider_
# https://game8.co/games/mariokarttour/archives/274706

Ribbon_Rider__TWO_x_Bonus_Points = ['Shy Guy Bazaar T', 'Koopa Troopa Beach R', 'London Loop', 'London Loop R/T', 'DS Rainbow Road R', 'Waluigi Pinball R/T', 'Vancouver Velocity R/T', 'London Loop 2', 'Choco Mountain', 'Tokyo Blur 3T', 'Merry Mountain R', 'RMX Rainbow Road 2', 'Berlin Byways 2R']

Ribbon_Rider__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar', 'Koopa Troopa Beach T', 'Mario Circuit', 'SNES Rainbow Road T', 'Choco Island 2T', 'DK Pass', 'London Loop T', 'Yoshi Circuit R/T', 'New York Minute 2', 'New York Minute 2R/T', 'DK Pass R/T', 'Frappe Snowland R/T', 'DS Rainbow Road R/T', 'Choco Mountain R', 'Choco Mountain T', 'Tokyo Blur 3R', 'Merry Mountain', 'Merry Mountain T', 'RMX Rainbow Road 2R', 'RMX Rainbow Road 2T', 'Berlin Byways 2']

Ribbon_Rider__lv3_courses = ['Mario Circuit', 'DK Pass R/T']

Ribbon_Rider__lv6_courses = ['DK Pass', 'Choco Mountain T']

Ribbon_Rider_ = race_tool('Ribbon_Rider_', 'High-End', Ribbon_Rider__TWO_x_Bonus_Points, Ribbon_Rider__ONEoFIVE_x_Bonus_Points, Ribbon_Rider__lv3_courses, Ribbon_Rider__lv6_courses)


#Swift_Jack_
# https://game8.co/games/mariokarttour/archives/274705

Swift_Jack__TWO_x_Bonus_Points = ['Yoshi Circuit R', "Bowser's Castle 1", 'London Loop R', "Bowser's Castle 1R/T", "Luigi's Mansion R/T", 'New York Minute 2R/T', 'Tokyo Blur 2R/T', 'Waluigi Pinball R/T', 'London Loop 2R', 'London Loop 2T', 'RMX Mario Circuit 1R/T', 'Royal Raceway R', 'Los Angeles Laps T', 'Sunset Wilds R', 'Berlin Byways 2R']

Swift_Jack__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 2T', 'Mario Circuit 2R', 'Mario Circuit 2', 'Mario Circuit R/T', 'Daisy Hills R/T', 'Mario Circuit 1R/T', 'Tokyo Blur 2', 'Tokyo Blur 2T', 'Mario Circuit 2R/T', 'Shy Guy Bazaar R/T', 'Paris Promenade 2R/T', 'Koopa Troopa Beach R/T', 'Mario Circuit 3R/T', 'London Loop 2', 'London Loop 2R/T', 'Royal Raceway', 'Los Angeles Laps R/T', 'Berlin Byways 2', 'Berlin Byways 2R/T']

Swift_Jack__lv3_courses = ['Mario Circuit 2', 'Mario Circuit 3R/T']

Swift_Jack__lv6_courses = ['Mario Circuit 2T', 'Daisy Hills R/T']

Swift_Jack_ = race_tool('Swift_Jack_', 'High-End', Swift_Jack__TWO_x_Bonus_Points, Swift_Jack__ONEoFIVE_x_Bonus_Points, Swift_Jack__lv3_courses, Swift_Jack__lv6_courses)


#Red_B_Dasher_
# https://game8.co/games/mariokarttour/archives/274948

Red_B_Dasher__TWO_x_Bonus_Points = ["Bowser's Castle 1T", 'Tokyo Blur R', 'SNES Rainbow Road', 'Mario Circuit 2T', 'Mario Circuit', 'Daisy Hills R/T', 'DS Rainbow Road', 'Mario Circuit 2R/T', 'Donut Plains 1', 'Donut Plains 1R', 'RMX Mario Circuit 1R/T', 'Tokyo Blur 3T', 'Sunset Wilds R', 'Sunset Wilds R/T', 'Merry Mountain R']

Red_B_Dasher__ONEoFIVE_x_Bonus_Points = ['Daisy Hills R', "Bowser's Castle 1", 'Tokyo Blur', 'Mario Circuit T', 'Mario Circuit 3R', 'London Loop', 'London Loop T', 'Frappe Snowland', 'Mario Circuit 3R/T', 'London Loop 2T', 'London Loop 2R/T', 'Donut Plains 1T', 'Choco Mountain', 'Choco Mountain R', 'Tokyo Blur 3', 'Tokyo Blur 3R', 'Tokyo Blur 3T', 'Sunset Wilds', 'Sunset Wilds T', 'RMX Rainbow Road 1R/T', 'Berlin Byways 2R', 'Berlin Byways 2R/T']

Red_B_Dasher__lv3_courses = ['Mario Circuit 3R/T', 'Donut Plains 1T']

Red_B_Dasher__lv6_courses = ['Mario Circuit 3R', 'Frappe Snowland']

Red_B_Dasher_ = race_tool('Red_B_Dasher_', 'High-End', Red_B_Dasher__TWO_x_Bonus_Points, Red_B_Dasher__ONEoFIVE_x_Bonus_Points, Red_B_Dasher__lv3_courses, Red_B_Dasher__lv6_courses)


#Jingle_Bells_
# https://game8.co/games/mariokarttour/archives/275172

Jingle_Bells__TWO_x_Bonus_Points = ['Rock Rock Mountain T', 'Cheep Cheep Lagoon T', 'Dino Dino Jungle', 'DK Pass T', 'SNES Rainbow Road R/T', 'New York Minute 2T', 'New York Minute 2', 'DK Pass R/T', 'Merry Mountain T', "Rosalina's Ice World T"]

Jingle_Bells__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain', 'Cheep Cheep Lagoon R', 'Dino Dino Jungle R', 'DK Pass R', 'DS Rainbow Road T', 'Neo Bowser City R/T', 'Toad Circuit R/T', 'Frappe Snowland', 'Frappe Snowland R', 'Vanilla Lake 1', 'RMX Mario Circuit 1R', 'New York Minute 3R/T', 'Merry Mountain', 'Merry Mountain R', "Rosalina's Ice World"]

Jingle_Bells__lv3_courses = ['Rock Rock Mountain', 'Toad Circuit R/T']

Jingle_Bells__lv6_courses = ['DK Pass R', 'Frappe Snowland']

Jingle_Bells_ = race_tool('Jingle_Bells_', 'High-End', Jingle_Bells__TWO_x_Bonus_Points, Jingle_Bells__ONEoFIVE_x_Bonus_Points, Jingle_Bells__lv3_courses, Jingle_Bells__lv6_courses)


#Platinum_Taxi_
# https://game8.co/games/mariokarttour/archives/275173

Platinum_Taxi__TWO_x_Bonus_Points = ['DK Pass R', 'New York Minute 2R', 'DS Rainbow Road R', 'Tokyo Blur 2R', 'Neo Bowser City R/T', 'Vanilla Lake 1', 'London Loop 2R/T', 'Royal Raceway R', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 1R/T']

Platinum_Taxi__ONEoFIVE_x_Bonus_Points = ["Bowser's Castle 1T", "Bowser's Castle 1", 'DK Pass', 'DK Pass T', 'SNES Rainbow Road R/T', 'New York Minute 2', 'Tokyo Blur 2', 'Toad Circuit R/T', 'Vanilla Lake 1T', 'Vancouver Velocity', 'Vancouver Velocity R/T', 'RMX Choco Island 1R', 'Royal Raceway T', 'Royal Raceway', 'RMX Rainbow Road 1T', 'Merry Mountain', 'Merry Mountain R']

Platinum_Taxi__lv3_courses = ["Bowser's Castle 1T", 'DK Pass']

Platinum_Taxi__lv6_courses = ['DK Pass T', 'RMX Rainbow Road 1T']

Platinum_Taxi_ = race_tool('Platinum_Taxi_', 'High-End', Platinum_Taxi__TWO_x_Bonus_Points, Platinum_Taxi__ONEoFIVE_x_Bonus_Points, Platinum_Taxi__lv3_courses, Platinum_Taxi__lv6_courses)


#Bruiser_
# https://game8.co/games/mariokarttour/archives/275174

Bruiser__TWO_x_Bonus_Points = ['Yoshi Circuit T', 'Kalimari Desert R', 'Neo Bowser City', 'London Loop R/T', 'London Loop T', 'New York Minute 2T', 'New York Minute 2', 'Kalimari Desert R/T', 'Neo Bowser City R/T', 'Shy Guy Bazaar R/T', 'Ghost Valley 1R/T', 'Kalimari Desert 2R']

Bruiser__ONEoFIVE_x_Bonus_Points = ['Kalimari Desert T', 'Kalimari Desert', "Luigi's Mansion", "Luigi's Mansion R", 'Waluigi Pinball R', 'Waluigi Pinball T', 'London Loop', "Bowser's Castle 1R/T", 'New York Minute 2R', 'Choco Island 2R/T', 'Dino Dino Jungle R/T', 'Kalimari Desert 2', 'RMX Choco Island 2R', 'RMX Choco Island 2T']

Bruiser__lv3_courses = ['Kalimari Desert T', "Bowser's Castle 1R/T"]

Bruiser__lv6_courses = ['Waluigi Pinball T', 'Kalimari Desert 2']

Bruiser_ = race_tool('Bruiser_', 'High-End', Bruiser__TWO_x_Bonus_Points, Bruiser__ONEoFIVE_x_Bonus_Points, Bruiser__lv3_courses, Bruiser__lv6_courses)


#Glam_Bruiser_
# https://game8.co/games/mariokarttour/archives/275394

Glam_Bruiser__TWO_x_Bonus_Points = ['Waluigi Pinball T', 'Mario Circuit 3T', 'Mario Circuit 3R', "Bowser's Castle 1R/T", 'Toad Circuit R/T', 'Choco Island 2R/T', "Bowser's Castle 2", "Bowser's Castle 2R", 'New York Minute 3R/T']

Glam_Bruiser__ONEoFIVE_x_Bonus_Points = ['Neo Bowser City T', 'Waluigi Pinball', 'Tokyo Blur 2R', 'Mario Circuit 2R/T', 'Vanilla Lake 1', 'Vanilla Lake 1R', 'Vanilla Lake 1T', 'Shy Guy Bazaar R/T', 'Waluigi Pinball R/T', 'Koopa Troopa Beach R/T', 'Mario Circuit 3R/T', "Bowser's Castle 2T", 'New York Minute 3', 'New York Minute 3R', 'Merry Mountain R', 'Merry Mountain T']

Glam_Bruiser__lv3_courses = ['Neo Bowser City T', 'Shy Guy Bazaar R/T']

Glam_Bruiser__lv6_courses = ['Waluigi Pinball', 'Waluigi Pinball R/T']

Glam_Bruiser_ = race_tool('Glam_Bruiser_', 'High-End', Glam_Bruiser__TWO_x_Bonus_Points, Glam_Bruiser__ONEoFIVE_x_Bonus_Points, Glam_Bruiser__lv3_courses, Glam_Bruiser__lv6_courses)


#Ice_blue_Poltergust_
# https://game8.co/games/mariokarttour/archives/275777

Ice_blue_Poltergust__TWO_x_Bonus_Points = ["Luigi's Mansion", 'DS Rainbow Road T', 'Frappe Snowland R', 'Vanilla Lake 1T', 'Ghost Valley 1R/T', 'Frappe Snowland R/T', 'DS Rainbow Road R/T', 'Vanilla Lake 1R/T', 'Berlin Byways 2', 'RMX Choco Island 2R']

Ice_blue_Poltergust__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar T', 'Choco Island 2R', 'Choco Island 2T', 'DS Rainbow Road', 'Cheep Cheep Lagoon R/T', 'Frappe Snowland', 'Frappe Snowland T', 'Vanilla Lake 1', 'Waluigi Pinball R/T', 'Vancouver Velocity T', 'Vancouver Velocity R/T', 'Berlin Byways 2T', 'Berlin Byways 2R/T', 'RMX Choco Island 2', 'DK Summit R']

Ice_blue_Poltergust__lv3_courses = ['Shy Guy Bazaar T', 'Choco Island 2T']

Ice_blue_Poltergust__lv6_courses = ['Frappe Snowland', 'Vanilla Lake 1']

Ice_blue_Poltergust_ = race_tool('Ice_blue_Poltergust_', 'High-End', Ice_blue_Poltergust__TWO_x_Bonus_Points, Ice_blue_Poltergust__ONEoFIVE_x_Bonus_Points, Ice_blue_Poltergust__lv3_courses, Ice_blue_Poltergust__lv6_courses)


#P_Wing
# https://game8.co/games/mariokarttour/archives/275776

P_Wing_TWO_x_Bonus_Points = ['Mario Circuit R', 'Mario Circuit T', 'Neo Bowser City T', 'Mario Circuit 3T', 'Yoshi Circuit R/T', 'Vanilla Lake 1T', 'Vancouver Velocity R', 'RMX Rainbow Road 1R']

P_Wing_ONEoFIVE_x_Bonus_Points = ['Neo Bowser City', 'Neo Bowser City', 'Mario Circuit 3', 'Mario Circuit 3R', "Bowser's Castle 1R/T", 'Frappe Snowland', 'Frappe Snowland T', 'Shy Guy Bazaar R/T', 'Ghost Valley 1R/T', 'Vancouver Velocity R/T', 'London Loop 2R', "Bowser's Castle 2", "Bowser's Castle 2R", 'RMX Mario Circuit 1R/T', 'Royal Raceway T', 'Royal Raceway', 'Airship Fortress R', 'Airship Fortress T']

P_Wing_lv3_courses = ['Mario Circuit 3', 'Ghost Valley 1R/T']

P_Wing_lv6_courses = ['Frappe Snowland T', 'Royal Raceway T']

P_Wing = race_tool('P_Wing', 'High-End', P_Wing_TWO_x_Bonus_Points, P_Wing_ONEoFIVE_x_Bonus_Points, P_Wing_lv3_courses, P_Wing_lv6_courses)


#Gilded_Prancer_
# https://game8.co/games/mariokarttour/archives/275775

Gilded_Prancer__TWO_x_Bonus_Points = ['DK Pass', 'Mario Circuit R/T', 'Daisy Hills R/T', 'Frappe Snowland', 'Frappe Snowland T', 'Vanilla Lake 1T', 'DK Pass R/T', 'DS Rainbow Road R/T', 'Royal Raceway T', 'Royal Raceway', 'Sunset Wilds R']

Gilded_Prancer__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar R', 'Toad Circuit', 'DK Pass R', 'Frappe Snowland R', 'Paris Promenade 2R', 'Paris Promenade 2R/T', 'Vancouver Velocity', 'Vancouver Velocity R/T', 'Royal Raceway R', 'Sunset Wilds T']

Gilded_Prancer__lv3_courses = ['Shy Guy Bazaar R', 'Toad Circuit']

Gilded_Prancer__lv6_courses = ['DK Pass R', 'Frappe Snowland R']

Gilded_Prancer_ = race_tool('Gilded_Prancer_', 'High-End', Gilded_Prancer__TWO_x_Bonus_Points, Gilded_Prancer__ONEoFIVE_x_Bonus_Points, Gilded_Prancer__lv3_courses, Gilded_Prancer__lv6_courses)


#Apple_Kart_
# https://game8.co/games/mariokarttour/archives/278440

Apple_Kart__TWO_x_Bonus_Points = ['Dino Dino Jungle R', 'Daisy Hills', 'Mario Circuit R/T', 'Tokyo Blur 2T', 'Frappe Snowland', 'Paris Promenade 2R', 'Paris Promenade 2', 'Paris Promenade 2R/T', 'Mario Circuit 3R/T', 'RMX Choco Island 1T', "Rosalina's Ice World"]

Apple_Kart__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar T', 'Shy Guy Bazaar R', 'Dino Dino Jungle T', 'Daisy Hills R', 'SNES Rainbow Road R', 'Tokyo Blur 2', 'Tokyo Blur 2R', 'Paris Promenade 2T', 'Frappe Snowland R/T', 'Koopa Troopa Beach R/T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1R', 'RMX Mario Circuit 1T', 'RMX Choco Island 1', 'Choco Island 1', 'Choco Island 1R', 'Choco Island 1T', "Rosalina's Ice World R", 'RMX Rainbow Road 2', 'RMX Choco Island 2', 'RMX Choco Island 2R']

Apple_Kart__lv3_courses = ['Shy Guy Bazaar R', 'Daisy Hills R']

Apple_Kart__lv6_courses = ['RMX Mario Circuit 1', 'Choco Island 1R']

Apple_Kart_ = race_tool('Apple_Kart_', 'High-End', Apple_Kart__TWO_x_Bonus_Points, Apple_Kart__ONEoFIVE_x_Bonus_Points, Apple_Kart__lv3_courses, Apple_Kart__lv6_courses)


#Comet_Tail_
# https://game8.co/games/mariokarttour/archives/279958

Comet_Tail__TWO_x_Bonus_Points = ['Cheep Cheep Lagoon T', "Luigi's Mansion R", 'SNES Rainbow Road R/T', 'DS Rainbow Road', 'DS Rainbow Road T', 'Frappe Snowland', 'Frappe Snowland T', 'Vancouver Velocity T', 'Vancouver Velocity', 'Vancouver Velocity R', 'Vancouver Velocity R/T', 'DS Rainbow Road R/T', 'Vanilla Lake 1R/T', 'RMX Rainbow Road 1R', "Rosalina's Ice World T", 'RMX Rainbow Road 2R']

Comet_Tail__ONEoFIVE_x_Bonus_Points = ['SNES Rainbow Road T', 'SNES Rainbow Road R', 'Paris Promenade', 'DS Rainbow Road R', 'Frappe Snowland R', 'RMX Mario Circuit 1', 'London Loop 2T', 'New York Minute 3', "Rosalina's Ice World", "Rosalina's Ice World R", 'RMX Rainbow Road 2T']

Comet_Tail__lv3_courses = ['SNES Rainbow Road T', 'Frappe Snowland R']

Comet_Tail__lv6_courses = ['DS Rainbow Road R', 'RMX Mario Circuit 1']

Comet_Tail_ = race_tool('Comet_Tail_', 'High-End', Comet_Tail__TWO_x_Bonus_Points, Comet_Tail__ONEoFIVE_x_Bonus_Points, Comet_Tail__lv3_courses, Comet_Tail__lv6_courses)


#Snow_Skimmer_
# https://game8.co/games/mariokarttour/archives/279959

Snow_Skimmer__TWO_x_Bonus_Points = ['Cheep Cheep Lagoon R', 'Cheep Cheep Lagoon', "Luigi's Mansion R", 'London Loop R/T', 'London Loop T', 'DS Rainbow Road R', 'Frappe Snowland', 'Vanilla Lake 1', 'Vanilla Lake 1T', 'Vancouver Velocity R', 'Koopa Troopa Beach R/T']

Snow_Skimmer__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain', 'Kalimari Desert R', 'Kalimari Desert', 'SNES Rainbow Road R/T', 'Mario Circuit R/T', 'London Loop', 'DS Rainbow Road T', 'Vanilla Lake 1R', 'Vancouver Velocity T', 'Vancouver Velocity R/T', 'Frappe Snowland R/T', 'RMX Mario Circuit 1T', 'Vanilla Lake 1R/T', 'New York Minute 3', 'RMX Rainbow Road 1R/T', 'DK Summit', 'DK Summit R']

Snow_Skimmer__lv3_courses = ['Kalimari Desert R', 'Mario Circuit R/T']

Snow_Skimmer__lv6_courses = ['Kalimari Desert', 'DS Rainbow Road T']

Snow_Skimmer_ = race_tool('Snow_Skimmer_', 'High-End', Snow_Skimmer__TWO_x_Bonus_Points, Snow_Skimmer__ONEoFIVE_x_Bonus_Points, Snow_Skimmer__lv3_courses, Snow_Skimmer__lv6_courses)


#Bright_Bunny_
# https://game8.co/games/mariokarttour/archives/285893

Bright_Bunny__TWO_x_Bonus_Points = ['Yoshi Circuit T', 'Yoshi Circuit', 'Choco Island 2T', 'Waluigi Pinball', 'Waluigi Pinball T', 'SNES Rainbow Road R/T', 'London Loop', 'London Loop R/T', 'Yoshi Circuit R/T', "Luigi's Mansion R/T", 'Vanilla Lake 1', 'Paris Promenade 2R', 'Paris Promenade 2', 'DS Rainbow Road R/T']

Bright_Bunny__ONEoFIVE_x_Bonus_Points = ['Koopa Troopa Beach T', 'Koopa Troopa Beach', 'Daisy Hills', 'Choco Island 2', 'Waluigi Pinball R', 'Mario Circuit R/T', 'Daisy Hills R/T', 'London Loop R', 'DS Rainbow Road', 'DS Rainbow Road', 'Toad Circuit R/T', 'Vanilla Lake 1R', 'Shy Guy Bazaar R/T', 'Paris Promenade 2T', 'Donut Plains 1R/T']

Bright_Bunny__lv3_courses = ['Choco Island 2', 'Waluigi Pinball R']

Bright_Bunny__lv6_courses = ['Koopa Troopa Beach', 'Vanilla Lake 1R']

Bright_Bunny_ = race_tool('Bright_Bunny_', 'High-End', Bright_Bunny__TWO_x_Bonus_Points, Bright_Bunny__ONEoFIVE_x_Bonus_Points, Bright_Bunny__lv3_courses, Bright_Bunny__lv6_courses)


#Dozer_Dasher_
# https://game8.co/games/mariokarttour/archives/286544

Dozer_Dasher__TWO_x_Bonus_Points = ['Rock Rock Mountain T', 'Mario Circuit 1T', 'Daisy Hills T', "Bowser's Castle 1T", 'Cheep Cheep Lagoon', 'Kalimari Desert T', 'Mario Circuit R/T', 'Choco Island 2R/T', 'RMX Mario Circuit 1T', "Bowser's Castle 2T", 'Choco Mountain T']

Dozer_Dasher__ONEoFIVE_x_Bonus_Points = ['Cheep Cheep Lagoon T', 'Toad Circuit T', 'Waluigi Pinball T', 'Daisy Hills R/T', 'Kalimari Desert R/T', 'Koopa Troopa Beach R/T', "Bowser's Castle 2", 'Donut Plains 1R/T', 'Vanilla Lake 1R/T', 'RMX Choco Island 1T', 'RMX Rainbow Road 1R/T', 'Merry Mountain T']

Dozer_Dasher__lv3_courses = ['Kalimari Desert R/T', 'Vanilla Lake 1R/T']

Dozer_Dasher__lv6_courses = ['Cheep Cheep Lagoon T', 'Donut Plains 1R/T']

Dozer_Dasher_ = race_tool('Dozer_Dasher_', 'High-End', Dozer_Dasher__TWO_x_Bonus_Points, Dozer_Dasher__ONEoFIVE_x_Bonus_Points, Dozer_Dasher__lv3_courses, Dozer_Dasher__lv6_courses)


#Clanky_Kart_
# https://game8.co/games/mariokarttour/archives/286545

Clanky_Kart__TWO_x_Bonus_Points = ['Mario Circuit 1T', 'Toad Circuit T', 'Waluigi Pinball T', 'Toad Circuit R/T', 'Dino Dino Jungle R/T', 'Ghost Valley 1R/T', 'Koopa Troopa Beach 2T', 'Choco Mountain', 'Sunset Wilds T', 'RMX Rainbow Road 1R/T', 'Merry Mountain T']

Clanky_Kart__ONEoFIVE_x_Bonus_Points = ['Daisy Hills T', 'Daisy Hills R/T', 'DS Rainbow Road T', 'Kalimari Desert R/T', 'Shy Guy Bazaar R/T', 'RMX Choco Island 1T', 'Koopa Troopa Beach 2R', 'Choco Mountain T', 'Airship Fortress R', 'Airship Fortress T', 'Sunset Wilds', 'Sunset Wilds R']

Clanky_Kart__lv3_courses = ['Daisy Hills R/T', 'Shy Guy Bazaar R/T']

Clanky_Kart__lv6_courses = ['Koopa Troopa Beach 2R', 'Airship Fortress T']

Clanky_Kart_ = race_tool('Clanky_Kart_', 'High-End', Clanky_Kart__TWO_x_Bonus_Points, Clanky_Kart__ONEoFIVE_x_Bonus_Points, Clanky_Kart__lv3_courses, Clanky_Kart__lv6_courses)


#Wild_Black_
# https://game8.co/games/mariokarttour/archives/286546

Wild_Black__TWO_x_Bonus_Points = ["Bowser's Castle 1", "Luigi's Mansion T", 'Ghost Valley 1', 'Ghost Valley 1', 'Ghost Valley 1T', 'Ghost Valley 1T', 'Daisy Hills R/T', "Bowser's Castle 1R/T", 'Tokyo Blur 2', 'Neo Bowser City R/T', 'Waluigi Pinball R/T', "Bowser's Castle 2", "Bowser's Castle 2R", "Bowser's Castle 2R/T", 'RMX Choco Island 1', 'Tokyo Blur 3', 'Berlin Byways 2', 'Berlin Byways 2R/T', 'DK Summit R']

Wild_Black__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar R', 'Shy Guy Bazaar', "Bowser's Castle 1R", 'Tokyo Blur R', 'Neo Bowser City', 'Waluigi Pinball R', 'Ghost Valley 1R', 'Mario Circuit R/T', "Luigi's Mansion R/T", 'Mario Circuit 2R/T', 'Toad Circuit R/T', 'Shy Guy Bazaar R/T', 'Ghost Valley 1R/T', "Bowser's Castle 2T", 'RMX Choco Island 1T', 'Airship Fortress', 'Tokyo Blur 3R', 'Berlin Byways 2R']

Wild_Black__lv3_courses = ["Bowser's Castle 1R", 'Mario Circuit R/T']

Wild_Black__lv6_courses = ['Shy Guy Bazaar R', 'Shy Guy Bazaar']

Wild_Black_ = race_tool('Wild_Black_', 'High-End', Wild_Black__TWO_x_Bonus_Points, Wild_Black__ONEoFIVE_x_Bonus_Points, Wild_Black__lv3_courses, Wild_Black__lv6_courses)


#Karp_Kart_
# https://game8.co/games/mariokarttour/archives/286547

Karp_Kart__TWO_x_Bonus_Points = ['Cheep Cheep Lagoon R/T', 'Mario Circuit 1R/T', 'Vanilla Lake 1', 'Vanilla Lake 1R', 'Vanilla Lake 1T', 'Frappe Snowland R/T', 'Vanilla Lake 1R/T', 'Royal Raceway', 'Airship Fortress T']

Karp_Kart__ONEoFIVE_x_Bonus_Points = ['SNES Rainbow Road R/T', 'Mario Circuit R/T', 'Shy Guy Bazaar R/T', 'Koopa Troopa Beach R/T', 'Mario Circuit 3R/T', 'Royal Raceway R', 'Royal Raceway T', 'Kalimari Desert 2', 'Kalimari Desert 2T', 'Airship Fortress']

Karp_Kart__lv3_courses = ['Shy Guy Bazaar R/T', 'Royal Raceway R']

Karp_Kart__lv6_courses = ['Kalimari Desert 2T', 'Airship Fortress']

Karp_Kart_ = race_tool('Karp_Kart_', 'High-End', Karp_Kart__TWO_x_Bonus_Points, Karp_Kart__ONEoFIVE_x_Bonus_Points, Karp_Kart__lv3_courses, Karp_Kart__lv6_courses)


#Prancer_
# https://game8.co/games/mariokarttour/archives/286866

Prancer__TWO_x_Bonus_Points = ['Yoshi Circuit R', 'Daisy Hills R', 'SNES Rainbow Road', 'Mario Circuit 2T', 'Mario Circuit 2R', 'Choco Island 2', 'London Loop', 'London Loop R/T', 'London Loop T', 'Shy Guy Bazaar R/T', 'Koopa Troopa Beach R/T', 'RMX Choco Island 1', 'Tokyo Blur 3', 'Tokyo Blur 3R', 'Sunset Wilds']

Prancer__ONEoFIVE_x_Bonus_Points = ['Daisy Hills', 'Mario Circuit 2', 'Choco Island 2R', 'SNES Rainbow Road T', 'Choco Island 2T', "Luigi's Mansion R", "Luigi's Mansion T", 'Paris Promenade T', 'Kalimari Desert R/T', 'RMX Choco Island 1R', 'RMX Choco Island 1T', 'Kalimari Desert 2', 'Kalimari Desert 2T', 'Sunset Wilds R', 'RMX Choco Island 2R', 'RMX Choco Island 2T']

Prancer__lv3_courses = ["Luigi's Mansion R", 'Kalimari Desert R/T']

Prancer__lv6_courses = ["Luigi's Mansion T", 'Kalimari Desert 2T']

Prancer_ = race_tool('Prancer_', 'High-End', Prancer__TWO_x_Bonus_Points, Prancer__ONEoFIVE_x_Bonus_Points, Prancer__lv3_courses, Prancer__lv6_courses)


#Rose_Queen_
# https://game8.co/games/mariokarttour/archives/286867

Rose_Queen__TWO_x_Bonus_Points = ['Shy Guy Bazaar R', 'Shy Guy Bazaar', 'Toad Circuit R', 'Mario Circuit R', 'SNES Rainbow Road R', 'Waluigi Pinball R', 'DS Rainbow Road T', 'Mario Circuit 1R/T', 'Vanilla Lake 1R', 'Mario Circuit 3R/T', 'Royal Raceway R', 'Airship Fortress', 'Airship Fortress R', 'RMX Rainbow Road 1T']

Rose_Queen__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 1T', 'Daisy Hills R', 'Mario Circuit T', 'Waluigi Pinball T', 'DS Rainbow Road R', 'Vanilla Lake 1T', 'Royal Raceway T', 'RMX Rainbow Road 1', 'Berlin Byways 2', 'Berlin Byways 2R']

Rose_Queen__lv3_courses = ['Mario Circuit 1T', 'Mario Circuit T']

Rose_Queen__lv6_courses = ['Vanilla Lake 1T', 'RMX Rainbow Road 1']

Rose_Queen_ = race_tool('Rose_Queen_', 'High-End', Rose_Queen__TWO_x_Bonus_Points, Rose_Queen__ONEoFIVE_x_Bonus_Points, Rose_Queen__lv3_courses, Rose_Queen__lv6_courses)


#Green_Apple_Kart_
# https://game8.co/games/mariokarttour/archives/286868

Green_Apple_Kart__TWO_x_Bonus_Points = ['Rock Rock Mountain', 'Yoshi Circuit', 'Shy Guy Bazaar T', 'Daisy Hills', 'Choco Island 2R/T', 'Shy Guy Bazaar R/T', 'Koopa Troopa Beach R/T', 'Donut Plains 1', 'Donut Plains 1R', 'RMX Choco Island 1T', 'Choco Island 1']

Green_Apple_Kart__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain T', 'Rock Rock Mountain R', 'Yoshi Circuit T', 'Yoshi Circuit R', 'Daisy Hills T', 'Mario Circuit R', "Luigi's Mansion T", 'Cheep Cheep Lagoon R/T', 'RMX Choco Island 1', 'RMX Choco Island 1R', 'Choco Mountain', 'RMX Rainbow Road 2', 'RMX Rainbow Road 2R']

Green_Apple_Kart__lv3_courses = ['Daisy Hills T', 'Mario Circuit R']

Green_Apple_Kart__lv6_courses = ["Luigi's Mansion T", 'RMX Choco Island 1R']

Green_Apple_Kart_ = race_tool('Green_Apple_Kart_', 'High-End', Green_Apple_Kart__TWO_x_Bonus_Points, Green_Apple_Kart__ONEoFIVE_x_Bonus_Points, Green_Apple_Kart__lv3_courses, Green_Apple_Kart__lv6_courses)


#Offroader_
# https://game8.co/games/mariokarttour/archives/288933

Offroader__TWO_x_Bonus_Points = ['Rock Rock Mountain', 'Dino Dino Jungle R', 'Toad Circuit R', 'Kalimari Desert T', 'Kalimari Desert', 'Neo Bowser City R/T', 'Neo Bowser City R/T', 'Toad Circuit R/T', 'Frappe Snowland R', 'Koopa Troopa Beach R/T', 'Koopa Troopa Beach R/T', "Bowser's Castle 2", "Bowser's Castle 2T", 'Koopa Troopa Beach 2', 'Airship Fortress T', 'Los Angeles Laps R/T', 'Sunset Wilds', 'Sunset Wilds R']

Offroader__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain T', 'Dino Dino Jungle T', 'Dino Dino Jungle', 'Toad Circuit T', 'Kalimari Desert R', 'Cheep Cheep Lagoon R/T', 'Frappe Snowland T', 'Choco Island 2R/T', "Bowser's Castle 2R", 'RMX Choco Island 1', 'RMX Choco Island 1R', 'RMX Choco Island 1T', 'Choco Island 1', 'Choco Island 1R', 'Koopa Troopa Beach 2R', 'Koopa Troopa Beach 2T', 'Airship Fortress', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 1T', 'Los Angeles Laps', 'Los Angeles Laps R', 'Sunset Wilds T', 'Donut Plains 2', 'Donut Plains 2T']

Offroader__lv3_courses = ['Rock Rock Mountain T', 'Dino Dino Jungle T']

Offroader__lv6_courses = ['RMX Choco Island 1', 'Choco Island 1']

Offroader_ = race_tool('Offroader_', 'High-End', Offroader__TWO_x_Bonus_Points, Offroader__ONEoFIVE_x_Bonus_Points, Offroader__lv3_courses, Offroader__lv6_courses)


#Banana_Master_
# https://game8.co/games/mariokarttour/archives/288934

Banana_Master__TWO_x_Bonus_Points = ['Cheep Cheep Lagoon T', 'Dino Dino Jungle T', 'Dino Dino Jungle R', 'Daisy Hills R', 'Vanilla Lake 1T', 'Choco Island 2R/T', 'RMX Choco Island 1R', 'RMX Choco Island 1T', 'Choco Island 1R', 'Airship Fortress T', 'Los Angeles Laps T', 'Sunset Wilds R/T']

Banana_Master__ONEoFIVE_x_Bonus_Points = ['Cheep Cheep Lagoon R', 'Dino Dino Jungle', 'Cheep Cheep Lagoon', 'Mario Circuit R', 'Mario Circuit 1R/T', 'Vanilla Lake 1', "Bowser's Castle 2", "Bowser's Castle 2R", 'Choco Island 1', 'Choco Island 1T', 'Los Angeles Laps', 'Los Angeles Laps R/T']

Banana_Master__lv3_courses = ['Cheep Cheep Lagoon R', "Bowser's Castle 2R"]

Banana_Master__lv6_courses = ['Cheep Cheep Lagoon', 'Vanilla Lake 1']

Banana_Master_ = race_tool('Banana_Master_', 'High-End', Banana_Master__TWO_x_Bonus_Points, Banana_Master__ONEoFIVE_x_Bonus_Points, Banana_Master__lv3_courses, Banana_Master__lv6_courses)


#Choco_Macharon_
# https://game8.co/games/mariokarttour/archives/289730

Choco_Macharon__TWO_x_Bonus_Points = ['Koopa Troopa Beach R', 'Choco Island 2R', 'Choco Island 2', 'Ghost Valley 1T', 'Frappe Snowland T', 'RMX Choco Island 1', 'RMX Choco Island 1T', 'RMX Choco Island 1T', 'Choco Island 1', 'Choco Island 1R', 'Kalimari Desert 2R', 'Sunset Wilds R/T', 'Donut Plains 2']

Choco_Macharon__ONEoFIVE_x_Bonus_Points = ['Koopa Troopa Beach T', 'Koopa Troopa Beach', 'Kalimari Desert', 'Choco Island 2T', 'Ghost Valley 1', 'Kalimari Desert 2T', 'RMX Rainbow Road 2', 'RMX Rainbow Road 2R', 'Donut Plains 2R']

Choco_Macharon__lv3_courses = ['Koopa Troopa Beach T', 'Ghost Valley 1']

Choco_Macharon__lv6_courses = ['Kalimari Desert', 'Kalimari Desert 2T']

Choco_Macharon_ = race_tool('Choco_Macharon_', 'High-End', Choco_Macharon__TWO_x_Bonus_Points, Choco_Macharon__ONEoFIVE_x_Bonus_Points, Choco_Macharon__lv3_courses, Choco_Macharon__lv6_courses)


#Gold_Egg_
# https://game8.co/games/mariokarttour/archives/289731

Gold_Egg__TWO_x_Bonus_Points = ['Yoshi Circuit T', 'Yoshi Circuit', 'Cheep Cheep Lagoon R', 'Tokyo Blur', 'Choco Island 2T', 'Tokyo Blur R/T', 'SNES Rainbow Road R/T', 'DS Rainbow Road', 'RMX Mario Circuit 1', 'Choco Island 1T', 'Choco Mountain R', 'Choco Mountain R', 'Tokyo Blur 3', 'New York Minute 3', 'RMX Rainbow Road 2R', 'RMX Rainbow Road 2T']

Gold_Egg__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit R', 'Cheep Cheep Lagoon T', 'Cheep Cheep Lagoon', 'Neo Bowser City R', 'DS Rainbow Road R', 'Tokyo Blur 2', 'Choco Island 1', 'Royal Raceway', 'Choco Mountain', 'Choco Mountain T', 'New York Minute 3R', 'RMX Rainbow Road 1R/T', 'RMX Rainbow Road 2']

Gold_Egg__lv3_courses = ['Yoshi Circuit R', 'DS Rainbow Road R']

Gold_Egg__lv6_courses = ['Neo Bowser City R', 'Royal Raceway']

Gold_Egg_ = race_tool('Gold_Egg_', 'High-End', Gold_Egg__TWO_x_Bonus_Points, Gold_Egg__ONEoFIVE_x_Bonus_Points, Gold_Egg__lv3_courses, Gold_Egg__lv6_courses)


#Poison_Apple_Kart_
# https://game8.co/games/mariokarttour/archives/289732

Poison_Apple_Kart__TWO_x_Bonus_Points = ['Kalimari Desert R', "Luigi's Mansion", 'Waluigi Pinball R', 'Ghost Valley 1', 'Ghost Valley 1T', 'Frappe Snowland T', 'Frappe Snowland R', 'Waluigi Pinball R/T', 'Ghost Valley 1R/T', 'Donut Plains 1', 'Choco Mountain', 'Choco Mountain R']

Poison_Apple_Kart__ONEoFIVE_x_Bonus_Points = ['Kalimari Desert T', 'Waluigi Pinball', 'Waluigi Pinball T', 'Ghost Valley 1R', 'Donut Plains 1R', 'Choco Island 1', 'Choco Island 1R', 'Choco Island 1T', "Rosalina's Ice World R", 'Donut Plains 2']

Poison_Apple_Kart__lv3_courses = ['Waluigi Pinball T', 'Donut Plains 1R']

Poison_Apple_Kart__lv6_courses = ['Choco Island 1', 'Choco Island 1T']

Poison_Apple_Kart_ = race_tool('Poison_Apple_Kart_', 'High-End', Poison_Apple_Kart__TWO_x_Bonus_Points, Poison_Apple_Kart__ONEoFIVE_x_Bonus_Points, Poison_Apple_Kart__lv3_courses, Poison_Apple_Kart__lv6_courses)


#Sweet_Daytripper_
# https://game8.co/games/mariokarttour/archives/290564

Sweet_Daytripper__TWO_x_Bonus_Points = ['Shy Guy Bazaar T', 'Koopa Troopa Beach T', 'Koopa Troopa Beach', 'SNES Rainbow Road', 'Mario Circuit R/T', "Luigi's Mansion R/T", "Bowser's Castle 2", 'RMX Choco Island 1', 'RMX Choco Island 1T', 'Choco Island 1T', 'Royal Raceway', 'RMX Choco Island 2']

Sweet_Daytripper__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar R', 'Shy Guy Bazaar', "Bowser's Castle 1T", "Bowser's Castle 1R", 'SNES Rainbow Road R', 'Toad Circuit R/T', 'Frappe Snowland R/T', "Bowser's Castle 2T", 'Royal Raceway T', 'Maple Treeway R', 'Sunset Wilds', 'Sunset Wilds T']

Sweet_Daytripper__lv3_courses = ["Bowser's Castle 1R", 'SNES Rainbow Road R']

Sweet_Daytripper__lv6_courses = ['Shy Guy Bazaar', "Bowser's Castle 1T"]

Sweet_Daytripper_ = race_tool('Sweet_Daytripper_', 'High-End', Sweet_Daytripper__TWO_x_Bonus_Points, Sweet_Daytripper__ONEoFIVE_x_Bonus_Points, Sweet_Daytripper__lv3_courses, Sweet_Daytripper__lv6_courses)


#Happy_Ride_
# https://game8.co/games/mariokarttour/archives/290565

Happy_Ride__TWO_x_Bonus_Points = ['Koopa Troopa Beach T', 'Koopa Troopa Beach R', 'Koopa Troopa Beach', 'Toad Circuit T', 'Toad Circuit', 'Mario Circuit', 'SNES Rainbow Road T', 'SNES Rainbow Road R', 'Mario Circuit R/T', 'Mario Circuit 1R/T', 'Paris Promenade 2', 'Donut Plains 1', 'Royal Raceway R', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 1T', 'RMX Choco Island 2T']

Happy_Ride__ONEoFIVE_x_Bonus_Points = ['Daisy Hills R', 'Toad Circuit R', 'SNES Rainbow Road', 'Mario Circuit 2T', 'Mario Circuit 2R', 'Mario Circuit T', 'Donut Plains 1R', 'Royal Raceway', 'RMX Rainbow Road 1']

Happy_Ride__lv3_courses = ['SNES Rainbow Road', 'Mario Circuit 2R']

Happy_Ride__lv6_courses = ['Mario Circuit 2T', 'Royal Raceway']

Happy_Ride_ = race_tool('Happy_Ride_', 'High-End', Happy_Ride__TWO_x_Bonus_Points, Happy_Ride__ONEoFIVE_x_Bonus_Points, Happy_Ride__lv3_courses, Happy_Ride__lv6_courses)


#Pink_Wing_
# https://game8.co/games/mariokarttour/archives/290566

Pink_Wing__TWO_x_Bonus_Points = ['Shy Guy Bazaar T', 'Shy Guy Bazaar', 'Mario Circuit', 'Mario Circuit T', 'Tokyo Blur R/T', 'Mario Circuit 3', 'Tokyo Blur 2', 'Tokyo Blur 2T', 'Paris Promenade 2', 'Mario Circuit 3R/T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1R', 'RMX Mario Circuit 1T', 'Royal Raceway T', 'Tokyo Blur 3', 'Los Angeles Laps T', 'Los Angeles Laps']

Pink_Wing__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit', 'Shy Guy Bazaar R', 'SNES Rainbow Road', 'SNES Rainbow Road R', 'Mario Circuit 3T', 'Mario Circuit 3R', 'Mario Circuit R/T', 'Tokyo Blur 2R', 'Paris Promenade 2R', 'Paris Promenade 2T', 'Royal Raceway R', 'Royal Raceway', 'Tokyo Blur 3T', 'Los Angeles Laps R', 'RMX Rainbow Road 2R', 'DK Summit']

Pink_Wing__lv3_courses = ['SNES Rainbow Road R', 'Mario Circuit R/T']

Pink_Wing__lv6_courses = ['Yoshi Circuit', 'Mario Circuit 3T']

Pink_Wing_ = race_tool('Pink_Wing_', 'High-End', Pink_Wing__TWO_x_Bonus_Points, Pink_Wing__ONEoFIVE_x_Bonus_Points, Pink_Wing__lv3_courses, Pink_Wing__lv6_courses)


#Red_Taxi_
# https://game8.co/games/mariokarttour/archives/290567

Red_Taxi__TWO_x_Bonus_Points = ['Koopa Troopa Beach T', 'Kalimari Desert', 'Choco Island 1', 'Choco Island 1T', 'Royal Raceway T', 'Koopa Troopa Beach 2', 'Kalimari Desert 2', 'Los Angeles Laps R/T', 'Sunset Wilds R/T']

Red_Taxi__ONEoFIVE_x_Bonus_Points = ['Koopa Troopa Beach R', 'Koopa Troopa Beach', 'Kalimari Desert T', 'Neo Bowser City R', 'Neo Bowser City T', 'Shy Guy Bazaar R/T', 'Royal Raceway R', 'Royal Raceway', 'Koopa Troopa Beach 2R', 'Koopa Troopa Beach 2T', 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'RMX Rainbow Road 1R/T']

Red_Taxi__lv3_courses = ['Kalimari Desert T', 'Koopa Troopa Beach 2T']

Red_Taxi__lv6_courses = ['Royal Raceway R', 'Kalimari Desert 2R']

Red_Taxi_ = race_tool('Red_Taxi_', 'High-End', Red_Taxi__TWO_x_Bonus_Points, Red_Taxi__ONEoFIVE_x_Bonus_Points, Red_Taxi__lv3_courses, Red_Taxi__lv6_courses)


#Blue_Soda_
# https://game8.co/games/mariokarttour/archives/291192

Blue_Soda__TWO_x_Bonus_Points = ['Koopa Troopa Beach', 'Mario Circuit 2R', 'Mario Circuit 2', 'Mario Circuit 1R/T', 'Frappe Snowland', 'Paris Promenade 2R', 'Vancouver Velocity T', 'Vancouver Velocity R', 'Koopa Troopa Beach R/T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1R', 'Royal Raceway T', 'Royal Raceway', 'Koopa Troopa Beach 2', 'Los Angeles Laps R/T', 'Los Angeles Laps R', "Rosalina's Ice World T", 'Donut Plains 2R']

Blue_Soda__ONEoFIVE_x_Bonus_Points = ['Koopa Troopa Beach R', 'Mario Circuit 2T', 'DS Rainbow Road R', 'Cheep Cheep Lagoon R/T', 'Frappe Snowland R', 'Paris Promenade 2', 'Vancouver Velocity', 'RMX Mario Circuit 1T', 'Koopa Troopa Beach 2R', 'Koopa Troopa Beach 2T', 'Los Angeles Laps T', "Rosalina's Ice World", 'Donut Plains 2']

Blue_Soda__lv3_courses = ['Mario Circuit 2T', 'Cheep Cheep Lagoon R/T']

Blue_Soda__lv6_courses = ['DS Rainbow Road R', 'Koopa Troopa Beach 2T']

Blue_Soda_ = race_tool('Blue_Soda_', 'High-End', Blue_Soda__TWO_x_Bonus_Points, Blue_Soda__ONEoFIVE_x_Bonus_Points, Blue_Soda__lv3_courses, Blue_Soda__lv6_courses)


#Gold_Cheep_Charger_
# https://game8.co/games/mariokarttour/archives/291193

Gold_Cheep_Charger__TWO_x_Bonus_Points = ['Cheep Cheep Lagoon T', 'Koopa Troopa Beach T', 'Cheep Cheep Lagoon', 'SNES Rainbow Road R', 'SNES Rainbow Road R', 'Paris Promenade T', 'Paris Promenade R/T', 'Paris Promenade R', 'SNES Rainbow Road R/T', 'DS Rainbow Road T', 'Vanilla Lake 1R', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1', 'Koopa Troopa Beach 2T', 'Tokyo Blur 3R', 'Tokyo Blur 3T', 'RMX Rainbow Road 1', 'New York Minute 3T', 'RMX Rainbow Road 2T']

Gold_Cheep_Charger__ONEoFIVE_x_Bonus_Points = ['Cheep Cheep Lagoon R', 'Koopa Troopa Beach R', 'SNES Rainbow Road T', 'Mario Circuit 3T', 'Paris Promenade', 'Mario Circuit 3R', 'Mario Circuit R/T', 'DS Rainbow Road', 'Vanilla Lake 1', 'RMX Mario Circuit 1R', 'RMX Choco Island 1R', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', 'RMX Rainbow Road 1T', 'New York Minute 3R', 'New York Minute 3R/T']

Gold_Cheep_Charger__lv3_courses = ['Koopa Troopa Beach R', 'Koopa Troopa Beach 2R']

Gold_Cheep_Charger__lv6_courses = ['Mario Circuit 3T', 'DS Rainbow Road']

Gold_Cheep_Charger_ = race_tool('Gold_Cheep_Charger_', 'High-End', Gold_Cheep_Charger__TWO_x_Bonus_Points, Gold_Cheep_Charger__ONEoFIVE_x_Bonus_Points, Gold_Cheep_Charger__lv3_courses, Gold_Cheep_Charger__lv6_courses)


#Gold_Cheep_Snorkel_
# https://game8.co/games/mariokarttour/archives/291194

Gold_Cheep_Snorkel__TWO_x_Bonus_Points = ['Cheep Cheep Lagoon R', 'Paris Promenade', 'Paris Promenade R/T', 'DS Rainbow Road', 'DS Rainbow Road R', 'Cheep Cheep Lagoon R/T', 'Donut Plains 1T', 'Koopa Troopa Beach 2R', 'Choco Mountain R', 'Airship Fortress R', 'Los Angeles Laps T']

Gold_Cheep_Snorkel__ONEoFIVE_x_Bonus_Points = ['Cheep Cheep Lagoon T', 'Tokyo Blur R/T', 'Ghost Valley 1', 'Ghost Valley 1R', 'Paris Promenade T', 'Paris Promenade R', 'DS Rainbow Road T', 'Donut Plains 1', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2T', 'Choco Mountain', 'Choco Mountain T', 'Airship Fortress', 'Airship Fortress T', 'Los Angeles Laps', 'Los Angeles Laps R/T', 'Los Angeles Laps R', 'Sunset Wilds', 'Sunset Wilds R', 'DK Summit R']

Gold_Cheep_Snorkel__lv3_courses = ['Cheep Cheep Lagoon T', 'DS Rainbow Road T']

Gold_Cheep_Snorkel__lv6_courses = ['Donut Plains 1', 'Choco Mountain']

Gold_Cheep_Snorkel_ = race_tool('Gold_Cheep_Snorkel_', 'High-End', Gold_Cheep_Snorkel__TWO_x_Bonus_Points, Gold_Cheep_Snorkel__ONEoFIVE_x_Bonus_Points, Gold_Cheep_Snorkel__lv3_courses, Gold_Cheep_Snorkel__lv6_courses)


#Cheep_Snorkel_
# https://game8.co/games/mariokarttour/archives/291195

Cheep_Snorkel__TWO_x_Bonus_Points = ['Cheep Cheep Lagoon T', 'Dino Dino Jungle T', 'Dino Dino Jungle', 'Cheep Cheep Lagoon', 'Cheep Cheep Lagoon R/T', 'Koopa Troopa Beach R/T', 'RMX Mario Circuit 1T', 'Vanilla Lake 1R/T', 'Koopa Troopa Beach 2R', 'Koopa Troopa Beach 2T', 'Airship Fortress', 'Airship Fortress R', 'Los Angeles Laps', 'RMX Choco Island 2T']

Cheep_Snorkel__ONEoFIVE_x_Bonus_Points = ['Cheep Cheep Lagoon R', 'Dino Dino Jungle R', 'Yoshi Circuit R/T', 'Choco Island 1T', 'Koopa Troopa Beach 2', 'Airship Fortress T', 'Los Angeles Laps R/T']

Cheep_Snorkel__lv3_courses = ['Dino Dino Jungle R', 'Yoshi Circuit R/T']

Cheep_Snorkel__lv6_courses = ['Koopa Troopa Beach 2', 'Airship Fortress T']

Cheep_Snorkel_ = race_tool('Cheep_Snorkel_', 'High-End', Cheep_Snorkel__TWO_x_Bonus_Points, Cheep_Snorkel__ONEoFIVE_x_Bonus_Points, Cheep_Snorkel__lv3_courses, Cheep_Snorkel__lv6_courses)


#Clackety_Kart_
# https://game8.co/games/mariokarttour/archives/291843

Clackety_Kart__TWO_x_Bonus_Points = ['Rock Rock Mountain T', 'Rock Rock Mountain R', 'Frappe Snowland R/T', 'Choco Island 1T', 'Royal Raceway', 'Choco Mountain R', 'Choco Mountain T']

Clackety_Kart__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain', 'Rock Rock Mountain', 'Mario Circuit 1R', 'Koopa Troopa Beach', 'Choco Island 2T', 'Ghost Valley 1R/T', 'Choco Island 1R', 'Royal Raceway T', 'Choco Mountain', 'Maple Treeway', 'Sunset Wilds', 'Sunset Wilds T']

Clackety_Kart__lv3_courses = ['Rock Rock Mountain', 'Choco Island 1R']

Clackety_Kart__lv6_courses = ['Ghost Valley 1R/T', 'Royal Raceway T']

Clackety_Kart_ = race_tool('Clackety_Kart_', 'High-End', Clackety_Kart__TWO_x_Bonus_Points, Clackety_Kart__ONEoFIVE_x_Bonus_Points, Clackety_Kart__lv3_courses, Clackety_Kart__lv6_courses)


#Gold_Clanky_Kart_
# https://game8.co/games/mariokarttour/archives/291844

Gold_Clanky_Kart__TWO_x_Bonus_Points = ['Rock Rock Mountain T', 'Rock Rock Mountain', 'Mario Circuit 3R', 'SNES Rainbow Road R/T', 'DS Rainbow Road', 'DS Rainbow Road R', 'Kalimari Desert R/T', 'Frappe Snowland T', 'Vancouver Velocity', 'Vancouver Velocity R/T', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', "Rosalina's Ice World R"]

Gold_Clanky_Kart__ONEoFIVE_x_Bonus_Points = ['Kalimari Desert R', 'DK Pass', 'DK Pass R', 'Mario Circuit 1R/T', 'Frappe Snowland R', 'Vancouver Velocity T', 'Vancouver Velocity R', 'Choco Mountain', 'Choco Mountain R', 'Choco Mountain T', 'New York Minute 3', 'New York Minute 3R/T', 'Sunset Wilds T', 'Merry Mountain', 'Merry Mountain R']

Gold_Clanky_Kart__lv3_courses = ['Frappe Snowland R', 'Choco Mountain T']

Gold_Clanky_Kart__lv6_courses = ['Kalimari Desert R', 'Choco Mountain']

Gold_Clanky_Kart_ = race_tool('Gold_Clanky_Kart_', 'High-End', Gold_Clanky_Kart__TWO_x_Bonus_Points, Gold_Clanky_Kart__ONEoFIVE_x_Bonus_Points, Gold_Clanky_Kart__lv3_courses, Gold_Clanky_Kart__lv6_courses)


#Dark_Buggy_
# https://game8.co/games/mariokarttour/archives/291845

Dark_Buggy__TWO_x_Bonus_Points = ['Dino Dino Jungle', "Luigi's Mansion T", 'Waluigi Pinball', 'Paris Promenade 2T', 'Koopa Troopa Beach 2T', 'Choco Mountain', 'Choco Mountain R', 'Kalimari Desert 2T', 'Airship Fortress R', 'Airship Fortress T', 'Sunset Wilds R/T', 'Merry Mountain R', "Rosalina's Ice World T"]

Dark_Buggy__ONEoFIVE_x_Bonus_Points = ['Dino Dino Jungle T', 'Dino Dino Jungle R', "Bowser's Castle 1T", "Bowser's Castle 1", "Luigi's Mansion", 'Waluigi Pinball R', 'Waluigi Pinball T', 'Dino Dino Jungle R/T', 'Dino Dino Jungle R/T', 'Choco Mountain T', 'Kalimari Desert 2R', 'Airship Fortress', 'Merry Mountain', "Rosalina's Ice World", 'Donut Plains 2', 'Donut Plains 2R', 'Donut Plains 2T', 'DK Summit']

Dark_Buggy__lv3_courses = ['Dino Dino Jungle T', "Bowser's Castle 1T"]

Dark_Buggy__lv6_courses = ["Luigi's Mansion", 'Airship Fortress']

Dark_Buggy_ = race_tool('Dark_Buggy_', 'High-End', Dark_Buggy__TWO_x_Bonus_Points, Dark_Buggy__ONEoFIVE_x_Bonus_Points, Dark_Buggy__lv3_courses, Dark_Buggy__lv6_courses)


#Koopa_King_
# https://game8.co/games/mariokarttour/archives/291846

Koopa_King__TWO_x_Bonus_Points = ['Dino Dino Jungle T', "Bowser's Castle 1R", 'Waluigi Pinball T', 'Dino Dino Jungle R/T', 'Frappe Snowland R/T', "Bowser's Castle 2T", 'Royal Raceway T', 'Royal Raceway', 'Choco Mountain T', 'Kalimari Desert 2R', 'Airship Fortress', 'DK Summit']

Koopa_King__ONEoFIVE_x_Bonus_Points = ["Bowser's Castle 1T", 'Waluigi Pinball R', "Bowser's Castle 2R", 'Royal Raceway R', 'Choco Mountain', 'Choco Mountain R', 'Kalimari Desert 2', 'Airship Fortress T']

Koopa_King__lv3_courses = ["Bowser's Castle 2R", 'Choco Mountain R']

Koopa_King__lv6_courses = ['Choco Mountain', 'Airship Fortress T']

Koopa_King_ = race_tool('Koopa_King_', 'High-End', Koopa_King__TWO_x_Bonus_Points, Koopa_King__ONEoFIVE_x_Bonus_Points, Koopa_King__lv3_courses, Koopa_King__lv6_courses)


#Brown_Offroader_
# https://game8.co/games/mariokarttour/archives/292310

Brown_Offroader__TWO_x_Bonus_Points = ['Choco Island 2', 'Choco Island 2T', 'Kalimari Desert R/T', 'Donut Plains 1R', 'Donut Plains 1R/T', 'Choco Island 1', 'Choco Island 1T', 'Kalimari Desert 2', 'Kalimari Desert 2T', 'Airship Fortress T', "Rosalina's Ice World T", 'DK Summit T']

Brown_Offroader__ONEoFIVE_x_Bonus_Points = ['Choco Island 2R', 'Vanilla Lake 1', 'Vanilla Lake 1R', 'Donut Plains 1', 'Donut Plains 1T', 'Kalimari Desert 2R', 'Airship Fortress R', 'RMX Rainbow Road 1R', "Rosalina's Ice World"]

Brown_Offroader__lv3_courses = ['Choco Island 2R', 'Vanilla Lake 1']

Brown_Offroader__lv6_courses = ['Donut Plains 1', 'Airship Fortress R']

Brown_Offroader_ = race_tool('Brown_Offroader_', 'High-End', Brown_Offroader__TWO_x_Bonus_Points, Brown_Offroader__ONEoFIVE_x_Bonus_Points, Brown_Offroader__lv3_courses, Brown_Offroader__lv6_courses)


#Cact_X
# https://game8.co/games/mariokarttour/archives/292311

Cact_X_TWO_x_Bonus_Points = ['Rock Rock Mountain R', 'Koopa Troopa Beach', 'Ghost Valley 1R', 'Ghost Valley 1T', 'Kalimari Desert R/T', 'Donut Plains 1', 'Choco Island 1T', 'Koopa Troopa Beach 2R', 'Koopa Troopa Beach 2T', 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'Los Angeles Laps']

Cact_X_ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain R', 'Koopa Troopa Beach R', 'Ghost Valley 1R', 'Koopa Troopa Beach R/T', 'Donut Plains 1R', 'Donut Plains 1T', 'Koopa Troopa Beach 2', 'Kalimari Desert 2', 'Airship Fortress', 'Airship Fortress R', 'Los Angeles Laps R', 'Sunset Wilds', 'Sunset Wilds R', 'Sunset Wilds T', 'Sunset Wilds R/T', "Rosalina's Ice World"]

Cact_X_lv3_courses = ['Rock Rock Mountain', 'Koopa Troopa Beach R/T']

Cact_X_lv6_courses = ['Koopa Troopa Beach 2', 'Kalimari Desert 2']

Cact_X = race_tool('Cact_X', 'High-End', Cact_X_TWO_x_Bonus_Points, Cact_X_ONEoFIVE_x_Bonus_Points, Cact_X_lv3_courses, Cact_X_lv6_courses)


#Silver_Bullet_Blaster_
# https://game8.co/games/mariokarttour/archives/292675

Silver_Bullet_Blaster__TWO_x_Bonus_Points = ["Bowser's Castle 1R", 'Neo Bowser City R/T', 'DK Pass R/T', 'Waluigi Pinball R/T', 'DS Rainbow Road R/T', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', 'Choco Mountain T', 'Airship Fortress R', 'Airship Fortress T', 'RMX Rainbow Road 1', 'RMX Choco Island 2', 'DK Summit R']

Silver_Bullet_Blaster__ONEoFIVE_x_Bonus_Points = ["Bowser's Castle 1", 'Neo Bowser City T', "Bowser's Castle 1R/T", 'Paris Promenade 2', "Bowser's Castle 2R/T", 'Koopa Troopa Beach 2T', 'Choco Mountain R', 'Airship Fortress', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 1T', 'RMX Choco Island 2R', 'RMX Choco Island 2T']

Silver_Bullet_Blaster__lv3_courses = ['Neo Bowser City T', "Bowser's Castle 2R/T"]

Silver_Bullet_Blaster__lv6_courses = ['Airship Fortress', 'RMX Rainbow Road 1T']

Silver_Bullet_Blaster_ = race_tool('Silver_Bullet_Blaster_', 'High-End', Silver_Bullet_Blaster__TWO_x_Bonus_Points, Silver_Bullet_Blaster__ONEoFIVE_x_Bonus_Points, Silver_Bullet_Blaster__lv3_courses, Silver_Bullet_Blaster__lv6_courses)


#Pirate_Sushi_Racer_
# https://game8.co/games/mariokarttour/archives/292674

Pirate_Sushi_Racer__TWO_x_Bonus_Points = ['Mario Circuit 1R', 'Tokyo Blur R', "Bowser's Castle 1R/T", 'Frappe Snowland R', 'Paris Promenade 2T', "Bowser's Castle 2R/T", 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2T', 'Airship Fortress', 'Airship Fortress R', 'RMX Rainbow Road 1R', 'Los Angeles Laps R/T', 'RMX Choco Island 2', 'RMX Choco Island 2R']

Pirate_Sushi_Racer__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 1', 'Tokyo Blur', 'Tokyo Blur T', 'Frappe Snowland T', 'Vanilla Lake 1T', 'Airship Fortress T', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1T', 'Los Angeles Laps R', 'RMX Choco Island 2T']

Pirate_Sushi_Racer__lv3_courses = ['Mario Circuit 1', 'Frappe Snowland T']

Pirate_Sushi_Racer__lv6_courses = ['Vanilla Lake 1T', 'Airship Fortress T']

Pirate_Sushi_Racer_ = race_tool('Pirate_Sushi_Racer_', 'High-End', Pirate_Sushi_Racer__TWO_x_Bonus_Points, Pirate_Sushi_Racer__ONEoFIVE_x_Bonus_Points, Pirate_Sushi_Racer__lv3_courses, Pirate_Sushi_Racer__lv6_courses)


#Festival_Girl_
# https://game8.co/games/mariokarttour/archives/293912

Festival_Girl__TWO_x_Bonus_Points = ['Shy Guy Bazaar R', 'Shy Guy Bazaar', 'Cheep Cheep Lagoon R', 'Tokyo Blur R/T', 'Ghost Valley 1R', 'London Loop R', 'Tokyo Blur 2', 'Tokyo Blur 2T', 'RMX Choco Island 1R', 'Tokyo Blur 3T', 'Los Angeles Laps R']

Festival_Girl__ONEoFIVE_x_Bonus_Points = ['Cheep Cheep Lagoon', 'Ghost Valley 1T', 'London Loop', 'London Loop R/T', 'Tokyo Blur 2R', 'Vanilla Lake 1', 'Vanilla Lake 1T', 'RMX Choco Island 1', 'Tokyo Blur 3', 'Tokyo Blur 3R', 'Los Angeles Laps R/T']

Festival_Girl__lv3_courses = ['Cheep Cheep Lagoon', 'Ghost Valley 1T']

Festival_Girl__lv6_courses = ['Vanilla Lake 1T']

Festival_Girl_ = race_tool('Festival_Girl_', 'High-End', Festival_Girl__TWO_x_Bonus_Points, Festival_Girl__ONEoFIVE_x_Bonus_Points, Festival_Girl__lv3_courses, Festival_Girl__lv6_courses)


#Black_Kabuki_Dasher_
# https://game8.co/games/mariokarttour/archives/293913

Black_Kabuki_Dasher__TWO_x_Bonus_Points = ['Shy Guy Bazaar R', 'Shy Guy Bazaar', 'Tokyo Blur', 'Mario Circuit 2R', 'Mario Circuit 2', 'Mario Circuit 3', 'Tokyo Blur 2', "Bowser's Castle 2R/T", 'Kalimari Desert 2T', 'Airship Fortress', 'Tokyo Blur 3', 'RMX Rainbow Road 1R/T', 'Berlin Byways 2R/T']

Black_Kabuki_Dasher__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar T', 'Tokyo Blur R', 'Tokyo Blur T', 'Mario Circuit 3T', 'SNES Rainbow Road R/T', 'Tokyo Blur 2R', 'Tokyo Blur 2T', 'Kalimari Desert 2', 'Airship Fortress R', 'Tokyo Blur 3R', 'Tokyo Blur 3T', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 1T', 'Maple Treeway', 'Berlin Byways 2T']

Black_Kabuki_Dasher__lv3_courses = ['Mario Circuit 3T', 'Airship Fortress R']

Black_Kabuki_Dasher__lv6_courses = ['RMX Rainbow Road 1', 'RMX Rainbow Road 1R']

Black_Kabuki_Dasher_ = race_tool('Black_Kabuki_Dasher_', 'High-End', Black_Kabuki_Dasher__TWO_x_Bonus_Points, Black_Kabuki_Dasher__ONEoFIVE_x_Bonus_Points, Black_Kabuki_Dasher__lv3_courses, Black_Kabuki_Dasher__lv6_courses)


#Head_Honcho_
# https://game8.co/games/mariokarttour/archives/293914

Head_Honcho__TWO_x_Bonus_Points = ['Tokyo Blur R', 'Tokyo Blur', 'DK Pass T', 'DK Pass R', 'Mario Circuit 2R/T', 'Koopa Troopa Beach 2', 'Choco Mountain T', 'Airship Fortress', 'Airship Fortress R', 'Airship Fortress T', 'RMX Rainbow Road 1T', 'Sunset Wilds T', 'Donut Plains 2T', 'RMX Choco Island 2R']

Head_Honcho__ONEoFIVE_x_Bonus_Points = ['SNES Rainbow Road R', 'Tokyo Blur T', 'Choco Mountain R', 'Tokyo Blur 3', 'Tokyo Blur 3R', 'Tokyo Blur 3T', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1R', 'Maple Treeway', 'Maple Treeway R', 'Sunset Wilds']

Head_Honcho__lv3_courses = ['Choco Mountain R', 'RMX Rainbow Road 1R']

Head_Honcho__lv6_courses = []

Head_Honcho_ = race_tool('Head_Honcho_', 'High-End', Head_Honcho__TWO_x_Bonus_Points, Head_Honcho__ONEoFIVE_x_Bonus_Points, Head_Honcho__lv3_courses, Head_Honcho__lv6_courses)


#Bit_Pipe_Frame_8_Bit_Pipe_Frame1
# https://game8.co/games/mariokarttour/archives/296086

Bit_Pipe_Frame_8_Bit_Pipe_Frame1_TWO_x_Bonus_Points = ['Yoshi Circuit T', 'Mario Circuit 1', 'Tokyo Blur', 'SNES Rainbow Road T', 'Tokyo Blur T', 'Ghost Valley 1R/T', 'RMX Mario Circuit 1R/T', 'RMX Choco Island 1R', 'RMX Choco Island 1T', 'RMX Rainbow Road 1']

Bit_Pipe_Frame_8_Bit_Pipe_Frame1_ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit', 'Mario Circuit 1T', 'Mario Circuit 1R', 'Tokyo Blur R', 'SNES Rainbow Road', 'SNES Rainbow Road R', 'Tokyo Blur R/T', 'RMX Mario Circuit 1', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 1T', 'Los Angeles Laps T', 'Los Angeles Laps']

Bit_Pipe_Frame_8_Bit_Pipe_Frame1_lv3_courses = ['Mario Circuit 1R', 'RMX Mario Circuit 1']

Bit_Pipe_Frame_8_Bit_Pipe_Frame1_lv6_courses = ['RMX Rainbow Road 1R']

Bit_Pipe_Frame_8_Bit_Pipe_Frame1 = race_tool('Bit_Pipe_Frame_8_Bit_Pipe_Frame1', 'High-End', Bit_Pipe_Frame_8_Bit_Pipe_Frame1_TWO_x_Bonus_Points, Bit_Pipe_Frame_8_Bit_Pipe_Frame1_ONEoFIVE_x_Bonus_Points, Bit_Pipe_Frame_8_Bit_Pipe_Frame1_lv3_courses, Bit_Pipe_Frame_8_Bit_Pipe_Frame1_lv6_courses)


#Gold_Pipe_Frame_
# https://game8.co/games/mariokarttour/archives/296087

Gold_Pipe_Frame__TWO_x_Bonus_Points = ['Mario Circuit 1', 'SNES Rainbow Road T', 'London Loop', 'London Loop T', 'DS Rainbow Road R', 'Neo Bowser City R/T', "Bowser's Castle 2R/T", 'Kalimari Desert 2', 'Airship Fortress', 'Airship Fortress T', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 1T']

Gold_Pipe_Frame__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 1T', 'Mario Circuit 1R', 'London Loop R', 'London Loop R/T', 'DS Rainbow Road T', 'Mario Circuit 2R/T', 'Vancouver Velocity T', 'Vancouver Velocity', 'RMX Mario Circuit 1T', 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'RMX Rainbow Road 1', 'DK Summit T']

Gold_Pipe_Frame__lv3_courses = ['DS Rainbow Road T', 'Mario Circuit 2R/T']

Gold_Pipe_Frame__lv6_courses = ['RMX Mario Circuit 1T', 'RMX Rainbow Road 1']

Gold_Pipe_Frame_ = race_tool('Gold_Pipe_Frame_', 'High-End', Gold_Pipe_Frame__TWO_x_Bonus_Points, Gold_Pipe_Frame__ONEoFIVE_x_Bonus_Points, Gold_Pipe_Frame__lv3_courses, Gold_Pipe_Frame__lv6_courses)


#DK_Maximum_
# https://game8.co/games/mariokarttour/archives/296088

DK_Maximum__TWO_x_Bonus_Points = ['Dino Dino Jungle', 'Ghost Valley 1', 'DK Pass', 'DK Pass T', 'DK Pass R/T', 'Dino Dino Jungle R/T', 'Vancouver Velocity R/T', 'Choco Mountain', 'RMX Rainbow Road 1T', 'New York Minute 3', 'New York Minute 3R', 'Maple Treeway', 'Sunset Wilds T', 'Berlin Byways 2', 'Berlin Byways 2R', 'DK Summit']

DK_Maximum__ONEoFIVE_x_Bonus_Points = ['Ghost Valley 1R', 'Ghost Valley 1T', 'Vancouver Velocity T', 'Vancouver Velocity R', "Bowser's Castle 2R", 'Choco Mountain R', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1R', 'Los Angeles Laps T', 'Los Angeles Laps', 'Maple Treeway R', 'Maple Treeway T', 'Sunset Wilds', 'Sunset Wilds R', 'RMX Rainbow Road 1R/T', 'Berlin Byways 2R/T', 'DK Summit T']

DK_Maximum__lv3_courses = ['Ghost Valley 1R', 'Ghost Valley 1T']

DK_Maximum__lv6_courses = ["Bowser's Castle 2R", 'Choco Mountain R']

DK_Maximum_ = race_tool('DK_Maximum_', 'High-End', DK_Maximum__TWO_x_Bonus_Points, DK_Maximum__ONEoFIVE_x_Bonus_Points, DK_Maximum__lv3_courses, DK_Maximum__lv6_courses)


#Surf_Sailer_
# https://game8.co/games/mariokarttour/archives/297364

Surf_Sailer__TWO_x_Bonus_Points = ['Frappe Snowland R', 'RMX Mario Circuit 1R/T', 'Choco Island 1', 'Choco Island 1R', 'Koopa Troopa Beach 2', 'Airship Fortress', 'Airship Fortress R', 'Los Angeles Laps', 'Los Angeles Laps R', "Rosalina's Ice World", 'Berlin Byways 2R', 'Berlin Byways 2T', 'Donut Plains 2']

Surf_Sailer__ONEoFIVE_x_Bonus_Points = ['Choco Island 2', 'SNES Rainbow Road R/T', 'Kalimari Desert R/T', 'Frappe Snowland', 'Frappe Snowland T', 'RMX Choco Island 1', 'RMX Choco Island 1T', 'Choco Island 1T', 'RMX Rainbow Road 1', 'Los Angeles Laps T', 'Los Angeles Laps R/T', 'New York Minute 3R', 'New York Minute 3R/T', 'Sunset Wilds R/T', 'Merry Mountain', "Rosalina's Ice World T", 'Donut Plains 2R']

Surf_Sailer__lv3_courses = ['RMX Choco Island 1T', 'Choco Island 1T']

Surf_Sailer__lv6_courses = ['Frappe Snowland T', 'RMX Choco Island 1']

Surf_Sailer_ = race_tool('Surf_Sailer_', 'High-End', Surf_Sailer__TWO_x_Bonus_Points, Surf_Sailer__ONEoFIVE_x_Bonus_Points, Surf_Sailer__lv3_courses, Surf_Sailer__lv6_courses)


#Star_Spangled_Flyer_
# https://game8.co/games/mariokarttour/archives/297365

Star_Spangled_Flyer__TWO_x_Bonus_Points = ['Vancouver Velocity', 'Vancouver Velocity', 'RMX Choco Island 1', 'Kalimari Desert 2', 'Kalimari Desert 2R', 'Los Angeles Laps', 'Los Angeles Laps R', 'New York Minute 3R', 'New York Minute 3T']

Star_Spangled_Flyer__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit R', 'Toad Circuit T', 'Toad Circuit R', 'Kalimari Desert', 'Neo Bowser City R/T', 'Vancouver Velocity T', 'Vancouver Velocity T', 'Koopa Troopa Beach R/T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1R', 'Koopa Troopa Beach 2', 'Los Angeles Laps T', 'Los Angeles Laps R/T', 'New York Minute 3', 'New York Minute 3R/T', 'Maple Treeway R', 'Maple Treeway T', 'RMX Rainbow Road 2T']

Star_Spangled_Flyer__lv3_courses = ['Yoshi Circuit R', 'Toad Circuit T']

Star_Spangled_Flyer__lv6_courses = ['Kalimari Desert', 'Maple Treeway R']

Star_Spangled_Flyer_ = race_tool('Star_Spangled_Flyer_', 'High-End', Star_Spangled_Flyer__TWO_x_Bonus_Points, Star_Spangled_Flyer__ONEoFIVE_x_Bonus_Points, Star_Spangled_Flyer__lv3_courses, Star_Spangled_Flyer__lv6_courses)


#Green_Circuit_
# https://game8.co/games/mariokarttour/archives/297366

Green_Circuit__TWO_x_Bonus_Points = ['Yoshi Circuit', 'Daisy Hills R', 'Mario Circuit R', 'Mario Circuit', 'Tokyo Blur T', 'Waluigi Pinball R', 'London Loop', 'London Loop R', 'London Loop T', "Luigi's Mansion R/T", 'Mario Circuit 1R/T', 'Toad Circuit R/T', 'Paris Promenade 2T', 'Vancouver Velocity T', 'Donut Plains 1R', 'RMX Rainbow Road 1', 'Los Angeles Laps T', 'Los Angeles Laps R/T']

Green_Circuit__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit T', 'Yoshi Circuit R', 'Mario Circuit T', 'Waluigi Pinball T', 'London Loop R/T', 'Paris Promenade 2R', 'Vancouver Velocity', 'Vancouver Velocity R', 'Koopa Troopa Beach R/T', 'Donut Plains 1', 'RMX Choco Island 1', 'Royal Raceway R', 'Royal Raceway', 'RMX Rainbow Road 1T', 'Los Angeles Laps', 'Los Angeles Laps R', 'Maple Treeway', 'Maple Treeway T', 'Sunset Wilds R/T']

Green_Circuit__lv3_courses = ['Yoshi Circuit T', 'Koopa Troopa Beach R/T']

Green_Circuit__lv6_courses = ['Waluigi Pinball T', 'RMX Choco Island 1T']

Green_Circuit_ = race_tool('Green_Circuit_', 'High-End', Green_Circuit__TWO_x_Bonus_Points, Green_Circuit__ONEoFIVE_x_Bonus_Points, Green_Circuit__lv3_courses, Green_Circuit__lv6_courses)


#Sushi_Racer_
# https://game8.co/games/mariokarttour/archives/297367

Sushi_Racer__TWO_x_Bonus_Points = ['Cheep Cheep Lagoon R/T', 'Frappe Snowland T', 'Vanilla Lake 1T', 'Vancouver Velocity', 'Vancouver Velocity R/T', 'Koopa Troopa Beach R/T', 'Koopa Troopa Beach 2', 'Airship Fortress T', 'Los Angeles Laps', 'Los Angeles Laps R/T', 'Merry Mountain R', "Rosalina's Ice World R"]

Sushi_Racer__ONEoFIVE_x_Bonus_Points = ['Choco Island 2', 'Neo Bowser City R/T', 'Frappe Snowland', 'Vanilla Lake 1R', 'Vancouver Velocity T', 'Vancouver Velocity R', 'Koopa Troopa Beach 2T', 'Airship Fortress R', 'Los Angeles Laps T', 'Los Angeles Laps R', 'Merry Mountain T', "Rosalina's Ice World", 'RMX Choco Island 2T']

Sushi_Racer__lv3_courses = ['Neo Bowser City R/T', 'Vanilla Lake 1R']

Sushi_Racer__lv6_courses = ['Choco Island 2', 'Frappe Snowland']

Sushi_Racer_ = race_tool('Sushi_Racer_', 'High-End', Sushi_Racer__TWO_x_Bonus_Points, Sushi_Racer__ONEoFIVE_x_Bonus_Points, Sushi_Racer__lv3_courses, Sushi_Racer__lv6_courses)


#Gilded_King_
# https://game8.co/games/mariokarttour/archives/304784

Gilded_King__TWO_x_Bonus_Points = ['Dino Dino Jungle R', "Bowser's Castle 1R", "Bowser's Castle 1", 'Kalimari Desert', 'Neo Bowser City R', 'Neo Bowser City T', 'London Loop R', 'London Loop T', "Bowser's Castle 1R/T", 'Shy Guy Bazaar R/T', "Bowser's Castle 2R", "Bowser's Castle 2R/T", 'RMX Choco Island 1T', 'Airship Fortress', 'New York Minute 3', 'Merry Mountain', 'RMX Rainbow Road 2T', 'Donut Plains 2T']

Gilded_King__ONEoFIVE_x_Bonus_Points = ['Dino Dino Jungle T', 'Kalimari Desert T', 'Kalimari Desert R', 'Neo Bowser City', 'Waluigi Pinball', "Bowser's Castle 2", "Bowser's Castle 2T", 'RMX Choco Island 1R', 'Airship Fortress R', 'New York Minute 3R', 'New York Minute 3T', 'RMX Rainbow Road 1R/T', 'Sunset Wilds R/T', 'Merry Mountain R', 'Merry Mountain T', 'RMX Rainbow Road 2', 'Berlin Byways 2', 'Berlin Byways 2R', 'Berlin Byways 2R/T', 'Donut Plains 2', 'DK Summit', 'DK Summit R']

Gilded_King__lv3_courses = ["Bowser's Castle 2T", 'Airship Fortress R']

Gilded_King__lv6_courses = ['Waluigi Pinball', "Bowser's Castle 2"]

Gilded_King_ = race_tool('Gilded_King_', 'High-End', Gilded_King__TWO_x_Bonus_Points, Gilded_King__ONEoFIVE_x_Bonus_Points, Gilded_King__lv3_courses, Gilded_King__lv6_courses)


#Sports_Coupe_
# https://game8.co/games/mariokarttour/archives/304785

Sports_Coupe__TWO_x_Bonus_Points = ['Mario Circuit 1R', 'Daisy Hills R', 'Toad Circuit', 'Mario Circuit R', 'Neo Bowser City', 'Mario Circuit T', 'Waluigi Pinball', 'Mario Circuit 3R', 'Mario Circuit R/T', 'London Loop', 'Mario Circuit 2R/T', 'Paris Promenade 2', 'Vancouver Velocity', 'New York Minute 3R/T', 'Merry Mountain T', "Rosalina's Ice World R", "Rosalina's Ice World T", 'Berlin Byways 2R', 'RMX Choco Island 2T']

Sports_Coupe__ONEoFIVE_x_Bonus_Points = ['Daisy Hills', 'Toad Circuit T', 'Toad Circuit R', 'Mario Circuit', 'Neo Bowser City R', 'Waluigi Pinball R', 'Mario Circuit 3', 'Mario Circuit 3T', 'London Loop R/T', 'London Loop T', 'Toad Circuit R/T', 'Paris Promenade 2T', 'RMX Mario Circuit 1R/T', 'New York Minute 3', 'New York Minute 3R', 'New York Minute 3T', 'Maple Treeway', 'Maple Treeway R', 'Merry Mountain', 'Berlin Byways 2', 'Berlin Byways 2T']

Sports_Coupe__lv3_courses = ['Toad Circuit T', 'Toad Circuit R']

Sports_Coupe__lv6_courses = ['Toad Circuit R/T', 'Maple Treeway R']

Sports_Coupe_ = race_tool('Sports_Coupe_', 'High-End', Sports_Coupe__TWO_x_Bonus_Points, Sports_Coupe__ONEoFIVE_x_Bonus_Points, Sports_Coupe__lv3_courses, Sports_Coupe__lv6_courses)


#Crawly_Kart_
# https://game8.co/games/mariokarttour/archives/305319

Crawly_Kart__TWO_x_Bonus_Points = ["Luigi's Mansion T", 'Waluigi Pinball', 'Shy Guy Bazaar R/T', 'DS Rainbow Road R/T', 'Choco Island 1', 'Royal Raceway', 'Maple Treeway', 'Sunset Wilds', "Rosalina's Ice World R", 'RMX Rainbow Road 2T', 'Berlin Byways 2', 'RMX Choco Island 2']

Crawly_Kart__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar R', 'Shy Guy Bazaar', 'Waluigi Pinball R', 'Waluigi Pinball R/T', 'Ghost Valley 1R/T', 'Choco Island 1R', 'Royal Raceway T', 'Maple Treeway R', 'Sunset Wilds R', "Rosalina's Ice World T", 'Berlin Byways 2R']

Crawly_Kart__lv3_courses = ['Shy Guy Bazaar', 'Ghost Valley 1R/T']

Crawly_Kart__lv6_courses = ['Shy Guy Bazaar R', 'Waluigi Pinball R']

Crawly_Kart_ = race_tool('Crawly_Kart_', 'High-End', Crawly_Kart__TWO_x_Bonus_Points, Crawly_Kart__ONEoFIVE_x_Bonus_Points, Crawly_Kart__lv3_courses, Crawly_Kart__lv6_courses)


#Dark_Trickster_
# https://game8.co/games/mariokarttour/archives/305320

Dark_Trickster__TWO_x_Bonus_Points = ['Waluigi Pinball R/T', "Bowser's Castle 2R", 'RMX Choco Island 1T', 'Maple Treeway T', 'Sunset Wilds T', 'Merry Mountain', 'RMX Rainbow Road 2T', 'Berlin Byways 2', 'Berlin Byways 2R', 'RMX Choco Island 2R']

Dark_Trickster__ONEoFIVE_x_Bonus_Points = ['DS Rainbow Road R', 'DS Rainbow Road T', 'Ghost Valley 1R/T', 'DS Rainbow Road R/T', "Bowser's Castle 2T", 'RMX Choco Island 1R', 'Royal Raceway T', 'Royal Raceway', 'Maple Treeway', 'Maple Treeway R', 'Sunset Wilds', 'Sunset Wilds R', 'Merry Mountain R', 'RMX Rainbow Road 2R', 'RMX Choco Island 2']

Dark_Trickster__lv3_courses = ['Ghost Valley 1R/T', "Bowser's Castle 2T"]

Dark_Trickster__lv6_courses = ['DS Rainbow Road R/T', 'Maple Treeway R']

Dark_Trickster_ = race_tool('Dark_Trickster_', 'High-End', Dark_Trickster__TWO_x_Bonus_Points, Dark_Trickster__ONEoFIVE_x_Bonus_Points, Dark_Trickster__lv3_courses, Dark_Trickster__lv6_courses)


#Pumpkin_Kart_
# https://game8.co/games/mariokarttour/archives/305321

Pumpkin_Kart__TWO_x_Bonus_Points = ['Choco Island 2', 'Neo Bowser City R', 'Neo Bowser City', "Luigi's Mansion R", 'Ghost Valley 1R/T', 'Maple Treeway', 'Merry Mountain', "Rosalina's Ice World", 'Berlin Byways 2R/T', 'RMX Choco Island 2']

Pumpkin_Kart__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar T', 'Choco Island 2T', 'Neo Bowser City T', "Luigi's Mansion T", 'Paris Promenade 2', 'RMX Choco Island 1R', 'RMX Choco Island 1T', 'Maple Treeway R', 'Maple Treeway T', 'Sunset Wilds R', 'Sunset Wilds T', 'Merry Mountain R', 'Merry Mountain T', "Rosalina's Ice World R", 'RMX Choco Island 2T']

Pumpkin_Kart__lv3_courses = ['Shy Guy Bazaar T', 'Maple Treeway R']

Pumpkin_Kart__lv6_courses = ['Choco Island 2T', 'Maple Treeway T']

Pumpkin_Kart_ = race_tool('Pumpkin_Kart_', 'High-End', Pumpkin_Kart__TWO_x_Bonus_Points, Pumpkin_Kart__ONEoFIVE_x_Bonus_Points, Pumpkin_Kart__lv3_courses, Pumpkin_Kart__lv6_courses)


#Black_Dozer_
# https://game8.co/games/mariokarttour/archives/305957

Black_Dozer__TWO_x_Bonus_Points = ['Kalimari Desert', 'Neo Bowser City R', "Bowser's Castle 1R/T", 'Neo Bowser City R/T', 'Frappe Snowland R/T', 'Choco Island 1R', 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'Sunset Wilds R/T', 'Merry Mountain', "Rosalina's Ice World T", 'Donut Plains 2T', 'DK Summit T']

Black_Dozer__ONEoFIVE_x_Bonus_Points = ['Dino Dino Jungle', 'Kalimari Desert T', 'Kalimari Desert R', 'Neo Bowser City', 'Neo Bowser City T', 'Mario Circuit 3', 'Mario Circuit 3R', 'Kalimari Desert R/T', 'Waluigi Pinball R/T', 'Choco Island 1', 'Sunset Wilds R', 'Sunset Wilds T', 'Merry Mountain R', 'Merry Mountain T', "Rosalina's Ice World", 'Donut Plains 2R', 'DK Summit']

Black_Dozer__lv3_courses = ['Neo Bowser City', 'Waluigi Pinball R/T']

Black_Dozer__lv6_courses = ['Dino Dino Jungle', 'Sunset Wilds R']

Black_Dozer_ = race_tool('Black_Dozer_', 'High-End', Black_Dozer__TWO_x_Bonus_Points, Black_Dozer__ONEoFIVE_x_Bonus_Points, Black_Dozer__lv3_courses, Black_Dozer__lv6_courses)


#Sunset_Cloud_
# https://game8.co/games/mariokarttour/archives/305958

Sunset_Cloud__TWO_x_Bonus_Points = ['Mario Circuit 1R', 'Koopa Troopa Beach', 'Mario Circuit 1', 'Kalimari Desert R/T', 'Maple Treeway T', 'Sunset Wilds R', 'Sunset Wilds R/T', 'Merry Mountain T', 'DK Summit T']

Sunset_Cloud__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 1T', 'Koopa Troopa Beach R', 'Daisy Hills R/T', "Bowser's Castle 1R/T", 'DK Pass R/T', 'Royal Raceway R', 'Royal Raceway T', 'Sunset Wilds', 'Sunset Wilds T', 'RMX Rainbow Road 1R/T', 'Merry Mountain', 'DK Summit']

Sunset_Cloud__lv3_courses = ['Royal Raceway R', 'Royal Raceway T']

Sunset_Cloud__lv6_courses = ['DK Pass R/T', 'Sunset Wilds T']

Sunset_Cloud_ = race_tool('Sunset_Cloud_', 'High-End', Sunset_Cloud__TWO_x_Bonus_Points, Sunset_Cloud__ONEoFIVE_x_Bonus_Points, Sunset_Cloud__lv3_courses, Sunset_Cloud__lv6_courses)


#Steel_Driver_
# https://game8.co/games/mariokarttour/archives/309368

Steel_Driver__TWO_x_Bonus_Points = ["Luigi's Mansion R/T", 'Cheep Cheep Lagoon R/T', 'Frappe Snowland R', 'Ghost Valley 1R/T', 'Koopa Troopa Beach 2T', 'Airship Fortress R', 'Sunset Wilds T', 'Merry Mountain T', "Rosalina's Ice World", 'RMX Rainbow Road 2', 'Donut Plains 2']

Steel_Driver__ONEoFIVE_x_Bonus_Points = ['Neo Bowser City R/T', 'Frappe Snowland', 'Vanilla Lake 1', 'Vanilla Lake 1R', 'Vanilla Lake 1T', 'Dino Dino Jungle R/T', 'Frappe Snowland R/T', 'Koopa Troopa Beach R/T', 'Vanilla Lake 1R/T', 'Koopa Troopa Beach 2', 'RMX Rainbow Road 1R/T', 'Merry Mountain', 'Merry Mountain R', "Rosalina's Ice World R", 'Donut Plains 2R', 'RMX Choco Island 2', 'RMX Choco Island 2R', 'DK Summit R']

Steel_Driver__lv3_courses = ['Neo Bowser City R/T', 'Vanilla Lake 1R/T']

Steel_Driver__lv6_courses = ['Koopa Troopa Beach R/T', 'RMX Rainbow Road 1R/T']

Steel_Driver_ = race_tool('Steel_Driver_', 'High-End', Steel_Driver__TWO_x_Bonus_Points, Steel_Driver__ONEoFIVE_x_Bonus_Points, Steel_Driver__lv3_courses, Steel_Driver__lv6_courses)


#Holiday_King_
# https://game8.co/games/mariokarttour/archives/311465

Holiday_King__TWO_x_Bonus_Points = ['Neo Bowser City R/T', 'Frappe Snowland', "Bowser's Castle 2T", 'RMX Rainbow Road 1T', 'Maple Treeway', 'Maple Treeway R', 'Sunset Wilds', 'Merry Mountain', "Rosalina's Ice World", 'Berlin Byways 2T', 'Donut Plains 2R', 'DK Summit', 'DK Summit R']

Holiday_King__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain T', 'DS Rainbow Road', 'DS Rainbow Road T', "Bowser's Castle 2", 'Choco Island 1', 'Maple Treeway T', 'RMX Rainbow Road 1R/T', 'Merry Mountain R', "Rosalina's Ice World T", 'Berlin Byways 2R', 'Berlin Byways 2R/T']

Holiday_King__lv3_courses = ['3DS Rainbow Road', 'Maple Treeway T']

Holiday_King__lv6_courses = ['DS Rainbow Road T', 'Merry Mountain R']

Holiday_King_ = race_tool('Holiday_King_', 'High-End', Holiday_King__TWO_x_Bonus_Points, Holiday_King__ONEoFIVE_x_Bonus_Points, Holiday_King__lv3_courses, Holiday_King__lv6_courses)


#Gold_Snow_Skimmer_
# https://game8.co/games/mariokarttour/archives/314373

Gold_Snow_Skimmer__TWO_x_Bonus_Points = ['DK Pass', 'DK Pass T', 'Kalimari Desert 2', 'Kalimari Desert 2R', 'RMX Rainbow Road 1', 'Sunset Wilds', "Rosalina's Ice World R", 'RMX Choco Island 2R']

Gold_Snow_Skimmer__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain R', 'Rock Rock Mountain', 'SNES Rainbow Road R', 'Choco Mountain R', 'Choco Mountain T', 'Kalimari Desert 2T', 'Sunset Wilds R', "Rosalina's Ice World", "Rosalina's Ice World T", 'Berlin Byways 2T', 'Donut Plains 2R', 'Donut Plains 2T', 'RMX Choco Island 2T', 'DK Summit R']

Gold_Snow_Skimmer__lv3_courses = ['Choco Mountain T', 'Sunset Wilds R']

Gold_Snow_Skimmer__lv6_courses = ['Choco Mountain R', "Rosalina's Ice World"]

Gold_Snow_Skimmer_ = race_tool('Gold_Snow_Skimmer_', 'High-End', Gold_Snow_Skimmer__TWO_x_Bonus_Points, Gold_Snow_Skimmer__ONEoFIVE_x_Bonus_Points, Gold_Snow_Skimmer__lv3_courses, Gold_Snow_Skimmer__lv6_courses)


#Dreamy_Egg_
# https://game8.co/games/mariokarttour/archives/314374

Dreamy_Egg__TWO_x_Bonus_Points = ['Waluigi Pinball', 'Waluigi Pinball T', 'Royal Raceway T', 'Royal Raceway', 'RMX Rainbow Road 1', 'Maple Treeway T', 'RMX Rainbow Road 1R/T', 'Merry Mountain', 'Donut Plains 2T']

Dreamy_Egg__ONEoFIVE_x_Bonus_Points = ['Cheep Cheep Lagoon R', 'SNES Rainbow Road T', 'Vanilla Lake 1R', 'Vanilla Lake 1T', 'DS Rainbow Road R/T', 'Choco Island 1', 'Royal Raceway R', 'Kalimari Desert 2', 'Merry Mountain T', "Rosalina's Ice World", "Rosalina's Ice World R", "Rosalina's Ice World T", 'RMX Rainbow Road 2', 'RMX Rainbow Road 2R', 'RMX Rainbow Road 2T', 'Donut Plains 2']

Dreamy_Egg__lv3_courses = ['RMX Rainbow Road 1T', "Rosalina's Ice World R"]

Dreamy_Egg__lv6_courses = ['Merry Mountain T', "Rosalina's Ice World T"]

Dreamy_Egg_ = race_tool('Dreamy_Egg_', 'High-End', Dreamy_Egg__TWO_x_Bonus_Points, Dreamy_Egg__ONEoFIVE_x_Bonus_Points, Dreamy_Egg__lv3_courses, Dreamy_Egg__lv6_courses)


#Party_Wing_
# https://game8.co/games/mariokarttour/archives/315372

Party_Wing__TWO_x_Bonus_Points = ['Mario Circuit 1T', 'Cheep Cheep Lagoon T', 'Cheep Cheep Lagoon R', 'Paris Promenade 2T', 'Choco Mountain', 'Choco Mountain R', 'RMX Rainbow Road 1T', 'RMX Rainbow Road 1R/T', "Rosalina's Ice World", 'RMX Rainbow Road 2', 'RMX Rainbow Road 2R', 'Berlin Byways 2R/T', 'DK Summit']

Party_Wing__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 1', 'Waluigi Pinball', 'Paris Promenade 2', 'DS Rainbow Road R/T', 'Vanilla Lake 1R/T', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1R', "Rosalina's Ice World R", 'RMX Rainbow Road 2T', 'Berlin Byways 2', 'Berlin Byways 2T', 'RMX Choco Island 2', 'RMX Choco Island 2T', 'DK Summit R']

Party_Wing__lv3_courses = ['Waluigi Pinball', 'RMX Rainbow Road 1']

Party_Wing__lv6_courses = ["Rosalina's Ice World R", 'RMX Rainbow Road 2T']

Party_Wing_ = race_tool('Party_Wing_', 'High-End', Party_Wing__TWO_x_Bonus_Points, Party_Wing__ONEoFIVE_x_Bonus_Points, Party_Wing__lv3_courses, Party_Wing__lv6_courses)


#Penguin_Slider_
# https://game8.co/games/mariokarttour/archives/316095

Penguin_Slider__TWO_x_Bonus_Points = ['Cheep Cheep Lagoon', 'Waluigi Pinball R', 'DK Pass R', 'Koopa Troopa Beach R/T', 'Merry Mountain', 'Merry Mountain R', "Rosalina's Ice World", "Rosalina's Ice World R", 'Berlin Byways 2R/T', 'Donut Plains 2R']

Penguin_Slider__ONEoFIVE_x_Bonus_Points = ['Cheep Cheep Lagoon T', 'Cheep Cheep Lagoon R', 'Frappe Snowland R', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2T', "Rosalina's Ice World T", 'Berlin Byways 2R', 'Donut Plains 2', 'DK Summit', 'DK Summit T']

Penguin_Slider__lv3_courses = ['Koopa Troopa Beach 2', 'Berlin Byways 2R']

Penguin_Slider__lv6_courses = ['Cheep Cheep Lagoon R', 'Koopa Troopa Beach 2T']

Penguin_Slider_ = race_tool('Penguin_Slider_', 'High-End', Penguin_Slider__TWO_x_Bonus_Points, Penguin_Slider__ONEoFIVE_x_Bonus_Points, Penguin_Slider__lv3_courses, Penguin_Slider__lv6_courses)


#Iron_Cucumber_
# https://game8.co/games/mariokarttour/archives/316094

Iron_Cucumber__TWO_x_Bonus_Points = ['Yoshi Circuit R', 'Mario Circuit 1T', 'Mario Circuit 3R', 'Paris Promenade 2R', 'Paris Promenade 2T', 'Choco Island 1R', 'Choco Mountain T', 'Merry Mountain T', 'RMX Rainbow Road 2', 'RMX Rainbow Road 2T', 'Berlin Byways 2', 'Berlin Byways 2T']

Iron_Cucumber__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit', 'Mario Circuit 3', 'Mario Circuit 3T', 'Neo Bowser City R/T', 'Paris Promenade 2', 'Royal Raceway R', 'Royal Raceway', 'Berlin Byways 2R', 'Berlin Byways 2R/T', 'RMX Choco Island 2', 'RMX Choco Island 2R', 'RMX Choco Island 2T', 'DK Summit R', 'DK Summit T']

Iron_Cucumber__lv3_courses = ['Mario Circuit 3T', 'Berlin Byways 2R']

Iron_Cucumber__lv6_courses = ['Mario Circuit 3', 'Berlin Byways 2R/T']

Iron_Cucumber_ = race_tool('Iron_Cucumber_', 'High-End', Iron_Cucumber__TWO_x_Bonus_Points, Iron_Cucumber__ONEoFIVE_x_Bonus_Points, Iron_Cucumber__lv3_courses, Iron_Cucumber__lv6_courses)


#Fast_Frank_
# https://game8.co/games/mariokarttour/archives/316093

Fast_Frank__TWO_x_Bonus_Points = ['Rock Rock Mountain', 'Shy Guy Bazaar T', 'Shy Guy Bazaar', 'Mario Circuit 2R', 'Kalimari Desert', 'Mario Circuit 3T', "Bowser's Castle 2", "Bowser's Castle 2T", 'Koopa Troopa Beach 2T', 'Sunset Wilds', 'Sunset Wilds T', 'Sunset Wilds R/T', 'Berlin Byways 2', 'Berlin Byways 2R/T']

Fast_Frank__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain T', 'Rock Rock Mountain R', 'Shy Guy Bazaar R', 'Dino Dino Jungle T', 'Dino Dino Jungle', 'Daisy Hills R', 'Daisy Hills', 'Mario Circuit 3', 'RMX Choco Island 1R', 'Koopa Troopa Beach 2R', 'Berlin Byways 2R']

Fast_Frank__lv3_courses = ['Rock Rock Mountain T', 'RMX Choco Island 1R']

Fast_Frank__lv6_courses = ['Mario Circuit 3', 'Koopa Troopa Beach 2R']

Fast_Frank_ = race_tool('Fast_Frank_', 'High-End', Fast_Frank__TWO_x_Bonus_Points, Fast_Frank__ONEoFIVE_x_Bonus_Points, Fast_Frank__lv3_courses, Fast_Frank__lv6_courses)


#Wild_Pink_
# https://game8.co/games/mariokarttour/archives/317073

Wild_Pink__TWO_x_Bonus_Points = ['Paris Promenade 2T', 'Paris Promenade 2', 'Maple Treeway T', "Rosalina's Ice World R", 'RMX Rainbow Road 2', 'RMX Rainbow Road 2T', 'Donut Plains 2T', 'RMX Choco Island 2T']

Wild_Pink__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar T', 'Shy Guy Bazaar', 'Mario Circuit 2R', 'Paris Promenade 2R', 'Maple Treeway', "Rosalina's Ice World T", 'Donut Plains 2', 'Donut Plains 2R', 'RMX Choco Island 2R']

Wild_Pink__lv3_courses = ['Paris Promenade 2R', 'Maple Treeway']

Wild_Pink__lv6_courses = ['Shy Guy Bazaar T', 'Donut Plains 2']

Wild_Pink_ = race_tool('Wild_Pink_', 'High-End', Wild_Pink__TWO_x_Bonus_Points, Wild_Pink__ONEoFIVE_x_Bonus_Points, Wild_Pink__lv3_courses, Wild_Pink__lv6_courses)


#Cat_Cruiser_
# https://game8.co/games/mariokarttour/archives/317072

Cat_Cruiser__TWO_x_Bonus_Points = ['Dino Dino Jungle T', 'Mario Circuit 2', 'Paris Promenade 2', 'Choco Island 1', 'Royal Raceway R', 'Maple Treeway R', 'RMX Rainbow Road 1R/T', 'Donut Plains 2']

Cat_Cruiser__ONEoFIVE_x_Bonus_Points = ['Dino Dino Jungle', 'Mario Circuit 2R', 'Paris Promenade 2R', 'Royal Raceway', 'Maple Treeway', 'Donut Plains 2T']

Cat_Cruiser__lv3_courses = ['Royal Raceway', 'Maple Treeway']

Cat_Cruiser__lv6_courses = ['Paris Promenade 2R', 'Donut Plains 2T']

Cat_Cruiser_ = race_tool('Cat_Cruiser_', 'High-End', Cat_Cruiser__TWO_x_Bonus_Points, Cat_Cruiser__ONEoFIVE_x_Bonus_Points, Cat_Cruiser__lv3_courses, Cat_Cruiser__lv6_courses)


#Rose_Taxi_
# https://game8.co/games/mariokarttour/archives/317798

Rose_Taxi__TWO_x_Bonus_Points = ['Yoshi Circuit R', 'Yoshi Circuit R', 'Donut Plains 2', 'Donut Plains 2T', 'RMX Choco Island 2R', 'RMX Choco Island 2T', 'DK Summit T']

Rose_Taxi__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit', 'Daisy Hills T', 'Daisy Hills R', 'SNES Rainbow Road R/T', 'DS Rainbow Road R/T', 'Choco Mountain', 'RMX Choco Island 2', 'DK Summit R']

Rose_Taxi__lv3_courses = ['Yoshi Circuit', 'Choco Mountain']

Rose_Taxi__lv6_courses = ['Daisy Hills R', 'SNES Rainbow Road R/T']

Rose_Taxi_ = race_tool('Rose_Taxi_', 'High-End', Rose_Taxi__TWO_x_Bonus_Points, Rose_Taxi__ONEoFIVE_x_Bonus_Points, Rose_Taxi__lv3_courses, Rose_Taxi__lv6_courses)


#Cact_Ice_
# https://game8.co/games/mariokarttour/archives/321007

Cact_Ice__TWO_x_Bonus_Points = ['DK Pass', 'DK Pass R', 'DK Summit R', 'DK Summit T']

Cact_Ice__ONEoFIVE_x_Bonus_Points = ['DK Pass T', 'Frappe Snowland', "Rosalina's Ice World", 'RMX Rainbow Road 2T', 'DK Summit']

Cact_Ice__lv3_courses = ['DK Pass T', 'RMX Rainbow Road 2T']

Cact_Ice__lv6_courses = ["Rosalina's Ice World", 'DK Summit']

Cact_Ice_ = race_tool('Cact_Ice_', 'High-End', Cact_Ice__TWO_x_Bonus_Points, Cact_Ice__ONEoFIVE_x_Bonus_Points, Cact_Ice__lv3_courses, Cact_Ice__lv6_courses)


#Black_Penguin_Slider_
# https://game8.co/games/mariokarttour/archives/321006

Black_Penguin_Slider__TWO_x_Bonus_Points = ['Frappe Snowland', 'Vanilla Lake 1T', "Rosalina's Ice World", 'DK Summit']

Black_Penguin_Slider__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 2', 'DK Pass T', 'Frappe Snowland R', "Rosalina's Ice World T", 'DK Summit R', 'DK Summit T']

Black_Penguin_Slider__lv3_courses = ['Mario Circuit 2', "Rosalina's Ice World T"]

Black_Penguin_Slider__lv6_courses = ['Frappe Snowland R', 'DK Summit T']

Black_Penguin_Slider_ = race_tool('Black_Penguin_Slider_', 'High-End', Black_Penguin_Slider__TWO_x_Bonus_Points, Black_Penguin_Slider__ONEoFIVE_x_Bonus_Points, Black_Penguin_Slider__lv3_courses, Black_Penguin_Slider__lv6_courses)


#B_Dasher_Mk_2_
# https://game8.co/games/mariokarttour/archives/322567

B_Dasher_Mk_2__TWO_x_Bonus_Points = ['Mario Circuit 1R', 'Toad Circuit T', 'RMX Mario Circuit 1R/T', 'Tokyo Blur 4']

B_Dasher_Mk_2__ONEoFIVE_x_Bonus_Points = ['Toad Circuit R', 'Mario Circuit 1R/T', 'RMX Mario Circuit 1R', 'RMX Mario Circuit 1T', 'Tokyo Blur 4T', 'Tokyo Blur 4R/T']

B_Dasher_Mk_2__lv3_courses = ['Toad Circuit R', 'Toad Circuit R', 'RMX Mario Circuit 1T']

B_Dasher_Mk_2__lv6_courses = ['Mario Circuit 1R/T', 'RMX Mario Circuit 1R']

B_Dasher_Mk_2_ = race_tool('B_Dasher_Mk_2_', 'High-End', B_Dasher_Mk_2__TWO_x_Bonus_Points, B_Dasher_Mk_2__ONEoFIVE_x_Bonus_Points, B_Dasher_Mk_2__lv3_courses, B_Dasher_Mk_2__lv6_courses)


#Decal_Streamliner_
# https://game8.co/games/mariokarttour/archives/322568

Decal_Streamliner__TWO_x_Bonus_Points = ['Mario Circuit 1T', 'DK Summit', 'Tokyo Blur 4', 'Tokyo Blur 4T', 'Tokyo Blur 4T']

Decal_Streamliner__ONEoFIVE_x_Bonus_Points = ['Toad Circuit', 'Mario Circuit 1R/T', 'DK Summit T', 'Tokyo Blur 4R', 'Tokyo Blur 4R/T']

Decal_Streamliner__lv3_courses = ['Toad Circuit', 'DK Summit T']

Decal_Streamliner__lv6_courses = ['Mario Circuit 1R/T', 'Tokyo Blur 4R/T']

Decal_Streamliner_ = race_tool('Decal_Streamliner_', 'High-End', Decal_Streamliner__TWO_x_Bonus_Points, Decal_Streamliner__ONEoFIVE_x_Bonus_Points, Decal_Streamliner__lv3_courses, Decal_Streamliner__lv6_courses)


#Bumble_V_
# https://game8.co/games/mariokarttour/archives/271639

Bumble_V__TWO_x_Bonus_Points = ['Dino Dino Jungle R', 'Daisy Hills', 'Mario Circuit 2R', 'Waluigi Pinball', 'Waluigi Pinball T', 'Mario Circuit 3', 'SNES Rainbow Road R/T', 'Paris Promenade 2T', 'Paris Promenade 2R/T', 'Waluigi Pinball R/T']

Bumble_V__ONEoFIVE_x_Bonus_Points = ['Dino Dino Jungle T', 'London Loop', 'London Loop R', 'Paris Promenade 2R', 'Paris Promenade 2', 'Donut Plains 1R/T', 'Choco Island 1T', 'Airship Fortress R', 'Airship Fortress T', 'Los Angeles Laps T', 'Los Angeles Laps R/T', "Rosalina's Ice World R", "Rosalina's Ice World T"]

Bumble_V__lv3_courses = ['Dino Dino Jungle T', 'Donut Plains 1R/T']

Bumble_V__lv6_courses = ['Choco Island 1T', 'Airship Fortress R']

Bumble_V_ = race_tool('Bumble_V_', 'High-End', Bumble_V__TWO_x_Bonus_Points, Bumble_V__ONEoFIVE_x_Bonus_Points, Bumble_V__lv3_courses, Bumble_V__lv6_courses)


#Barrel_Train_
# https://game8.co/games/mariokarttour/archives/270465

Barrel_Train__TWO_x_Bonus_Points = ['Rock Rock Mountain R', 'Rock Rock Mountain', 'Dino Dino Jungle R', 'Kalimari Desert T', 'Kalimari Desert R/T']

Barrel_Train__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain T', 'Shy Guy Bazaar R', 'Koopa Troopa Beach R', 'New York Minute', 'Dino Dino Jungle', 'Kalimari Desert R', 'RMX Mario Circuit 1T', 'RMX Choco Island 2R']

Barrel_Train__lv3_courses = ['Kalimari Desert R']

Barrel_Train__lv6_courses = ['Koopa Troopa Beach R']

Barrel_Train_ = race_tool('Barrel_Train_', 'Super', Barrel_Train__TWO_x_Bonus_Points, Barrel_Train__ONEoFIVE_x_Bonus_Points, Barrel_Train__lv3_courses, Barrel_Train__lv6_courses)


#Flame_Flyer_
# https://game8.co/games/mariokarttour/archives/270464

Flame_Flyer__TWO_x_Bonus_Points = ['Dino Dino Jungle', "Bowser's Castle 1T", 'DK Pass', 'New York Minute 2R/T']

Flame_Flyer__ONEoFIVE_x_Bonus_Points = ['New York Minute R', 'New York Minute R/T', 'Rock Rock Mountain R', 'Shy Guy Bazaar', 'Dino Dino Jungle R', 'Daisy Hills T', 'New York Minute T', 'Neo Bowser City T', 'DK Pass R', 'RMX Mario Circuit 1R', "Bowser's Castle 2R/T"]

Flame_Flyer__lv3_courses = ['Dino Dino Jungle R']

Flame_Flyer__lv6_courses = ['Daisy Hills T']

Flame_Flyer_ = race_tool('Flame_Flyer_', 'Super', Flame_Flyer__TWO_x_Bonus_Points, Flame_Flyer__ONEoFIVE_x_Bonus_Points, Flame_Flyer__lv3_courses, Flame_Flyer__lv6_courses)


#Gold_Blooper_
# https://game8.co/games/mariokarttour/archives/270463

Gold_Blooper__TWO_x_Bonus_Points = ['New York Minute R', 'Mario Circuit 1R', 'Shy Guy Bazaar', 'Cheep Cheep Lagoon R', 'Koopa Troopa Beach T', 'Koopa Troopa Beach']

Gold_Blooper__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit R', 'Cheep Cheep Lagoon T', 'Koopa Troopa Beach R', 'Cheep Cheep Lagoon', 'SNES Rainbow Road', 'SNES Rainbow Road T', "Bowser's Castle 1R/T", 'Yoshi Circuit R/T', 'Donut Plains 1R/T', 'Choco Mountain R', 'RMX Rainbow Road 2']

Gold_Blooper__lv3_courses = ["Bowser's Castle 1R/T"]

Gold_Blooper__lv6_courses = ['Koopa Troopa Beach R']

Gold_Blooper_ = race_tool('Gold_Blooper_', 'Super', Gold_Blooper__TWO_x_Bonus_Points, Gold_Blooper__ONEoFIVE_x_Bonus_Points, Gold_Blooper__lv3_courses, Gold_Blooper__lv6_courses)


#Super_Blooper_
# https://game8.co/games/mariokarttour/archives/270462

Super_Blooper__TWO_x_Bonus_Points = ['Cheep Cheep Lagoon T', 'Koopa Troopa Beach R', 'Cheep Cheep Lagoon', 'Mario Circuit 2R']

Super_Blooper__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit', 'Cheep Cheep Lagoon R', 'Koopa Troopa Beach T', "Bowser's Castle 1T", 'Toad Circuit', 'Choco Island 2', 'Neo Bowser City', 'Vanilla Lake 1R/T', "Rosalina's Ice World R"]

Super_Blooper__lv3_courses = ['Choco Island 2']

Super_Blooper__lv6_courses = ['Toad Circuit']

Super_Blooper_ = race_tool('Super_Blooper_', 'Super', Super_Blooper__TWO_x_Bonus_Points, Super_Blooper__ONEoFIVE_x_Bonus_Points, Super_Blooper__lv3_courses, Super_Blooper__lv6_courses)


#Soda_Jet_
# https://game8.co/games/mariokarttour/archives/270461

Soda_Jet__TWO_x_Bonus_Points = ['Koopa Troopa Beach T', 'New York Minute', 'Cheep Cheep Lagoon', 'Tokyo Blur', 'DS Rainbow Road R/T', 'Vanilla Lake 1R/T', 'Los Angeles Laps R', 'New York Minute 3R']

Soda_Jet__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain T', 'Yoshi Circuit T', 'Mario Circuit 1R', 'Cheep Cheep Lagoon R', 'Koopa Troopa Beach', 'Tokyo Blur T', 'New York Minute 3R', 'New York Minute 3R/T', 'RMX Rainbow Road 2', 'RMX Rainbow Road 2R']

Soda_Jet__lv3_courses = ['Koopa Troopa Beach']

Soda_Jet__lv6_courses = ['Cheep Cheep Lagoon R']

Soda_Jet_ = race_tool('Soda_Jet_', 'Super', Soda_Jet__TWO_x_Bonus_Points, Soda_Jet__ONEoFIVE_x_Bonus_Points, Soda_Jet__lv3_courses, Soda_Jet__lv6_courses)


#Turbo_Yoshi_
# https://game8.co/games/mariokarttour/archives/270460

Turbo_Yoshi__TWO_x_Bonus_Points = ['Yoshi Circuit', 'Mario Circuit 1T', 'Dino Dino Jungle T']

Turbo_Yoshi__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain', 'Yoshi Circuit R', 'Dino Dino Jungle R', 'Dino Dino Jungle', 'Daisy Hills', 'Toad Circuit R', 'Yoshi Circuit R/T', 'Royal Raceway T', 'Royal Raceway']

Turbo_Yoshi__lv3_courses = ['Yoshi Circuit R/T']

Turbo_Yoshi__lv6_courses = ['Daisy Hills']

Turbo_Yoshi_ = race_tool('Turbo_Yoshi_', 'Super', Turbo_Yoshi__TWO_x_Bonus_Points, Turbo_Yoshi__ONEoFIVE_x_Bonus_Points, Turbo_Yoshi__lv3_courses, Turbo_Yoshi__lv6_courses)


#Daytripper_
# https://game8.co/games/mariokarttour/archives/270459

Daytripper__TWO_x_Bonus_Points = ['Shy Guy Bazaar R', 'Daisy Hills', 'Mario Circuit 2']

Daytripper__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 1T', 'New York Minute', 'Daisy Hills T', 'Toad Circuit R', 'SNES Rainbow Road', 'Mario Circuit', 'SNES Rainbow Road T', 'Paris Promenade T', 'Frappe Snowland', 'DK Pass R/T', 'Tokyo Blur 3', 'Tokyo Blur 3R']

Daytripper__lv3_courses = ['DK Pass R/T']

Daytripper__lv6_courses = ['SNES Rainbow Road T']

Daytripper_ = race_tool('Daytripper_', 'Super', Daytripper__TWO_x_Bonus_Points, Daytripper__ONEoFIVE_x_Bonus_Points, Daytripper__lv3_courses, Daytripper__lv6_courses)


#Mach_8_
# https://game8.co/games/mariokarttour/archives/270458

Mach_8__TWO_x_Bonus_Points = ['Rock Rock Mountain T', 'Yoshi Circuit R', 'Shy Guy Bazaar R', 'Mario Circuit 1']

Mach_8__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit T', 'Yoshi Circuit', 'Toad Circuit T', 'Toad Circuit', "Luigi's Mansion T", 'Waluigi Pinball', 'Shy Guy Bazaar R/T', 'Donut Plains 1R', 'Royal Raceway R']

Mach_8__lv3_courses = ['Shy Guy Bazaar R/T']

Mach_8__lv6_courses = ['Toad Circuit']

Mach_8_ = race_tool('Mach_8_', 'Super', Mach_8__TWO_x_Bonus_Points, Mach_8__ONEoFIVE_x_Bonus_Points, Mach_8__lv3_courses, Mach_8__lv6_courses)


#Chrome_DK_Jumbo_
# https://game8.co/games/mariokarttour/archives/270708

Chrome_DK_Jumbo__TWO_x_Bonus_Points = ['Dino Dino Jungle T', 'Kalimari Desert R', 'Tokyo Blur R/T', 'DK Pass T', 'Vanilla Lake 1R', 'Dino Dino Jungle R/T', 'RMX Mario Circuit 1R']

Chrome_DK_Jumbo__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain R', 'Daisy Hills R', "Bowser's Castle 1R", 'Tokyo Blur R', 'Kalimari Desert T', 'Kalimari Desert', 'Tokyo Blur T', 'Paris Promenade R', 'DK Pass R/T', 'Ghost Valley 1R/T', 'Frappe Snowland R/T']

Chrome_DK_Jumbo__lv3_courses = ['Frappe Snowland R/T']

Chrome_DK_Jumbo__lv6_courses = ['Rock Rock Mountain R']

Chrome_DK_Jumbo_ = race_tool('Chrome_DK_Jumbo_', 'Super', Chrome_DK_Jumbo__TWO_x_Bonus_Points, Chrome_DK_Jumbo__ONEoFIVE_x_Bonus_Points, Chrome_DK_Jumbo__lv3_courses, Chrome_DK_Jumbo__lv6_courses)


#DK_Jumbo_
# https://game8.co/games/mariokarttour/archives/270707

DK_Jumbo__TWO_x_Bonus_Points = ['Rock Rock Mountain T', 'Rock Rock Mountain', 'Dino Dino Jungle', 'Choco Island 2R', 'Kalimari Desert']

DK_Jumbo__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain R', 'Dino Dino Jungle T', 'Dino Dino Jungle R', 'Kalimari Desert T', 'Choco Island 2T', 'New York Minute 2T', 'Kalimari Desert R/T', 'New York Minute 2R/T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1R', 'RMX Choco Island 1', 'RMX Choco Island 1R', 'New York Minute 3', 'New York Minute 3', 'New York Minute 3T', 'New York Minute 3T']

DK_Jumbo__lv3_courses = ['Choco Island 2T']

DK_Jumbo__lv6_courses = ['RMX Mario Circuit 1R']

DK_Jumbo_ = race_tool('DK_Jumbo_', 'Super', DK_Jumbo__TWO_x_Bonus_Points, DK_Jumbo__ONEoFIVE_x_Bonus_Points, DK_Jumbo__lv3_courses, DK_Jumbo__lv6_courses)


#Cloud_9_
# https://game8.co/games/mariokarttour/archives/270706

Cloud_9__TWO_x_Bonus_Points = ['SNES Rainbow Road', 'Tokyo Blur T', 'Mario Circuit R/T', 'Cheep Cheep Lagoon R/T', 'Kalimari Desert R/T', 'Mario Circuit 2R/T']

Cloud_9__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar T', 'Cheep Cheep Lagoon', 'Mario Circuit 2', 'Kalimari Desert R', 'Neo Bowser City R', 'Tokyo Blur R/T', 'Paris Promenade R/T', 'SNES Rainbow Road R/T', 'Vanilla Lake 1R', 'Vanilla Lake 1T']

Cloud_9__lv3_courses = ['SNES Rainbow Road R/T']

Cloud_9__lv6_courses = ['Mario Circuit 2']

Cloud_9_ = race_tool('Cloud_9_', 'Super', Cloud_9__TWO_x_Bonus_Points, Cloud_9__ONEoFIVE_x_Bonus_Points, Cloud_9__lv3_courses, Cloud_9__lv6_courses)


#Royale_
# https://game8.co/games/mariokarttour/archives/270705

Royale__TWO_x_Bonus_Points = ['Choco Island 2', 'Mario Circuit R', 'SNES Rainbow Road T']

Royale__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit', 'Mario Circuit 1R', 'Daisy Hills R', 'Daisy Hills', 'Toad Circuit T', 'Toad Circuit R', 'Mario Circuit', 'Paris Promenade T', 'London Loop 2R/T', 'DS Rainbow Road R/T', 'Donut Plains 1T', 'RMX Choco Island 2']

Royale__lv3_courses = ['DS Rainbow Road R/T']

Royale__lv6_courses = ['Donut Plains 1T']

Royale_ = race_tool('Royale_', 'Super', Royale__TWO_x_Bonus_Points, Royale__ONEoFIVE_x_Bonus_Points, Royale__lv3_courses, Royale__lv6_courses)


#Koopa_Clown_
# https://game8.co/games/mariokarttour/archives/270704

Koopa_Clown__TWO_x_Bonus_Points = ['Neo Bowser City', 'SNES Rainbow Road R', 'DS Rainbow Road T', "Bowser's Castle 2R"]

Koopa_Clown__ONEoFIVE_x_Bonus_Points = ["Bowser's Castle 1T", "Bowser's Castle 1R", "Bowser's Castle 1", 'Kalimari Desert R', 'Neo Bowser City R', 'Neo Bowser City T', 'DS Rainbow Road R', 'Kalimari Desert R/T', 'Neo Bowser City R/T', 'DS Rainbow Road R/T', "Bowser's Castle 2", "Bowser's Castle 2T"]

Koopa_Clown__lv3_courses = ['Kalimari Desert R/T']

Koopa_Clown__lv6_courses = ["Bowser's Castle 1"]

Koopa_Clown_ = race_tool('Koopa_Clown_', 'Super', Koopa_Clown__TWO_x_Bonus_Points, Koopa_Clown__ONEoFIVE_x_Bonus_Points, Koopa_Clown__lv3_courses, Koopa_Clown__lv6_courses)


#Poltergust_4000_
# https://game8.co/games/mariokarttour/archives/271634

Poltergust_4000__TWO_x_Bonus_Points = ["Luigi's Mansion R", 'Ghost Valley 1', 'SNES Rainbow Road R/T', "Luigi's Mansion R/T"]

Poltergust_4000__ONEoFIVE_x_Bonus_Points = ['Koopa Troopa Beach T', 'Koopa Troopa Beach', "Luigi's Mansion T", 'Waluigi Pinball', 'Ghost Valley 1R', 'Ghost Valley 1R/T', 'Donut Plains 1R/T', 'Choco Island 1R', 'Donut Plains 2T', 'DK Summit T']

Poltergust_4000__lv3_courses = ['Koopa Troopa Beach T']

Poltergust_4000__lv6_courses = ['Ghost Valley 1R/T']

Poltergust_4000_ = race_tool('Poltergust_4000_', 'Super', Poltergust_4000__TWO_x_Bonus_Points, Poltergust_4000__ONEoFIVE_x_Bonus_Points, Poltergust_4000__lv3_courses, Poltergust_4000__lv6_courses)


#Dark_Clown_
# https://game8.co/games/mariokarttour/archives/271635

Dark_Clown__TWO_x_Bonus_Points = ["Bowser's Castle 1R", 'Waluigi Pinball', 'Vanilla Lake 1R', 'DS Rainbow Road R/T', "Bowser's Castle 2", "Bowser's Castle 2R", "Bowser's Castle 2T"]

Dark_Clown__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain T', "Bowser's Castle 1T", 'Neo Bowser City R', 'Neo Bowser City', 'Waluigi Pinball R', 'Waluigi Pinball T', 'DK Pass']

Dark_Clown__lv3_courses = ['Waluigi Pinball R']

Dark_Clown__lv6_courses = ['Neo Bowser City']

Dark_Clown_ = race_tool('Dark_Clown_', 'Super', Dark_Clown__TWO_x_Bonus_Points, Dark_Clown__ONEoFIVE_x_Bonus_Points, Dark_Clown__lv3_courses, Dark_Clown__lv6_courses)


#Streamliner_
# https://game8.co/games/mariokarttour/archives/272260

Streamliner__TWO_x_Bonus_Points = ['Mario Circuit T', 'Mario Circuit 3', 'Mario Circuit 3T', 'Mario Circuit 1R/T', 'Vancouver Velocity T', 'Mario Circuit 3R/T']

Streamliner__ONEoFIVE_x_Bonus_Points = ['Mario Circuit', 'Paris Promenade', 'Mario Circuit 3R', 'New York Minute 2T', 'DS Rainbow Road', 'Paris Promenade 2T', 'Paris Promenade 2R/T', 'Vancouver Velocity', 'Vancouver Velocity R/T', 'Donut Plains 1', 'Donut Plains 1T', 'RMX Mario Circuit 1R/T']

Streamliner__lv3_courses = ['RMX Mario Circuit 1R/T']

Streamliner__lv6_courses = ['Donut Plains 1T']

Streamliner_ = race_tool('Streamliner_', 'Super', Streamliner__TWO_x_Bonus_Points, Streamliner__ONEoFIVE_x_Bonus_Points, Streamliner__lv3_courses, Streamliner__lv6_courses)


#White_Royale_
# https://game8.co/games/mariokarttour/archives/272261

White_Royale__TWO_x_Bonus_Points = ['Rock Rock Mountain', "Luigi's Mansion", "Luigi's Mansion T", 'Paris Promenade R', 'New York Minute 2R/T', 'Donut Plains 1R', 'Vanilla Lake 1R/T']

White_Royale__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 3T', 'Paris Promenade', 'Paris Promenade R/T', 'New York Minute 2T', 'DS Rainbow Road', 'DS Rainbow Road T', 'Mario Circuit 1R/T', "Bowser's Castle 2R/T"]

White_Royale__lv3_courses = ['Mario Circuit 1R/T']

White_Royale__lv6_courses = ['DS Rainbow Road']

White_Royale_ = race_tool('White_Royale_', 'Super', White_Royale__TWO_x_Bonus_Points, White_Royale__ONEoFIVE_x_Bonus_Points, White_Royale__lv3_courses, White_Royale__lv6_courses)


#Para_Wing_
# https://game8.co/games/mariokarttour/archives/274708

Para_Wing__TWO_x_Bonus_Points = ['Rock Rock Mountain R', 'Ghost Valley 1R', 'Ghost Valley 1T', 'Cheep Cheep Lagoon R/T', 'Vanilla Lake 1R', "Bowser's Castle 2", "Bowser's Castle 2T"]

Para_Wing__ONEoFIVE_x_Bonus_Points = ['Cheep Cheep Lagoon', 'Neo Bowser City', 'London Loop R/T', "Bowser's Castle 1R/T", 'Kalimari Desert R/T', 'Tokyo Blur 2T', 'Neo Bowser City R/T', 'Frappe Snowland', 'Frappe Snowland R/T', 'London Loop 2R', 'London Loop 2T', 'DS Rainbow Road R/T', "Bowser's Castle 2R"]

Para_Wing__lv3_courses = ["Bowser's Castle 1R/T"]

Para_Wing__lv6_courses = ['DS Rainbow Road R/T']

Para_Wing_ = race_tool('Para_Wing_', 'Super', Para_Wing__TWO_x_Bonus_Points, Para_Wing__ONEoFIVE_x_Bonus_Points, Para_Wing__lv3_courses, Para_Wing__lv6_courses)


#Zucchini_
# https://game8.co/games/mariokarttour/archives/274935

Zucchini__TWO_x_Bonus_Points = ['Yoshi Circuit', 'Mario Circuit 1R', 'Cheep Cheep Lagoon R', 'Daisy Hills T', 'Toad Circuit R', 'Yoshi Circuit R/T']

Zucchini__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit R', 'Toad Circuit', 'Mario Circuit 1', 'Choco Island 2', 'Mario Circuit 3', 'Mario Circuit 3R', 'Mario Circuit 1R/T', 'Royal Raceway T']

Zucchini__lv3_courses = ['Mario Circuit 1R/T', 'Mario Circuit 1R/T']

Zucchini__lv6_courses = ['Mario Circuit 1']

Zucchini_ = race_tool('Zucchini_', 'Super', Zucchini__TWO_x_Bonus_Points, Zucchini__ONEoFIVE_x_Bonus_Points, Zucchini__lv3_courses, Zucchini__lv6_courses)


#Turbo_Birdo_
# https://game8.co/games/mariokarttour/archives/275171

Turbo_Birdo__TWO_x_Bonus_Points = ["Luigi's Mansion T", 'Yoshi Circuit R/T', 'New York Minute 2R', 'Choco Island 2R/T', 'London Loop 2T']

Turbo_Birdo__ONEoFIVE_x_Bonus_Points = ['Daisy Hills', 'Choco Island 2R', "Luigi's Mansion R/T", 'DS Rainbow Road', 'DS Rainbow Road R', 'Neo Bowser City R/T', 'Frappe Snowland T', 'Frappe Snowland R', 'Vanilla Lake 1T', 'Dino Dino Jungle R/T', 'Waluigi Pinball R/T', "Bowser's Castle 2R", "Bowser's Castle 2T", 'Donut Plains 1R/T']

Turbo_Birdo__lv3_courses = ['Dino Dino Jungle R/T']

Turbo_Birdo__lv6_courses = ['Daisy Hills']

Turbo_Birdo_ = race_tool('Turbo_Birdo_', 'Super', Turbo_Birdo__TWO_x_Bonus_Points, Turbo_Birdo__ONEoFIVE_x_Bonus_Points, Turbo_Birdo__lv3_courses, Turbo_Birdo__lv6_courses)


#Red_Streamliner_
# https://game8.co/games/mariokarttour/archives/275190

Red_Streamliner__TWO_x_Bonus_Points = ['Yoshi Circuit R', 'Toad Circuit', 'Tokyo Blur R', 'Mario Circuit 2T', 'Mario Circuit', 'Yoshi Circuit R/T', 'Mario Circuit 2R/T', 'RMX Mario Circuit 1R/T', 'Berlin Byways 2R']

Red_Streamliner__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 2R', 'Mario Circuit T', "Luigi's Mansion R/T", 'New York Minute 2R', 'New York Minute 2', 'Mario Circuit 1R/T', 'Tokyo Blur 2R', 'Tokyo Blur 2T', 'Shy Guy Bazaar R/T', 'Paris Promenade 2R', 'Paris Promenade 2', 'Vancouver Velocity R/T', 'Tokyo Blur 3T', 'Berlin Byways 2T']

Red_Streamliner__lv3_courses = ["Luigi's Mansion R/T"]

Red_Streamliner__lv6_courses = ['Mario Circuit 2R']

Red_Streamliner_ = race_tool('Red_Streamliner_', 'Super', Red_Streamliner__TWO_x_Bonus_Points, Red_Streamliner__ONEoFIVE_x_Bonus_Points, Red_Streamliner__lv3_courses, Red_Streamliner__lv6_courses)


#Red_Turbo_Yoshi_
# https://game8.co/games/mariokarttour/archives/275396

Red_Turbo_Yoshi__TWO_x_Bonus_Points = ['Yoshi Circuit T', 'Mario Circuit 2', 'Daisy Hills R/T', 'Tokyo Blur 2T', 'Frappe Snowland R', 'Koopa Troopa Beach R/T', 'RMX Mario Circuit 1']

Red_Turbo_Yoshi__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit', 'Tokyo Blur R/T', 'Paris Promenade', 'Paris Promenade R', 'Tokyo Blur 2', 'Tokyo Blur 2R', 'Frappe Snowland T', 'Vanilla Lake 1R', 'Choco Island 2R/T', 'Mario Circuit 3R/T', 'Donut Plains 1T', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', 'Koopa Troopa Beach 2T']

Red_Turbo_Yoshi__lv3_courses = ['Mario Circuit 3R/T']

Red_Turbo_Yoshi__lv6_courses = ['Yoshi Circuit']

Red_Turbo_Yoshi_ = race_tool('Red_Turbo_Yoshi_', 'Super', Red_Turbo_Yoshi__TWO_x_Bonus_Points, Red_Turbo_Yoshi__ONEoFIVE_x_Bonus_Points, Red_Turbo_Yoshi__lv3_courses, Red_Turbo_Yoshi__lv6_courses)


#Blue_Seven_
# https://game8.co/games/mariokarttour/archives/275778

Blue_Seven__TWO_x_Bonus_Points = ['Yoshi Circuit R', 'DK Pass T', 'DS Rainbow Road R', 'Frappe Snowland T', 'Vanilla Lake 1', 'Shy Guy Bazaar R/T', 'Frappe Snowland R/T', 'RMX Mario Circuit 1T', 'Koopa Troopa Beach 2R']

Blue_Seven__ONEoFIVE_x_Bonus_Points = ['Frappe Snowland R', 'Vanilla Lake 1R', 'Vanilla Lake 1T', 'Vancouver Velocity T', 'Vancouver Velocity R', 'DS Rainbow Road R/T', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2T']

Blue_Seven__lv3_courses = ['DS Rainbow Road R/T']

Blue_Seven__lv6_courses = ['Frappe Snowland R']

Blue_Seven_ = race_tool('Blue_Seven_', 'Super', Blue_Seven__TWO_x_Bonus_Points, Blue_Seven__ONEoFIVE_x_Bonus_Points, Blue_Seven__lv3_courses, Blue_Seven__lv6_courses)


#Light_blue_Turbo_Birdo_
# https://game8.co/games/mariokarttour/archives/279957

Light_blue_Turbo_Birdo__TWO_x_Bonus_Points = ['Dino Dino Jungle R', "Luigi's Mansion R", "Luigi's Mansion T", 'Frappe Snowland', 'DK Pass R/T', 'Vancouver Velocity R', 'Koopa Troopa Beach R/T']

Light_blue_Turbo_Birdo__ONEoFIVE_x_Bonus_Points = ['Koopa Troopa Beach T', 'Koopa Troopa Beach R', 'Cheep Cheep Lagoon', 'Kalimari Desert R', "Luigi's Mansion", 'Cheep Cheep Lagoon R/T', 'Vanilla Lake 1', 'Vancouver Velocity T', 'Vancouver Velocity', 'Frappe Snowland R/T', 'Donut Plains 1R/T', 'Airship Fortress R']

Light_blue_Turbo_Birdo__lv3_courses = ['Frappe Snowland R/T']

Light_blue_Turbo_Birdo__lv6_courses = ['Koopa Troopa Beach T']

Light_blue_Turbo_Birdo_ = race_tool('Light_blue_Turbo_Birdo_', 'Super', Light_blue_Turbo_Birdo__TWO_x_Bonus_Points, Light_blue_Turbo_Birdo__ONEoFIVE_x_Bonus_Points, Light_blue_Turbo_Birdo__lv3_courses, Light_blue_Turbo_Birdo__lv6_courses)


#Super_1_
# https://game8.co/games/mariokarttour/archives/281113

Super_1__TWO_x_Bonus_Points = ['Toad Circuit', 'Tokyo Blur T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1R', 'Donut Plains 1', 'RMX Mario Circuit 1R/T', 'Maple Treeway T']

Super_1__ONEoFIVE_x_Bonus_Points = ['Koopa Troopa Beach', 'Tokyo Blur R', 'Tokyo Blur', 'Cheep Cheep Lagoon R/T', 'RMX Mario Circuit 1T', 'London Loop 2', 'London Loop 2R/T', 'Maple Treeway R', 'Sunset Wilds R/T']

Super_1__lv3_courses = ['Koopa Troopa Beach']

Super_1__lv6_courses = ['RMX Mario Circuit 1T']

Super_1_ = race_tool('Super_1_', 'Super', Super_1__TWO_x_Bonus_Points, Super_1__ONEoFIVE_x_Bonus_Points, Super_1__lv3_courses, Super_1__lv6_courses)


#Dasher_II_
# https://game8.co/games/mariokarttour/archives/281114

Dasher_II__TWO_x_Bonus_Points = ['Shy Guy Bazaar R', 'Choco Island 2', 'Waluigi Pinball R', 'RMX Mario Circuit 1T']

Dasher_II__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar T', 'Choco Island 2T', "Luigi's Mansion", "Luigi's Mansion R", 'Waluigi Pinball', 'Ghost Valley 1R/T', 'RMX Mario Circuit 1', 'London Loop 2R', 'London Loop 2T', 'Donut Plains 1', 'Donut Plains 1R/T', 'RMX Mario Circuit 1R/T', 'RMX Rainbow Road 1R/T', 'RMX Choco Island 2R']

Dasher_II__lv3_courses = ['Choco Island 2T']

Dasher_II__lv6_courses = ['Donut Plains 1R/T']

Dasher_II_ = race_tool('Dasher_II_', 'Super', Dasher_II__TWO_x_Bonus_Points, Dasher_II__ONEoFIVE_x_Bonus_Points, Dasher_II__lv3_courses, Dasher_II__lv6_courses)


#Tea_Coupe_
# https://game8.co/games/mariokarttour/archives/282824

Tea_Coupe__TWO_x_Bonus_Points = ['Tokyo Blur R', 'Paris Promenade T', 'London Loop R', 'RMX Mario Circuit 1T', 'London Loop 2', 'London Loop 2R', 'Donut Plains 1R', 'Donut Plains 1T', 'Donut Plains 1R/T', 'Choco Island 1']

Tea_Coupe__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar T', 'Daisy Hills T', 'Daisy Hills', 'Paris Promenade', 'Tokyo Blur 2', 'Choco Island 2R/T', 'London Loop 2T', 'London Loop 2R/T', 'Donut Plains 1', 'Vanilla Lake 1R/T', 'Choco Island 1T', 'Tokyo Blur 3']

Tea_Coupe__lv3_courses = ['Choco Island 2R/T']

Tea_Coupe__lv6_courses = ['Shy Guy Bazaar T']

Tea_Coupe_ = race_tool('Tea_Coupe_', 'Super', Tea_Coupe__TWO_x_Bonus_Points, Tea_Coupe__ONEoFIVE_x_Bonus_Points, Tea_Coupe__lv3_courses, Tea_Coupe__lv6_courses)


#Yellow_Turbo_Birdo_
# https://game8.co/games/mariokarttour/archives/285891

Yellow_Turbo_Birdo__TWO_x_Bonus_Points = ["Luigi's Mansion", 'Ghost Valley 1', 'Donut Plains 1R/T', "Bowser's Castle 2R/T", 'Choco Mountain R']

Yellow_Turbo_Birdo__ONEoFIVE_x_Bonus_Points = ['SNES Rainbow Road', "Luigi's Mansion R", "Luigi's Mansion T", 'Ghost Valley 1R', 'Ghost Valley 1T', 'Yoshi Circuit R/T', 'Cheep Cheep Lagoon R/T', 'Kalimari Desert R/T', 'Koopa Troopa Beach R/T', 'RMX Mario Circuit 1R/T', 'Choco Mountain']

Yellow_Turbo_Birdo__lv3_courses = ['Yoshi Circuit R/T']

Yellow_Turbo_Birdo__lv6_courses = ['RMX Mario Circuit 1R/T']

Yellow_Turbo_Birdo_ = race_tool('Yellow_Turbo_Birdo_', 'Super', Yellow_Turbo_Birdo__TWO_x_Bonus_Points, Yellow_Turbo_Birdo__ONEoFIVE_x_Bonus_Points, Yellow_Turbo_Birdo__lv3_courses, Yellow_Turbo_Birdo__lv6_courses)


#Egg_1_
# https://game8.co/games/mariokarttour/archives/285892

Egg_1__TWO_x_Bonus_Points = ['Yoshi Circuit R', 'Mario Circuit 1', 'Choco Island 2R', 'SNES Rainbow Road T', 'Paris Promenade T', 'Yoshi Circuit R/T', 'Tokyo Blur 2R', 'Vanilla Lake 1R', 'Dino Dino Jungle R/T', 'Donut Plains 1R/T']

Egg_1__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit T', 'Yoshi Circuit', 'Mario Circuit 1R', 'Koopa Troopa Beach R', 'Tokyo Blur 2', 'Toad Circuit R/T', 'Koopa Troopa Beach R/T', 'Choco Mountain R', 'Choco Mountain T']

Egg_1__lv3_courses = ['Mario Circuit 1R']

Egg_1__lv6_courses = ['Koopa Troopa Beach R/T']

Egg_1_ = race_tool('Egg_1_', 'Super', Egg_1__TWO_x_Bonus_Points, Egg_1__ONEoFIVE_x_Bonus_Points, Egg_1__lv3_courses, Egg_1__lv6_courses)


#Birthday_Girl_Daisy_
# https://game8.co/games/mariokarttour/archives/286869

Birthday_Girl_Daisy__TWO_x_Bonus_Points = ['Daisy Hills', 'Yoshi Circuit R/T', 'RMX Choco Island 1R', 'Choco Island 1R']

Birthday_Girl_Daisy__ONEoFIVE_x_Bonus_Points = ['Daisy Hills R', 'Mario Circuit', "Luigi's Mansion R", 'Choco Island 2R/T', 'RMX Choco Island 1', 'RMX Choco Island 1T', 'Choco Island 1T', 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'New York Minute 3', 'New York Minute 3T', 'Maple Treeway R', 'DK Summit R']

Birthday_Girl_Daisy__lv3_courses = ['Choco Island 2R/T']

Birthday_Girl_Daisy__lv6_courses = ["Luigi's Mansion R"]

Birthday_Girl_Daisy_ = race_tool('Birthday_Girl_Daisy_', 'Super', Birthday_Girl_Daisy__TWO_x_Bonus_Points, Birthday_Girl_Daisy__ONEoFIVE_x_Bonus_Points, Birthday_Girl_Daisy__lv3_courses, Birthday_Girl_Daisy__lv6_courses)


#Bolt_Buggy_
# https://game8.co/games/mariokarttour/archives/288931

Bolt_Buggy__TWO_x_Bonus_Points = ['Dino Dino Jungle R', 'Dino Dino Jungle', 'Kalimari Desert R', 'Vanilla Lake 1', 'Vanilla Lake 1R', 'Donut Plains 1']

Bolt_Buggy__ONEoFIVE_x_Bonus_Points = ['Dino Dino Jungle T', 'Kalimari Desert T', 'Kalimari Desert', 'DK Pass R', 'Donut Plains 1R', 'RMX Choco Island 1', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2T', 'Airship Fortress', 'Airship Fortress T', 'Los Angeles Laps', 'Los Angeles Laps R', "Rosalina's Ice World R", "Rosalina's Ice World T", 'Donut Plains 2', 'Donut Plains 2R']

Bolt_Buggy__lv3_courses = ['Kalimari Desert T']

Bolt_Buggy__lv6_courses = ['Donut Plains 1R']

Bolt_Buggy_ = race_tool('Bolt_Buggy_', 'Super', Bolt_Buggy__TWO_x_Bonus_Points, Bolt_Buggy__ONEoFIVE_x_Bonus_Points, Bolt_Buggy__lv3_courses, Bolt_Buggy__lv6_courses)


#Rambi_Rider_
# https://game8.co/games/mariokarttour/archives/288932

Rambi_Rider__TWO_x_Bonus_Points = ['Rock Rock Mountain R', 'Rock Rock Mountain', 'Dino Dino Jungle T', 'Kalimari Desert T', 'DK Pass']

Rambi_Rider__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain T', 'Dino Dino Jungle R', 'Dino Dino Jungle', 'Kalimari Desert R', 'Kalimari Desert', 'DK Pass R', 'RMX Choco Island 1R', 'Choco Island 1R', 'Choco Island 1T', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', 'RMX Rainbow Road 1R']

Rambi_Rider__lv3_courses = ['Kalimari Desert R']

Rambi_Rider__lv6_courses = ['Dino Dino Jungle R']

Rambi_Rider_ = race_tool('Rambi_Rider_', 'Super', Rambi_Rider__TWO_x_Bonus_Points, Rambi_Rider__ONEoFIVE_x_Bonus_Points, Rambi_Rider__lv3_courses, Rambi_Rider__lv6_courses)


#Red_Standard_8_
# https://game8.co/games/mariokarttour/archives/309242

Red_Standard_8__TWO_x_Bonus_Points = ['Mario Circuit 2T', 'Mario Circuit 3T', 'Mario Circuit 2R/T', 'RMX Mario Circuit 1', 'Donut Plains 1R', 'Donut Plains 1R/T', 'Royal Raceway']

Red_Standard_8__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 1', 'Mario Circuit 2', 'Mario Circuit R/T', 'DS Rainbow Road R', 'Mario Circuit 1R/T', 'Choco Island 2R/T', 'RMX Mario Circuit 1R', 'Choco Island 1R', 'Koopa Troopa Beach 2T', 'RMX Rainbow Road 1R/T', "Rosalina's Ice World", 'Donut Plains 2']

Red_Standard_8__lv3_courses = ['Choco Island 2R/T']

Red_Standard_8__lv6_courses = ['Mario Circuit R/T']

Red_Standard_8_ = race_tool('Red_Standard_8_', 'Super', Red_Standard_8__TWO_x_Bonus_Points, Red_Standard_8__ONEoFIVE_x_Bonus_Points, Red_Standard_8__lv3_courses, Red_Standard_8__lv6_courses)


#Green_Standard_8_
# https://game8.co/games/mariokarttour/archives/309243

Green_Standard_8__TWO_x_Bonus_Points = ['Yoshi Circuit T', 'Mario Circuit 1R', 'Mario Circuit 2', "Luigi's Mansion R/T", 'RMX Mario Circuit 1T', 'RMX Mario Circuit 1R/T', 'Royal Raceway T']

Green_Standard_8__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit R', 'Mario Circuit 2T', "Bowser's Castle 1R/T", 'Waluigi Pinball R/T', 'Ghost Valley 1R/T', 'RMX Mario Circuit 1', 'Sunset Wilds R/T', 'Merry Mountain T', "Rosalina's Ice World T", 'Berlin Byways 2T', 'Donut Plains 2T']

Green_Standard_8__lv3_courses = ['Waluigi Pinball R/T']

Green_Standard_8__lv6_courses = ["Bowser's Castle 1R/T"]

Green_Standard_8_ = race_tool('Green_Standard_8_', 'Super', Green_Standard_8__TWO_x_Bonus_Points, Green_Standard_8__ONEoFIVE_x_Bonus_Points, Green_Standard_8__lv3_courses, Green_Standard_8__lv6_courses)


#Cucumber_
# https://game8.co/games/mariokarttour/archives/316096

Cucumber__TWO_x_Bonus_Points = ['Koopa Troopa Beach 2T', 'Kalimari Desert 2', 'Sunset Wilds R/T', 'Merry Mountain', 'Berlin Byways 2R/T']

Cucumber__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain T', 'Rock Rock Mountain', 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'Berlin Byways 2', 'RMX Choco Island 2T']

Cucumber__lv3_courses = ['Kalimari Desert 2T']

Cucumber__lv6_courses = ['Rock Rock Mountain']

Cucumber_ = race_tool('Cucumber_', 'Super', Cucumber__TWO_x_Bonus_Points, Cucumber__ONEoFIVE_x_Bonus_Points, Cucumber__lv3_courses, Cucumber__lv6_courses)


#Decal_Streamliner_
# https://game8.co/games/mariokarttour/archives/322568

Decal_Streamliner__TWO_x_Bonus_Points = ['Mario Circuit 1T', 'DK Summit', 'Tokyo Blur 4', 'Tokyo Blur 4T', 'Tokyo Blur 4T']

Decal_Streamliner__ONEoFIVE_x_Bonus_Points = ['Toad Circuit', 'Mario Circuit 1R/T', 'DK Summit T', 'Tokyo Blur 4R', 'Tokyo Blur 4R/T']

Decal_Streamliner__lv3_courses = ['Toad Circuit', 'DK Summit T']

Decal_Streamliner__lv6_courses = ['Mario Circuit 1R/T', 'Tokyo Blur 4R/T']

Decal_Streamliner_ = race_tool('Decal_Streamliner_', 'High-End', Decal_Streamliner__TWO_x_Bonus_Points, Decal_Streamliner__ONEoFIVE_x_Bonus_Points, Decal_Streamliner__lv3_courses, Decal_Streamliner__lv6_courses)


#Bumble_V_
# https://game8.co/games/mariokarttour/archives/271639

Bumble_V__TWO_x_Bonus_Points = ['Dino Dino Jungle R', 'Daisy Hills', 'Mario Circuit 2R', 'Waluigi Pinball', 'Waluigi Pinball T', 'Mario Circuit 3', 'SNES Rainbow Road R/T', 'Paris Promenade 2T', 'Paris Promenade 2R/T', 'Waluigi Pinball R/T']

Bumble_V__ONEoFIVE_x_Bonus_Points = ['Dino Dino Jungle T', 'London Loop', 'London Loop R', 'Paris Promenade 2R', 'Paris Promenade 2', 'Donut Plains 1R/T', 'Choco Island 1T', 'Airship Fortress R', 'Airship Fortress T', 'Los Angeles Laps T', 'Los Angeles Laps R/T', "Rosalina's Ice World R", "Rosalina's Ice World T"]

Bumble_V__lv3_courses = ['Dino Dino Jungle T', 'Donut Plains 1R/T']

Bumble_V__lv6_courses = ['Choco Island 1T', 'Airship Fortress R']

Bumble_V_ = race_tool('Bumble_V_', 'High-End', Bumble_V__TWO_x_Bonus_Points, Bumble_V__ONEoFIVE_x_Bonus_Points, Bumble_V__lv3_courses, Bumble_V__lv6_courses)


#Bulls_Eye_Banzai_
# https://game8.co/games/mariokarttour/archives/270457

Bulls_Eye_Banzai__TWO_x_Bonus_Points = ["Bowser's Castle 1T", 'New York Minute T', "Bowser's Castle 2"]

Bulls_Eye_Banzai__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain', 'Shy Guy Bazaar T', 'Shy Guy Bazaar R', 'Shy Guy Bazaar', "Bowser's Castle 1R", "Bowser's Castle 1", 'SNES Rainbow Road', 'RMX Mario Circuit 1R', "Bowser's Castle 2T", "Bowser's Castle 2R/T", 'Airship Fortress R', 'Airship Fortress T']

Bulls_Eye_Banzai__lv3_courses = []

Bulls_Eye_Banzai__lv6_courses = ["Bowser's Castle 1"]

Bulls_Eye_Banzai_ = race_tool('Bulls_Eye_Banzai_', 'Normal', Bulls_Eye_Banzai__TWO_x_Bonus_Points, Bulls_Eye_Banzai__ONEoFIVE_x_Bonus_Points, Bulls_Eye_Banzai__lv3_courses, Bulls_Eye_Banzai__lv6_courses)


#Bullet_Blaster_
# https://game8.co/games/mariokarttour/archives/270456

Bullet_Blaster__TWO_x_Bonus_Points = ['Shy Guy Bazaar T', "Bowser's Castle 1"]

Bullet_Blaster__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain R', 'Shy Guy Bazaar', "Bowser's Castle 1R", 'Kalimari Desert', 'Neo Bowser City', 'RMX Mario Circuit 1R', "Bowser's Castle 2R/T", 'Airship Fortress', 'Airship Fortress R']

Bullet_Blaster__lv3_courses = []

Bullet_Blaster__lv6_courses = ["Bowser's Castle 1R"]

Bullet_Blaster_ = race_tool('Bullet_Blaster_', 'Normal', Bullet_Blaster__TWO_x_Bonus_Points, Bullet_Blaster__ONEoFIVE_x_Bonus_Points, Bullet_Blaster__lv3_courses, Bullet_Blaster__lv6_courses)


#Koopa_Dasher_
# https://game8.co/games/mariokarttour/archives/270455

Koopa_Dasher__TWO_x_Bonus_Points = ['Koopa Troopa Beach']

Koopa_Dasher__ONEoFIVE_x_Bonus_Points = ['Shy Guy Bazaar R', 'Cheep Cheep Lagoon T', 'Cheep Cheep Lagoon R', 'Koopa Troopa Beach T', 'Koopa Troopa Beach R', 'Dino Dino Jungle T', 'Mario Circuit 2R', 'Choco Island 2R', 'Kalimari Desert T', 'RMX Mario Circuit 1', "Bowser's Castle 2R/T"]

Koopa_Dasher__lv3_courses = []

Koopa_Dasher__lv6_courses = ['Choco Island 2R']

Koopa_Dasher_ = race_tool('Koopa_Dasher_', 'Normal', Koopa_Dasher__TWO_x_Bonus_Points, Koopa_Dasher__ONEoFIVE_x_Bonus_Points, Koopa_Dasher__lv3_courses, Koopa_Dasher__lv6_courses)


#Mushmellow_
# https://game8.co/games/mariokarttour/archives/270454

Mushmellow__TWO_x_Bonus_Points = ['Toad Circuit T', 'Toad Circuit']

Mushmellow__ONEoFIVE_x_Bonus_Points = ['Cheep Cheep Lagoon R', 'Daisy Hills', 'Toad Circuit R', 'Mario Circuit 3T', 'Vanilla Lake 1R/T']

Mushmellow__lv3_courses = []

Mushmellow__lv6_courses = ['Vanilla Lake 1R/T']

Mushmellow_ = race_tool('Mushmellow_', 'Normal', Mushmellow__TWO_x_Bonus_Points, Mushmellow__ONEoFIVE_x_Bonus_Points, Mushmellow__lv3_courses, Mushmellow__lv6_courses)


#Birthday_Girl_
# https://game8.co/games/mariokarttour/archives/270453

Birthday_Girl__TWO_x_Bonus_Points = ['Daisy Hills R', 'Toad Circuit T', 'Choco Island 2T']

Birthday_Girl__ONEoFIVE_x_Bonus_Points = ['Yoshi Circuit T', 'Daisy Hills T', 'Daisy Hills', 'Mario Circuit R', 'Frappe Snowland R', 'Choco Island 2R/T', 'London Loop 2', 'London Loop 2T']

Birthday_Girl__lv3_courses = []

Birthday_Girl__lv6_courses = ['Daisy Hills']

Birthday_Girl_ = race_tool('Birthday_Girl_', 'Normal', Birthday_Girl__TWO_x_Bonus_Points, Birthday_Girl__ONEoFIVE_x_Bonus_Points, Birthday_Girl__lv3_courses, Birthday_Girl__lv6_courses)


#Pipe_Frame_
# https://game8.co/games/mariokarttour/archives/270428

Pipe_Frame__TWO_x_Bonus_Points = ['Mario Circuit 1R']

Pipe_Frame__ONEoFIVE_x_Bonus_Points = ['Koopa Troopa Beach R', 'Koopa Troopa Beach', 'Dino Dino Jungle', 'Toad Circuit T', 'Mario Circuit 1', 'Mario Circuit 2', 'London Loop R', "Luigi's Mansion R/T", 'RMX Mario Circuit 1R/T', 'Choco Island 1', 'Maple Treeway']

Pipe_Frame__lv3_courses = []

Pipe_Frame__lv6_courses = ["Luigi's Mansion R/T"]

Pipe_Frame_ = race_tool('Pipe_Frame_', 'Normal', Pipe_Frame__TWO_x_Bonus_Points, Pipe_Frame__ONEoFIVE_x_Bonus_Points, Pipe_Frame__lv3_courses, Pipe_Frame__lv6_courses)


#Landship_
# https://game8.co/games/mariokarttour/archives/270703

Landship__TWO_x_Bonus_Points = ["Bowser's Castle 1R", 'Kalimari Desert T', 'Kalimari Desert R', "Bowser's Castle 1R/T"]

Landship__ONEoFIVE_x_Bonus_Points = ["Bowser's Castle 1", 'Neo Bowser City R', 'RMX Mario Circuit 1R', "Bowser's Castle 2R/T", 'Koopa Troopa Beach 2R', 'Koopa Troopa Beach 2T']

Landship__lv3_courses = []

Landship__lv6_courses = ["Bowser's Castle 1"]

Landship_ = race_tool('Landship_', 'Normal', Landship__TWO_x_Bonus_Points, Landship__ONEoFIVE_x_Bonus_Points, Landship__lv3_courses, Landship__lv6_courses)


#Cheep_Charger_
# https://game8.co/games/mariokarttour/archives/270702

Cheep_Charger__TWO_x_Bonus_Points = ['Cheep Cheep Lagoon R', 'Koopa Troopa Beach R', 'Choco Island 2R']

Cheep_Charger__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 1R', 'Koopa Troopa Beach', 'Cheep Cheep Lagoon', 'Mario Circuit 2T', 'Choco Island 2', 'SNES Rainbow Road R', 'Cheep Cheep Lagoon R/T']

Cheep_Charger__lv3_courses = []

Cheep_Charger__lv6_courses = ['Cheep Cheep Lagoon R/T']

Cheep_Charger_ = race_tool('Cheep_Charger_', 'Normal', Cheep_Charger__TWO_x_Bonus_Points, Cheep_Charger__ONEoFIVE_x_Bonus_Points, Cheep_Charger__lv3_courses, Cheep_Charger__lv6_courses)


#Blue_Biddybuggy_
# https://game8.co/games/mariokarttour/archives/270701

Blue_Biddybuggy__TWO_x_Bonus_Points = ['Mario Circuit 2R', 'Kalimari Desert T']

Blue_Biddybuggy__ONEoFIVE_x_Bonus_Points = ['Toad Circuit', 'Mario Circuit 1', 'Cheep Cheep Lagoon', 'Tokyo Blur', 'Mario Circuit 2T', 'Mario Circuit 2', 'Choco Island 2R', 'Tokyo Blur T', 'Ghost Valley 1T', 'Vanilla Lake 1R/T']

Blue_Biddybuggy__lv3_courses = []

Blue_Biddybuggy__lv6_courses = ['Choco Island 2R']

Blue_Biddybuggy_ = race_tool('Blue_Biddybuggy_', 'Normal', Blue_Biddybuggy__TWO_x_Bonus_Points, Blue_Biddybuggy__ONEoFIVE_x_Bonus_Points, Blue_Biddybuggy__lv3_courses, Blue_Biddybuggy__lv6_courses)


#Biddybuggy_
# https://game8.co/games/mariokarttour/archives/270700

Biddybuggy__TWO_x_Bonus_Points = ['Koopa Troopa Beach T', 'Choco Island 2']

Biddybuggy__ONEoFIVE_x_Bonus_Points = ['Cheep Cheep Lagoon T', 'Toad Circuit R', 'Tokyo Blur', 'Mario Circuit', 'Choco Island 2T', 'Mario Circuit T', 'Toad Circuit R/T']

Biddybuggy__lv3_courses = []

Biddybuggy__lv6_courses = ['Toad Circuit R/T']

Biddybuggy_ = race_tool('Biddybuggy_', 'Normal', Biddybuggy__TWO_x_Bonus_Points, Biddybuggy__ONEoFIVE_x_Bonus_Points, Biddybuggy__lv3_courses, Biddybuggy__lv6_courses)


#Pipe_Buggy_
# https://game8.co/games/mariokarttour/archives/271632

Pipe_Buggy__TWO_x_Bonus_Points = ['Waluigi Pinball R']

Pipe_Buggy__ONEoFIVE_x_Bonus_Points = ['Dino Dino Jungle T', 'Dino Dino Jungle R', 'Waluigi Pinball', 'Waluigi Pinball T', 'DK Pass', 'Dino Dino Jungle R/T', 'Waluigi Pinball R/T']

Pipe_Buggy__lv3_courses = []

Pipe_Buggy__lv6_courses = ['Dino Dino Jungle R/T']

Pipe_Buggy_ = race_tool('Pipe_Buggy_', 'Normal', Pipe_Buggy__TWO_x_Bonus_Points, Pipe_Buggy__ONEoFIVE_x_Bonus_Points, Pipe_Buggy__lv3_courses, Pipe_Buggy__lv6_courses)


#Warship_
# https://game8.co/games/mariokarttour/archives/271633

Warship__TWO_x_Bonus_Points = ['Neo Bowser City R', 'Ghost Valley 1R']

Warship__ONEoFIVE_x_Bonus_Points = ["Bowser's Castle 1", 'Kalimari Desert', "Luigi's Mansion", 'Ghost Valley 1', 'Neo Bowser City R/T', 'Los Angeles Laps T']

Warship__lv3_courses = []

Warship__lv6_courses = ['Neo Bowser City R/T']

Warship_ = race_tool('Warship_', 'Normal', Warship__TWO_x_Bonus_Points, Warship__ONEoFIVE_x_Bonus_Points, Warship__lv3_courses, Warship__lv6_courses)


#Pink_Mushmellow_
# https://game8.co/games/mariokarttour/archives/272259

Pink_Mushmellow__TWO_x_Bonus_Points = ['Mario Circuit 3R']

Pink_Mushmellow__ONEoFIVE_x_Bonus_Points = ['Rock Rock Mountain R', 'Mario Circuit 3', 'Paris Promenade R/T', 'DK Pass T', 'Daisy Hills R/T', 'London Loop', 'London Loop R/T', 'Paris Promenade 2T', 'Dino Dino Jungle R/T', 'Donut Plains 1R', 'Donut Plains 1T', 'Donut Plains 1R/T', 'RMX Choco Island 1R', 'Merry Mountain', 'Donut Plains 2R']

Pink_Mushmellow__lv3_courses = []

Pink_Mushmellow__lv6_courses = ['Daisy Hills R/T']

Pink_Mushmellow_ = race_tool('Pink_Mushmellow_', 'Normal', Pink_Mushmellow__TWO_x_Bonus_Points, Pink_Mushmellow__ONEoFIVE_x_Bonus_Points, Pink_Mushmellow__lv3_courses, Pink_Mushmellow__lv6_courses)


#Green_Cheep_Charger_
# https://game8.co/games/mariokarttour/archives/273758

Green_Cheep_Charger__TWO_x_Bonus_Points = ['Daisy Hills T', 'Cheep Cheep Lagoon', 'Dino Dino Jungle R/T']

Green_Cheep_Charger__ONEoFIVE_x_Bonus_Points = ['Cheep Cheep Lagoon T', 'Ghost Valley 1R', 'Mario Circuit R/T', 'London Loop T', 'Yoshi Circuit R/T', 'Cheep Cheep Lagoon R/T', 'Paris Promenade 2R', 'Ghost Valley 1R/T', 'Donut Plains 1R/T', 'Los Angeles Laps R']

Green_Cheep_Charger__lv3_courses = []

Green_Cheep_Charger__lv6_courses = ['Cheep Cheep Lagoon R/T']

Green_Cheep_Charger_ = race_tool('Green_Cheep_Charger_', 'Normal', Green_Cheep_Charger__TWO_x_Bonus_Points, Green_Cheep_Charger__ONEoFIVE_x_Bonus_Points, Green_Cheep_Charger__lv3_courses, Green_Cheep_Charger__lv6_courses)


#Birthday_Girl_Rosalina_
# https://game8.co/games/mariokarttour/archives/274709

Birthday_Girl_Rosalina__TWO_x_Bonus_Points = ['Daisy Hills T', 'Ghost Valley 1R', 'Toad Circuit R/T']

Birthday_Girl_Rosalina__ONEoFIVE_x_Bonus_Points = ['Mario Circuit R/T', 'London Loop R', 'London Loop R/T', 'Tokyo Blur 2R', 'Mario Circuit 2R/T', 'Frappe Snowland', 'Frappe Snowland T', 'Vanilla Lake 1', 'Vanilla Lake 1T', 'London Loop 2']

Birthday_Girl_Rosalina__lv3_courses = []

Birthday_Girl_Rosalina__lv6_courses = ['Mario Circuit 2R/T']

Birthday_Girl_Rosalina_ = race_tool('Birthday_Girl_Rosalina_', 'Normal', Birthday_Girl_Rosalina__TWO_x_Bonus_Points, Birthday_Girl_Rosalina__ONEoFIVE_x_Bonus_Points, Birthday_Girl_Rosalina__lv3_courses, Birthday_Girl_Rosalina__lv6_courses)


#Green_Kiddie_Kart_
# https://game8.co/games/mariokarttour/archives/278439

Green_Kiddie_Kart__TWO_x_Bonus_Points = ['Daisy Hills T', "Luigi's Mansion", 'Ghost Valley 1R', 'Toad Circuit R/T', 'Paris Promenade 2R', 'Donut Plains 1T']

Green_Kiddie_Kart__ONEoFIVE_x_Bonus_Points = ['Choco Island 2', 'London Loop R', 'London Loop R/T', 'Tokyo Blur 2R', 'Mario Circuit 2R/T', 'Paris Promenade 2T', 'Paris Promenade 2', 'Donut Plains 1']

Green_Kiddie_Kart__lv3_courses = []

Green_Kiddie_Kart__lv6_courses = ['Mario Circuit 2R/T']

Green_Kiddie_Kart_ = race_tool('Green_Kiddie_Kart_', 'Normal', Green_Kiddie_Kart__TWO_x_Bonus_Points, Green_Kiddie_Kart__ONEoFIVE_x_Bonus_Points, Green_Kiddie_Kart__lv3_courses, Green_Kiddie_Kart__lv6_courses)


#Red_Kiddie_Kart_
# https://game8.co/games/mariokarttour/archives/281115

Red_Kiddie_Kart__TWO_x_Bonus_Points = ['Daisy Hills R', 'Cheep Cheep Lagoon R/T', 'RMX Mario Circuit 1R']

Red_Kiddie_Kart__ONEoFIVE_x_Bonus_Points = ['Mario Circuit 2', 'Choco Island 2', 'Mario Circuit T', 'Daisy Hills R/T', 'Choco Island 2R/T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1T', 'Donut Plains 1R']

Red_Kiddie_Kart__lv3_courses = []

Red_Kiddie_Kart__lv6_courses = ['Choco Island 2R/T']

Red_Kiddie_Kart_ = race_tool('Red_Kiddie_Kart_', 'Normal', Red_Kiddie_Kart__TWO_x_Bonus_Points, Red_Kiddie_Kart__ONEoFIVE_x_Bonus_Points, Red_Kiddie_Kart__lv3_courses, Red_Kiddie_Kart__lv6_courses)


#Decal_Streamliner_
# https://game8.co/games/mariokarttour/archives/322568

Decal_Streamliner__TWO_x_Bonus_Points = ['Mario Circuit 1T', 'DK Summit', 'Tokyo Blur 4', 'Tokyo Blur 4T', 'Tokyo Blur 4T']

Decal_Streamliner__ONEoFIVE_x_Bonus_Points = ['Toad Circuit', 'Mario Circuit 1R/T', 'DK Summit T', 'Tokyo Blur 4R', 'Tokyo Blur 4R/T']

Decal_Streamliner__lv3_courses = ['Toad Circuit', 'DK Summit T']

Decal_Streamliner__lv6_courses = ['Mario Circuit 1R/T', 'Tokyo Blur 4R/T']

Decal_Streamliner_ = race_tool('Decal_Streamliner_', 'High-End', Decal_Streamliner__TWO_x_Bonus_Points, Decal_Streamliner__ONEoFIVE_x_Bonus_Points, Decal_Streamliner__lv3_courses, Decal_Streamliner__lv6_courses)


#Bumble_V_
# https://game8.co/games/mariokarttour/archives/271639

Bumble_V__TWO_x_Bonus_Points = ['Dino Dino Jungle R', 'Daisy Hills', 'Mario Circuit 2R', 'Waluigi Pinball', 'Waluigi Pinball T', 'Mario Circuit 3', 'SNES Rainbow Road R/T', 'Paris Promenade 2T', 'Paris Promenade 2R/T', 'Waluigi Pinball R/T']

Bumble_V__ONEoFIVE_x_Bonus_Points = ['Dino Dino Jungle T', 'London Loop', 'London Loop R', 'Paris Promenade 2R', 'Paris Promenade 2', 'Donut Plains 1R/T', 'Choco Island 1T', 'Airship Fortress R', 'Airship Fortress T', 'Los Angeles Laps T', 'Los Angeles Laps R/T', "Rosalina's Ice World R", "Rosalina's Ice World T"]

Bumble_V__lv3_courses = ['Dino Dino Jungle T', 'Donut Plains 1R/T']

Bumble_V__lv6_courses = ['Choco Island 1T', 'Airship Fortress R']

Bumble_V_ = race_tool('Bumble_V_', 'High-End', Bumble_V__TWO_x_Bonus_Points, Bumble_V__ONEoFIVE_x_Bonus_Points, Bumble_V__lv3_courses, Bumble_V__lv6_courses)

