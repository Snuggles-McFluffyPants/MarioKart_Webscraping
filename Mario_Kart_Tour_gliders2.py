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


#Fare_Flier_
# https://game8.co/games/mariokarttour/archives/270480

Fare_Flier__3x_Combo_Boost = ['New York Minute R', 'Cheep Cheep Lagoon R', 'New York Minute', 'New York Minute T', 'Neo Bowser City T', 'Waluigi Pinball T', 'London Loop T', 'Shy Guy Bazaar R/T', 'Los Angeles Laps T', 'New York Minute 3', 'New York Minute 3R', 'New York Minute 3T', 'New York Minute 3R/T']

Fare_Flier__2x_Combo_Boost = ['New York Minute R/T', 'Yoshi Circuit R', 'Mario Circuit 1T', 'Shy Guy Bazaar', 'Toad Circuit R', 'Mario Circuit 2R', 'Mario Circuit 2', 'Neo Bowser City', "Luigi's Mansion T", 'Ghost Valley 1R', 'Paris Promenade R/T', 'SNES Rainbow Road R/T', 'Frappe Snowland T', 'Vanilla Lake 1', 'Los Angeles Laps R/T', 'Sunset Wilds R/T', 'Berlin Byways 2', 'Berlin Byways 2T']

Fare_Flier__lv3_courses = ['Mario Circuit 2', 'SNES Rainbow Road R/T']

Fare_Flier__lv6_courses = ['Frappe Snowland T', 'Vanilla Lake 1']

Fare_Flier_ = race_tool('Fare_Flier_', 'High-End', Fare_Flier__3x_Combo_Boost, Fare_Flier__2x_Combo_Boost, Fare_Flier__lv3_courses, Fare_Flier__lv6_courses)


#Bullet_Bill_Parachute_
# https://game8.co/games/mariokarttour/archives/270479

Bullet_Bill_Parachute__3x_Combo_Boost = ['Yoshi Circuit R', "Bowser's Castle 1", 'SNES Rainbow Road R', 'DK Pass T', 'Mario Circuit R/T', 'Neo Bowser City R/T', 'Airship Fortress R', 'Airship Fortress T', 'New York Minute 3R/T', 'RMX Rainbow Road 1R/T']

Bullet_Bill_Parachute__2x_Combo_Boost = ['New York Minute R', 'Rock Rock Mountain R', 'Shy Guy Bazaar T', 'Shy Guy Bazaar', 'Koopa Troopa Beach', 'Daisy Hills R', "Bowser's Castle 1T", "Bowser's Castle 1R", 'Kalimari Desert T', 'DK Pass R', 'Daisy Hills R/T', 'Tokyo Blur 2R/T', 'Airship Fortress', 'New York Minute 3']

Bullet_Bill_Parachute__lv3_courses = ['Koopa Troopa Beach', 'Kalimari Desert T']

Bullet_Bill_Parachute__lv6_courses = ['Shy Guy Bazaar T', 'Daisy Hills R']

Bullet_Bill_Parachute_ = race_tool('Bullet_Bill_Parachute_', 'High-End', Bullet_Bill_Parachute__3x_Combo_Boost, Bullet_Bill_Parachute__2x_Combo_Boost, Bullet_Bill_Parachute__lv3_courses, Bullet_Bill_Parachute__lv6_courses)


#Gold_Glider_
# https://game8.co/games/mariokarttour/archives/270478

Gold_Glider__3x_Combo_Boost = ['New York Minute R/T', 'Mario Circuit 1T', 'Mario Circuit 1R', 'Koopa Troopa Beach R', 'Toad Circuit T', 'Toad Circuit', 'Mario Circuit 1', 'SNES Rainbow Road', 'SNES Rainbow Road T', "Luigi's Mansion T", 'DK Pass T', 'New York Minute 3R/T', 'RMX Rainbow Road 2R', 'RMX Choco Island 2R']

Gold_Glider__2x_Combo_Boost = ['Cheep Cheep Lagoon R', 'New York Minute', 'Daisy Hills', "Bowser's Castle 1T", 'Mario Circuit', 'Choco Island 2T', 'DS Rainbow Road', 'Mario Circuit 1R/T', 'Los Angeles Laps', 'New York Minute 3', 'New York Minute 3R', 'New York Minute 3T', 'RMX Rainbow Road 2', 'Donut Plains 2T', 'RMX Choco Island 2']

Gold_Glider__lv3_courses = ["Bowser's Castle 1T", 'Mario Circuit 1R/T']

Gold_Glider__lv6_courses = ['Cheep Cheep Lagoon R', 'DS Rainbow Road']

Gold_Glider_ = race_tool('Gold_Glider_', 'High-End', Gold_Glider__3x_Combo_Boost, Gold_Glider__2x_Combo_Boost, Gold_Glider__lv3_courses, Gold_Glider__lv6_courses)


#Swooper_
# https://game8.co/games/mariokarttour/archives/270477

Swooper__3x_Combo_Boost = ['Rock Rock Mountain T', 'Rock Rock Mountain', 'Dino Dino Jungle T', 'Dino Dino Jungle R', "Bowser's Castle 1T", 'Ghost Valley 1', 'Ghost Valley 1T', 'New York Minute 2', "Bowser's Castle 2R/T"]

Swooper__2x_Combo_Boost = ['New York Minute R', 'Rock Rock Mountain R', 'Shy Guy Bazaar T', 'Shy Guy Bazaar R', 'Dino Dino Jungle', "Bowser's Castle 1R", "Bowser's Castle 1", 'Neo Bowser City T', 'Kalimari Desert R/T', 'Tokyo Blur 3R', 'Tokyo Blur 3T']

Swooper__lv3_courses = ["Bowser's Castle 1R", "Bowser's Castle 1"]

Swooper__lv6_courses = ['Shy Guy Bazaar T', 'Dino Dino Jungle']

Swooper_ = race_tool('Swooper_', 'High-End', Swooper__3x_Combo_Boost, Swooper__2x_Combo_Boost, Swooper__lv3_courses, Swooper__lv6_courses)


#Cloud_Glider_
# https://game8.co/games/mariokarttour/archives/270737

Cloud_Glider__3x_Combo_Boost = ['Yoshi Circuit', 'Daisy Hills R', 'Cheep Cheep Lagoon', 'Choco Island 2R', 'Kalimari Desert T', 'Mario Circuit', 'Neo Bowser City R', 'Mario Circuit T', 'Vancouver Velocity T', 'Koopa Troopa Beach 2R', 'Los Angeles Laps R']

Cloud_Glider__2x_Combo_Boost = ['Rock Rock Mountain', 'Shy Guy Bazaar R', 'Shy Guy Bazaar', 'Toad Circuit T', 'Mario Circuit 2T', 'Paris Promenade R', 'London Loop R', 'Vancouver Velocity R/T', 'Vanilla Lake 1R/T', 'Los Angeles Laps', "Rosalina's Ice World", 'DK Summit', 'DK Summit T']

Cloud_Glider__lv3_courses = ['Rock Rock Mountain', 'Toad Circuit T']

Cloud_Glider__lv6_courses = ['Shy Guy Bazaar', 'Vanilla Lake 1R/T']

Cloud_Glider_ = race_tool('Cloud_Glider_', 'High-End', Cloud_Glider__3x_Combo_Boost, Cloud_Glider__2x_Combo_Boost, Cloud_Glider__lv3_courses, Cloud_Glider__lv6_courses)


#Full_Flight_
# https://game8.co/games/mariokarttour/archives/270736

Full_Flight__3x_Combo_Boost = ['Koopa Troopa Beach T', 'Tokyo Blur R', 'Neo Bowser City', 'Tokyo Blur R/T', 'Mario Circuit 3', 'New York Minute 2R/T', 'Vanilla Lake 1R/T', 'Tokyo Blur 3R', 'New York Minute 3', 'Maple Treeway R']

Full_Flight__2x_Combo_Boost = ['Koopa Troopa Beach R', 'Daisy Hills', "Bowser's Castle 1", 'Cheep Cheep Lagoon', 'Tokyo Blur', 'Mario Circuit 2', 'SNES Rainbow Road R', 'Tokyo Blur T', 'Waluigi Pinball', 'Paris Promenade R', 'Mario Circuit 3R', 'DS Rainbow Road T', 'London Loop 2T', "Bowser's Castle 2R/T", 'Tokyo Blur 3', 'Tokyo Blur 3T', 'RMX Rainbow Road 1', 'Los Angeles Laps T', 'Los Angeles Laps R/T', 'New York Minute 3T', 'New York Minute 3R/T', 'Maple Treeway']

Full_Flight__lv3_courses = ['Daisy Hills', "Bowser's Castle 1"]

Full_Flight__lv6_courses = ['Koopa Troopa Beach R', "Bowser's Castle 2R/T"]

Full_Flight_ = race_tool('Full_Flight_', 'High-End', Full_Flight__3x_Combo_Boost, Full_Flight__2x_Combo_Boost, Full_Flight__lv3_courses, Full_Flight__lv6_courses)


#Purple_Oilpaper_Umbrella_
# https://game8.co/games/mariokarttour/archives/270735

Purple_Oilpaper_Umbrella__3x_Combo_Boost = ['Dino Dino Jungle R', 'Daisy Hills R', 'Tokyo Blur', 'Tokyo Blur T', 'Ghost Valley 1R', 'Paris Promenade R', 'Paris Promenade R', 'Mario Circuit 3R', 'Mario Circuit R/T', 'Ghost Valley 1R/T', 'Tokyo Blur 3T', 'RMX Rainbow Road 2', 'RMX Rainbow Road 2R']

Purple_Oilpaper_Umbrella__2x_Combo_Boost = ['Daisy Hills T', 'Toad Circuit', 'Tokyo Blur R', 'Mario Circuit 2', 'Mario Circuit R', 'Mario Circuit T', 'Ghost Valley 1', 'Ghost Valley 1T', 'Paris Promenade', 'Paris Promenade R/T', 'DK Pass', 'DK Pass T', 'Daisy Hills R/T', 'Paris Promenade 2R', 'Paris Promenade 2', 'DS Rainbow Road R/T', 'Tokyo Blur 3R', 'New York Minute 3R', 'New York Minute 3R/T', "Rosalina's Ice World R", 'RMX Rainbow Road 2T']

Purple_Oilpaper_Umbrella__lv3_courses = ['Mario Circuit 2', 'Daisy Hills R/T']

Purple_Oilpaper_Umbrella__lv6_courses = ['Mario Circuit R', 'Ghost Valley 1']

Purple_Oilpaper_Umbrella_ = race_tool('Purple_Oilpaper_Umbrella_', 'High-End', Purple_Oilpaper_Umbrella__3x_Combo_Boost, Purple_Oilpaper_Umbrella__2x_Combo_Boost, Purple_Oilpaper_Umbrella__lv3_courses, Purple_Oilpaper_Umbrella__lv6_courses)


#Rainy_Balloons_
# https://game8.co/games/mariokarttour/archives/271643

Rainy_Balloons__3x_Combo_Boost = ['Toad Circuit R', "Luigi's Mansion R", "Luigi's Mansion T", 'Waluigi Pinball R', 'Ghost Valley 1R', 'Cheep Cheep Lagoon R/T', 'Donut Plains 1', "Bowser's Castle 2", 'Donut Plains 1R/T', 'Kalimari Desert 2', 'DK Summit R']

Rainy_Balloons__2x_Combo_Boost = ['Yoshi Circuit T', 'Toad Circuit T', 'SNES Rainbow Road', 'Neo Bowser City R', 'Neo Bowser City', "Luigi's Mansion", 'Mario Circuit 3T', 'Paris Promenade T', 'Mario Circuit R/T', "Luigi's Mansion R/T", 'Donut Plains 1R', 'Donut Plains 1T', 'RMX Mario Circuit 1R/T', 'Koopa Troopa Beach 2R', 'Koopa Troopa Beach 2T', 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'Maple Treeway', 'Maple Treeway R', "Rosalina's Ice World", "Rosalina's Ice World R", 'DK Summit']

Rainy_Balloons__lv3_courses = ["Luigi's Mansion R/T", 'RMX Mario Circuit 1R/T']

Rainy_Balloons__lv6_courses = ['Donut Plains 1T', 'Koopa Troopa Beach 2T']

Rainy_Balloons_ = race_tool('Rainy_Balloons_', 'High-End', Rainy_Balloons__3x_Combo_Boost, Rainy_Balloons__2x_Combo_Boost, Rainy_Balloons__lv3_courses, Rainy_Balloons__lv6_courses)


#Wicked_Wings_
# https://game8.co/games/mariokarttour/archives/271642

Wicked_Wings__3x_Combo_Boost = ['Rock Rock Mountain R', 'Yoshi Circuit T', "Bowser's Castle 1R", "Luigi's Mansion", 'Waluigi Pinball', 'Waluigi Pinball T', 'Ghost Valley 1', 'Daisy Hills R/T', "Luigi's Mansion R/T", "Bowser's Castle 2", "Bowser's Castle 2T", 'Airship Fortress T', 'Sunset Wilds']

Wicked_Wings__2x_Combo_Boost = ['DK Pass R', "Bowser's Castle 1R/T", 'Ghost Valley 1R/T', 'London Loop 2T', "Bowser's Castle 2R", 'Airship Fortress', 'Airship Fortress R', 'Maple Treeway T', 'Sunset Wilds R']

Wicked_Wings__lv3_courses = ['Ghost Valley 1R/T', "Bowser's Castle 2R"]

Wicked_Wings__lv6_courses = ['Airship Fortress', 'Airship Fortress R']

Wicked_Wings_ = race_tool('Wicked_Wings_', 'High-End', Wicked_Wings__3x_Combo_Boost, Wicked_Wings__2x_Combo_Boost, Wicked_Wings__lv3_courses, Wicked_Wings__lv6_courses)


#Strawberry_Crepe_
# https://game8.co/games/mariokarttour/archives/272267

Strawberry_Crepe__3x_Combo_Boost = ['Toad Circuit', 'Choco Island 2R', 'Paris Promenade', 'Paris Promenade R/T', 'New York Minute 2R', 'Tokyo Blur 2R/T', 'Mario Circuit 2R/T', 'Vanilla Lake 1', 'Choco Island 2R/T', 'Paris Promenade 2R', 'Donut Plains 1T', 'Choco Island 1T', 'Berlin Byways 2R/T']

Strawberry_Crepe__2x_Combo_Boost = ['Choco Island 2', 'Paris Promenade T', 'Paris Promenade R', 'DK Pass T', 'Daisy Hills R/T', 'Tokyo Blur 2', 'Tokyo Blur 2R', 'Frappe Snowland R', 'Vanilla Lake 1R', 'Vanilla Lake 1T', 'Paris Promenade 2T', 'Frappe Snowland R/T', 'DS Rainbow Road R/T', 'Donut Plains 1R', 'RMX Choco Island 1R', 'Berlin Byways 2R', 'RMX Choco Island 2', 'RMX Choco Island 2T']

Strawberry_Crepe__lv3_courses = ['Choco Island 2', 'Frappe Snowland R/T']

Strawberry_Crepe__lv6_courses = ['Donut Plains 1R', 'RMX Choco Island 1R']

Strawberry_Crepe_ = race_tool('Strawberry_Crepe_', 'High-End', Strawberry_Crepe__3x_Combo_Boost, Strawberry_Crepe__2x_Combo_Boost, Strawberry_Crepe__lv3_courses, Strawberry_Crepe__lv6_courses)


#Le_Tricolore_
# https://game8.co/games/mariokarttour/archives/272268

Le_Tricolore__3x_Combo_Boost = ['SNES Rainbow Road T', 'Mario Circuit 3', 'Paris Promenade T', 'Paris Promenade R', 'SNES Rainbow Road R/T', 'Daisy Hills R/T', 'Mario Circuit 1R/T', 'Paris Promenade 2R/T', 'Dino Dino Jungle R/T', 'Mario Circuit 3R/T', "Bowser's Castle 2R"]

Le_Tricolore__2x_Combo_Boost = ['Choco Island 2', 'SNES Rainbow Road R', 'Mario Circuit 3T', 'Paris Promenade R/T', 'London Loop', 'London Loop R/T', 'Yoshi Circuit R/T', 'New York Minute 2R', 'DS Rainbow Road', 'Mario Circuit 2R/T', 'Toad Circuit R/T', 'Choco Island 2R/T', 'Paris Promenade 2', 'RMX Mario Circuit 1R/T', 'RMX Choco Island 1', 'RMX Choco Island 1R', 'Choco Island 1', 'Choco Island 1R', 'New York Minute 3R/T']

Le_Tricolore__lv3_courses = ['Choco Island 2', 'Mario Circuit 2R/T']

Le_Tricolore__lv6_courses = ['Yoshi Circuit R/T', 'Choco Island 1R']

Le_Tricolore_ = race_tool('Le_Tricolore_', 'High-End', Le_Tricolore__3x_Combo_Boost, Le_Tricolore__2x_Combo_Boost, Le_Tricolore__lv3_courses, Le_Tricolore__lv6_courses)


#Starchute_
# https://game8.co/games/mariokarttour/archives/273764

Starchute__3x_Combo_Boost = ['Dino Dino Jungle T', 'Mario Circuit 3', 'Paris Promenade T', 'DK Pass', 'DK Pass R', 'SNES Rainbow Road R/T', 'Yoshi Circuit R/T', 'Toad Circuit R/T', 'Dino Dino Jungle R/T', 'RMX Choco Island 1R', 'Koopa Troopa Beach 2R', 'Los Angeles Laps', 'New York Minute 3T', 'Merry Mountain T', "Rosalina's Ice World R"]

Starchute__2x_Combo_Boost = ['Mario Circuit', "Luigi's Mansion T", 'Paris Promenade', 'DK Pass T', 'London Loop T', "Bowser's Castle 1R/T", 'Tokyo Blur 2T', 'Paris Promenade 2R', 'Paris Promenade 2R/T', 'Waluigi Pinball R/T', 'RMX Mario Circuit 1R/T', 'Vanilla Lake 1R/T', 'RMX Choco Island 1', 'Koopa Troopa Beach 2T', 'New York Minute 3R', 'Merry Mountain', 'Merry Mountain R', "Rosalina's Ice World", "Rosalina's Ice World T"]

Starchute__lv3_courses = ['Mario Circuit', "Bowser's Castle 1R/T"]

Starchute__lv6_courses = ["Luigi's Mansion T", 'Koopa Troopa Beach 2T']

Starchute_ = race_tool('Starchute_', 'High-End', Starchute__3x_Combo_Boost, Starchute__2x_Combo_Boost, Starchute__lv3_courses, Starchute__lv6_courses)


#Royal_Parachute_
# https://game8.co/games/mariokarttour/archives/273765

Royal_Parachute__3x_Combo_Boost = ['Daisy Hills T', 'Mario Circuit 2T', 'Mario Circuit 2', 'Choco Island 2', 'Mario Circuit', 'Mario Circuit 3T', 'Daisy Hills R/T', 'Paris Promenade 2T', 'Choco Island 1R', 'Royal Raceway T', 'Royal Raceway', 'Sunset Wilds']

Royal_Parachute__2x_Combo_Boost = ['Mario Circuit 1R', 'Daisy Hills', 'Mario Circuit 1', 'DK Pass', 'DK Pass R', 'London Loop R', 'Mario Circuit 2R/T', 'Toad Circuit R/T', 'Paris Promenade 2R', 'Paris Promenade 2', 'Choco Island 1', 'Choco Island 1T', 'Sunset Wilds R']

Royal_Parachute__lv3_courses = ['Mario Circuit 1', 'DK Pass']

Royal_Parachute__lv6_courses = ['Choco Island 1', 'Choco Island 1T']

Royal_Parachute_ = race_tool('Royal_Parachute_', 'High-End', Royal_Parachute__3x_Combo_Boost, Royal_Parachute__2x_Combo_Boost, Royal_Parachute__lv3_courses, Royal_Parachute__lv6_courses)


#Glitter_Glider_
# https://game8.co/games/mariokarttour/archives/274700

Glitter_Glider__3x_Combo_Boost = ['Daisy Hills R', 'Daisy Hills', 'Choco Island 2R', "Luigi's Mansion R", 'DK Pass', 'London Loop', 'London Loop R/T', 'London Loop 2R/T', 'Vanilla Lake 1R/T', 'Royal Raceway R', 'Maple Treeway', "Rosalina's Ice World T", 'Berlin Byways 2T']

Glitter_Glider__2x_Combo_Boost = ['Choco Island 2T', "Luigi's Mansion", 'London Loop T', 'DS Rainbow Road T', 'New York Minute 2R/T', 'Tokyo Blur 2', 'Tokyo Blur 2R', 'Choco Island 2R/T', 'Shy Guy Bazaar R/T', 'Paris Promenade 2T', 'Paris Promenade 2R/T', 'Donut Plains 1', 'Donut Plains 1R', "Bowser's Castle 2R/T", 'Royal Raceway T', 'Royal Raceway', 'Maple Treeway T', 'Merry Mountain R', 'Merry Mountain T', "Rosalina's Ice World R", 'Berlin Byways 2R', 'Berlin Byways 2R/T']

Glitter_Glider__lv3_courses = ['Choco Island 2T', 'Choco Island 2R/T']

Glitter_Glider__lv6_courses = ["Luigi's Mansion", 'Donut Plains 1R']

Glitter_Glider_ = race_tool('Glitter_Glider_', 'High-End', Glitter_Glider__3x_Combo_Boost, Glitter_Glider__2x_Combo_Boost, Glitter_Glider__lv3_courses, Glitter_Glider__lv6_courses)


#Soaring_Jack_
# https://game8.co/games/mariokarttour/archives/274701

Soaring_Jack__3x_Combo_Boost = ['Shy Guy Bazaar T', "Bowser's Castle 1T", "Bowser's Castle 1R", 'London Loop R', 'London Loop R/T', 'Yoshi Circuit R/T', 'Kalimari Desert R/T', 'Neo Bowser City R/T', 'Koopa Troopa Beach R/T', 'London Loop 2R/T']

Soaring_Jack__2x_Combo_Boost = ['Yoshi Circuit', 'Neo Bowser City R', 'SNES Rainbow Road R', 'Paris Promenade', 'Paris Promenade R', 'Mario Circuit R/T', 'London Loop', 'London Loop T', "Bowser's Castle 1R/T", 'New York Minute 2T', 'DS Rainbow Road R', 'DS Rainbow Road T', 'New York Minute 2R/T', 'DK Pass R/T', 'Shy Guy Bazaar R/T', 'Frappe Snowland R/T', 'London Loop 2T', 'Choco Island 1R', 'DK Summit T']

Soaring_Jack__lv3_courses = ["Bowser's Castle 1R/T", 'Frappe Snowland R/T']

Soaring_Jack__lv6_courses = ['Neo Bowser City R', 'Choco Island 1R']

Soaring_Jack_ = race_tool('Soaring_Jack_', 'High-End', Soaring_Jack__3x_Combo_Boost, Soaring_Jack__2x_Combo_Boost, Soaring_Jack__lv3_courses, Soaring_Jack__lv6_courses)


#Gift_Glider_
# https://game8.co/games/mariokarttour/archives/275169

Gift_Glider__3x_Combo_Boost = ["Luigi's Mansion", 'New York Minute 2T', 'New York Minute 2', 'DS Rainbow Road', 'Cheep Cheep Lagoon R/T', 'Neo Bowser City R/T', 'Vanilla Lake 1T', 'Vancouver Velocity R/T', "Bowser's Castle 2T", 'Royal Raceway R', 'Merry Mountain R', 'Merry Mountain T']

Gift_Glider__2x_Combo_Boost = ['Rock Rock Mountain T', 'Rock Rock Mountain', "Luigi's Mansion R", 'Yoshi Circuit R/T', 'New York Minute 2R', 'DS Rainbow Road R', 'Tokyo Blur 2', 'Toad Circuit R/T', 'Shy Guy Bazaar R/T', 'Dino Dino Jungle R/T', 'Vancouver Velocity T', 'Vancouver Velocity', 'Donut Plains 1T', "Bowser's Castle 2", "Bowser's Castle 2R", 'Royal Raceway T', 'Royal Raceway', 'Merry Mountain', 'RMX Rainbow Road 2T']

Gift_Glider__lv3_courses = ['Toad Circuit R/T', 'Shy Guy Bazaar R/T']

Gift_Glider__lv6_courses = ["Luigi's Mansion R", 'Royal Raceway T']

Gift_Glider_ = race_tool('Gift_Glider_', 'High-End', Gift_Glider__3x_Combo_Boost, Gift_Glider__2x_Combo_Boost, Gift_Glider__lv3_courses, Gift_Glider__lv6_courses)


#New_Years_2020_
# https://game8.co/games/mariokarttour/archives/275170

New_Years_2020__3x_Combo_Boost = ['Mario Circuit R', 'DK Pass', 'DS Rainbow Road R', 'DS Rainbow Road T', 'New York Minute 2R/T', 'Tokyo Blur 2T', 'Shy Guy Bazaar R/T', 'Paris Promenade 2R/T', 'London Loop 2R/T', 'Tokyo Blur 3R', 'RMX Rainbow Road 2R']

New_Years_2020__2x_Combo_Boost = ['Shy Guy Bazaar T', "Luigi's Mansion T", 'New York Minute 2', 'Tokyo Blur 2', 'Frappe Snowland', 'Frappe Snowland R', 'Vanilla Lake 1', 'Paris Promenade 2R', 'Koopa Troopa Beach R/T', 'Mario Circuit 3R/T', 'Tokyo Blur 3', 'New York Minute 3R', 'New York Minute 3R/T', "Rosalina's Ice World", 'RMX Rainbow Road 2', 'RMX Rainbow Road 2T']

New_Years_2020__lv3_courses = ['Koopa Troopa Beach R/T', 'Mario Circuit 3R/T']

New_Years_2020__lv6_courses = ['Frappe Snowland R', 'Vanilla Lake 1']

New_Years_2020_ = race_tool('New_Years_2020_', 'High-End', New_Years_2020__3x_Combo_Boost, New_Years_2020__2x_Combo_Boost, New_Years_2020__lv3_courses, New_Years_2020__lv6_courses)


#Crimson_Crane_
# https://game8.co/games/mariokarttour/archives/275397

Crimson_Crane__3x_Combo_Boost = ['Choco Island 2T', 'SNES Rainbow Road R', 'Tokyo Blur R/T', 'Mario Circuit 3R', 'DS Rainbow Road', 'Tokyo Blur 2R', 'Mario Circuit 2R/T', 'Choco Island 2R/T', 'Mario Circuit 3R/T', 'RMX Mario Circuit 1R', 'Donut Plains 1R', 'Tokyo Blur 3', 'Sunset Wilds R', 'RMX Rainbow Road 2R']

Crimson_Crane__2x_Combo_Boost = ['Dino Dino Jungle R', 'Mario Circuit 1', 'SNES Rainbow Road', 'Choco Island 2R', 'Mario Circuit 3', 'Tokyo Blur 2T', 'Tokyo Blur 2R/T', 'Toad Circuit R/T', 'Paris Promenade 2T', 'Paris Promenade 2', 'Ghost Valley 1R/T', 'RMX Mario Circuit 1', 'Donut Plains 1', 'Donut Plains 1T', 'Donut Plains 1R/T', 'Tokyo Blur 3T', 'Berlin Byways 2', 'Berlin Byways 2R', 'RMX Choco Island 2R', 'RMX Choco Island 2T']

Crimson_Crane__lv3_courses = ['SNES Rainbow Road', 'Ghost Valley 1R/T']

Crimson_Crane__lv6_courses = ['Dino Dino Jungle R', 'RMX Mario Circuit 1']

Crimson_Crane_ = race_tool('Crimson_Crane_', 'High-End', Crimson_Crane__3x_Combo_Boost, Crimson_Crane__2x_Combo_Boost, Crimson_Crane__lv3_courses, Crimson_Crane__lv6_courses)


#Fireworks_Parachute_
# https://game8.co/games/mariokarttour/archives/275398

Fireworks_Parachute__3x_Combo_Boost = ['Toad Circuit T', 'Tokyo Blur R', 'Waluigi Pinball', "Bowser's Castle 1R/T", 'Toad Circuit R/T', 'Vanilla Lake 1R', 'London Loop 2R', 'DS Rainbow Road R/T', "Bowser's Castle 2R", 'Koopa Troopa Beach 2', 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'Merry Mountain R']

Fireworks_Parachute__2x_Combo_Boost = ['Mario Circuit R/T', 'Mario Circuit 1R/T', 'Tokyo Blur 2R', 'Tokyo Blur 2T', 'Tokyo Blur 2R/T', 'Frappe Snowland T', 'Vanilla Lake 1', 'Vanilla Lake 1T', 'DK Pass R/T', 'Shy Guy Bazaar R/T', 'Vancouver Velocity T', 'Vancouver Velocity R', 'London Loop 2', "Bowser's Castle 2", 'RMX Choco Island 1', 'Koopa Troopa Beach 2T', 'Kalimari Desert 2', 'Tokyo Blur 3', 'Tokyo Blur 3R', 'Merry Mountain']

Fireworks_Parachute__lv3_courses = ['Shy Guy Bazaar R/T', "Bowser's Castle 2"]

Fireworks_Parachute__lv6_courses = ['RMX Choco Island 1', 'Kalimari Desert 2']

Fireworks_Parachute_ = race_tool('Fireworks_Parachute_', 'High-End', Fireworks_Parachute__3x_Combo_Boost, Fireworks_Parachute__2x_Combo_Boost, Fireworks_Parachute__lv3_courses, Fireworks_Parachute__lv6_courses)


#New_Years_Kite_
# https://game8.co/games/mariokarttour/archives/275399

New_Years_Kite__3x_Combo_Boost = ['Tokyo Blur', 'SNES Rainbow Road', 'Mario Circuit T', 'Tokyo Blur T', 'Tokyo Blur R/T', 'Yoshi Circuit R/T', 'DS Rainbow Road R', 'Tokyo Blur 2', 'Tokyo Blur 2R', 'Tokyo Blur 2R/T', 'Shy Guy Bazaar R/T', 'RMX Mario Circuit 1R/T', 'RMX Rainbow Road 2', 'Berlin Byways 2R', 'Berlin Byways 2R/T', 'Donut Plains 2R']

New_Years_Kite__2x_Combo_Boost = ['Koopa Troopa Beach T', 'Tokyo Blur R', 'SNES Rainbow Road T', 'Ghost Valley 1', 'Ghost Valley 1R', "Luigi's Mansion R/T", 'Cheep Cheep Lagoon R/T', 'Kalimari Desert R/T', 'Tokyo Blur 2T', 'Frappe Snowland T', 'Vanilla Lake 1T', 'Waluigi Pinball R/T', 'London Loop 2', 'DS Rainbow Road R/T', 'RMX Rainbow Road 2R', 'RMX Rainbow Road 2T', 'Berlin Byways 2T', 'Donut Plains 2T', 'RMX Choco Island 2']

New_Years_Kite__lv3_courses = ['Cheep Cheep Lagoon R/T', 'DS Rainbow Road R/T']

New_Years_Kite__lv6_courses = ['Frappe Snowland T', 'Vanilla Lake 1T']

New_Years_Kite_ = race_tool('New_Years_Kite_', 'High-End', New_Years_Kite__3x_Combo_Boost, New_Years_Kite__2x_Combo_Boost, New_Years_Kite__lv3_courses, New_Years_Kite__lv6_courses)


#Baby_Mario_Hanafuda_
# https://game8.co/games/mariokarttour/archives/275400

Baby_Mario_Hanafuda__3x_Combo_Boost = ['Ghost Valley 1', 'Ghost Valley 1R', 'Ghost Valley 1T', "Luigi's Mansion R/T", 'DS Rainbow Road', 'DS Rainbow Road R', 'DS Rainbow Road T', 'RMX Mario Circuit 1R/T']

Baby_Mario_Hanafuda__2x_Combo_Boost = ['Tokyo Blur 2', 'Tokyo Blur 2R', 'Tokyo Blur 2T', 'Tokyo Blur 2R/T', 'DK Pass R/T', 'Choco Island 2R/T', 'Shy Guy Bazaar R/T', 'Dino Dino Jungle R/T', 'Waluigi Pinball R/T', 'Ghost Valley 1R/T', 'London Loop 2', 'London Loop 2R', 'London Loop 2T', 'London Loop 2R/T', 'Donut Plains 1', 'Donut Plains 1R', 'Donut Plains 1T', 'Choco Mountain', 'Choco Mountain R', 'Choco Mountain T']

Baby_Mario_Hanafuda__lv3_courses = ['Dino Dino Jungle R/T', 'Ghost Valley 1R/T']

Baby_Mario_Hanafuda__lv6_courses = ['Donut Plains 1', 'Choco Mountain T']

Baby_Mario_Hanafuda_ = race_tool('Baby_Mario_Hanafuda_', 'High-End', Baby_Mario_Hanafuda__3x_Combo_Boost, Baby_Mario_Hanafuda__2x_Combo_Boost, Baby_Mario_Hanafuda__lv3_courses, Baby_Mario_Hanafuda__lv6_courses)


#Blizzard_Parasol_
# https://game8.co/games/mariokarttour/archives/275781

Blizzard_Parasol__3x_Combo_Boost = ['Mario Circuit 1T', 'SNES Rainbow Road R', 'Mario Circuit 1R/T', 'Frappe Snowland', 'Frappe Snowland R', 'DK Pass R/T', 'Waluigi Pinball R/T', 'Vancouver Velocity R/T', 'RMX Mario Circuit 1T', 'Royal Raceway T', 'Royal Raceway', 'DK Summit T']

Blizzard_Parasol__2x_Combo_Boost = ['Ghost Valley 1R', 'Ghost Valley 1T', 'Neo Bowser City R/T', 'Frappe Snowland T', 'Vanilla Lake 1T', 'Paris Promenade 2R/T', 'Vancouver Velocity T', 'Vancouver Velocity R', 'RMX Mario Circuit 1', 'RMX Choco Island 1', 'Royal Raceway R', 'DK Summit R']

Blizzard_Parasol__lv3_courses = ['Neo Bowser City R/T', 'Vanilla Lake 1T']

Blizzard_Parasol__lv6_courses = ['Frappe Snowland T', 'RMX Choco Island 1']

Blizzard_Parasol_ = race_tool('Blizzard_Parasol_', 'High-End', Blizzard_Parasol__3x_Combo_Boost, Blizzard_Parasol__2x_Combo_Boost, Blizzard_Parasol__lv3_courses, Blizzard_Parasol__lv6_courses)


#Blizzard_Balloons_
# https://game8.co/games/mariokarttour/archives/275780

Blizzard_Balloons__3x_Combo_Boost = ['Mario Circuit R/T', 'Frappe Snowland T', 'Vanilla Lake 1', 'Vanilla Lake 1T', 'Waluigi Pinball R/T', 'Frappe Snowland R/T', 'DS Rainbow Road R/T', 'Donut Plains 1R', 'RMX Choco Island 1', 'Koopa Troopa Beach 2T', "Rosalina's Ice World T", 'Donut Plains 2R']

Blizzard_Balloons__2x_Combo_Boost = ['Neo Bowser City', 'Neo Bowser City T', 'Neo Bowser City R/T', 'Frappe Snowland R', 'Choco Island 2R/T', 'Vancouver Velocity', 'Vancouver Velocity R/T', 'RMX Mario Circuit 1R', 'RMX Mario Circuit 1T', 'Donut Plains 1T', "Bowser's Castle 2T", 'RMX Choco Island 1R', 'RMX Choco Island 1T', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', "Rosalina's Ice World"]

Blizzard_Balloons__lv3_courses = ['Neo Bowser City R/T', 'RMX Mario Circuit 1R']

Blizzard_Balloons__lv6_courses = ['RMX Mario Circuit 1T', 'RMX Choco Island 1T']

Blizzard_Balloons_ = race_tool('Blizzard_Balloons_', 'High-End', Blizzard_Balloons__3x_Combo_Boost, Blizzard_Balloons__2x_Combo_Boost, Blizzard_Balloons__lv3_courses, Blizzard_Balloons__lv6_courses)


#Gold_Swooper_
# https://game8.co/games/mariokarttour/archives/275779

Gold_Swooper__3x_Combo_Boost = ['Rock Rock Mountain R', 'Shy Guy Bazaar', 'Tokyo Blur R', 'Kalimari Desert', 'DS Rainbow Road', 'Vanilla Lake 1R', 'DK Pass R/T', 'Shy Guy Bazaar R/T', 'Ghost Valley 1R/T', 'Donut Plains 1', 'Donut Plains 1T', 'Choco Mountain', 'Choco Mountain T', 'Kalimari Desert 2T']

Gold_Swooper__2x_Combo_Boost = ['Rock Rock Mountain T', 'Rock Rock Mountain', 'Shy Guy Bazaar T', 'Cheep Cheep Lagoon', 'Tokyo Blur', 'Kalimari Desert R', 'Neo Bowser City R', 'Neo Bowser City', 'Tokyo Blur T', 'SNES Rainbow Road R/T', 'DS Rainbow Road R', 'Kalimari Desert R/T', 'London Loop 2R', "Bowser's Castle 2", 'Choco Mountain R']

Gold_Swooper__lv3_courses = ['Kalimari Desert R', 'Kalimari Desert R/T']

Gold_Swooper__lv6_courses = ["Bowser's Castle 2", 'Choco Mountain R']

Gold_Swooper_ = race_tool('Gold_Swooper_', 'High-End', Gold_Swooper__3x_Combo_Boost, Gold_Swooper__2x_Combo_Boost, Gold_Swooper__lv3_courses, Gold_Swooper__lv6_courses)


#Sweetheart_Glider_
# https://game8.co/games/mariokarttour/archives/278441

Sweetheart_Glider__3x_Combo_Boost = ['Mario Circuit R/T', 'Frappe Snowland', 'Frappe Snowland T', 'Paris Promenade 2R', 'Paris Promenade 2T', 'Paris Promenade 2', 'Mario Circuit 3R/T', 'DS Rainbow Road R/T', 'RMX Choco Island 1T', 'Choco Island 1R', 'RMX Rainbow Road 1', 'Sunset Wilds R', 'Merry Mountain']

Sweetheart_Glider__2x_Combo_Boost = ['Dino Dino Jungle T', 'Waluigi Pinball R', 'Waluigi Pinball T', 'SNES Rainbow Road R/T', 'DS Rainbow Road', 'Vancouver Velocity R', 'Frappe Snowland R/T', 'London Loop 2', 'London Loop 2R', 'RMX Choco Island 1T', 'Choco Island 1', 'Choco Island 1T', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 1T', 'Merry Mountain R', 'RMX Choco Island 2', 'RMX Choco Island 2T']

Sweetheart_Glider__lv3_courses = ['Dino Dino Jungle T', 'Frappe Snowland R/T']

Sweetheart_Glider__lv6_courses = ['Choco Island 1', 'RMX Rainbow Road 1T']

Sweetheart_Glider_ = race_tool('Sweetheart_Glider_', 'High-End', Sweetheart_Glider__3x_Combo_Boost, Sweetheart_Glider__2x_Combo_Boost, Sweetheart_Glider__lv3_courses, Sweetheart_Glider__lv6_courses)


#Heart_Balloons_
# https://game8.co/games/mariokarttour/archives/278442

Heart_Balloons__3x_Combo_Boost = ['Waluigi Pinball R', 'Paris Promenade', 'Paris Promenade R', 'SNES Rainbow Road R/T', 'Toad Circuit R/T', 'Frappe Snowland R', 'Vanilla Lake 1', 'Vanilla Lake 1T', 'Paris Promenade 2R', 'Waluigi Pinball R/T', 'Koopa Troopa Beach R/T', 'London Loop 2R', 'DS Rainbow Road R/T', 'Donut Plains 1T', 'RMX Choco Island 1T']

Heart_Balloons__2x_Combo_Boost = ['Yoshi Circuit T', 'Yoshi Circuit R', 'Choco Island 2', 'SNES Rainbow Road T', 'Neo Bowser City T', 'Paris Promenade T', 'Yoshi Circuit R/T', 'Frappe Snowland', 'Paris Promenade 2T', 'Paris Promenade 2R/T', 'Ghost Valley 1R/T', 'Vancouver Velocity', 'Vancouver Velocity R', 'Vancouver Velocity R/T', 'Donut Plains 1R/T', 'RMX Choco Island 1', 'RMX Choco Island 1R', 'Maple Treeway R', 'RMX Choco Island 2', 'RMX Choco Island 2R']

Heart_Balloons__lv3_courses = ['Yoshi Circuit T', 'SNES Rainbow Road T']

Heart_Balloons__lv6_courses = ['Frappe Snowland', 'RMX Choco Island 1']

Heart_Balloons_ = race_tool('Heart_Balloons_', 'High-End', Heart_Balloons__3x_Combo_Boost, Heart_Balloons__2x_Combo_Boost, Heart_Balloons__lv3_courses, Heart_Balloons__lv6_courses)


#Rainbow_Starchute_
# https://game8.co/games/mariokarttour/archives/279961

Rainbow_Starchute__3x_Combo_Boost = ['DK Pass', 'DK Pass R', 'DS Rainbow Road R', 'DS Rainbow Road T', 'Vancouver Velocity R', 'RMX Mario Circuit 1R', 'DS Rainbow Road R/T', 'Vanilla Lake 1R/T', 'Kalimari Desert 2', 'New York Minute 3R', 'New York Minute 3T', 'Sunset Wilds R/T', 'RMX Rainbow Road 2R']

Rainbow_Starchute__2x_Combo_Boost = ['Dino Dino Jungle T', 'Dino Dino Jungle', 'SNES Rainbow Road R/T', 'DS Rainbow Road', 'Waluigi Pinball R/T', 'Vancouver Velocity T', 'Vancouver Velocity R/T', 'Frappe Snowland R/T', 'RMX Mario Circuit 1R/T', 'Royal Raceway R', 'Royal Raceway', 'Kalimari Desert 2R', 'New York Minute 3', 'Maple Treeway', 'Maple Treeway T', 'DK Summit R']

Rainbow_Starchute__lv3_courses = ['SNES Rainbow Road R/T', 'Waluigi Pinball R/T']

Rainbow_Starchute__lv6_courses = ['Royal Raceway', 'Kalimari Desert 2R']

Rainbow_Starchute_ = race_tool('Rainbow_Starchute_', 'High-End', Rainbow_Starchute__3x_Combo_Boost, Rainbow_Starchute__2x_Combo_Boost, Rainbow_Starchute__lv3_courses, Rainbow_Starchute__lv6_courses)


#Yoshis_Egg_Hanafuda_
# https://game8.co/games/mariokarttour/archives/279963

Yoshis_Egg_Hanafuda__3x_Combo_Boost = ['Dino Dino Jungle T', 'Dino Dino Jungle R', 'Dino Dino Jungle', 'Mario Circuit 2T', 'Mario Circuit 2R', 'Mario Circuit 2', 'Toad Circuit R/T']

Yoshis_Egg_Hanafuda__2x_Combo_Boost = ["Bowser's Castle 1T", "Bowser's Castle 1R", "Bowser's Castle 1", 'Vanilla Lake 1', 'Vanilla Lake 1R', 'Vanilla Lake 1T', 'DK Pass R/T', 'Vancouver Velocity T', 'Vancouver Velocity', 'Vancouver Velocity R', 'Vancouver Velocity R/T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1R', 'RMX Mario Circuit 1T', 'RMX Mario Circuit 1R/T', 'Vanilla Lake 1R/T', 'Tokyo Blur 3', 'Tokyo Blur 3R', 'Tokyo Blur 3T']

Yoshis_Egg_Hanafuda__lv3_courses = ["Bowser's Castle 1", 'RMX Mario Circuit 1R/T']

Yoshis_Egg_Hanafuda__lv6_courses = ['Vanilla Lake 1R', 'RMX Mario Circuit 1T']

Yoshis_Egg_Hanafuda_ = race_tool('Yoshis_Egg_Hanafuda_', 'High-End', Yoshis_Egg_Hanafuda__3x_Combo_Boost, Yoshis_Egg_Hanafuda__2x_Combo_Boost, Yoshis_Egg_Hanafuda__lv3_courses, Yoshis_Egg_Hanafuda__lv6_courses)


#Luma_Parafoil_
# https://game8.co/games/mariokarttour/archives/279964

Luma_Parafoil__3x_Combo_Boost = ['Mario Circuit 1R', 'Shy Guy Bazaar R', 'Neo Bowser City', 'Mario Circuit T', 'SNES Rainbow Road R/T', 'London Loop R', 'Frappe Snowland', 'Frappe Snowland R', 'DK Pass R/T', 'Vancouver Velocity T', 'Vancouver Velocity', 'Koopa Troopa Beach 2', 'Los Angeles Laps T']

Luma_Parafoil__2x_Combo_Boost = ['Shy Guy Bazaar T', 'Shy Guy Bazaar', 'Mario Circuit', 'Neo Bowser City T', 'Paris Promenade T', 'DS Rainbow Road', 'Vancouver Velocity R/T', 'Frappe Snowland R/T', 'RMX Mario Circuit 1', 'London Loop 2R', 'London Loop 2R/T', 'DS Rainbow Road R/T', 'Koopa Troopa Beach 2R', 'Los Angeles Laps', 'Los Angeles Laps R/T', 'New York Minute 3', "Rosalina's Ice World", 'RMX Rainbow Road 2R']

Luma_Parafoil__lv3_courses = ['Neo Bowser City T', 'DS Rainbow Road R/T']

Luma_Parafoil__lv6_courses = ['Shy Guy Bazaar', 'RMX Mario Circuit 1']

Luma_Parafoil_ = race_tool('Luma_Parafoil_', 'High-End', Luma_Parafoil__3x_Combo_Boost, Luma_Parafoil__2x_Combo_Boost, Luma_Parafoil__lv3_courses, Luma_Parafoil__lv6_courses)


#Peach_Hanafuda_
# https://game8.co/games/mariokarttour/archives/285096

Peach_Hanafuda__3x_Combo_Boost = ['Cheep Cheep Lagoon T', 'Cheep Cheep Lagoon R', 'Cheep Cheep Lagoon', 'Mario Circuit R', 'Mario Circuit', 'Mario Circuit T', 'Mario Circuit 3', 'Mario Circuit 3T', 'Mario Circuit 3R', 'Mario Circuit R/T', 'Donut Plains 1R/T']

Peach_Hanafuda__2x_Combo_Boost = ['Yoshi Circuit T', 'Yoshi Circuit R', 'Yoshi Circuit', 'Mario Circuit 1T', 'Mario Circuit 1R', 'Koopa Troopa Beach T', 'Koopa Troopa Beach R', 'Koopa Troopa Beach', 'Mario Circuit 1', 'Yoshi Circuit R/T', 'Donut Plains 1', 'Donut Plains 1R', 'Donut Plains 1T', 'Maple Treeway', 'Maple Treeway R', 'Maple Treeway T']

Peach_Hanafuda__lv3_courses = ['Koopa Troopa Beach', 'Mario Circuit 1']

Peach_Hanafuda__lv6_courses = ['Donut Plains 1', 'Donut Plains 1T']

Peach_Hanafuda_ = race_tool('Peach_Hanafuda_', 'High-End', Peach_Hanafuda__3x_Combo_Boost, Peach_Hanafuda__2x_Combo_Boost, Peach_Hanafuda__lv3_courses, Peach_Hanafuda__lv6_courses)


#Safety_Glider_
# https://game8.co/games/mariokarttour/archives/286548

Safety_Glider__3x_Combo_Boost = ['Mario Circuit 1T', 'Shy Guy Bazaar T', 'Waluigi Pinball T', 'Tokyo Blur 2T', 'DK Pass R/T', 'Vancouver Velocity R/T', 'Frappe Snowland R/T', 'RMX Mario Circuit 1T', "Bowser's Castle 2", "Bowser's Castle 2R/T", 'Airship Fortress T', 'Tokyo Blur 3T', 'Sunset Wilds R/T']

Safety_Glider__2x_Combo_Boost = ['Cheep Cheep Lagoon T', 'Daisy Hills T', "Bowser's Castle 1T", 'Choco Island 2T', 'Mario Circuit T', 'Daisy Hills R/T', 'DS Rainbow Road T', 'Cheep Cheep Lagoon R/T', 'Kalimari Desert R/T', 'Neo Bowser City R/T', 'Toad Circuit R/T', 'Donut Plains 1R/T', 'Choco Mountain T', 'RMX Rainbow Road 1R/T', 'Merry Mountain T']

Safety_Glider__lv3_courses = ['Choco Island 2T', 'Toad Circuit R/T']

Safety_Glider__lv6_courses = ['Donut Plains 1R/T', 'Choco Mountain T']

Safety_Glider_ = race_tool('Safety_Glider_', 'High-End', Safety_Glider__3x_Combo_Boost, Safety_Glider__2x_Combo_Boost, Safety_Glider__lv3_courses, Safety_Glider__lv6_courses)


#Bright_Glider_
# https://game8.co/games/mariokarttour/archives/285887

Bright_Glider__3x_Combo_Boost = ['Rock Rock Mountain T', 'Yoshi Circuit', 'SNES Rainbow Road T', 'SNES Rainbow Road R', "Luigi's Mansion", "Luigi's Mansion T", 'Ghost Valley 1', 'Ghost Valley 1', 'Ghost Valley 1', 'London Loop', 'London Loop R/T', 'Yoshi Circuit R/T', 'Koopa Troopa Beach R/T', "Bowser's Castle 2", 'RMX Mario Circuit 1R/T', 'RMX Choco Island 2']

Bright_Glider__2x_Combo_Boost = ['Rock Rock Mountain R', 'Yoshi Circuit T', 'Koopa Troopa Beach', 'Ghost Valley 1R', 'Ghost Valley 1R', 'Ghost Valley 1R', 'Ghost Valley 1T', 'Ghost Valley 1T', 'Ghost Valley 1T', 'Mario Circuit R/T', 'Daisy Hills R/T', 'London Loop R', 'Cheep Cheep Lagoon R/T', "Bowser's Castle 2R", 'Donut Plains 1R/T', "Bowser's Castle 2R/T", 'Vanilla Lake 1R/T', 'Royal Raceway R', 'Royal Raceway T', 'New York Minute 3R', 'New York Minute 3T', 'Berlin Byways 2R/T']

Bright_Glider__lv3_courses = ['Mario Circuit R/T', 'Daisy Hills R/T']

Bright_Glider__lv6_courses = ["Bowser's Castle 2R/T", 'Royal Raceway R']

Bright_Glider_ = race_tool('Bright_Glider_', 'High-End', Bright_Glider__3x_Combo_Boost, Bright_Glider__2x_Combo_Boost, Bright_Glider__lv3_courses, Bright_Glider__lv6_courses)


#Barrel_Hanafuda_
# https://game8.co/games/mariokarttour/archives/286549

Barrel_Hanafuda__3x_Combo_Boost = ["Bowser's Castle 1T", "Bowser's Castle 1R", "Bowser's Castle 1", 'Neo Bowser City R', 'Neo Bowser City', 'Neo Bowser City T', 'Daisy Hills R/T', "Bowser's Castle 1R/T", 'Kalimari Desert R/T', 'Dino Dino Jungle R/T', "Bowser's Castle 2", "Bowser's Castle 2R", "Bowser's Castle 2T"]

Barrel_Hanafuda__2x_Combo_Boost = ['Shy Guy Bazaar T', 'Shy Guy Bazaar R', 'Shy Guy Bazaar', 'Kalimari Desert T', 'Kalimari Desert R', 'Kalimari Desert', "Luigi's Mansion", "Luigi's Mansion R", "Luigi's Mansion T"]

Barrel_Hanafuda__lv3_courses = ['Shy Guy Bazaar R', 'Kalimari Desert T']

Barrel_Hanafuda__lv6_courses = ['Kalimari Desert', "Luigi's Mansion R"]

Barrel_Hanafuda_ = race_tool('Barrel_Hanafuda_', 'High-End', Barrel_Hanafuda__3x_Combo_Boost, Barrel_Hanafuda__2x_Combo_Boost, Barrel_Hanafuda__lv3_courses, Barrel_Hanafuda__lv6_courses)


#Daisy_Glider_
# https://game8.co/games/mariokarttour/archives/286872

Daisy_Glider__3x_Combo_Boost = ['Yoshi Circuit T', 'Yoshi Circuit R', 'Shy Guy Bazaar', 'Daisy Hills T', 'Daisy Hills', 'Tokyo Blur R', 'Mario Circuit R', 'DK Pass T', 'DK Pass T', 'Tokyo Blur 2', 'Frappe Snowland T', 'Frappe Snowland R/T', 'Koopa Troopa Beach R/T', 'Tokyo Blur 3', 'Tokyo Blur 3R', 'RMX Rainbow Road 1T', 'Maple Treeway T', 'Sunset Wilds T', 'Berlin Byways 2R']

Daisy_Glider__2x_Combo_Boost = ['Daisy Hills R', 'Tokyo Blur', 'Tokyo Blur R/T', 'DK Pass', 'DK Pass R', 'Yoshi Circuit R/T', 'Tokyo Blur 2R', 'Frappe Snowland', 'Frappe Snowland R', 'RMX Choco Island 1R', 'Maple Treeway R', 'Sunset Wilds R', 'Berlin Byways 2R/T']

Daisy_Glider__lv3_courses = ['Daisy Hills R', 'DK Pass R']

Daisy_Glider__lv6_courses = ['DK Pass', 'Frappe Snowland R']

Daisy_Glider_ = race_tool('Daisy_Glider_', 'High-End', Daisy_Glider__3x_Combo_Boost, Daisy_Glider__2x_Combo_Boost, Daisy_Glider__lv3_courses, Daisy_Glider__lv6_courses)


#Pink_Gold_Paper_Glider_
# https://game8.co/games/mariokarttour/archives/286870

Pink_Gold_Paper_Glider__3x_Combo_Boost = ['Waluigi Pinball T', 'Mario Circuit 3R', 'DS Rainbow Road T', 'Paris Promenade 2', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1R', 'RMX Choco Island 1', 'RMX Choco Island 1R', 'RMX Choco Island 1T', 'Kalimari Desert 2R', 'Airship Fortress', 'RMX Rainbow Road 1R']

Pink_Gold_Paper_Glider__2x_Combo_Boost = ['Yoshi Circuit R', 'Shy Guy Bazaar R', 'Toad Circuit R', 'Mario Circuit 2T', 'Waluigi Pinball R', 'DK Pass', 'Vanilla Lake 1', 'Vanilla Lake 1R', 'RMX Mario Circuit 1T', 'Choco Mountain', 'Kalimari Desert 2', 'Kalimari Desert 2T', 'RMX Rainbow Road 1T', 'RMX Rainbow Road 1R/T', 'Sunset Wilds R/T']

Pink_Gold_Paper_Glider__lv3_courses = ['Waluigi Pinball R', 'Vanilla Lake 1R']

Pink_Gold_Paper_Glider__lv6_courses = ['Choco Mountain', 'Kalimari Desert 2T']

Pink_Gold_Paper_Glider_ = race_tool('Pink_Gold_Paper_Glider_', 'High-End', Pink_Gold_Paper_Glider__3x_Combo_Boost, Pink_Gold_Paper_Glider__2x_Combo_Boost, Pink_Gold_Paper_Glider__lv3_courses, Pink_Gold_Paper_Glider__lv6_courses)


#Butterfly_Sunset_
# https://game8.co/games/mariokarttour/archives/286871

Butterfly_Sunset__3x_Combo_Boost = ['Daisy Hills', 'Toad Circuit R', 'Toad Circuit', 'Kalimari Desert T', 'Kalimari Desert R', 'DK Pass R/T', "Bowser's Castle 2", 'Vanilla Lake 1R/T', 'RMX Choco Island 1R', 'Choco Island 1', 'Koopa Troopa Beach 2T', 'Kalimari Desert 2R', 'RMX Rainbow Road 1R', 'Maple Treeway']

Butterfly_Sunset__2x_Combo_Boost = ['Daisy Hills T', 'Daisy Hills R', 'Kalimari Desert', 'RMX Choco Island 1', 'RMX Choco Island 1T', 'Choco Island 1R', 'Choco Island 1T', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', 'Kalimari Desert 2', 'Kalimari Desert 2T', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1T', 'Maple Treeway T', 'Sunset Wilds', 'Sunset Wilds R']

Butterfly_Sunset__lv3_courses = ['Daisy Hills T', 'Daisy Hills R']

Butterfly_Sunset__lv6_courses = ['Koopa Troopa Beach 2', 'RMX Rainbow Road 1']

Butterfly_Sunset_ = race_tool('Butterfly_Sunset_', 'High-End', Butterfly_Sunset__3x_Combo_Boost, Butterfly_Sunset__2x_Combo_Boost, Butterfly_Sunset__lv3_courses, Butterfly_Sunset__lv6_courses)


#Banana_Wingtip_
# https://game8.co/games/mariokarttour/archives/288935

Banana_Wingtip__3x_Combo_Boost = ['Mario Circuit 1R', 'Cheep Cheep Lagoon T', 'Koopa Troopa Beach T', 'Kalimari Desert R/T', 'Toad Circuit R/T', 'Choco Island 2R/T', 'Paris Promenade 2T', 'Choco Island 1R', 'Choco Mountain T', 'Tokyo Blur 3T', 'Los Angeles Laps T', 'Los Angeles Laps R/T']

Banana_Wingtip__2x_Combo_Boost = ['Rock Rock Mountain T', 'Rock Rock Mountain R', 'Cheep Cheep Lagoon R', 'Koopa Troopa Beach R', 'Dino Dino Jungle T', 'Toad Circuit R', 'Toad Circuit', 'Mario Circuit 1', 'Cheep Cheep Lagoon', 'DK Pass R/T', 'Dino Dino Jungle R/T', 'RMX Choco Island 1', 'Choco Island 1', 'Choco Mountain', 'Tokyo Blur 3R', 'Los Angeles Laps', 'Los Angeles Laps R', 'Maple Treeway R', 'Donut Plains 2R', 'Donut Plains 2T']

Banana_Wingtip__lv3_courses = ['Dino Dino Jungle T', 'Mario Circuit 1']

Banana_Wingtip__lv6_courses = ['Toad Circuit', 'Choco Mountain']

Banana_Wingtip_ = race_tool('Banana_Wingtip_', 'High-End', Banana_Wingtip__3x_Combo_Boost, Banana_Wingtip__2x_Combo_Boost, Banana_Wingtip__lv3_courses, Banana_Wingtip__lv6_courses)


#Tropical_Glider_
# https://game8.co/games/mariokarttour/archives/288936

Tropical_Glider__3x_Combo_Boost = ['Yoshi Circuit T', 'Koopa Troopa Beach T', 'Koopa Troopa Beach', 'Dino Dino Jungle R', 'Dino Dino Jungle', 'Daisy Hills T', 'Tokyo Blur', 'Choco Island 2R', 'Choco Island 2', 'Tokyo Blur T', 'Toad Circuit R/T', 'Dino Dino Jungle R/T', 'Donut Plains 1', 'Donut Plains 1R', 'RMX Choco Island 1', 'RMX Choco Island 1R', 'RMX Rainbow Road 1T']

Tropical_Glider__2x_Combo_Boost = ['Yoshi Circuit', 'Koopa Troopa Beach R', 'Dino Dino Jungle T', 'Daisy Hills', 'Choco Island 2T', 'Vanilla Lake 1', 'Vanilla Lake 1R', 'Choco Island 2R/T', 'Shy Guy Bazaar R/T', 'Donut Plains 1T', "Bowser's Castle 2", 'RMX Choco Island 1T', 'Choco Island 1', 'Choco Island 1R', 'Choco Island 1T', 'Tokyo Blur 3', 'Tokyo Blur 3T', 'RMX Rainbow Road 1R', 'Los Angeles Laps R', 'Donut Plains 2', 'Donut Plains 2R']

Tropical_Glider__lv3_courses = ['Daisy Hills', 'Shy Guy Bazaar R/T']

Tropical_Glider__lv6_courses = ['Choco Island 1T', 'RMX Rainbow Road 1R']

Tropical_Glider_ = race_tool('Tropical_Glider_', 'High-End', Tropical_Glider__3x_Combo_Boost, Tropical_Glider__2x_Combo_Boost, Tropical_Glider__lv3_courses, Tropical_Glider__lv6_courses)


#Dragon_Wings_
# https://game8.co/games/mariokarttour/archives/288937

Dragon_Wings__3x_Combo_Boost = ['Rock Rock Mountain T', 'Rock Rock Mountain', 'Dino Dino Jungle T', 'Dino Dino Jungle R', 'Kalimari Desert T', 'Neo Bowser City R', 'Neo Bowser City', 'Neo Bowser City T', 'Waluigi Pinball R', 'DK Pass T', 'DK Pass R', 'London Loop R', 'London Loop T', "Bowser's Castle 1R/T", 'Dino Dino Jungle R/T', "Bowser's Castle 2R", "Bowser's Castle 2T", "Bowser's Castle 2R/T", 'RMX Choco Island 1R', 'New York Minute 3', 'Sunset Wilds T', 'Donut Plains 2']

Dragon_Wings__2x_Combo_Boost = ['Rock Rock Mountain R', 'Dino Dino Jungle', 'Kalimari Desert R', 'Kalimari Desert', 'Waluigi Pinball', 'Waluigi Pinball R', 'London Loop R/T', 'Vanilla Lake 1R', 'DK Pass R/T', "Bowser's Castle 2", 'RMX Choco Island 1', 'Choco Island 1T', 'Choco Mountain', 'Choco Mountain R', 'New York Minute 3R', 'New York Minute 3R/T', 'Donut Plains 2T']

Dragon_Wings__lv3_courses = ['Waluigi Pinball', 'DK Pass R/T']

Dragon_Wings__lv6_courses = ['Kalimari Desert', 'Choco Island 1T']

Dragon_Wings_ = race_tool('Dragon_Wings_', 'High-End', Dragon_Wings__3x_Combo_Boost, Dragon_Wings__2x_Combo_Boost, Dragon_Wings__lv3_courses, Dragon_Wings__lv6_courses)


#Blooper_Hanafuda_
# https://game8.co/games/mariokarttour/archives/288938

Blooper_Hanafuda__3x_Combo_Boost = ['Koopa Troopa Beach T', 'Koopa Troopa Beach R', 'Koopa Troopa Beach', 'Choco Island 2R', 'Choco Island 2', 'Choco Island 2T', 'Cheep Cheep Lagoon R/T', 'Mario Circuit 1R/T', 'Mario Circuit 2R/T', 'Vanilla Lake 1', 'Vanilla Lake 1R', 'Vanilla Lake 1T']

Blooper_Hanafuda__2x_Combo_Boost = ['Cheep Cheep Lagoon T', 'Cheep Cheep Lagoon R', 'Cheep Cheep Lagoon', 'Mario Circuit 2T', 'Mario Circuit 2T', 'Mario Circuit 2R', 'Mario Circuit 2R', 'Mario Circuit 2', 'Mario Circuit 2', 'DK Pass', 'DK Pass T', 'DK Pass R', "Rosalina's Ice World", "Rosalina's Ice World R", "Rosalina's Ice World T"]

Blooper_Hanafuda__lv3_courses = ['Mario Circuit 2R', 'DK Pass T']

Blooper_Hanafuda__lv6_courses = ['Cheep Cheep Lagoon', 'DK Pass']

Blooper_Hanafuda_ = race_tool('Blooper_Hanafuda_', 'High-End', Blooper_Hanafuda__3x_Combo_Boost, Blooper_Hanafuda__2x_Combo_Boost, Blooper_Hanafuda__lv3_courses, Blooper_Hanafuda__lv6_courses)


#Chocolate_Donut_
# https://game8.co/games/mariokarttour/archives/289733

Chocolate_Donut__3x_Combo_Boost = ['Koopa Troopa Beach T', 'Koopa Troopa Beach R', 'Daisy Hills R', 'Choco Island 2T', 'Donut Plains 1', 'Donut Plains 1R', 'Donut Plains 1R/T', 'Choco Island 1', 'Choco Mountain R', 'Maple Treeway', 'Sunset Wilds', 'Sunset Wilds R/T', 'Donut Plains 2']

Chocolate_Donut__2x_Combo_Boost = ['Daisy Hills T', 'Choco Island 2R', 'Kalimari Desert', 'Donut Plains 1T', 'Choco Island 1R', 'Choco Island 1T', 'Royal Raceway T', 'Royal Raceway', 'Choco Mountain', 'Choco Mountain T', 'Maple Treeway T', 'Sunset Wilds T', 'Donut Plains 2R', 'Donut Plains 2T']

Chocolate_Donut__lv3_courses = ['Daisy Hills T', 'Choco Island 2R']

Chocolate_Donut__lv6_courses = ['Royal Raceway T', 'Royal Raceway']

Chocolate_Donut_ = race_tool('Chocolate_Donut_', 'High-End', Chocolate_Donut__3x_Combo_Boost, Chocolate_Donut__2x_Combo_Boost, Chocolate_Donut__lv3_courses, Chocolate_Donut__lv6_courses)


#Gold_Crane_
# https://game8.co/games/mariokarttour/archives/289734

Gold_Crane__3x_Combo_Boost = ['Mario Circuit 2R', 'Mario Circuit 2', 'Kalimari Desert R', 'Kalimari Desert', 'Tokyo Blur R/T', 'Mario Circuit 1R/T', 'Mario Circuit 1R/T', 'Paris Promenade 2R', 'Paris Promenade 2T', 'Waluigi Pinball R/T', 'Vancouver Velocity', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1T', 'Koopa Troopa Beach 2', 'RMX Rainbow Road 1', 'New York Minute 3', 'New York Minute 3R', 'Sunset Wilds T', 'RMX Choco Island 2T']

Gold_Crane__2x_Combo_Boost = ['Kalimari Desert T', 'Waluigi Pinball', 'Waluigi Pinball T', 'DS Rainbow Road T', 'Tokyo Blur 2', 'Tokyo Blur 2R', 'Donut Plains 1', 'RMX Choco Island 1R', 'Choco Island 1R', 'Choco Island 1T', 'Koopa Troopa Beach 2T', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 1T', 'New York Minute 3R/T']

Gold_Crane__lv3_courses = ['Waluigi Pinball T', 'DS Rainbow Road T']

Gold_Crane__lv6_courses = ['Koopa Troopa Beach 2T', 'RMX Rainbow Road 1T']

Gold_Crane_ = race_tool('Gold_Crane_', 'High-End', Gold_Crane__3x_Combo_Boost, Gold_Crane__2x_Combo_Boost, Gold_Crane__lv3_courses, Gold_Crane__lv6_courses)


#Chocolate_Banana_Crepe_
# https://game8.co/games/mariokarttour/archives/289735

Chocolate_Banana_Crepe__3x_Combo_Boost = ['Yoshi Circuit R', 'Yoshi Circuit', 'Cheep Cheep Lagoon R', 'Vanilla Lake 1', 'Choco Island 1R', 'Choco Island 1T', 'Choco Mountain', 'Choco Mountain R', 'Kalimari Desert 2', 'Kalimari Desert 2T', 'Maple Treeway T', 'Sunset Wilds R/T']

Chocolate_Banana_Crepe__2x_Combo_Boost = ['Cheep Cheep Lagoon T', 'Cheep Cheep Lagoon', 'Ghost Valley 1', 'Choco Island 1', 'Royal Raceway R', 'Royal Raceway T', 'Choco Mountain T', 'Kalimari Desert 2R', 'Maple Treeway R', 'RMX Rainbow Road 1R/T']

Chocolate_Banana_Crepe__lv3_courses = ['Cheep Cheep Lagoon T', 'Choco Island 1']

Chocolate_Banana_Crepe__lv6_courses = ['Choco Mountain T', 'Kalimari Desert 2R']

Chocolate_Banana_Crepe_ = race_tool('Chocolate_Banana_Crepe_', 'High-End', Chocolate_Banana_Crepe__3x_Combo_Boost, Chocolate_Banana_Crepe__2x_Combo_Boost, Chocolate_Banana_Crepe__lv3_courses, Chocolate_Banana_Crepe__lv6_courses)


#Strawberry_Donut_
# https://game8.co/games/mariokarttour/archives/289736

Strawberry_Donut__3x_Combo_Boost = ['Yoshi Circuit T', 'Yoshi Circuit', 'Daisy Hills R', 'Paris Promenade 2T', 'Ghost Valley 1R/T', 'Vancouver Velocity T', 'Vancouver Velocity R', 'Donut Plains 1', 'Donut Plains 1T', 'Choco Island 1T', 'Royal Raceway T', 'Choco Mountain', 'Choco Mountain T', 'Maple Treeway T', 'Berlin Byways 2R/T', 'Donut Plains 2R', 'DK Summit R']

Strawberry_Donut__2x_Combo_Boost = ['Yoshi Circuit R', 'Daisy Hills', "Luigi's Mansion", 'Frappe Snowland R', 'Donut Plains 1R', 'Choco Island 1', 'Choco Island 1R', 'Royal Raceway R', 'Choco Mountain R', 'Maple Treeway R', 'Sunset Wilds', 'Sunset Wilds R', 'Berlin Byways 2', 'Berlin Byways 2T', 'Donut Plains 2']

Strawberry_Donut__lv3_courses = ['Yoshi Circuit R', 'Daisy Hills']

Strawberry_Donut__lv6_courses = ['Choco Island 1R', 'Choco Mountain R']

Strawberry_Donut_ = race_tool('Strawberry_Donut_', 'High-End', Strawberry_Donut__3x_Combo_Boost, Strawberry_Donut__2x_Combo_Boost, Strawberry_Donut__lv3_courses, Strawberry_Donut__lv6_courses)


#Cape_Mario_Hanafuda_
# https://game8.co/games/mariokarttour/archives/290563

Cape_Mario_Hanafuda__3x_Combo_Boost = ['Mario Circuit 1T', 'Mario Circuit 1R', 'Mario Circuit 1', 'Mario Circuit 3R/T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1R', 'RMX Mario Circuit 1T', 'RMX Choco Island 1', 'RMX Choco Island 1R', 'RMX Choco Island 1T']

Cape_Mario_Hanafuda__2x_Combo_Boost = ['Toad Circuit T', 'Toad Circuit R', 'Toad Circuit', 'Tokyo Blur R', 'Tokyo Blur', 'Mario Circuit R', 'Mario Circuit', 'Mario Circuit T', 'Tokyo Blur T', 'Tokyo Blur R/T', 'Mario Circuit 3', 'Mario Circuit 3T', 'Mario Circuit 3R', 'Mario Circuit R/T', 'DS Rainbow Road', 'DS Rainbow Road R', 'DS Rainbow Road T', 'Toad Circuit R/T']

Cape_Mario_Hanafuda__lv3_courses = ['Mario Circuit', 'Mario Circuit T']

Cape_Mario_Hanafuda__lv6_courses = ['Toad Circuit', 'DS Rainbow Road R']

Cape_Mario_Hanafuda_ = race_tool('Cape_Mario_Hanafuda_', 'High-End', Cape_Mario_Hanafuda__3x_Combo_Boost, Cape_Mario_Hanafuda__2x_Combo_Boost, Cape_Mario_Hanafuda__lv3_courses, Cape_Mario_Hanafuda__lv6_courses)


#Silver_Bells_
# https://game8.co/games/mariokarttour/archives/290562

Silver_Bells__3x_Combo_Boost = ['Shy Guy Bazaar T', 'SNES Rainbow Road', 'Mario Circuit T', 'Paris Promenade T', 'Paris Promenade', 'Paris Promenade R', 'Mario Circuit R/T', 'Daisy Hills R/T', 'Frappe Snowland R', 'Waluigi Pinball R/T', 'Frappe Snowland R/T', 'DS Rainbow Road R/T', 'Royal Raceway', 'Choco Mountain', 'Sunset Wilds T', 'Berlin Byways 2T', 'RMX Choco Island 2']

Silver_Bells__2x_Combo_Boost = ['Shy Guy Bazaar R', 'Choco Island 2R', 'Mario Circuit', 'Choco Island 2T', 'Paris Promenade R/T', 'Yoshi Circuit R/T', 'Yoshi Circuit R/T', "Luigi's Mansion R/T", 'DS Rainbow Road', 'DS Rainbow Road R', 'Mario Circuit 1R/T', 'Frappe Snowland T', 'Koopa Troopa Beach 2', 'Choco Mountain R', 'Choco Mountain T', 'Berlin Byways 2R', 'RMX Choco Island 2R', 'RMX Choco Island 2T', 'DK Summit R']

Silver_Bells__lv3_courses = ['Shy Guy Bazaar R', "Luigi's Mansion R/T"]

Silver_Bells__lv6_courses = ['DS Rainbow Road R', 'Koopa Troopa Beach 2']

Silver_Bells_ = race_tool('Silver_Bells_', 'High-End', Silver_Bells__3x_Combo_Boost, Silver_Bells__2x_Combo_Boost, Silver_Bells__lv3_courses, Silver_Bells__lv6_courses)


#Silver_and_Gold_Hearts_
# https://game8.co/games/mariokarttour/archives/290561

Silver_and_Gold_Hearts__3x_Combo_Boost = ['SNES Rainbow Road', 'Mario Circuit 3', 'Mario Circuit 3', 'Paris Promenade T', 'Paris Promenade', 'Paris Promenade R/T', 'Paris Promenade R', 'Donut Plains 1R/T', 'Donut Plains 1R/T', 'RMX Choco Island 1', 'Choco Island 1T', 'Royal Raceway R', 'Royal Raceway', 'Kalimari Desert 2', 'Kalimari Desert 2T', 'Los Angeles Laps R', 'Merry Mountain', 'RMX Rainbow Road 2T']

Silver_and_Gold_Hearts__2x_Combo_Boost = ['Mario Circuit R', 'Mario Circuit', 'SNES Rainbow Road R', 'Mario Circuit 3T', 'Mario Circuit 3R', 'Cheep Cheep Lagoon R/T', 'Mario Circuit 3R/T', 'RMX Choco Island 1T', 'Royal Raceway T', 'Kalimari Desert 2R', 'Los Angeles Laps T', 'Los Angeles Laps R/T', 'New York Minute 3', 'New York Minute 3R', 'Sunset Wilds', 'Sunset Wilds T', 'Merry Mountain T']

Silver_and_Gold_Hearts__lv3_courses = ['Mario Circuit 3R/T']

Silver_and_Gold_Hearts__lv6_courses = ['RMX Choco Island 1T', 'Royal Raceway T']

Silver_and_Gold_Hearts_ = race_tool('Silver_and_Gold_Hearts_', 'High-End', Silver_and_Gold_Hearts__3x_Combo_Boost, Silver_and_Gold_Hearts__2x_Combo_Boost, Silver_and_Gold_Hearts__lv3_courses, Silver_and_Gold_Hearts__lv6_courses)


#Manta_Glider_
# https://game8.co/games/mariokarttour/archives/291196

Manta_Glider__3x_Combo_Boost = ['Cheep Cheep Lagoon T', 'Cheep Cheep Lagoon R', 'Cheep Cheep Lagoon', 'DK Pass R', 'SNES Rainbow Road R/T', 'Cheep Cheep Lagoon R/T', 'RMX Mario Circuit 1T', 'Vanilla Lake 1R/T', 'Koopa Troopa Beach 2R', 'Airship Fortress', 'Airship Fortress R', 'Los Angeles Laps', 'Los Angeles Laps R', "Rosalina's Ice World", "Rosalina's Ice World R"]

Manta_Glider__2x_Combo_Boost = ['Cheep Cheep Lagoon R', 'Koopa Troopa Beach T', 'Koopa Troopa Beach', 'DK Pass', 'Yoshi Circuit R/T', 'Vanilla Lake 1T', 'Koopa Troopa Beach R/T', 'RMX Mario Circuit 1R', 'Royal Raceway', 'Koopa Troopa Beach 2', 'Airship Fortress T', 'Los Angeles Laps T', "Rosalina's Ice World T"]

Manta_Glider__lv3_courses = ['Koopa Troopa Beach T', 'Koopa Troopa Beach 2T', 'Koopa Troopa Beach 2T']

Manta_Glider__lv6_courses = ['Royal Raceway', 'Airship Fortress T']

Manta_Glider_ = race_tool('Manta_Glider_', 'High-End', Manta_Glider__3x_Combo_Boost, Manta_Glider__2x_Combo_Boost, Manta_Glider__lv3_courses, Manta_Glider__lv6_courses)


#Blooper_Wingtip_
# https://game8.co/games/mariokarttour/archives/291197

Blooper_Wingtip__3x_Combo_Boost = ['Cheep Cheep Lagoon T', 'Mario Circuit 2', 'Ghost Valley 1', 'Yoshi Circuit R/T', 'Choco Island 1', 'Choco Island 1', 'Choco Island 1T', 'Choco Island 1T', 'Royal Raceway', 'Choco Mountain R', 'Choco Mountain T', 'Los Angeles Laps R/T', 'Merry Mountain T', 'Berlin Byways 2T', 'Berlin Byways 2R/T', 'DK Summit']

Blooper_Wingtip__2x_Combo_Boost = ['Cheep Cheep Lagoon R', 'Ghost Valley 1R', 'Ghost Valley 1T', 'Cheep Cheep Lagoon R/T', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', 'Choco Mountain', 'Airship Fortress', 'Airship Fortress R', 'Los Angeles Laps T', 'Merry Mountain', 'Berlin Byways 2R', 'DK Summit T']

Blooper_Wingtip__lv3_courses = ['Mario Circuit 2T', 'Koopa Troopa Beach 2R']

Blooper_Wingtip__lv6_courses = ['Cheep Cheep Lagoon R', 'Airship Fortress']

Blooper_Wingtip_ = race_tool('Blooper_Wingtip_', 'High-End', Blooper_Wingtip__3x_Combo_Boost, Blooper_Wingtip__2x_Combo_Boost, Blooper_Wingtip__lv3_courses, Blooper_Wingtip__lv6_courses)


#Treasure_Map_
# https://game8.co/games/mariokarttour/archives/291847

Treasure_Map__3x_Combo_Boost = ['Rock Rock Mountain R', 'Toad Circuit', 'Dino Dino Jungle R/T', 'Royal Raceway', 'Koopa Troopa Beach 2', 'Choco Mountain R', 'Choco Mountain T', 'Kalimari Desert 2R', 'Airship Fortress']

Treasure_Map__2x_Combo_Boost = ['Rock Rock Mountain', 'Toad Circuit R', 'RMX Choco Island 1', 'Koopa Troopa Beach 2T', 'Choco Mountain', 'Kalimari Desert 2', 'Kalimari Desert 2T', 'Airship Fortress R', 'Airship Fortress T', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1R', 'Sunset Wilds R/T']

Treasure_Map__lv3_courses = ['Rock Rock Mountain', 'Airship Fortress R']

Treasure_Map__lv6_courses = ['Choco Mountain', 'RMX Rainbow Road 1']

Treasure_Map_ = race_tool('Treasure_Map_', 'High-End', Treasure_Map__3x_Combo_Boost, Treasure_Map__2x_Combo_Boost, Treasure_Map__lv3_courses, Treasure_Map__lv6_courses)


#Butterfly_Wings_
# https://game8.co/games/mariokarttour/archives/292314

Butterfly_Wings__3x_Combo_Boost = ['Dino Dino Jungle T', 'Dino Dino Jungle', 'Kalimari Desert R/T', 'Vanilla Lake 1T', 'Vancouver Velocity', 'Vancouver Velocity R', 'Vancouver Velocity R/T', 'Donut Plains 1R', 'Donut Plains 1T', 'Royal Raceway T', 'Airship Fortress R', 'Tokyo Blur 3', 'Tokyo Blur 3R', 'RMX Rainbow Road 1R', 'Merry Mountain T', "Rosalina's Ice World T", 'Berlin Byways 2', 'Berlin Byways 2R']

Butterfly_Wings__2x_Combo_Boost = ['Dino Dino Jungle R', 'Frappe Snowland', 'Frappe Snowland T', 'Vancouver Velocity T', 'Frappe Snowland R/T', 'Donut Plains 1', 'Royal Raceway R', 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'Airship Fortress', 'Airship Fortress T', 'RMX Rainbow Road 1T', 'RMX Rainbow Road 1R/T', 'Merry Mountain', "Rosalina's Ice World", "Rosalina's Ice World R"]

Butterfly_Wings__lv3_courses = ['Mario Circuit 1R', 'Dino Dino Jungle R']

Butterfly_Wings__lv6_courses = ['Kalimari Desert 2T', 'Airship Fortress T']

Butterfly_Wings_ = race_tool('Butterfly_Wings_', 'High-End', Butterfly_Wings__3x_Combo_Boost, Butterfly_Wings__2x_Combo_Boost, Butterfly_Wings__lv3_courses, Butterfly_Wings__lv6_courses)


#Bullet_Bill_Hanafuda_
# https://game8.co/games/mariokarttour/archives/292313

Bullet_Bill_Hanafuda__3x_Combo_Boost = ['Rock Rock Mountain T', 'Rock Rock Mountain R', 'Rock Rock Mountain', 'Frappe Snowland', 'Frappe Snowland T', 'Frappe Snowland R', 'Frappe Snowland R/T', 'Royal Raceway R', 'Royal Raceway T', 'Royal Raceway']

Bullet_Bill_Hanafuda__2x_Combo_Boost = ['Waluigi Pinball', 'Waluigi Pinball R', 'Waluigi Pinball T', 'RMX Choco Island 1', 'RMX Choco Island 1R', 'RMX Choco Island 1T', 'Kalimari Desert 2', 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'Airship Fortress', 'Airship Fortress R', 'Airship Fortress T']

Bullet_Bill_Hanafuda__lv3_courses = ['Waluigi Pinball', 'Waluigi Pinball T']

Bullet_Bill_Hanafuda__lv6_courses = ['Kalimari Desert 2T', 'Airship Fortress']

Bullet_Bill_Hanafuda_ = race_tool('Bullet_Bill_Hanafuda_', 'High-End', Bullet_Bill_Hanafuda__3x_Combo_Boost, Bullet_Bill_Hanafuda__2x_Combo_Boost, Bullet_Bill_Hanafuda__lv3_courses, Bullet_Bill_Hanafuda__lv6_courses)


#Nabbit_Oilpaper_Umbrella_
# https://game8.co/games/mariokarttour/archives/292312

Nabbit_Oilpaper_Umbrella__3x_Combo_Boost = ['Shy Guy Bazaar', "Bowser's Castle 1T", "Bowser's Castle 1", 'Neo Bowser City R', 'Tokyo Blur T', "Luigi's Mansion R/T", "Luigi's Mansion R/T", 'Donut Plains 1R', "Bowser's Castle 2T", 'Vanilla Lake 1R/T', 'Choco Mountain', 'Choco Mountain R', 'Choco Mountain T', 'Tokyo Blur 3R', 'Tokyo Blur 3T', 'RMX Choco Island 2T', 'DK Summit T']

Nabbit_Oilpaper_Umbrella__2x_Combo_Boost = ['Mario Circuit 1T', 'Shy Guy Bazaar R', 'Mario Circuit 1', 'Tokyo Blur R', 'Tokyo Blur', 'Choco Island 2R', 'Choco Island 2T', 'Neo Bowser City T', 'Kalimari Desert 2', 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'Airship Fortress R', 'Airship Fortress T', 'Tokyo Blur 3', 'Donut Plains 2R', 'Donut Plains 2T', 'RMX Choco Island 2R']

Nabbit_Oilpaper_Umbrella__lv3_courses = ['Mario Circuit 1T', 'Neo Bowser City T']

Nabbit_Oilpaper_Umbrella__lv6_courses = ['Kalimari Desert 2', 'Airship Fortress T']

Nabbit_Oilpaper_Umbrella_ = race_tool('Nabbit_Oilpaper_Umbrella_', 'High-End', Nabbit_Oilpaper_Umbrella__3x_Combo_Boost, Nabbit_Oilpaper_Umbrella__2x_Combo_Boost, Nabbit_Oilpaper_Umbrella__lv3_courses, Nabbit_Oilpaper_Umbrella__lv6_courses)


#Great_Sail_
# https://game8.co/games/mariokarttour/archives/292676

Great_Sail__3x_Combo_Boost = ['Tokyo Blur 2', 'Tokyo Blur 2T', 'Frappe Snowland T', 'Choco Island 1R', 'Royal Raceway', 'Koopa Troopa Beach 2R', 'Koopa Troopa Beach 2T', 'Kalimari Desert 2', 'Kalimari Desert 2T', 'Airship Fortress', 'Los Angeles Laps R/T']

Great_Sail__2x_Combo_Boost = ['Daisy Hills T', 'Daisy Hills', 'Yoshi Circuit R/T', 'Tokyo Blur 2R', 'Royal Raceway R', 'Airship Fortress T', 'RMX Rainbow Road 1T', 'Los Angeles Laps', 'Los Angeles Laps R', "Rosalina's Ice World R", 'DK Summit']

Great_Sail__lv3_courses = ['Daisy Hills T', 'Yoshi Circuit R/T']

Great_Sail__lv6_courses = ['Royal Raceway R', 'RMX Rainbow Road 1T']

Great_Sail_ = race_tool('Great_Sail_', 'High-End', Great_Sail__3x_Combo_Boost, Great_Sail__2x_Combo_Boost, Great_Sail__lv3_courses, Great_Sail__lv6_courses)


#Boo_Hanafuda_
# https://game8.co/games/mariokarttour/archives/292677

Boo_Hanafuda__3x_Combo_Boost = ["Luigi's Mansion", "Luigi's Mansion R", "Luigi's Mansion T", "Luigi's Mansion R/T", 'Shy Guy Bazaar R/T', 'Ghost Valley 1R/T', 'Kalimari Desert 2', 'Kalimari Desert 2R', 'Kalimari Desert 2T']

Boo_Hanafuda__2x_Combo_Boost = ['Shy Guy Bazaar T', 'Shy Guy Bazaar R', 'Shy Guy Bazaar', "Bowser's Castle 1T", "Bowser's Castle 1R", "Bowser's Castle 1", 'Ghost Valley 1', 'Ghost Valley 1R', 'Ghost Valley 1T', 'London Loop', 'London Loop R', 'London Loop R/T', 'London Loop T']

Boo_Hanafuda__lv3_courses = ['Shy Guy Bazaar R', "Bowser's Castle 1R"]

Boo_Hanafuda__lv6_courses = ['Shy Guy Bazaar', 'Ghost Valley 1R']

Boo_Hanafuda_ = race_tool('Boo_Hanafuda_', 'High-End', Boo_Hanafuda__3x_Combo_Boost, Boo_Hanafuda__2x_Combo_Boost, Boo_Hanafuda__lv3_courses, Boo_Hanafuda__lv6_courses)


#Festival_Wings_
# https://game8.co/games/mariokarttour/archives/293915

Festival_Wings__3x_Combo_Boost = ['Rock Rock Mountain R', 'Shy Guy Bazaar T', 'Shy Guy Bazaar R', 'Tokyo Blur', 'Tokyo Blur R/T', 'Mario Circuit 3T', 'Cheep Cheep Lagoon R/T', 'Mario Circuit 2R/T', 'Koopa Troopa Beach R/T', 'Airship Fortress T', 'Tokyo Blur 3', 'RMX Rainbow Road 1T', 'Berlin Byways 2T']

Festival_Wings__2x_Combo_Boost = ['Daisy Hills', 'Tokyo Blur R', 'Kalimari Desert R', 'Tokyo Blur T', 'Waluigi Pinball', 'Waluigi Pinball R', 'Mario Circuit 3', 'Shy Guy Bazaar R/T', 'Airship Fortress', 'Tokyo Blur 3R', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1R', 'Los Angeles Laps T', 'Los Angeles Laps', 'Los Angeles Laps R', 'Berlin Byways 2R']

Festival_Wings__lv3_courses = ['Mario Circuit 3', 'RMX Rainbow Road 1R']

Festival_Wings__lv6_courses = ['Kalimari Desert R', 'Waluigi Pinball']

Festival_Wings_ = race_tool('Festival_Wings_', 'High-End', Festival_Wings__3x_Combo_Boost, Festival_Wings__2x_Combo_Boost, Festival_Wings__lv3_courses, Festival_Wings__lv6_courses)


#Cheep_Cheep_Mask_
# https://game8.co/games/mariokarttour/archives/293916

Cheep_Cheep_Mask__3x_Combo_Boost = ['Cheep Cheep Lagoon R', 'Cheep Cheep Lagoon', 'Tokyo Blur', 'Neo Bowser City T', 'Ghost Valley 1T', 'Cheep Cheep Lagoon R/T', 'Tokyo Blur 2', 'Vanilla Lake 1R', 'Choco Island 1R', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2T', 'Choco Mountain R', 'Airship Fortress T', 'Los Angeles Laps', 'Maple Treeway R', 'Donut Plains 2T']

Cheep_Cheep_Mask__2x_Combo_Boost = ['Cheep Cheep Lagoon T', 'Neo Bowser City R', 'Tokyo Blur T', 'Ghost Valley 1', 'Vanilla Lake 1T', 'Waluigi Pinball R/T', 'Ghost Valley 1R/T', 'Tokyo Blur 3', 'Tokyo Blur 3T', 'RMX Rainbow Road 1', 'Los Angeles Laps R/T', 'Los Angeles Laps R', 'Maple Treeway']

Cheep_Cheep_Mask__lv3_courses = ['Cheep Cheep Lagoon T', 'Ghost Valley 1']

Cheep_Cheep_Mask__lv6_courses = ['Vanilla Lake 1T', 'RMX Rainbow Road 1']

Cheep_Cheep_Mask_ = race_tool('Cheep_Cheep_Mask_', 'High-End', Cheep_Cheep_Mask__3x_Combo_Boost, Cheep_Cheep_Mask__2x_Combo_Boost, Cheep_Cheep_Mask__lv3_courses, Cheep_Cheep_Mask__lv6_courses)


#Bit_Star_8_Bit_Star1
# https://game8.co/games/mariokarttour/archives/296089

Bit_Star_8_Bit_Star1_3x_Combo_Boost = ['Choco Island 2R', 'SNES Rainbow Road T', 'SNES Rainbow Road R', 'Mario Circuit 3T', 'DK Pass T', 'RMX Mario Circuit 1R/T', 'Choco Island 1', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1T', 'Los Angeles Laps R', 'Sunset Wilds R', 'RMX Rainbow Road 1R/T', "Rosalina's Ice World", 'RMX Rainbow Road 2', 'Berlin Byways 2']

Bit_Star_8_Bit_Star1_2x_Combo_Boost = ['SNES Rainbow Road', 'Mario Circuit 2R', 'Choco Island 2', 'Mario Circuit 3R', 'DK Pass R', 'SNES Rainbow Road R/T', 'DS Rainbow Road T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1R', 'RMX Mario Circuit 1T', 'Choco Island 1R', 'Choco Island 1T', 'RMX Rainbow Road 1R', 'Los Angeles Laps T', 'Los Angeles Laps', 'Los Angeles Laps R/T', 'Sunset Wilds', 'RMX Rainbow Road 2R']

Bit_Star_8_Bit_Star1_lv3_courses = ['DK Pass R', 'DS Rainbow Road T']

Bit_Star_8_Bit_Star1_lv6_courses = ['RMX Mario Circuit 1', 'RMX Mario Circuit 1T']

Bit_Star_8_Bit_Star1 = race_tool('Bit_Star_8_Bit_Star1', 'High-End', Bit_Star_8_Bit_Star1_3x_Combo_Boost, Bit_Star_8_Bit_Star1_2x_Combo_Boost, Bit_Star_8_Bit_Star1_lv3_courses, Bit_Star_8_Bit_Star1_lv6_courses)


#Super_Mario_Kart_Glider_
# https://game8.co/games/mariokarttour/archives/296090

Super_Mario_Kart_Glider__3x_Combo_Boost = ['Mario Circuit 1R', 'Mario Circuit 1', 'SNES Rainbow Road', 'Choco Island 2', 'SNES Rainbow Road T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1R/T', "Bowser's Castle 2R/T", 'RMX Choco Island 1', 'RMX Choco Island 1T', 'New York Minute 3R', 'Donut Plains 2R', 'Donut Plains 2T']

Super_Mario_Kart_Glider__2x_Combo_Boost = ['Mario Circuit 1T', 'Mario Circuit 2', 'Choco Island 2T', 'Choco Island 2T', 'SNES Rainbow Road R', 'London Loop R/T', 'Mario Circuit 2R/T', 'Ghost Valley 1R/T', 'RMX Mario Circuit 1R', 'Donut Plains 1', 'Donut Plains 1R', 'RMX Choco Island 1R', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 1T', 'New York Minute 3', 'New York Minute 3R/T', 'Sunset Wilds R', 'Sunset Wilds T', 'RMX Rainbow Road 2', 'Donut Plains 2']

Super_Mario_Kart_Glider__lv3_courses = ['Mario Circuit 1T', 'Mario Circuit 2R/T']

Super_Mario_Kart_Glider__lv6_courses = ['Donut Plains 1', 'RMX Choco Island 1R']

Super_Mario_Kart_Glider_ = race_tool('Super_Mario_Kart_Glider_', 'High-End', Super_Mario_Kart_Glider__3x_Combo_Boost, Super_Mario_Kart_Glider__2x_Combo_Boost, Super_Mario_Kart_Glider__lv3_courses, Super_Mario_Kart_Glider__lv6_courses)


#Piranha_Plant_Hanafuda_
# https://game8.co/games/mariokarttour/archives/297362

Piranha_Plant_Hanafuda__3x_Combo_Boost = ['Kalimari Desert R/T', 'Donut Plains 1', 'Donut Plains 1R', 'Donut Plains 1T', 'Donut Plains 1R/T', 'Choco Island 1', 'Choco Island 1R', 'Choco Island 1T', 'Kalimari Desert 2', 'Kalimari Desert 2R', 'Kalimari Desert 2T']

Piranha_Plant_Hanafuda__2x_Combo_Boost = ['SNES Rainbow Road', 'SNES Rainbow Road T', 'SNES Rainbow Road R', 'Paris Promenade T', 'Paris Promenade', 'Paris Promenade R/T', 'Paris Promenade R', 'SNES Rainbow Road R/T', 'Frappe Snowland', 'Frappe Snowland T', 'Frappe Snowland R', 'Frappe Snowland R/T']

Piranha_Plant_Hanafuda__lv3_courses = ['SNES Rainbow Road', 'Frappe Snowland R']

Piranha_Plant_Hanafuda__lv6_courses = ['SNES Rainbow Road R', 'Frappe Snowland']

Piranha_Plant_Hanafuda_ = race_tool('Piranha_Plant_Hanafuda_', 'High-End', Piranha_Plant_Hanafuda__3x_Combo_Boost, Piranha_Plant_Hanafuda__2x_Combo_Boost, Piranha_Plant_Hanafuda__lv3_courses, Piranha_Plant_Hanafuda__lv6_courses)


#Star_Spangled_Glider_
# https://game8.co/games/mariokarttour/archives/297363

Star_Spangled_Glider__3x_Combo_Boost = ['Rock Rock Mountain R', 'Koopa Troopa Beach', 'Kalimari Desert R', 'Kalimari Desert', 'Vancouver Velocity R', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1T', 'Los Angeles Laps T', 'Los Angeles Laps', 'New York Minute 3R', 'New York Minute 3T', 'RMX Rainbow Road 1R/T', 'Merry Mountain', 'Merry Mountain R', "Rosalina's Ice World", "Rosalina's Ice World R"]

Star_Spangled_Glider__2x_Combo_Boost = ['Rock Rock Mountain T', 'Rock Rock Mountain', 'Koopa Troopa Beach T', 'Koopa Troopa Beach R', 'Kalimari Desert T', 'Shy Guy Bazaar R/T', 'Vancouver Velocity T', 'Vancouver Velocity', 'Koopa Troopa Beach R/T', "Bowser's Castle 2R", "Bowser's Castle 2T", 'Kalimari Desert 2', 'Kalimari Desert 2R', 'RMX Rainbow Road 1R', 'Los Angeles Laps R/T', 'Los Angeles Laps R', 'New York Minute 3', 'New York Minute 3R/T', 'Merry Mountain T']

Star_Spangled_Glider__lv3_courses = ['Koopa Troopa Beach R/T', 'RMX Rainbow Road 1R']

Star_Spangled_Glider__lv6_courses = ["Bowser's Castle 2R", 'Kalimari Desert 2R']

Star_Spangled_Glider_ = race_tool('Star_Spangled_Glider_', 'High-End', Star_Spangled_Glider__3x_Combo_Boost, Star_Spangled_Glider__2x_Combo_Boost, Star_Spangled_Glider__lv3_courses, Star_Spangled_Glider__lv6_courses)


#Goomba_Hanafuda_
# https://game8.co/games/mariokarttour/archives/304786

Goomba_Hanafuda__3x_Combo_Boost = ['Daisy Hills T', 'Daisy Hills R', 'Daisy Hills', 'Toad Circuit T', 'Toad Circuit R', 'Toad Circuit', 'Waluigi Pinball', 'Waluigi Pinball R', 'Waluigi Pinball T', 'Waluigi Pinball R/T']

Goomba_Hanafuda__2x_Combo_Boost = ['Dino Dino Jungle T', 'Dino Dino Jungle R', 'Dino Dino Jungle', 'Choco Island 2R', 'Choco Island 2', 'Neo Bowser City R', 'Neo Bowser City', 'Choco Island 2T', 'Neo Bowser City T', 'Dino Dino Jungle R/T', "Bowser's Castle 2", "Bowser's Castle 2R", "Bowser's Castle 2T", "Bowser's Castle 2R/T", 'New York Minute 3', 'New York Minute 3R', 'New York Minute 3T', 'New York Minute 3R/T']

Goomba_Hanafuda__lv3_courses = ['Choco Island 2R', "Bowser's Castle 2R"]

Goomba_Hanafuda__lv6_courses = ['Choco Island 2T', "Bowser's Castle 2T"]

Goomba_Hanafuda_ = race_tool('Goomba_Hanafuda_', 'High-End', Goomba_Hanafuda__3x_Combo_Boost, Goomba_Hanafuda__2x_Combo_Boost, Goomba_Hanafuda__lv3_courses, Goomba_Hanafuda__lv6_courses)


#Spider_Glider_
# https://game8.co/games/mariokarttour/archives/305318

Spider_Glider__3x_Combo_Boost = ['Rock Rock Mountain', 'Neo Bowser City R', 'Neo Bowser City T', 'Neo Bowser City R/T', 'RMX Choco Island 1R', 'Royal Raceway R', 'Maple Treeway R', 'Maple Treeway T', 'Sunset Wilds R/T', 'Merry Mountain', 'RMX Rainbow Road 2T', 'Berlin Byways 2']

Spider_Glider__2x_Combo_Boost = ['Rock Rock Mountain T', 'Neo Bowser City', "Luigi's Mansion R", "Luigi's Mansion T", "Bowser's Castle 1R/T", "Luigi's Mansion R/T", 'Ghost Valley 1R/T', "Bowser's Castle 2R", "Bowser's Castle 2T", 'RMX Choco Island 1T', 'Royal Raceway T', 'Maple Treeway', 'Sunset Wilds', 'Sunset Wilds T', 'Merry Mountain R', 'Berlin Byways 2T']

Spider_Glider__lv3_courses = ["Luigi's Mansion R", "Bowser's Castle 2T"]

Spider_Glider__lv6_courses = ["Luigi's Mansion T", 'Ghost Valley 1R/T']

Spider_Glider_ = race_tool('Spider_Glider_', 'High-End', Spider_Glider__3x_Combo_Boost, Spider_Glider__2x_Combo_Boost, Spider_Glider__lv3_courses, Spider_Glider__lv6_courses)


#Jumping_Mario_Hanafuda_
# https://game8.co/games/mariokarttour/archives/305959

Jumping_Mario_Hanafuda__3x_Combo_Boost = ['Yoshi Circuit T', 'Yoshi Circuit R', 'Yoshi Circuit', 'SNES Rainbow Road', 'SNES Rainbow Road T', 'SNES Rainbow Road R', 'Choco Mountain', 'Choco Mountain R', 'Choco Mountain T']

Jumping_Mario_Hanafuda__2x_Combo_Boost = ['Rock Rock Mountain T', 'Rock Rock Mountain R', 'Rock Rock Mountain', 'Mario Circuit 2T', 'Mario Circuit 2R', 'Mario Circuit 2', 'SNES Rainbow Road R/T', 'Daisy Hills R/T', 'Daisy Hills R/T', 'Royal Raceway R', 'Royal Raceway T', 'Royal Raceway', 'Sunset Wilds', 'Sunset Wilds R', 'Sunset Wilds T', 'Sunset Wilds R/T']

Jumping_Mario_Hanafuda__lv3_courses = ['Royal Raceway R', 'Royal Raceway']

Jumping_Mario_Hanafuda__lv6_courses = ['Sunset Wilds R', 'Sunset Wilds T']

Jumping_Mario_Hanafuda_ = race_tool('Jumping_Mario_Hanafuda_', 'High-End', Jumping_Mario_Hanafuda__3x_Combo_Boost, Jumping_Mario_Hanafuda__2x_Combo_Boost, Jumping_Mario_Hanafuda__lv3_courses, Jumping_Mario_Hanafuda__lv6_courses)


#Sunset_Balloons_
# https://game8.co/games/mariokarttour/archives/305960

Sunset_Balloons__3x_Combo_Boost = ['Mario Circuit 1', 'Kalimari Desert R', 'Kalimari Desert', 'SNES Rainbow Road R/T', 'DS Rainbow Road R', 'Donut Plains 1R/T', 'Royal Raceway T', 'Airship Fortress', 'Maple Treeway', 'Maple Treeway R', 'Sunset Wilds', 'Sunset Wilds T', 'Sunset Wilds R/T', 'Berlin Byways 2R/T', 'Donut Plains 2T']

Sunset_Balloons__2x_Combo_Boost = ['Kalimari Desert T', 'Neo Bowser City', 'Neo Bowser City T', 'Kalimari Desert R/T', 'Neo Bowser City R/T', 'Waluigi Pinball R/T', 'DS Rainbow Road R/T', 'Royal Raceway', 'Airship Fortress R', 'Maple Treeway T', 'Sunset Wilds R', 'Merry Mountain', 'Merry Mountain T', 'Berlin Byways 2', 'Donut Plains 2R']

Sunset_Balloons__lv3_courses = ['Neo Bowser City', 'Waluigi Pinball R/T']

Sunset_Balloons__lv6_courses = ['Neo Bowser City T', 'Sunset Wilds R']

Sunset_Balloons_ = race_tool('Sunset_Balloons_', 'High-End', Sunset_Balloons__3x_Combo_Boost, Sunset_Balloons__2x_Combo_Boost, Sunset_Balloons__lv3_courses, Sunset_Balloons__lv6_courses)


#Jolly_Bells_
# https://game8.co/games/mariokarttour/archives/311466

Jolly_Bells__3x_Combo_Boost = ['Rock Rock Mountain', 'SNES Rainbow Road R', 'DK Pass', 'DS Rainbow Road', 'DS Rainbow Road T', 'RMX Choco Island 1T', 'Royal Raceway R', 'Royal Raceway T', 'Merry Mountain', "Rosalina's Ice World R", 'RMX Rainbow Road 2', 'Berlin Byways 2R/T']

Jolly_Bells__2x_Combo_Boost = ['SNES Rainbow Road T', 'Mario Circuit 3', 'Frappe Snowland', 'Frappe Snowland T', 'Frappe Snowland R', 'Vanilla Lake 1', 'Vanilla Lake 1R', 'Paris Promenade 2T', 'Paris Promenade 2', 'RMX Choco Island 1R', 'Merry Mountain R', "Rosalina's Ice World T", 'RMX Rainbow Road 2R', 'Berlin Byways 2T', 'DK Summit R']

Jolly_Bells__lv3_courses = ['Frappe Snowland T', 'Frappe Snowland R']

Jolly_Bells__lv6_courses = ['SNES Rainbow Road T', 'Merry Mountain R']

Jolly_Bells_ = race_tool('Jolly_Bells_', 'High-End', Jolly_Bells__3x_Combo_Boost, Jolly_Bells__2x_Combo_Boost, Jolly_Bells__lv3_courses, Jolly_Bells__lv6_courses)


#Silver_Starchute_
# https://game8.co/games/mariokarttour/archives/311467

Silver_Starchute__3x_Combo_Boost = ['Frappe Snowland', 'Frappe Snowland R', 'Choco Mountain', 'Maple Treeway T', 'Merry Mountain T', "Rosalina's Ice World T", 'RMX Rainbow Road 2T', 'Berlin Byways 2R', 'Berlin Byways 2T', 'Donut Plains 2', 'RMX Choco Island 2R', 'RMX Choco Island 2T', 'DK Summit']

Silver_Starchute__2x_Combo_Boost = ['Rock Rock Mountain R', 'Rock Rock Mountain', 'Frappe Snowland', 'DK Pass R/T', 'Choco Mountain R', 'Maple Treeway R', 'Merry Mountain', 'Merry Mountain R', "Rosalina's Ice World", 'RMX Rainbow Road 2', 'RMX Rainbow Road 2R', 'Berlin Byways 2', 'Berlin Byways 2R/T', 'Donut Plains 2R']

Silver_Starchute__lv3_courses = ['DK Pass R/T']

Silver_Starchute__lv6_courses = ['Maple Treeway R', 'Merry Mountain']

Silver_Starchute_ = race_tool('Silver_Starchute_', 'High-End', Silver_Starchute__3x_Combo_Boost, Silver_Starchute__2x_Combo_Boost, Silver_Starchute__lv3_courses, Silver_Starchute__lv6_courses)


#Bowser_Hanafuda_
# https://game8.co/games/mariokarttour/archives/311468

Bowser_Hanafuda__3x_Combo_Boost = ['DK Pass R/T', 'Airship Fortress', 'Airship Fortress R', 'Airship Fortress T', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 1T', 'Maple Treeway', 'Maple Treeway R', 'Maple Treeway T']

Bowser_Hanafuda__2x_Combo_Boost = ['Daisy Hills T', 'Daisy Hills R', 'Daisy Hills', 'Daisy Hills R/T', 'Choco Island 1', 'Choco Island 1R', 'Choco Island 1T', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', 'Koopa Troopa Beach 2T']

Bowser_Hanafuda__lv3_courses = ['Choco Island 1R', 'Choco Island 1T']

Bowser_Hanafuda__lv6_courses = ['Daisy Hills T', 'Daisy Hills R']

Bowser_Hanafuda_ = race_tool('Bowser_Hanafuda_', 'High-End', Bowser_Hanafuda__3x_Combo_Boost, Bowser_Hanafuda__2x_Combo_Boost, Bowser_Hanafuda__lv3_courses, Bowser_Hanafuda__lv6_courses)


#Planet_Glider_
# https://game8.co/games/mariokarttour/archives/314375

Planet_Glider__3x_Combo_Boost = ['Cheep Cheep Lagoon', 'Vanilla Lake 1R/T', 'Vanilla Lake 1R/T', 'Merry Mountain R', "Rosalina's Ice World", "Rosalina's Ice World R", 'RMX Rainbow Road 2T', 'Berlin Byways 2R', 'DK Summit T']

Planet_Glider__2x_Combo_Boost = ['SNES Rainbow Road R', 'Vanilla Lake 1T', 'DS Rainbow Road R/T', 'RMX Rainbow Road 1', 'Merry Mountain', 'Merry Mountain T', "Rosalina's Ice World T", 'RMX Rainbow Road 2', 'RMX Rainbow Road 2R', 'Berlin Byways 2T', 'Berlin Byways 2R/T', 'DK Summit', 'DK Summit R']

Planet_Glider__lv3_courses = ['RMX Rainbow Road 1', 'Merry Mountain T']

Planet_Glider__lv6_courses = ['SNES Rainbow Road R', 'Merry Mountain']

Planet_Glider_ = race_tool('Planet_Glider_', 'High-End', Planet_Glider__3x_Combo_Boost, Planet_Glider__2x_Combo_Boost, Planet_Glider__lv3_courses, Planet_Glider__lv6_courses)


#Butterfly_Prism_
# https://game8.co/games/mariokarttour/archives/314376

Butterfly_Prism__3x_Combo_Boost = ['Mario Circuit 3', 'Mario Circuit 3T', 'Vanilla Lake 1T', 'Paris Promenade 2R', "Bowser's Castle 2", 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', 'Sunset Wilds T', "Rosalina's Ice World", 'RMX Choco Island 2']

Butterfly_Prism__2x_Combo_Boost = ['Shy Guy Bazaar', 'SNES Rainbow Road T', 'SNES Rainbow Road R', 'Vanilla Lake 1R', 'Paris Promenade 2T', 'Frappe Snowland R/T', 'Kalimari Desert 2R', 'Kalimari Desert 2T', 'Sunset Wilds', 'Merry Mountain', "Rosalina's Ice World R", 'RMX Rainbow Road 2', 'RMX Rainbow Road 2T', 'RMX Choco Island 2T']

Butterfly_Prism__lv3_courses = ['SNES Rainbow Road R', 'Merry Mountain']

Butterfly_Prism__lv6_courses = ['Frappe Snowland R/T', 'Sunset Wilds']

Butterfly_Prism_ = race_tool('Butterfly_Prism_', 'High-End', Butterfly_Prism__3x_Combo_Boost, Butterfly_Prism__2x_Combo_Boost, Butterfly_Prism__lv3_courses, Butterfly_Prism__lv6_courses)


#New_Years_2021_
# https://game8.co/games/mariokarttour/archives/314377

New_Years_2021__3x_Combo_Boost = ['Daisy Hills T', 'Kalimari Desert T', 'Waluigi Pinball', 'Neo Bowser City R/T', 'Paris Promenade 2T', 'Paris Promenade 2', 'Kalimari Desert 2', 'Kalimari Desert 2R', 'RMX Rainbow Road 1', 'Sunset Wilds R', 'Merry Mountain R', 'RMX Rainbow Road 2R', 'RMX Choco Island 2R']

New_Years_2021__2x_Combo_Boost = ['RMX Rainbow Road 1T', 'Sunset Wilds', 'Merry Mountain T', "Rosalina's Ice World R", "Rosalina's Ice World T", 'RMX Rainbow Road 2T', 'Berlin Byways 2', 'Berlin Byways 2R/T', 'Donut Plains 2T', 'RMX Choco Island 2']

New_Years_2021__lv3_courses = ['RMX Rainbow Road 1T', "Rosalina's Ice World R"]

New_Years_2021__lv6_courses = ['Merry Mountain T', "Rosalina's Ice World T"]

New_Years_2021_ = race_tool('New_Years_2021_', 'High-End', New_Years_2021__3x_Combo_Boost, New_Years_2021__2x_Combo_Boost, New_Years_2021__lv3_courses, New_Years_2021__lv6_courses)


#Gold_New_Years_Kite_
# https://game8.co/games/mariokarttour/archives/315374

Gold_New_Years_Kite__3x_Combo_Boost = ['Mario Circuit 1T', 'Shy Guy Bazaar R', 'Shy Guy Bazaar', 'Mario Circuit 2R', 'Mario Circuit 2', 'SNES Rainbow Road R/T', "Bowser's Castle 2R/T", 'Airship Fortress R', 'Sunset Wilds T', 'Berlin Byways 2R']

Gold_New_Years_Kite__2x_Combo_Boost = ['Neo Bowser City R/T', 'RMX Choco Island 1T', 'Sunset Wilds R/T', "Rosalina's Ice World R", 'RMX Rainbow Road 2', 'RMX Rainbow Road 2R', 'RMX Rainbow Road 2T', 'Berlin Byways 2', 'Berlin Byways 2T', 'Berlin Byways 2R/T', 'Donut Plains 2', 'DK Summit']

Gold_New_Years_Kite__lv3_courses = ['RMX Choco Island 1T', 'Sunset Wilds R/T']

Gold_New_Years_Kite__lv6_courses = ["Rosalina's Ice World R", 'RMX Rainbow Road 2']

Gold_New_Years_Kite_ = race_tool('Gold_New_Years_Kite_', 'High-End', Gold_New_Years_Kite__3x_Combo_Boost, Gold_New_Years_Kite__2x_Combo_Boost, Gold_New_Years_Kite__lv3_courses, Gold_New_Years_Kite__lv6_courses)


#Dry_Bowser_Umbrella_
# https://game8.co/games/mariokarttour/archives/315373

Dry_Bowser_Umbrella__3x_Combo_Boost = ['Shy Guy Bazaar', 'Waluigi Pinball', 'Neo Bowser City R/T', "Bowser's Castle 2R", "Bowser's Castle 2T", 'Sunset Wilds', 'Sunset Wilds T', 'Sunset Wilds R/T', 'Merry Mountain', "Rosalina's Ice World", "Rosalina's Ice World T", 'RMX Rainbow Road 2T', 'Berlin Byways 2', 'Berlin Byways 2R/T']

Dry_Bowser_Umbrella__2x_Combo_Boost = ['Rock Rock Mountain', 'Cheep Cheep Lagoon', 'Kalimari Desert T', 'Kalimari Desert', 'Waluigi Pinball T', "Bowser's Castle 2R/T", 'RMX Rainbow Road 2', 'RMX Rainbow Road 2R']

Dry_Bowser_Umbrella__lv3_courses = ["Bowser's Castle 2R/T", 'RMX Rainbow Road 2R']

Dry_Bowser_Umbrella__lv6_courses = ['Kalimari Desert T', 'Waluigi Pinball T']

Dry_Bowser_Umbrella_ = race_tool('Dry_Bowser_Umbrella_', 'High-End', Dry_Bowser_Umbrella__3x_Combo_Boost, Dry_Bowser_Umbrella__2x_Combo_Boost, Dry_Bowser_Umbrella__lv3_courses, Dry_Bowser_Umbrella__lv6_courses)


#Penguin_Wingtip_
# https://game8.co/games/mariokarttour/archives/316098

Penguin_Wingtip__3x_Combo_Boost = ['Cheep Cheep Lagoon R', 'Neo Bowser City R/T', 'Frappe Snowland R', 'Vanilla Lake 1R/T', 'Koopa Troopa Beach 2T', 'Merry Mountain', 'Merry Mountain T', "Rosalina's Ice World", "Rosalina's Ice World R", 'DK Summit R']

Penguin_Wingtip__2x_Combo_Boost = ['Yoshi Circuit R', 'Yoshi Circuit', 'Cheep Cheep Lagoon T', 'Cheep Cheep Lagoon', 'Frappe Snowland', 'Koopa Troopa Beach 2R', 'Airship Fortress R', 'Airship Fortress T', 'Merry Mountain R', "Rosalina's Ice World T", 'Berlin Byways 2T', 'Berlin Byways 2R/T', 'Donut Plains 2', 'DK Summit T']

Penguin_Wingtip__lv3_courses = ['Cheep Cheep Lagoon', 'Airship Fortress T']

Penguin_Wingtip__lv6_courses = ['Cheep Cheep Lagoon T', 'Berlin Byways 2T']

Penguin_Wingtip_ = race_tool('Penguin_Wingtip_', 'High-End', Penguin_Wingtip__3x_Combo_Boost, Penguin_Wingtip__2x_Combo_Boost, Penguin_Wingtip__lv3_courses, Penguin_Wingtip__lv6_courses)


#Calico_Parafoil_
# https://game8.co/games/mariokarttour/archives/317075

Calico_Parafoil__3x_Combo_Boost = ['Dino Dino Jungle R', 'Dino Dino Jungle', 'Choco Island 1R', 'Choco Island 1T', 'Maple Treeway T', 'Sunset Wilds R', 'Merry Mountain R', 'Donut Plains 2T', 'DK Summit T']

Calico_Parafoil__2x_Combo_Boost = ['Dino Dino Jungle T', 'Choco Island 1', 'Maple Treeway', 'Maple Treeway R', 'Sunset Wilds', 'Sunset Wilds T', 'Donut Plains 2', 'Donut Plains 2R', 'RMX Choco Island 2', 'DK Summit R']

Calico_Parafoil__lv3_courses = ['Maple Treeway R', 'Sunset Wilds T']

Calico_Parafoil__lv6_courses = ['Sunset Wilds', 'Donut Plains 2']

Calico_Parafoil_ = race_tool('Calico_Parafoil_', 'High-End', Calico_Parafoil__3x_Combo_Boost, Calico_Parafoil__2x_Combo_Boost, Calico_Parafoil__lv3_courses, Calico_Parafoil__lv6_courses)


#Toe_Bean_Balloons_
# https://game8.co/games/mariokarttour/archives/317074

Toe_Bean_Balloons__3x_Combo_Boost = ['Daisy Hills', 'Paris Promenade 2', 'Koopa Troopa Beach R/T', 'Merry Mountain R', 'Donut Plains 2', 'Donut Plains 2R', 'RMX Choco Island 2R', 'DK Summit', 'DK Summit R']

Toe_Bean_Balloons__2x_Combo_Boost = ['Dino Dino Jungle T', 'Dino Dino Jungle', 'Daisy Hills R', 'Kalimari Desert R', 'Paris Promenade 2R', 'Maple Treeway', 'Maple Treeway R', 'RMX Rainbow Road 1R/T', 'Donut Plains 2T']

Toe_Bean_Balloons__lv3_courses = ['Paris Promenade 2R', 'Maple Treeway']

Toe_Bean_Balloons__lv6_courses = ['RMX Rainbow Road 1R/T', 'Donut Plains 2T']

Toe_Bean_Balloons_ = race_tool('Toe_Bean_Balloons_', 'High-End', Toe_Bean_Balloons__3x_Combo_Boost, Toe_Bean_Balloons__2x_Combo_Boost, Toe_Bean_Balloons__lv3_courses, Toe_Bean_Balloons__lv6_courses)


#Rose_Parasol_
# https://game8.co/games/mariokarttour/archives/317801

Rose_Parasol__3x_Combo_Boost = ['Maple Treeway', 'Maple Treeway R', 'Sunset Wilds R/T', 'RMX Rainbow Road 2', 'RMX Choco Island 2T']

Rose_Parasol__2x_Combo_Boost = ['Yoshi Circuit T', 'Yoshi Circuit R', 'Royal Raceway R', 'Royal Raceway T', 'RMX Rainbow Road 2R', 'RMX Choco Island 2', 'RMX Choco Island 2R', 'DK Summit']

Rose_Parasol__lv3_courses = ['Yoshi Circuit T', 'Royal Raceway T']

Rose_Parasol__lv6_courses = ['Yoshi Circuit R', 'RMX Choco Island 2']

Rose_Parasol_ = race_tool('Rose_Parasol_', 'High-End', Rose_Parasol__3x_Combo_Boost, Rose_Parasol__2x_Combo_Boost, Rose_Parasol__lv3_courses, Rose_Parasol__lv6_courses)


#Silver_Manta_Glider_
# https://game8.co/games/mariokarttour/archives/317800

Silver_Manta_Glider__3x_Combo_Boost = ['Yoshi Circuit T', 'DK Pass R', 'Choco Island 1', "Rosalina's Ice World T", 'RMX Choco Island 2', 'RMX Choco Island 2R', 'DK Summit T']

Silver_Manta_Glider__2x_Combo_Boost = ['Yoshi Circuit', 'DK Pass R', 'Frappe Snowland', 'Royal Raceway R', 'Royal Raceway T', "Rosalina's Ice World", 'DK Summit R']

Silver_Manta_Glider__lv3_courses = ['Yoshi Circuit', 'Royal Raceway R']

Silver_Manta_Glider__lv6_courses = ["Rosalina's Ice World", 'RMX Choco Island 2T']

Silver_Manta_Glider_ = race_tool('Silver_Manta_Glider_', 'High-End', Silver_Manta_Glider__3x_Combo_Boost, Silver_Manta_Glider__2x_Combo_Boost, Silver_Manta_Glider__lv3_courses, Silver_Manta_Glider__lv6_courses)


#Black_Great_Sail_
# https://game8.co/games/mariokarttour/archives/317799

Black_Great_Sail__3x_Combo_Boost = ['Vanilla Lake 1', 'Vanilla Lake 1T', "Bowser's Castle 2R", 'RMX Choco Island 2', 'RMX Choco Island 2T', 'DK Summit R']

Black_Great_Sail__2x_Combo_Boost = ['Yoshi Circuit', "Bowser's Castle 2", "Bowser's Castle 2T", 'Sunset Wilds R/T', 'RMX Choco Island 2R', 'DK Summit', 'DK Summit T']

Black_Great_Sail__lv3_courses = ['Yoshi Circuit', "Bowser's Castle 2"]

Black_Great_Sail__lv6_courses = ['Sunset Wilds R/T', 'RMX Choco Island 2R']

Black_Great_Sail_ = race_tool('Black_Great_Sail_', 'High-End', Black_Great_Sail__3x_Combo_Boost, Black_Great_Sail__2x_Combo_Boost, Black_Great_Sail__lv3_courses, Black_Great_Sail__lv6_courses)


#Snow_Crystals_
# https://game8.co/games/mariokarttour/archives/321008

Snow_Crystals__3x_Combo_Boost = ['Frappe Snowland', 'DS Rainbow Road R/T', 'RMX Rainbow Road 2', 'DK Summit', 'DK Summit R']

Snow_Crystals__2x_Combo_Boost = ['DK Pass', 'DK Pass T', 'Frappe Snowland T', "Rosalina's Ice World", "Rosalina's Ice World T", 'DK Summit T']

Snow_Crystals__lv3_courses = ["Rosalina's Ice World", "Rosalina's Ice World T"]

Snow_Crystals__lv6_courses = ['DK Pass T', 'DK Summit T']

Snow_Crystals_ = race_tool('Snow_Crystals_', 'High-End', Snow_Crystals__3x_Combo_Boost, Snow_Crystals__2x_Combo_Boost, Snow_Crystals__lv3_courses, Snow_Crystals__lv6_courses)


#Bit_Fire_Flower_8_Bit_Fire_Flower1
# https://game8.co/games/mariokarttour/archives/322570

Bit_Fire_Flower_8_Bit_Fire_Flower1_3x_Combo_Boost = ["Bowser's Castle 1R/T", 'DS Rainbow Road', 'Tokyo Blur 4', 'Tokyo Blur 4T']

Bit_Fire_Flower_8_Bit_Fire_Flower1_2x_Combo_Boost = ['Mario Circuit 1R', 'Ghost Valley 1', 'RMX Mario Circuit 1R', 'RMX Mario Circuit 1T', 'Tokyo Blur 4R', 'Tokyo Blur 4R/T']

Bit_Fire_Flower_8_Bit_Fire_Flower1_lv3_courses = ['Ghost Valley 1', 'RMX Mario Circuit 1T']

Bit_Fire_Flower_8_Bit_Fire_Flower1_lv6_courses = ['Mario Circuit 1R', 'Tokyo Blur 4R/T']

Bit_Fire_Flower_8_Bit_Fire_Flower1 = race_tool('Bit_Fire_Flower_8_Bit_Fire_Flower1', 'High-End', Bit_Fire_Flower_8_Bit_Fire_Flower1_3x_Combo_Boost, Bit_Fire_Flower_8_Bit_Fire_Flower1_2x_Combo_Boost, Bit_Fire_Flower_8_Bit_Fire_Flower1_lv3_courses, Bit_Fire_Flower_8_Bit_Fire_Flower1_lv6_courses)


#B_Dasher_
# https://game8.co/games/mariokarttour/archives/270466

B_Dasher__3x_Combo_Boost = ['Cheep Cheep Lagoon T', 'Daisy Hills', 'Toad Circuit R', 'Toad Circuit', 'Mario Circuit 1', 'Mario Circuit', 'Mario Circuit 3R/T', 'Tokyo Blur 3R', 'RMX Rainbow Road 2R']

B_Dasher__2x_Combo_Boost = ['New York Minute R', 'New York Minute R/T', 'Yoshi Circuit T', 'Mario Circuit 1T', 'Mario Circuit 1R', 'Donut Plains 1T', 'RMX Mario Circuit 1R/T', 'Tokyo Blur 3', 'Tokyo Blur 3T', 'RMX Rainbow Road 2T']

B_Dasher__lv3_courses = ['Mario Circuit 1T', 'Mario Circuit 1R']

B_Dasher__lv6_courses = ['Yoshi Circuit T', 'RMX Mario Circuit 1R/T']

B_Dasher_ = race_tool('B_Dasher_', 'High-End', B_Dasher__3x_Combo_Boost, B_Dasher__2x_Combo_Boost, B_Dasher__lv3_courses, B_Dasher__lv6_courses)


#Toadette__Explorer_
# https://game8.co/games/mariokarttour/archives/291842

Toadette__Explorer__3x_Combo_Boost = ['Kalimari Desert R', 'Choco Island 2T', 'Kalimari Desert R/T', 'Rock Rock Mountain', 'Sunset Wilds R/T', 'Daisy Hills', 'Daisy Hills R', 'Choco Island 2T', 'Royal Raceway', 'Royal Raceway R', 'Choco Mountain T', 'Toad Circuit', 'Toad Circuit R', 'DK Summit', 'Koopa Troopa Beach T', 'Kalimari Desert 2R']

Toadette__Explorer__2x_Combo_Boost = ['Rock Rock Mountain R', 'Kalimari Desert 2T', 'Kalimari Desert 2', 'Sunset Wilds', 'Sunset Wilds T', 'Choco Island 2R/T', 'Choco Island 2R', "Luigi's Mansion T", 'Vanilla Lake 1R', 'Choco Island 1', 'Kalimari Desert R', 'Sunset Wilds R', 'Koopa Troopa Beach R', 'Dino Dino Jungle R/T', 'DS Rainbow Road R/T', 'Choco Mountain R', 'Dino Dino Jungle', 'Dino Dino Jungle R', 'Toad Circuit T']

Toadette__Explorer__lv3_courses = ['Dino Dino Jungle', 'DS Rainbow Road R/T']

Toadette__Explorer__lv6_courses = ['Choco Mountain R', 'Kalimari Desert 2']

Toadette__Explorer_ = race_tool('Toadette__Explorer_', 'High-End', Toadette__Explorer__3x_Combo_Boost, Toadette__Explorer__2x_Combo_Boost, Toadette__Explorer__lv3_courses, Toadette__Explorer__lv6_courses)


#Decal_Streamliner_
# https://game8.co/games/mariokarttour/archives/322568

Decal_Streamliner__3x_Combo_Boost = ['Mario Circuit 1T', 'DK Summit', 'Tokyo Blur 4', 'Tokyo Blur 4T', 'Tokyo Blur 4T']

Decal_Streamliner__2x_Combo_Boost = ['Toad Circuit', 'Mario Circuit 1R/T', 'DK Summit T', 'Tokyo Blur 4R', 'Tokyo Blur 4R/T']

Decal_Streamliner__lv3_courses = ['Toad Circuit', 'DK Summit T']

Decal_Streamliner__lv6_courses = ['Mario Circuit 1R/T', 'Tokyo Blur 4R/T']

Decal_Streamliner_ = race_tool('Decal_Streamliner_', 'High-End', Decal_Streamliner__3x_Combo_Boost, Decal_Streamliner__2x_Combo_Boost, Decal_Streamliner__lv3_courses, Decal_Streamliner__lv6_courses)


#B_Dasher_Mk_2_
# https://game8.co/games/mariokarttour/archives/322567

B_Dasher_Mk_2__3x_Combo_Boost = ['Mario Circuit 1R', 'Toad Circuit T', 'RMX Mario Circuit 1R/T', 'Tokyo Blur 4']

B_Dasher_Mk_2__2x_Combo_Boost = ['Toad Circuit R', 'Mario Circuit 1R/T', 'RMX Mario Circuit 1R', 'RMX Mario Circuit 1T', 'Tokyo Blur 4T', 'Tokyo Blur 4R/T']

B_Dasher_Mk_2__lv3_courses = ['Toad Circuit R', 'Toad Circuit R', 'RMX Mario Circuit 1T']

B_Dasher_Mk_2__lv6_courses = ['Mario Circuit 1R/T', 'RMX Mario Circuit 1R']

B_Dasher_Mk_2_ = race_tool('B_Dasher_Mk_2_', 'High-End', B_Dasher_Mk_2__3x_Combo_Boost, B_Dasher_Mk_2__2x_Combo_Boost, B_Dasher_Mk_2__lv3_courses, B_Dasher_Mk_2__lv6_courses)


#Shell_Parachute_
# https://game8.co/games/mariokarttour/archives/270476

Shell_Parachute__3x_Combo_Boost = ['Yoshi Circuit T', 'Yoshi Circuit R', 'Dino Dino Jungle T', 'Daisy Hills T']

Shell_Parachute__2x_Combo_Boost = ['Rock Rock Mountain T', 'Rock Rock Mountain', 'Cheep Cheep Lagoon T', 'Koopa Troopa Beach R', 'Koopa Troopa Beach', "Bowser's Castle 1", 'Toad Circuit', 'Mario Circuit 1', 'Neo Bowser City', "Bowser's Castle 2R/T"]

Shell_Parachute__lv3_courses = ['Rock Rock Mountain']

Shell_Parachute__lv6_courses = ['Koopa Troopa Beach']

Shell_Parachute_ = race_tool('Shell_Parachute_', 'Super', Shell_Parachute__3x_Combo_Boost, Shell_Parachute__2x_Combo_Boost, Shell_Parachute__lv3_courses, Shell_Parachute__lv6_courses)


#Bob_omb_Parafoil_
# https://game8.co/games/mariokarttour/archives/270475

Bob_omb_Parafoil__3x_Combo_Boost = ['Shy Guy Bazaar T', 'Koopa Troopa Beach T', 'Dino Dino Jungle', "Bowser's Castle 1", 'Toad Circuit R']

Bob_omb_Parafoil__2x_Combo_Boost = ['Rock Rock Mountain T', 'Rock Rock Mountain R', 'New York Minute', "Bowser's Castle 1R", 'Kalimari Desert', 'Neo Bowser City R', 'Kalimari Desert R/T', 'Koopa Troopa Beach R/T', 'Choco Mountain R', 'Choco Mountain T', 'Airship Fortress', 'Airship Fortress R', 'Airship Fortress T']

Bob_omb_Parafoil__lv3_courses = ['Kalimari Desert R/T']

Bob_omb_Parafoil__lv6_courses = ['Rock Rock Mountain R']

Bob_omb_Parafoil_ = race_tool('Bob_omb_Parafoil_', 'Super', Bob_omb_Parafoil__3x_Combo_Boost, Bob_omb_Parafoil__2x_Combo_Boost, Bob_omb_Parafoil__lv3_courses, Bob_omb_Parafoil__lv6_courses)


#Peach_Parasol_
# https://game8.co/games/mariokarttour/archives/270474

Peach_Parasol__3x_Combo_Boost = ['Cheep Cheep Lagoon T', 'Koopa Troopa Beach', 'Choco Island 2', 'Mario Circuit', 'Mario Circuit T']

Peach_Parasol__2x_Combo_Boost = ['Yoshi Circuit T', 'Mario Circuit 1T', 'Mario Circuit 1R', 'Cheep Cheep Lagoon R', 'Daisy Hills R', 'Cheep Cheep Lagoon', 'New York Minute T', "Luigi's Mansion R", 'Cheep Cheep Lagoon R/T', 'Paris Promenade 2R']

Peach_Parasol__lv3_courses = ['Cheep Cheep Lagoon R/T']

Peach_Parasol__lv6_courses = ['Mario Circuit 1R']

Peach_Parasol_ = race_tool('Peach_Parasol_', 'Super', Peach_Parasol__3x_Combo_Boost, Peach_Parasol__2x_Combo_Boost, Peach_Parasol__lv3_courses, Peach_Parasol__lv6_courses)


#Flower_Glider_
# https://game8.co/games/mariokarttour/archives/270473

Flower_Glider__3x_Combo_Boost = ['Shy Guy Bazaar R', 'Shy Guy Bazaar', 'Cheep Cheep Lagoon R', 'Daisy Hills']

Flower_Glider__2x_Combo_Boost = ['New York Minute R/T', 'Yoshi Circuit', 'Mario Circuit 1R', 'Daisy Hills T', 'Toad Circuit T', 'Toad Circuit R', 'Mario Circuit R', "Luigi's Mansion", "Luigi's Mansion T", 'Vanilla Lake 1R/T', 'Kalimari Desert 2']

Flower_Glider__lv3_courses = ['Toad Circuit T']

Flower_Glider__lv6_courses = ['Toad Circuit R']

Flower_Glider_ = race_tool('Flower_Glider_', 'Super', Flower_Glider__3x_Combo_Boost, Flower_Glider__2x_Combo_Boost, Flower_Glider__lv3_courses, Flower_Glider__lv6_courses)


#Wario_Wing_
# https://game8.co/games/mariokarttour/archives/270734

Wario_Wing__3x_Combo_Boost = ['Neo Bowser City', 'Neo Bowser City T', "Luigi's Mansion", 'Waluigi Pinball', "Luigi's Mansion R/T", 'Kalimari Desert R/T', 'London Loop 2T']

Wario_Wing__2x_Combo_Boost = ['New York Minute R', "Bowser's Castle 1T", 'Kalimari Desert R', 'Kalimari Desert', 'Tokyo Blur R/T', 'Waluigi Pinball R', 'London Loop T', 'DK Summit T']

Wario_Wing__lv3_courses = ['Waluigi Pinball R']

Wario_Wing__lv6_courses = ['Kalimari Desert R']

Wario_Wing_ = race_tool('Wario_Wing_', 'Super', Wario_Wing__3x_Combo_Boost, Wario_Wing__2x_Combo_Boost, Wario_Wing__lv3_courses, Wario_Wing__lv6_courses)


#Lightning_Oilpaper_
# https://game8.co/games/mariokarttour/archives/270733

Lightning_Oilpaper__3x_Combo_Boost = ['Shy Guy Bazaar', 'Cheep Cheep Lagoon T', 'Mario Circuit 2T', 'Kalimari Desert R', 'Kalimari Desert', 'Neo Bowser City R', 'Ghost Valley 1T', 'Airship Fortress R']

Lightning_Oilpaper__2x_Combo_Boost = ['Mario Circuit 2R', 'SNES Rainbow Road T', 'Tokyo Blur R/T', 'Waluigi Pinball T', 'Paris Promenade T', 'Paris Promenade R/T', 'Mario Circuit 3R', 'DK Pass T', 'DK Pass R', "Bowser's Castle 2R/T", 'Airship Fortress', 'Airship Fortress T']

Lightning_Oilpaper__lv3_courses = ['SNES Rainbow Road T']

Lightning_Oilpaper__lv6_courses = ['Mario Circuit 3R']

Lightning_Oilpaper_ = race_tool('Lightning_Oilpaper_', 'Super', Lightning_Oilpaper__3x_Combo_Boost, Lightning_Oilpaper__2x_Combo_Boost, Lightning_Oilpaper__lv3_courses, Lightning_Oilpaper__lv6_courses)


#Oilpaper_Umbrella_
# https://game8.co/games/mariokarttour/archives/270732

Oilpaper_Umbrella__3x_Combo_Boost = ['Dino Dino Jungle', 'SNES Rainbow Road', 'Mario Circuit R', 'Mario Circuit 3T', 'Mario Circuit R/T', 'New York Minute 2R', 'RMX Mario Circuit 1R/T', 'RMX Rainbow Road 2R']

Oilpaper_Umbrella__2x_Combo_Boost = ['Tokyo Blur R', 'Kalimari Desert R', 'Mario Circuit', 'SNES Rainbow Road T', 'SNES Rainbow Road R', 'Tokyo Blur T', 'Mario Circuit 3', 'Paris Promenade R', 'New York Minute 2T', 'Mario Circuit 1R/T', 'Dino Dino Jungle R/T', 'Donut Plains 1R/T', 'Tokyo Blur 3', 'Tokyo Blur 3T', 'RMX Rainbow Road 2T']

Oilpaper_Umbrella__lv3_courses = ['Mario Circuit 1R/T']

Oilpaper_Umbrella__lv6_courses = ['SNES Rainbow Road T']

Oilpaper_Umbrella_ = race_tool('Oilpaper_Umbrella_', 'Super', Oilpaper_Umbrella__3x_Combo_Boost, Oilpaper_Umbrella__2x_Combo_Boost, Oilpaper_Umbrella__lv3_courses, Oilpaper_Umbrella__lv6_courses)


#Waluigi_Wing_
# https://game8.co/games/mariokarttour/archives/271641

Waluigi_Wing__3x_Combo_Boost = ['Rock Rock Mountain T', 'Koopa Troopa Beach', "Bowser's Castle 1R", "Luigi's Mansion R", 'Waluigi Pinball', 'London Loop 2T']

Waluigi_Wing__2x_Combo_Boost = ['Dino Dino Jungle T', 'Dino Dino Jungle R', 'SNES Rainbow Road', 'SNES Rainbow Road T', 'Waluigi Pinball R', 'DK Pass', 'DK Pass R', "Bowser's Castle 1R/T", 'London Loop 2R/T', "Bowser's Castle 2R/T"]

Waluigi_Wing__lv3_courses = ["Bowser's Castle 1R/T"]

Waluigi_Wing__lv6_courses = ['Waluigi Pinball R']

Waluigi_Wing_ = race_tool('Waluigi_Wing_', 'Super', Waluigi_Wing__3x_Combo_Boost, Waluigi_Wing__2x_Combo_Boost, Waluigi_Wing__lv3_courses, Waluigi_Wing__lv6_courses)


#BaNaNa_Parafoil_
# https://game8.co/games/mariokarttour/archives/272266

BaNaNa_Parafoil__3x_Combo_Boost = ['Waluigi Pinball T', 'Ghost Valley 1R', 'Mario Circuit 3R', 'Daisy Hills R/T', 'London Loop R', 'Vanilla Lake 1R', 'Choco Island 2R/T', 'Dino Dino Jungle R/T', "Bowser's Castle 2R", 'Choco Island 1']

BaNaNa_Parafoil__2x_Combo_Boost = ['Choco Island 2R', 'Choco Island 2', 'Mario Circuit 3', 'Paris Promenade', "Luigi's Mansion R/T", 'Waluigi Pinball R/T', 'London Loop 2R/T', 'Donut Plains 1', 'Donut Plains 1R', "Bowser's Castle 2", "Bowser's Castle 2T", 'RMX Choco Island 1R', 'RMX Choco Island 1T']

BaNaNa_Parafoil__lv3_courses = ['Choco Island 2']

BaNaNa_Parafoil__lv6_courses = ['Mario Circuit 3']

BaNaNa_Parafoil_ = race_tool('BaNaNa_Parafoil_', 'Super', BaNaNa_Parafoil__3x_Combo_Boost, BaNaNa_Parafoil__2x_Combo_Boost, BaNaNa_Parafoil__lv3_courses, BaNaNa_Parafoil__lv6_courses)


#Pink_Flower_Glider_
# https://game8.co/games/mariokarttour/archives/275168

Pink_Flower_Glider__3x_Combo_Boost = ['Kalimari Desert R', 'Paris Promenade T', 'DS Rainbow Road T', 'Tokyo Blur 2T', 'Shy Guy Bazaar R/T', 'Ghost Valley 1R/T', 'London Loop 2R/T', 'Los Angeles Laps R/T']

Pink_Flower_Glider__2x_Combo_Boost = ['Shy Guy Bazaar', 'Cheep Cheep Lagoon R', 'Daisy Hills T', 'Kalimari Desert T', 'Kalimari Desert', 'Waluigi Pinball T', 'New York Minute 2T', 'Cheep Cheep Lagoon R/T', 'Vanilla Lake 1', 'Vanilla Lake 1R', 'Paris Promenade 2T', 'Paris Promenade 2', 'Mario Circuit 3R/T', 'DS Rainbow Road R/T', 'Donut Plains 1R', 'Donut Plains 1R/T', 'Vanilla Lake 1R/T', 'Los Angeles Laps']

Pink_Flower_Glider__lv3_courses = ['Cheep Cheep Lagoon R/T']

Pink_Flower_Glider__lv6_courses = ['DS Rainbow Road R/T']

Pink_Flower_Glider_ = race_tool('Pink_Flower_Glider_', 'Super', Pink_Flower_Glider__3x_Combo_Boost, Pink_Flower_Glider__2x_Combo_Boost, Pink_Flower_Glider__lv3_courses, Pink_Flower_Glider__lv6_courses)


#Blue_Flower_Glider_
# https://game8.co/games/mariokarttour/archives/279960

Blue_Flower_Glider__3x_Combo_Boost = ['Cheep Cheep Lagoon R', 'DK Pass', 'DS Rainbow Road R', 'Cheep Cheep Lagoon R/T', 'Neo Bowser City R/T', 'Frappe Snowland', 'Vanilla Lake 1T', 'Vancouver Velocity R']

Blue_Flower_Glider__2x_Combo_Boost = ['Dino Dino Jungle T', 'Dino Dino Jungle', "Luigi's Mansion", "Luigi's Mansion R", 'DK Pass T', 'SNES Rainbow Road R/T', 'DS Rainbow Road T', 'Vanilla Lake 1', 'Vanilla Lake 1R', 'Vancouver Velocity', 'Frappe Snowland R/T', 'Vanilla Lake 1R/T']

Blue_Flower_Glider__lv3_courses = ['Dino Dino Jungle R/T']

Blue_Flower_Glider__lv6_courses = ['SNES Rainbow Road R/T']

Blue_Flower_Glider_ = race_tool('Blue_Flower_Glider_', 'Super', Blue_Flower_Glider__3x_Combo_Boost, Blue_Flower_Glider__2x_Combo_Boost, Blue_Flower_Glider__lv3_courses, Blue_Flower_Glider__lv6_courses)


#Bit_Jumping_Mario_8_Bit_Jumping_Mario1
# https://game8.co/games/mariokarttour/archives/281116

Bit_Jumping_Mario_8_Bit_Jumping_Mario1_3x_Combo_Boost = ['Mario Circuit 1R', 'Mario Circuit 1', 'Mario Circuit 2R', 'London Loop', 'Mario Circuit 2R/T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1T', "Bowser's Castle 2R", 'RMX Mario Circuit 1R/T']

Bit_Jumping_Mario_8_Bit_Jumping_Mario1_2x_Combo_Boost = ['Mario Circuit 2T', 'Mario Circuit 2', 'Mario Circuit T', 'Mario Circuit 3T', 'Mario Circuit 3R', 'Mario Circuit R/T', 'London Loop R/T', 'Mario Circuit 1R/T', 'RMX Mario Circuit 1R', 'London Loop 2R/T', 'Donut Plains 1', "Bowser's Castle 2T", 'Koopa Troopa Beach 2T', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1T', 'RMX Rainbow Road 1R/T', 'Sunset Wilds R/T']

Bit_Jumping_Mario_8_Bit_Jumping_Mario1_lv3_courses = ['Mario Circuit 1R/T']

Bit_Jumping_Mario_8_Bit_Jumping_Mario1_lv6_courses = ['Mario Circuit 2']

Bit_Jumping_Mario_8_Bit_Jumping_Mario1 = race_tool('Bit_Jumping_Mario_8_Bit_Jumping_Mario1', 'Super', Bit_Jumping_Mario_8_Bit_Jumping_Mario1_3x_Combo_Boost, Bit_Jumping_Mario_8_Bit_Jumping_Mario1_2x_Combo_Boost, Bit_Jumping_Mario_8_Bit_Jumping_Mario1_lv3_courses, Bit_Jumping_Mario_8_Bit_Jumping_Mario1_lv6_courses)


#Block__Block1
# https://game8.co/games/mariokarttour/archives/281117

Block__Block1_3x_Combo_Boost = ['Toad Circuit T', 'Toad Circuit', 'Mario Circuit 3T', "Bowser's Castle 1R/T", 'Yoshi Circuit R/T', 'Frappe Snowland T', 'RMX Mario Circuit 1R', 'London Loop 2R', "Bowser's Castle 2T"]

Block__Block1_2x_Combo_Boost = ['Neo Bowser City R', 'Mario Circuit T', 'Mario Circuit 3', 'Mario Circuit 3R', 'Mario Circuit 1R/T', 'Neo Bowser City R/T', 'Toad Circuit R/T', 'Frappe Snowland', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1T', 'London Loop 2', "Bowser's Castle 2R", 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 1T']

Block__Block1_lv3_courses = ['Koopa Troopa Beach 2R']

Block__Block1_lv6_courses = ['Toad Circuit R/T']

Block__Block1 = race_tool('Block__Block1', 'Super', Block__Block1_3x_Combo_Boost, Block__Block1_2x_Combo_Boost, Block__Block1_lv3_courses, Block__Block1_lv6_courses)


#Plaid_Ribbon_
# https://game8.co/games/mariokarttour/archives/282826

Plaid_Ribbon__3x_Combo_Boost = ['Koopa Troopa Beach R', 'Choco Island 2T', 'London Loop R', 'London Loop T', 'Vancouver Velocity T', 'Frappe Snowland R/T', 'RMX Mario Circuit 1', 'London Loop 2', 'Donut Plains 1R', 'Choco Island 1']

Plaid_Ribbon__2x_Combo_Boost = ['Shy Guy Bazaar T', 'Koopa Troopa Beach T', 'Mario Circuit 2T', 'Mario Circuit 2R', 'Choco Island 2R', 'Choco Island 2', 'London Loop', 'Yoshi Circuit R/T', 'Choco Island 2R/T', 'Vancouver Velocity', 'London Loop 2R', 'London Loop 2T', 'London Loop 2R/T', 'Donut Plains 1', 'Donut Plains 1R/T', 'Vanilla Lake 1R/T', 'Choco Island 1R', 'Choco Island 1T', 'Maple Treeway T']

Plaid_Ribbon__lv3_courses = ['Choco Island 2R/T']

Plaid_Ribbon__lv6_courses = ['Mario Circuit 2R']

Plaid_Ribbon_ = race_tool('Plaid_Ribbon_', 'Super', Plaid_Ribbon__3x_Combo_Boost, Plaid_Ribbon__2x_Combo_Boost, Plaid_Ribbon__lv3_courses, Plaid_Ribbon__lv6_courses)


#Eggshell_Glider_
# https://game8.co/games/mariokarttour/archives/285886

Eggshell_Glider__3x_Combo_Boost = ['Yoshi Circuit R', "Luigi's Mansion T", 'Paris Promenade', 'Paris Promenade R/T', 'Kalimari Desert R/T', 'Donut Plains 1R/T', 'Vanilla Lake 1R/T', 'Royal Raceway R']

Eggshell_Glider__2x_Combo_Boost = ['Yoshi Circuit T', 'Yoshi Circuit', 'Dino Dino Jungle R', 'Dino Dino Jungle', "Luigi's Mansion", 'Paris Promenade T', 'Mario Circuit 2R/T', 'Koopa Troopa Beach R/T', 'Mario Circuit 3R/T', "Bowser's Castle 2", "Bowser's Castle 2R", "Bowser's Castle 2T", 'Royal Raceway T', 'Royal Raceway', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', 'Airship Fortress R', 'Airship Fortress T', 'DK Summit']

Eggshell_Glider__lv3_courses = ['Koopa Troopa Beach R/T']

Eggshell_Glider__lv6_courses = ['Yoshi Circuit']

Eggshell_Glider_ = race_tool('Eggshell_Glider_', 'Super', Eggshell_Glider__3x_Combo_Boost, Eggshell_Glider__2x_Combo_Boost, Eggshell_Glider__lv3_courses, Eggshell_Glider__lv6_courses)


#B_Dasher_
# https://game8.co/games/mariokarttour/archives/270466

B_Dasher__3x_Combo_Boost = ['Cheep Cheep Lagoon T', 'Daisy Hills', 'Toad Circuit R', 'Toad Circuit', 'Mario Circuit 1', 'Mario Circuit', 'Mario Circuit 3R/T', 'Tokyo Blur 3R', 'RMX Rainbow Road 2R']

B_Dasher__2x_Combo_Boost = ['New York Minute R', 'New York Minute R/T', 'Yoshi Circuit T', 'Mario Circuit 1T', 'Mario Circuit 1R', 'Donut Plains 1T', 'RMX Mario Circuit 1R/T', 'Tokyo Blur 3', 'Tokyo Blur 3T', 'RMX Rainbow Road 2T']

B_Dasher__lv3_courses = ['Mario Circuit 1T', 'Mario Circuit 1R']

B_Dasher__lv6_courses = ['Yoshi Circuit T', 'RMX Mario Circuit 1R/T']

B_Dasher_ = race_tool('B_Dasher_', 'High-End', B_Dasher__3x_Combo_Boost, B_Dasher__2x_Combo_Boost, B_Dasher__lv3_courses, B_Dasher__lv6_courses)


#Toadette__Explorer_
# https://game8.co/games/mariokarttour/archives/291842

Toadette__Explorer__3x_Combo_Boost = ['Kalimari Desert R', 'Choco Island 2T', 'Kalimari Desert R/T', 'Rock Rock Mountain', 'Sunset Wilds R/T', 'Daisy Hills', 'Daisy Hills R', 'Choco Island 2T', 'Royal Raceway', 'Royal Raceway R', 'Choco Mountain T', 'Toad Circuit', 'Toad Circuit R', 'DK Summit', 'Koopa Troopa Beach T', 'Kalimari Desert 2R']

Toadette__Explorer__2x_Combo_Boost = ['Rock Rock Mountain R', 'Kalimari Desert 2T', 'Kalimari Desert 2', 'Sunset Wilds', 'Sunset Wilds T', 'Choco Island 2R/T', 'Choco Island 2R', "Luigi's Mansion T", 'Vanilla Lake 1R', 'Choco Island 1', 'Kalimari Desert R', 'Sunset Wilds R', 'Koopa Troopa Beach R', 'Dino Dino Jungle R/T', 'DS Rainbow Road R/T', 'Choco Mountain R', 'Dino Dino Jungle', 'Dino Dino Jungle R', 'Toad Circuit T']

Toadette__Explorer__lv3_courses = ['Dino Dino Jungle', 'DS Rainbow Road R/T']

Toadette__Explorer__lv6_courses = ['Choco Mountain R', 'Kalimari Desert 2']

Toadette__Explorer_ = race_tool('Toadette__Explorer_', 'High-End', Toadette__Explorer__3x_Combo_Boost, Toadette__Explorer__2x_Combo_Boost, Toadette__Explorer__lv3_courses, Toadette__Explorer__lv6_courses)


#Decal_Streamliner_
# https://game8.co/games/mariokarttour/archives/322568

Decal_Streamliner__3x_Combo_Boost = ['Mario Circuit 1T', 'DK Summit', 'Tokyo Blur 4', 'Tokyo Blur 4T', 'Tokyo Blur 4T']

Decal_Streamliner__2x_Combo_Boost = ['Toad Circuit', 'Mario Circuit 1R/T', 'DK Summit T', 'Tokyo Blur 4R', 'Tokyo Blur 4R/T']

Decal_Streamliner__lv3_courses = ['Toad Circuit', 'DK Summit T']

Decal_Streamliner__lv6_courses = ['Mario Circuit 1R/T', 'Tokyo Blur 4R/T']

Decal_Streamliner_ = race_tool('Decal_Streamliner_', 'High-End', Decal_Streamliner__3x_Combo_Boost, Decal_Streamliner__2x_Combo_Boost, Decal_Streamliner__lv3_courses, Decal_Streamliner__lv6_courses)


#B_Dasher_Mk_2_
# https://game8.co/games/mariokarttour/archives/322567

B_Dasher_Mk_2__3x_Combo_Boost = ['Mario Circuit 1R', 'Toad Circuit T', 'RMX Mario Circuit 1R/T', 'Tokyo Blur 4']

B_Dasher_Mk_2__2x_Combo_Boost = ['Toad Circuit R', 'Mario Circuit 1R/T', 'RMX Mario Circuit 1R', 'RMX Mario Circuit 1T', 'Tokyo Blur 4T', 'Tokyo Blur 4R/T']

B_Dasher_Mk_2__lv3_courses = ['Toad Circuit R', 'Toad Circuit R', 'RMX Mario Circuit 1T']

B_Dasher_Mk_2__lv6_courses = ['Mario Circuit 1R/T', 'RMX Mario Circuit 1R']

B_Dasher_Mk_2_ = race_tool('B_Dasher_Mk_2_', 'High-End', B_Dasher_Mk_2__3x_Combo_Boost, B_Dasher_Mk_2__2x_Combo_Boost, B_Dasher_Mk_2__lv3_courses, B_Dasher_Mk_2__lv6_courses)


#Parafoil_
# https://game8.co/games/mariokarttour/archives/270472

Parafoil__3x_Combo_Boost = ['Rock Rock Mountain', 'Toad Circuit T', 'Cheep Cheep Lagoon']

Parafoil__2x_Combo_Boost = ['Rock Rock Mountain T', 'Mario Circuit 1R', 'Koopa Troopa Beach T', 'Koopa Troopa Beach', 'Daisy Hills R', 'Daisy Hills', 'Mario Circuit 2T', "Bowser's Castle 2R/T"]

Parafoil__lv3_courses = []

Parafoil__lv6_courses = ['Koopa Troopa Beach T']

Parafoil_ = race_tool('Parafoil_', 'Normal', Parafoil__3x_Combo_Boost, Parafoil__2x_Combo_Boost, Parafoil__lv3_courses, Parafoil__lv6_courses)


#Parachute_
# https://game8.co/games/mariokarttour/archives/270471

Parachute__3x_Combo_Boost = ['Rock Rock Mountain R', 'Yoshi Circuit']

Parachute__2x_Combo_Boost = ['New York Minute R', 'Yoshi Circuit R', 'Cheep Cheep Lagoon T', 'Koopa Troopa Beach R', 'Dino Dino Jungle R', 'Toad Circuit', 'SNES Rainbow Road', 'Kalimari Desert R', 'DS Rainbow Road R', 'DS Rainbow Road R/T']

Parachute__lv3_courses = []

Parachute__lv6_courses = ['SNES Rainbow Road']

Parachute_ = race_tool('Parachute_', 'Normal', Parachute__3x_Combo_Boost, Parachute__2x_Combo_Boost, Parachute__lv3_courses, Parachute__lv6_courses)


#Super_Glider_
# https://game8.co/games/mariokarttour/archives/270433

Super_Glider__3x_Combo_Boost = ['Mario Circuit 1']

Super_Glider__2x_Combo_Boost = ['Yoshi Circuit T', 'Mario Circuit 1T', 'Koopa Troopa Beach T', 'Koopa Troopa Beach R', 'Daisy Hills R', 'Toad Circuit T', 'Toad Circuit', 'Mario Circuit 2R', 'Mario Circuit R', 'Ghost Valley 1', 'Vanilla Lake 1R/T', 'Maple Treeway']

Super_Glider__lv3_courses = []

Super_Glider__lv6_courses = ['Mario Circuit 2R']

Super_Glider_ = race_tool('Super_Glider_', 'Normal', Super_Glider__3x_Combo_Boost, Super_Glider__2x_Combo_Boost, Super_Glider__lv3_courses, Super_Glider__lv6_courses)


#BBIA_Parafoil_
# https://game8.co/games/mariokarttour/archives/270731

BBIA_Parafoil__3x_Combo_Boost = ['Mario Circuit 1T', 'Shy Guy Bazaar R', 'Daisy Hills', 'SNES Rainbow Road T']

BBIA_Parafoil__2x_Combo_Boost = ['Toad Circuit', 'Tokyo Blur', 'Mario Circuit 2', 'SNES Rainbow Road R', 'Mario Circuit T', 'Tokyo Blur R/T', 'Paris Promenade', 'Mario Circuit R/T', 'Daisy Hills R/T', 'Frappe Snowland T', 'Vanilla Lake 1T']

BBIA_Parafoil__lv3_courses = []

BBIA_Parafoil__lv6_courses = ['Daisy Hills R/T']

BBIA_Parafoil_ = race_tool('BBIA_Parafoil_', 'Normal', BBIA_Parafoil__3x_Combo_Boost, BBIA_Parafoil__2x_Combo_Boost, BBIA_Parafoil__lv3_courses, BBIA_Parafoil__lv6_courses)


#Droplet_Glider_
# https://game8.co/games/mariokarttour/archives/270730

Droplet_Glider__3x_Combo_Boost = ['Choco Island 2', 'Choco Island 2T', 'Koopa Troopa Beach 2R']

Droplet_Glider__2x_Combo_Boost = ['Mario Circuit 1R', 'Toad Circuit R', 'Mario Circuit 2R', 'Choco Island 2R', 'Kalimari Desert T', 'Kalimari Desert', 'Waluigi Pinball', "Luigi's Mansion R/T", 'Koopa Troopa Beach 2']

Droplet_Glider__lv3_courses = []

Droplet_Glider__lv6_courses = ["Luigi's Mansion R/T"]

Droplet_Glider_ = race_tool('Droplet_Glider_', 'Normal', Droplet_Glider__3x_Combo_Boost, Droplet_Glider__2x_Combo_Boost, Droplet_Glider__lv3_courses, Droplet_Glider__lv6_courses)


#Paper_Glider_
# https://game8.co/games/mariokarttour/archives/270729

Paper_Glider__3x_Combo_Boost = ['Daisy Hills T', 'Mario Circuit 2R', 'Mario Circuit 2']

Paper_Glider__2x_Combo_Boost = ['Yoshi Circuit', 'Mario Circuit 1', 'Mario Circuit 2T', 'Choco Island 2', 'Choco Island 2T', "Luigi's Mansion R", "Luigi's Mansion T", 'Waluigi Pinball R', 'Ghost Valley 1', 'Vanilla Lake 1R/T']

Paper_Glider__lv3_courses = []

Paper_Glider__lv6_courses = ['Choco Island 2T']

Paper_Glider_ = race_tool('Paper_Glider_', 'Normal', Paper_Glider__3x_Combo_Boost, Paper_Glider__2x_Combo_Boost, Paper_Glider__lv3_courses, Paper_Glider__lv6_courses)


#Piranha_Plant_Parafoil_
# https://game8.co/games/mariokarttour/archives/271640

Piranha_Plant_Parafoil__3x_Combo_Boost = ['Koopa Troopa Beach', 'Kalimari Desert T', 'Waluigi Pinball R', "Bowser's Castle 1R/T"]

Piranha_Plant_Parafoil__2x_Combo_Boost = ['Dino Dino Jungle T', 'Dino Dino Jungle R', "Bowser's Castle 1R", "Bowser's Castle 1", 'SNES Rainbow Road', 'Waluigi Pinball', 'Donut Plains 1R/T', 'RMX Mario Circuit 1R/T']

Piranha_Plant_Parafoil__lv3_courses = []

Piranha_Plant_Parafoil__lv6_courses = ["Bowser's Castle 1R"]

Piranha_Plant_Parafoil_ = race_tool('Piranha_Plant_Parafoil_', 'Normal', Piranha_Plant_Parafoil__3x_Combo_Boost, Piranha_Plant_Parafoil__2x_Combo_Boost, Piranha_Plant_Parafoil__lv3_courses, Piranha_Plant_Parafoil__lv6_courses)


#Minion_Paper_Glider_
# https://game8.co/games/mariokarttour/archives/273763

Minion_Paper_Glider__3x_Combo_Boost = ['DK Pass T', 'DK Pass R']

Minion_Paper_Glider__2x_Combo_Boost = ['Dino Dino Jungle R', 'Dino Dino Jungle', "Luigi's Mansion R", 'Daisy Hills R/T', 'Frappe Snowland', 'Frappe Snowland R', 'Vanilla Lake 1R/T', 'RMX Choco Island 1R', "Rosalina's Ice World R", "Rosalina's Ice World T"]

Minion_Paper_Glider__lv3_courses = []

Minion_Paper_Glider__lv6_courses = ['Dino Dino Jungle']

Minion_Paper_Glider_ = race_tool('Minion_Paper_Glider_', 'Normal', Minion_Paper_Glider__3x_Combo_Boost, Minion_Paper_Glider__2x_Combo_Boost, Minion_Paper_Glider__lv3_courses, Minion_Paper_Glider__lv6_courses)


#Piston_Glider_
# https://game8.co/games/mariokarttour/archives/274699

Piston_Glider__3x_Combo_Boost = ['Toad Circuit R', 'Mario Circuit', 'Mario Circuit 3', 'Mario Circuit 1R/T']

Piston_Glider__2x_Combo_Boost = ['Toad Circuit T', 'Mario Circuit T', 'London Loop', 'London Loop R', 'New York Minute 2', 'Kalimari Desert R/T', 'Tokyo Blur 2T', 'Mario Circuit 2R/T', 'Neo Bowser City R/T', 'Dino Dino Jungle R/T', 'Vancouver Velocity T', 'Koopa Troopa Beach R/T', 'Mario Circuit 3R/T', 'Donut Plains 1T']

Piston_Glider__lv3_courses = []

Piston_Glider__lv6_courses = ['Kalimari Desert R/T']

Piston_Glider_ = race_tool('Piston_Glider_', 'Normal', Piston_Glider__3x_Combo_Boost, Piston_Glider__2x_Combo_Boost, Piston_Glider__lv3_courses, Piston_Glider__lv6_courses)


#B_Dasher_
# https://game8.co/games/mariokarttour/archives/270466

B_Dasher__3x_Combo_Boost = ['Cheep Cheep Lagoon T', 'Daisy Hills', 'Toad Circuit R', 'Toad Circuit', 'Mario Circuit 1', 'Mario Circuit', 'Mario Circuit 3R/T', 'Tokyo Blur 3R', 'RMX Rainbow Road 2R']

B_Dasher__2x_Combo_Boost = ['New York Minute R', 'New York Minute R/T', 'Yoshi Circuit T', 'Mario Circuit 1T', 'Mario Circuit 1R', 'Donut Plains 1T', 'RMX Mario Circuit 1R/T', 'Tokyo Blur 3', 'Tokyo Blur 3T', 'RMX Rainbow Road 2T']

B_Dasher__lv3_courses = ['Mario Circuit 1T', 'Mario Circuit 1R']

B_Dasher__lv6_courses = ['Yoshi Circuit T', 'RMX Mario Circuit 1R/T']

B_Dasher_ = race_tool('B_Dasher_', 'High-End', B_Dasher__3x_Combo_Boost, B_Dasher__2x_Combo_Boost, B_Dasher__lv3_courses, B_Dasher__lv6_courses)


#Toadette__Explorer_
# https://game8.co/games/mariokarttour/archives/291842

Toadette__Explorer__3x_Combo_Boost = ['Kalimari Desert R', 'Choco Island 2T', 'Kalimari Desert R/T', 'Rock Rock Mountain', 'Sunset Wilds R/T', 'Daisy Hills', 'Daisy Hills R', 'Choco Island 2T', 'Royal Raceway', 'Royal Raceway R', 'Choco Mountain T', 'Toad Circuit', 'Toad Circuit R', 'DK Summit', 'Koopa Troopa Beach T', 'Kalimari Desert 2R']

Toadette__Explorer__2x_Combo_Boost = ['Rock Rock Mountain R', 'Kalimari Desert 2T', 'Kalimari Desert 2', 'Sunset Wilds', 'Sunset Wilds T', 'Choco Island 2R/T', 'Choco Island 2R', "Luigi's Mansion T", 'Vanilla Lake 1R', 'Choco Island 1', 'Kalimari Desert R', 'Sunset Wilds R', 'Koopa Troopa Beach R', 'Dino Dino Jungle R/T', 'DS Rainbow Road R/T', 'Choco Mountain R', 'Dino Dino Jungle', 'Dino Dino Jungle R', 'Toad Circuit T']

Toadette__Explorer__lv3_courses = ['Dino Dino Jungle', 'DS Rainbow Road R/T']

Toadette__Explorer__lv6_courses = ['Choco Mountain R', 'Kalimari Desert 2']

Toadette__Explorer_ = race_tool('Toadette__Explorer_', 'High-End', Toadette__Explorer__3x_Combo_Boost, Toadette__Explorer__2x_Combo_Boost, Toadette__Explorer__lv3_courses, Toadette__Explorer__lv6_courses)


#Decal_Streamliner_
# https://game8.co/games/mariokarttour/archives/322568

Decal_Streamliner__3x_Combo_Boost = ['Mario Circuit 1T', 'DK Summit', 'Tokyo Blur 4', 'Tokyo Blur 4T', 'Tokyo Blur 4T']

Decal_Streamliner__2x_Combo_Boost = ['Toad Circuit', 'Mario Circuit 1R/T', 'DK Summit T', 'Tokyo Blur 4R', 'Tokyo Blur 4R/T']

Decal_Streamliner__lv3_courses = ['Toad Circuit', 'DK Summit T']

Decal_Streamliner__lv6_courses = ['Mario Circuit 1R/T', 'Tokyo Blur 4R/T']

Decal_Streamliner_ = race_tool('Decal_Streamliner_', 'High-End', Decal_Streamliner__3x_Combo_Boost, Decal_Streamliner__2x_Combo_Boost, Decal_Streamliner__lv3_courses, Decal_Streamliner__lv6_courses)


#B_Dasher_Mk_2_
# https://game8.co/games/mariokarttour/archives/322567

B_Dasher_Mk_2__3x_Combo_Boost = ['Mario Circuit 1R', 'Toad Circuit T', 'RMX Mario Circuit 1R/T', 'Tokyo Blur 4']

B_Dasher_Mk_2__2x_Combo_Boost = ['Toad Circuit R', 'Mario Circuit 1R/T', 'RMX Mario Circuit 1R', 'RMX Mario Circuit 1T', 'Tokyo Blur 4T', 'Tokyo Blur 4R/T']

B_Dasher_Mk_2__lv3_courses = ['Toad Circuit R', 'Toad Circuit R', 'RMX Mario Circuit 1T']

B_Dasher_Mk_2__lv6_courses = ['Mario Circuit 1R/T', 'RMX Mario Circuit 1R']

B_Dasher_Mk_2_ = race_tool('B_Dasher_Mk_2_', 'High-End', B_Dasher_Mk_2__3x_Combo_Boost, B_Dasher_Mk_2__2x_Combo_Boost, B_Dasher_Mk_2__lv3_courses, B_Dasher_Mk_2__lv6_courses)

