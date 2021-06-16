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


#Dry_Bowser
# https://game8.co/games/mariokarttour/archives/270452

Dry_Bowser_3items = ["Bowser's Castle 2", "Bowser's Castle 2R", 'Dino Dino Jungle', 'Dino Dino Jungle T', "Bowser's Castle 1R", 'Shy Guy Bazaar R', 'Neo Bowser City R/T', 'DK Pass R', "Bowser's Castle 1R/T", 'Neo Bowser City T', 'Choco Mountain R', 'New York Minute 3T']

Dry_Bowser_2items = ['Neo Bowser City R', 'Kalimari Desert R/T', 'DK Pass R/T', 'RMX Rainbow Road 1R/T', 'Kalimari Desert T', 'Daisy Hills T', "Bowser's Castle 1", "Bowser's Castle 2T", 'Rock Rock Mountain', 'Rock Rock Mountain T', 'Berlin Byways 2R', 'Choco Mountain T', 'RMX Rainbow Road 2R', 'RMX Mario Circuit 1T', 'New York Minute 3', 'Neo Bowser City']

Dry_Bowser_lv3_courses = ['DK Pass R/T', "Bowser's Castle 2T"]

Dry_Bowser_lv6_courses = ['Rock Rock Mountain T', 'RMX Mario Circuit 1T']

Dry_Bowser = race_tool('Dry_Bowser', 'High-End', Dry_Bowser_3items, Dry_Bowser_2items, Dry_Bowser_lv3_courses, Dry_Bowser_lv6_courses)


#Mario__Musician_
# https://game8.co/games/mariokarttour/archives/270451

Mario__Musician__3items = ['RMX Rainbow Road 1R', 'Paris Promenade 2R/T', 'Daisy Hills', 'Yoshi Circuit R', 'New York Minute T', 'Donut Plains 1R', 'New York Minute 3R/T', 'New York Minute 3R', 'New York Minute R', 'Waluigi Pinball R', 'Mario Circuit 3', 'New York Minute 2R/T', 'RMX Rainbow Road 1T']

Mario__Musician__2items = ['Paris Promenade 2', 'Shy Guy Bazaar R/T', 'Mario Circuit R/T', 'Berlin Byways 2T', 'Daisy Hills R', 'Rock Rock Mountain T', 'New York Minute', 'New York Minute R/T', 'Donut Plains 1T', 'SNES Rainbow Road T', 'New York Minute 3T', "Luigi's Mansion", 'Mario Circuit T', 'Mario Circuit 3R', 'Neo Bowser City T', 'Paris Promenade R/T', 'New York Minute 2R', 'Neo Bowser City R/T', 'RMX Rainbow Road 1R']

Mario__Musician__lv3_courses = ['Neo Bowser City R/T', 'Mario Circuit 3R', 'Neo Bowser City R/T']

Mario__Musician__lv6_courses = ["Luigi's Mansion", 'Neo Bowser City T']

Mario__Musician_ = race_tool('Mario__Musician_', 'High-End', Mario__Musician__3items, Mario__Musician__2items, Mario__Musician__lv3_courses, Mario__Musician__lv6_courses)


#Pauline
# https://game8.co/games/mariokarttour/archives/270450

Pauline_3items = ['Daisy Hills R/T', 'Choco Island 1', 'New York Minute', 'New York Minute R/T', 'New York Minute 2', 'New York Minute 3', 'New York Minute 3T', "Luigi's Mansion R", 'Waluigi Pinball T', 'London Loop T', 'New York Minute 2R', 'Waluigi Pinball R/T']

Pauline_2items = ['Paris Promenade 2R/T', 'Paris Promenade 2T', 'Neo Bowser City R/T', 'Yoshi Circuit T', 'Cheep Cheep Lagoon T', 'Shy Guy Bazaar', 'Tokyo Blur 3R', 'Shy Guy Bazaar R', 'Tokyo Blur 3', 'New York Minute T', 'New York Minute 3R/T', 'New York Minute 3R', 'DK Pass T', 'DK Pass R', 'SNES Rainbow Road R/T', "Luigi's Mansion T", "Bowser's Castle 1R/T", 'RMX Choco Island 2T', 'Choco Island 1R', 'RMX Choco Island 2R', 'Koopa Troopa Beach R/T', 'Choco Island 1T', 'Neo Bowser City']

Pauline_lv3_courses = ['Neo Bowser City R/T', 'SNES Rainbow Road R/T']

Pauline_lv6_courses = ['Shy Guy Bazaar R', 'Choco Island 1R']

Pauline = race_tool('Pauline', 'High-End', Pauline_3items, Pauline_2items, Pauline_lv3_courses, Pauline_lv6_courses)


#Peachette
# https://game8.co/games/mariokarttour/archives/270449

Peachette_3items = ['Dino Dino Jungle R', 'Toad Circuit', 'Toad Circuit T', 'Mario Circuit', 'Royal Raceway', 'Waluigi Pinball T', 'Mario Circuit R/T', 'Choco Island 1R', 'Donut Plains 1R/T']

Peachette_2items = ['Daisy Hills R/T', 'Daisy Hills', 'Yoshi Circuit T', 'Mario Circuit 1', 'Mario Circuit 1R', 'Yoshi Circuit', 'Mario Circuit R', 'Royal Raceway T', 'Royal Raceway R', 'Donut Plains 1R', 'Donut Plains 1', 'SNES Rainbow Road R', "Luigi's Mansion", 'DS Rainbow Road T', 'Vancouver Velocity R/T', 'Mario Circuit 3', 'Choco Island 1T']

Peachette_lv3_courses = ['Yoshi Circuit T', 'DS Rainbow Road T']

Peachette_lv6_courses = ["Luigi's Mansion", 'Donut Plains 1']

Peachette = race_tool('Peachette', 'High-End', Peachette_3items, Peachette_2items, Peachette_lv3_courses, Peachette_lv6_courses)


#Metal_Mario
# https://game8.co/games/mariokarttour/archives/270448

Metal_Mario_3items = ['RMX Rainbow Road 1R', 'Frappe Snowland R', 'Rock Rock Mountain R', 'RMX Mario Circuit 1', 'DK Pass T', 'Shy Guy Bazaar', 'Mario Circuit 2R', 'SNES Rainbow Road', "Bowser's Castle 2R/T", 'SNES Rainbow Road T']

Metal_Mario_2items = ['Yoshi Circuit T', 'Vanilla Lake 1R', 'RMX Rainbow Road 1', 'Vanilla Lake 1T', 'Mario Circuit 1T', 'Shy Guy Bazaar R', 'Shy Guy Bazaar T', 'SNES Rainbow Road R', 'Vanilla Lake 1R/T', 'Waluigi Pinball', 'New York Minute 3R', 'Dino Dino Jungle T', 'Toad Circuit', 'Yoshi Circuit R']

Metal_Mario_lv3_courses = ['Toad Circuit', 'SNES Rainbow Road R']

Metal_Mario_lv6_courses = ['Waluigi Pinball', 'Vanilla Lake 1R']

Metal_Mario = race_tool('Metal_Mario', 'High-End', Metal_Mario_3items, Metal_Mario_2items, Metal_Mario_lv3_courses, Metal_Mario_lv6_courses)


#Mario__Hakama_
# https://game8.co/games/mariokarttour/archives/270727

Mario__Hakama__3items = ['Tokyo Blur 3T', 'Tokyo Blur 3R', 'New York Minute 3R/T', 'Waluigi Pinball R', 'Mario Circuit 1', 'Mario Circuit 1T', 'Mario Circuit 3R', 'RMX Mario Circuit 1R/T', "Bowser's Castle 1T", 'Mario Circuit T', 'Mario Circuit 2', 'Tokyo Blur', 'Tokyo Blur R/T']

Mario__Hakama__2items = ['Dino Dino Jungle R/T', 'Paris Promenade 2R', 'Paris Promenade 2R/T', 'Waluigi Pinball R/T', 'Tokyo Blur 3', 'DK Pass R', 'New York Minute 3T', 'RMX Rainbow Road 1R/T', 'Mario Circuit 1R', 'Dino Dino Jungle R', "Bowser's Castle 1R", 'Shy Guy Bazaar T', 'Waluigi Pinball', 'Mario Circuit 2T', 'SNES Rainbow Road T', 'Ghost Valley 1T', 'Tokyo Blur T', 'RMX Choco Island 2', "Rosalina's Ice World T", 'Tokyo Blur 2R']

Mario__Hakama__lv3_courses = ['Waluigi Pinball', 'SNES Rainbow Road T']

Mario__Hakama__lv6_courses = ['Mario Circuit 1R', 'Ghost Valley 1T']

Mario__Hakama_ = race_tool('Mario__Hakama_', 'High-End', Mario__Hakama__3items, Mario__Hakama__2items, Mario__Hakama__lv3_courses, Mario__Hakama__lv6_courses)


#Peach__Kimono_
# https://game8.co/games/mariokarttour/archives/270726

Peach__Kimono__3items = ['RMX Rainbow Road 2R', 'Paris Promenade 2R/T', 'Tokyo Blur 3T', 'Royal Raceway R', 'Donut Plains 1R', 'Daisy Hills R', 'Waluigi Pinball', 'Mario Circuit 3T', 'Donut Plains 1R/T', 'Mario Circuit', 'Mario Circuit 2R', 'Tokyo Blur R', 'Tokyo Blur T']

Peach__Kimono__2items = ['RMX Rainbow Road 2', 'RMX Rainbow Road 2T', 'Shy Guy Bazaar R/T', 'Paris Promenade 2R', 'Paris Promenade 2T', 'Tokyo Blur 3R', 'Yoshi Circuit R/T', 'Mario Circuit R/T', 'Mario Circuit R', 'SNES Rainbow Road', 'Mario Circuit 1', 'New York Minute 3R/T', 'Royal Raceway T', 'New York Minute 3R', 'Tokyo Blur', 'Royal Raceway', 'London Loop 2', 'Tokyo Blur R/T', 'Paris Promenade T', 'RMX Mario Circuit 1R/T', 'Tokyo Blur 2', 'Tokyo Blur 2T', 'Tokyo Blur 2R/T']

Peach__Kimono__lv3_courses = ['Mario Circuit 1', 'Mario Circuit R']

Peach__Kimono__lv6_courses = ['SNES Rainbow Road', 'Royal Raceway']

Peach__Kimono_ = race_tool('Peach__Kimono_', 'High-End', Peach__Kimono__3items, Peach__Kimono__2items, Peach__Kimono__lv3_courses, Peach__Kimono__lv6_courses)


#Rosalina__Halloween_
# https://game8.co/games/mariokarttour/archives/271648

Rosalina__Halloween__3items = ['Shy Guy Bazaar', 'Choco Island 2', "Luigi's Mansion", 'Ghost Valley 1', 'Ghost Valley 1T', 'DK Pass R/T', 'SNES Rainbow Road R/T', 'Maple Treeway R', 'New York Minute 3T', 'Tokyo Blur 2R/T', "Rosalina's Ice World T"]

Rosalina__Halloween__2items = ['RMX Rainbow Road 2T', 'RMX Rainbow Road 2R', 'Frappe Snowland T', 'Daisy Hills R/T', 'SNES Rainbow Road', 'SNES Rainbow Road R', 'SNES Rainbow Road T', 'Ghost Valley 1R', 'Maple Treeway', 'New York Minute 3R', "Bowser's Castle 2R", "Bowser's Castle 2T", 'Los Angeles Laps', 'Los Angeles Laps T', 'Neo Bowser City', 'Neo Bowser City R/T', 'Paris Promenade R', 'Paris Promenade', "Rosalina's Ice World", 'DS Rainbow Road R/T']

Rosalina__Halloween__lv3_courses = ['Neo Bowser City', 'SNES Rainbow Road T']

Rosalina__Halloween__lv6_courses = ['Frappe Snowland T', 'Ghost Valley 1R']

Rosalina__Halloween_ = race_tool('Rosalina__Halloween_', 'High-End', Rosalina__Halloween__3items, Rosalina__Halloween__2items, Rosalina__Halloween__lv3_courses, Rosalina__Halloween__lv6_courses)


#King_Boo__Luigis_Mansion_
# https://game8.co/games/mariokarttour/archives/271649

King_Boo__Luigis_Mansion__3items = ['Airship Fortress T', "Bowser's Castle 1", 'Shy Guy Bazaar T', "Luigi's Mansion T", 'Rock Rock Mountain T', 'Ghost Valley 1', 'Ghost Valley 1R', 'SNES Rainbow Road R/T', 'RMX Choco Island 2R', 'RMX Rainbow Road 2R']

King_Boo__Luigis_Mansion__2items = ['Airship Fortress', 'DK Pass R/T', 'Yoshi Circuit', 'Yoshi Circuit T', "Luigi's Mansion R", "Bowser's Castle 2", 'Ghost Valley 1T', "Bowser's Castle 2R", 'DK Summit R', 'Ghost Valley 1R/T', 'Maple Treeway T', 'Maple Treeway R', 'DK Pass T', 'RMX Rainbow Road 2', 'Rock Rock Mountain R']

King_Boo__Luigis_Mansion__lv3_courses = ["Luigi's Mansion R", "Bowser's Castle 2"]

King_Boo__Luigis_Mansion__lv6_courses = ['DK Pass T', 'Rock Rock Mountain R']

King_Boo__Luigis_Mansion_ = race_tool('King_Boo__Luigis_Mansion_', 'High-End', King_Boo__Luigis_Mansion__3items, King_Boo__Luigis_Mansion__2items, King_Boo__Luigis_Mansion__lv3_courses, King_Boo__Luigis_Mansion__lv6_courses)


#Peach__Vacation_
# https://game8.co/games/mariokarttour/archives/272256

Peach__Vacation__3items = ['Paris Promenade 2R', 'Maple Treeway R', 'Paris Promenade R/T', 'Mario Circuit 1R', 'Mario Circuit 3', 'Paris Promenade', 'Toad Circuit R', 'Koopa Troopa Beach T', 'Daisy Hills T', 'Mario Circuit R', 'Koopa Troopa Beach R/T', 'Koopa Troopa Beach', 'Royal Raceway R', 'Cheep Cheep Lagoon R/T']

Peach__Vacation__2items = ['RMX Rainbow Road 2R', 'Paris Promenade 2T', 'London Loop R', 'Maple Treeway', 'Mario Circuit', 'Mario Circuit 3R', 'Yoshi Circuit R/T', 'Vancouver Velocity', 'Vancouver Velocity R/T', 'Mario Circuit 1', 'Cheep Cheep Lagoon R', 'RMX Choco Island 2T', 'Royal Raceway T', 'RMX Mario Circuit 1R/T', 'DS Rainbow Road R', 'New York Minute 2']

Peach__Vacation__lv3_courses = ['Cheep Cheep Lagoon R', 'Yoshi Circuit R/T']

Peach__Vacation__lv6_courses = ['DS Rainbow Road R', 'Mario Circuit']

Peach__Vacation_ = race_tool('Peach__Vacation_', 'High-End', Peach__Vacation__3items, Peach__Vacation__2items, Peach__Vacation__lv3_courses, Peach__Vacation__lv6_courses)


#Shy_Guy__Pastry_Chef_
# https://game8.co/games/mariokarttour/archives/272255

Shy_Guy__Pastry_Chef__3items = ["Luigi's Mansion R/T", 'Berlin Byways 2R', 'Berlin Byways 2', 'Choco Island 1R', 'Tokyo Blur 2R/T', 'RMX Mario Circuit 1T', 'Choco Mountain T', 'Shy Guy Bazaar R', 'Koopa Troopa Beach R', 'Koopa Troopa Beach T', 'RMX Choco Island 2R', 'Kalimari Desert', 'Neo Bowser City R', 'Paris Promenade R', 'Paris Promenade T', 'New York Minute 3R/T', 'New York Minute 3R']

Shy_Guy__Pastry_Chef__2items = ['Choco Island 1', 'New York Minute 2T', 'Kalimari Desert R/T', 'Cheep Cheep Lagoon R/T', 'Frappe Snowland R/T', 'Koopa Troopa Beach R/T', 'Choco Island 2', 'Tokyo Blur 2', 'Tokyo Blur 2R', 'Neo Bowser City R/T', 'Choco Mountain', 'Choco Mountain R', 'RMX Rainbow Road 2R', 'Paris Promenade R/T', 'Shy Guy Bazaar', 'Choco Island 2R', 'Rock Rock Mountain T', 'London Loop T', 'Paris Promenade', 'New York Minute 3']

Shy_Guy__Pastry_Chef__lv3_courses = ['Choco Island 2R', 'Kalimari Desert R/T']

Shy_Guy__Pastry_Chef__lv6_courses = ['Rock Rock Mountain T', 'Choco Mountain']

Shy_Guy__Pastry_Chef_ = race_tool('Shy_Guy__Pastry_Chef_', 'High-End', Shy_Guy__Pastry_Chef__3items, Shy_Guy__Pastry_Chef__2items, Shy_Guy__Pastry_Chef__lv3_courses, Shy_Guy__Pastry_Chef__lv6_courses)


#Pink_Gold_Peach
# https://game8.co/games/mariokarttour/archives/273756

Pink_Gold_Peach_3items = ['3DS Rainbow Road T', 'Kalimari Desert 2R', 'Waluigi Pinball R/T', 'Yoshi Circuit R/T', "Luigi's Mansion T", 'Choco Mountain', 'RMX Choco Island 2R', 'DK Pass T', 'SNES Rainbow Road T', 'RMX Choco Island 1', 'SNES Rainbow Road R/T', 'Royal Raceway T', 'DS Rainbow Road R/T']

Pink_Gold_Peach_2items = ['Frappe Snowland R', 'Vanilla Lake 1R', 'Paris Promenade 2', 'Berlin Byways 2', 'Berlin Byways 2T', 'Berlin Byways 2R/T', 'Choco Mountain T', 'Donut Plains 1R', 'Sunset Wilds R/T', 'London Loop', 'RMX Choco Island 2', 'RMX Choco Island 2T', "Rosalina's Ice World T", "Rosalina's Ice World R", 'RMX Choco Island 1T', 'Royal Raceway R', 'Tokyo Blur 2R/T', 'Royal Raceway', 'Mario Circuit 1T', 'Waluigi Pinball T', 'Mario Circuit 3T', 'DK Pass', 'Mario Circuit', 'Neo Bowser City R', 'RMX Rainbow Road 1']

Pink_Gold_Peach_lv3_courses = ['Mario Circuit 3T', 'Mario Circuit']

Pink_Gold_Peach_lv6_courses = ['Royal Raceway', 'Royal Raceway R']

Pink_Gold_Peach = race_tool('Pink_Gold_Peach', 'High-End', Pink_Gold_Peach_3items, Pink_Gold_Peach_2items, Pink_Gold_Peach_lv3_courses, Pink_Gold_Peach_lv6_courses)


#Mario__Santa_
# https://game8.co/games/mariokarttour/archives/273755

Mario__Santa__3items = ['Vanilla Lake 1T', 'Paris Promenade', 'Paris Promenade R', 'Mario Circuit 1R', 'DK Pass', 'SNES Rainbow Road R', 'SNES Rainbow Road T', "Rosalina's Ice World T", 'Mario Circuit R/T', 'Mario Circuit 1R/T', 'Merry Mountain R', "Luigi's Mansion"]

Mario__Santa__2items = ['New York Minute 2R/T', 'DK Pass R/T', 'Vanilla Lake 1R', 'Paris Promenade R/T', 'Donut Plains 1', 'London Loop T', 'RMX Choco Island 1T', "Rosalina's Ice World", 'Choco Island 2', 'Tokyo Blur 2', 'Mario Circuit 3R', 'Mario Circuit 2R/T', 'DK Pass R', 'Rock Rock Mountain R', 'SNES Rainbow Road R/T', 'DS Rainbow Road', 'DS Rainbow Road T']

Mario__Santa__lv3_courses = ['Mario Circuit 3R', 'DK Pass R/T']

Mario__Santa__lv6_courses = ['Choco Island 2', 'DK Pass R']

Mario__Santa_ = race_tool('Mario__Santa_', 'High-End', Mario__Santa__3items, Mario__Santa__2items, Mario__Santa__lv3_courses, Mario__Santa__lv6_courses)


#Daisy__Holiday_Cheer_
# https://game8.co/games/mariokarttour/archives/274703

Daisy__Holiday_Cheer__3items = ['Mario Circuit 3R', 'Koopa Troopa Beach R', 'Tokyo Blur 3T', 'London Loop R/T', 'London Loop', 'Daisy Hills R', 'Shy Guy Bazaar T', 'Sunset Wilds R/T', 'Toad Circuit R/T', 'RMX Choco Island 1T', 'Merry Mountain R']

Daisy__Holiday_Cheer__2items = ['New York Minute 2R/T', 'New York Minute 2T', "Luigi's Mansion R", 'Koopa Troopa Beach', 'Tokyo Blur 3', 'Tokyo Blur 3R', 'Frappe Snowland', 'Frappe Snowland T', 'Vanilla Lake 1T', 'Choco Island 2R', 'Shy Guy Bazaar R', 'Daisy Hills', 'Daisy Hills T', 'London Loop R', 'London Loop T', 'RMX Mario Circuit 1T', 'Vancouver Velocity T', "Rosalina's Ice World", "Rosalina's Ice World T", 'Vancouver Velocity R/T', 'RMX Choco Island 1', 'Merry Mountain T', 'Merry Mountain']

Daisy__Holiday_Cheer__lv3_courses = ['Choco Island 2R', 'Daisy Hills T']

Daisy__Holiday_Cheer__lv6_courses = ["Luigi's Mansion R", 'RMX Mario Circuit 1T']

Daisy__Holiday_Cheer_ = race_tool('Daisy__Holiday_Cheer_', 'High-End', Daisy__Holiday_Cheer__3items, Daisy__Holiday_Cheer__2items, Daisy__Holiday_Cheer__lv3_courses, Daisy__Holiday_Cheer__lv6_courses)


#Waluigi__Bus_Driver_
# https://game8.co/games/mariokarttour/archives/274704

Waluigi__Bus_Driver__3items = ['Berlin Byways 2R/T', 'Shy Guy Bazaar R/T', 'Yoshi Circuit R', 'Waluigi Pinball R', 'Waluigi Pinball T', 'Neo Bowser City', 'Neo Bowser City T', 'London Loop R', "Bowser's Castle 2R", "Luigi's Mansion T", 'London Loop 2T', 'Ghost Valley 1R/T', 'Paris Promenade', 'New York Minute 3R', 'New York Minute 3']

Waluigi__Bus_Driver__2items = ['Berlin Byways 2T', 'RMX Rainbow Road 1R/T', 'New York Minute 2T', 'New York Minute 2', 'Donut Plains 2R', 'Mario Circuit 1R/T', "Luigi's Mansion R", "Luigi's Mansion", 'Mario Circuit T', 'Kalimari Desert R', 'Donut Plains 1R', 'London Loop', "Bowser's Castle 2", 'London Loop T', 'London Loop R/T', 'Tokyo Blur 2T', 'Toad Circuit R/T', 'Donut Plains 1R', 'Paris Promenade R/T']

Waluigi__Bus_Driver__lv3_courses = ['Mario Circuit 1R/T', 'Mario Circuit T', "Luigi's Mansion"]

Waluigi__Bus_Driver__lv6_courses = ['Kalimari Desert R']

Waluigi__Bus_Driver_ = race_tool('Waluigi__Bus_Driver_', 'High-End', Waluigi__Bus_Driver__3items, Waluigi__Bus_Driver__2items, Waluigi__Bus_Driver__lv3_courses, Waluigi__Bus_Driver__lv6_courses)


#Yoshi__Reindeer_
# https://game8.co/games/mariokarttour/archives/275176

Yoshi__Reindeer__3items = ['Tokyo Blur 3', 'Tokyo Blur 3R', 'Yoshi Circuit', 'Yoshi Circuit T', 'Dino Dino Jungle', 'New York Minute 2', 'New York Minute 2T', 'Vanilla Lake 1T', 'Rock Rock Mountain', 'Vancouver Velocity R/T', 'Koopa Troopa Beach R/T', 'London Loop 2R/T', 'Merry Mountain T', 'RMX Rainbow Road 1T', 'RMX Rainbow Road 1R']

Yoshi__Reindeer__2items = ['Tokyo Blur 3T', 'New York Minute 2R', 'Shy Guy Bazaar T', 'Frappe Snowland', 'Frappe Snowland R', 'Vanilla Lake 1', 'Berlin Byways 2R', 'Dino Dino Jungle R/T', 'Vancouver Velocity', 'Vancouver Velocity R', 'Vancouver Velocity T', 'Tokyo Blur 2R', 'Tokyo Blur 2R/T', 'Royal Raceway R', 'Merry Mountain', 'London Loop 2R']

Yoshi__Reindeer__lv3_courses = ['Dino Dino Jungle R/T', 'Shy Guy Bazaar T']

Yoshi__Reindeer__lv6_courses = ['Frappe Snowland', 'Frappe Snowland R']

Yoshi__Reindeer_ = race_tool('Yoshi__Reindeer_', 'High-End', Yoshi__Reindeer__3items, Yoshi__Reindeer__2items, Yoshi__Reindeer__lv3_courses, Yoshi__Reindeer__lv6_courses)


#Pauline__Party_Time_
# https://game8.co/games/mariokarttour/archives/275177

Pauline__Party_Time__3items = ['Kalimari Desert 2', 'Royal Raceway', 'DS Rainbow Road R', 'New York Minute 2T', 'New York Minute 2R', 'New York Minute 2R/T', 'Frappe Snowland R', 'SNES Rainbow Road', 'Shy Guy Bazaar R/T', 'Waluigi Pinball', 'New York Minute 3', 'Los Angeles Laps', 'Neo Bowser City R/T', 'London Loop 2R/T', 'RMX Rainbow Road 2R']

Pauline__Party_Time__2items = ['Royal Raceway T', 'Berlin Byways 2T', 'Berlin Byways 2R', 'Berlin Byways 2R/T', 'New York Minute 2', 'SNES Rainbow Road R', 'DK Pass R', "Bowser's Castle 1T", 'Paris Promenade 2T', 'Kalimari Desert 2R', 'New York Minute 3T', 'RMX Rainbow Road 1R/T', 'RMX Rainbow Road 1R/T', 'Los Angeles Laps R', "Bowser's Castle 2T", "Luigi's Mansion T", 'Tokyo Blur 2', 'Tokyo Blur 2T', 'Tokyo Blur 2R', "Bowser's Castle 1R/T", 'RMX Choco Island 1R', 'RMX Mario Circuit 1R/T', 'RMX Rainbow Road 2']

Pauline__Party_Time__lv3_courses = ['DK Pass R', "Bowser's Castle 1R/T"]

Pauline__Party_Time__lv6_courses = ['Royal Raceway T', 'Kalimari Desert 2R']

Pauline__Party_Time_ = race_tool('Pauline__Party_Time_', 'High-End', Pauline__Party_Time__3items, Pauline__Party_Time__2items, Pauline__Party_Time__lv3_courses, Pauline__Party_Time__lv6_courses)


#Mario__Happi_
# https://game8.co/games/mariokarttour/archives/275390

Mario__Happi__3items = ['Mario Circuit 2', 'Mario Circuit 2R', 'Mario Circuit', 'Tokyo Blur 2R', 'Tokyo Blur 2', 'Mario Circuit 3T', 'Rock Rock Mountain R', 'Koopa Troopa Beach T', 'DS Rainbow Road', 'Cheep Cheep Lagoon R/T', 'Tokyo Blur', 'Tokyo Blur 3', 'RMX Rainbow Road 1']

Mario__Happi__2items = ['Ghost Valley 1R/T', 'Shy Guy Bazaar R/T', 'Mario Circuit 2T', 'Cheep Cheep Lagoon', "Bowser's Castle 1R", "Bowser's Castle 1T", 'Tokyo Blur 2T', 'Rock Rock Mountain', 'Mario Circuit 2R/T', 'Mario Circuit R', 'RMX Rainbow Road 1T', 'Royal Raceway', 'Royal Raceway R']

Mario__Happi__lv3_courses = ['Rock Rock Mountain', 'Ghost Valley 1R/T']

Mario__Happi__lv6_courses = ['Cheep Cheep Lagoon', 'Royal Raceway R']

Mario__Happi_ = race_tool('Mario__Happi_', 'High-End', Mario__Happi__3items, Mario__Happi__2items, Mario__Happi__lv3_courses, Mario__Happi__lv6_courses)


#Toad__Party_Time_
# https://game8.co/games/mariokarttour/archives/275393

Toad__Party_Time__3items = ['Berlin Byways 2R/T', 'Choco Island 2R/T', 'Maple Treeway', 'Tokyo Blur 2R', 'Toad Circuit R', 'Toad Circuit T', 'Koopa Troopa Beach R', 'Mario Circuit R', 'Los Angeles Laps', 'Mario Circuit 3R/T', 'Toad Circuit R/T', 'Mario Circuit 2R/T', 'Tokyo Blur']

Toad__Party_Time__2items = ['Kalimari Desert 2T', 'Berlin Byways 2R', 'Berlin Byways 2', 'DK Pass R/T', 'Vanilla Lake 1', 'Vanilla Lake 1T', 'Mario Circuit 2', 'Mario Circuit 2R', 'Maple Treeway T', 'Tokyo Blur R', 'Tokyo Blur T', 'London Loop 2', 'London Loop 2R/T', 'Donut Plains 2', 'Donut Plains 2T', 'Koopa Troopa Beach R/T', 'Tokyo Blur 2T', 'Mario Circuit 1R/T', 'Koopa Troopa Beach', 'Choco Island 1R', 'RMX Rainbow Road 2R']

Toad__Party_Time__lv3_courses = ['DK Pass R/T', 'Mario Circuit 1R/T']

Toad__Party_Time__lv6_courses = ['Mario Circuit 2', 'Kalimari Desert 2T']

Toad__Party_Time_ = race_tool('Toad__Party_Time_', 'High-End', Toad__Party_Time__3items, Toad__Party_Time__2items, Toad__Party_Time__lv3_courses, Toad__Party_Time__lv6_courses)


#Gold_Koopa__Freerunning_
# https://game8.co/games/mariokarttour/archives/275391

Gold_Koopa__Freerunning__3items = ['Donut Plains 1T', 'Koopa Troopa Beach R/T', 'Mario Circuit 1R/T', 'Choco Island 1R', 'DS Rainbow Road R/T', 'Dino Dino Jungle R', 'Tokyo Blur 2T', 'Tokyo Blur 2R/T', 'Koopa Troopa Beach', 'RMX Choco Island 2R', 'Koopa Troopa Beach R', 'Mario Circuit 2R/T', 'Mario Circuit T', 'Neo Bowser City R', 'Paris Promenade R', 'Paris Promenade R/T']

Gold_Koopa__Freerunning__2items = ['Koopa Troopa Beach 2R', 'Koopa Troopa Beach 2', 'Donut Plains 1', 'London Loop 2R', 'London Loop 2R/T', 'Mario Circuit 3R/T', 'Choco Island 1T', 'Mario Circuit 3R', 'RMX Rainbow Road 1T', 'RMX Choco Island 2', 'RMX Choco Island 2T', 'RMX Rainbow Road 2R', 'Cheep Cheep Lagoon T', 'Dino Dino Jungle', 'Toad Circuit R/T', 'Koopa Troopa Beach T', 'Neo Bowser City', 'Tokyo Blur R/T', 'Paris Promenade T', 'Berlin Byways 2R/T']

Gold_Koopa__Freerunning__lv3_courses = ['Toad Circuit R/T', 'Koopa Troopa Beach T']

Gold_Koopa__Freerunning__lv6_courses = ['Cheep Cheep Lagoon T', 'Dino Dino Jungle']

Gold_Koopa__Freerunning_ = race_tool('Gold_Koopa__Freerunning_', 'High-End', Gold_Koopa__Freerunning__3items, Gold_Koopa__Freerunning__2items, Gold_Koopa__Freerunning__lv3_courses, Gold_Koopa__Freerunning__lv6_courses)


#Ice_Mario
# https://game8.co/games/mariokarttour/archives/275772

Ice_Mario_3items = ['Mario Circuit 2R/T', 'Neo Bowser City R/T', 'DK Pass R/T', 'DS Rainbow Road R/T', 'Donut Plains 2R', "Rosalina's Ice World R", 'SNES Rainbow Road R', 'SNES Rainbow Road', 'Frappe Snowland R/T', 'Vancouver Velocity T', 'DS Rainbow Road T', 'Mario Circuit 1R/T', 'Vanilla Lake 1R', 'Koopa Troopa Beach 2T', 'Vanilla Lake 1']

Ice_Mario_2items = ['Vanilla Lake 1T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1T', 'Mario Circuit 3R/T', 'London Loop 2T', 'London Loop 2R/T', 'Donut Plains 2', "Rosalina's Ice World T", 'Frappe Snowland', 'Frappe Snowland T', 'Frappe Snowland R', 'Vancouver Velocity R', 'Mario Circuit R/T', 'Koopa Troopa Beach 2R', 'Koopa Troopa Beach 2']

Ice_Mario_lv3_courses = ['Mario Circuit R/T', 'Koopa Troopa Beach 2R']

Ice_Mario_lv6_courses = ['Vanilla Lake 1T', 'RMX Mario Circuit 1']

Ice_Mario = race_tool('Ice_Mario', 'High-End', Ice_Mario_3items, Ice_Mario_2items, Ice_Mario_lv3_courses, Ice_Mario_lv6_courses)


#Penguin_Luigi
# https://game8.co/games/mariokarttour/archives/275773

Penguin_Luigi_3items = ['DK Pass R/T', 'London Loop R', 'Mario Circuit 2R/T', 'RMX Rainbow Road 1R/T', 'Waluigi Pinball R/T', 'DK Pass', 'Frappe Snowland T', 'Rock Rock Mountain R', 'Donut Plains 2T', "Rosalina's Ice World T", 'Mario Circuit R/T', 'RMX Choco Island 1R', 'DK Pass R', 'Merry Mountain', 'RMX Rainbow Road 1T', 'RMX Mario Circuit 1R', 'Koopa Troopa Beach 2', 'Mario Circuit 2R/T', 'Berlin Byways 2T', 'Berlin Byways 2R', 'Vanilla Lake 1']

Penguin_Luigi_2items = ['London Loop', 'London Loop R/T', 'DS Rainbow Road R/T', 'Royal Raceway R', 'Paris Promenade T', 'Paris Promenade R/T', "Luigi's Mansion R/T", 'Donut Plains 2R', 'Paris Promenade 2T', 'Frappe Snowland R/T', 'Vancouver Velocity R', "Luigi's Mansion R", 'Rock Rock Mountain', 'Frappe Snowland R', 'Koopa Troopa Beach 2T', 'RMX Rainbow Road 2R']

Penguin_Luigi_lv3_courses = ["Luigi's Mansion R", 'DS Rainbow Road R/T']

Penguin_Luigi_lv6_courses = ['Rock Rock Mountain', 'Koopa Troopa Beach 2T']

Penguin_Luigi = race_tool('Penguin_Luigi', 'High-End', Penguin_Luigi_3items, Penguin_Luigi_2items, Penguin_Luigi_lv3_courses, Penguin_Luigi_lv6_courses)


#Peach__Wintertime_
# https://game8.co/games/mariokarttour/archives/275774

Peach__Wintertime__3items = ['Paris Promenade R', 'Royal Raceway T', 'Frappe Snowland R/T', 'Mario Circuit R/T', 'Yoshi Circuit', 'Yoshi Circuit T', 'Choco Island 2T', 'RMX Choco Island 1R', 'Frappe Snowland', 'Frappe Snowland T', 'Vanilla Lake 1T', 'London Loop 2R/T']

Peach__Wintertime__2items = ['Royal Raceway R', 'Paris Promenade R/T', 'Paris Promenade T', 'Yoshi Circuit R/T', 'Paris Promenade 2', 'RMX Mario Circuit 1', 'Paris Promenade 2R', 'Vancouver Velocity', 'Vancouver Velocity T', 'SNES Rainbow Road R/T', "Rosalina's Ice World", "Rosalina's Ice World R", 'RMX Choco Island 1T', 'Vanilla Lake 1', 'Choco Island 2R', 'RMX Choco Island 1', 'Merry Mountain R', 'Merry Mountain T', 'London Loop 2T']

Peach__Wintertime__lv3_courses = ['Choco Island 2R', 'RMX Choco Island 1T']

Peach__Wintertime__lv6_courses = ['RMX Mario Circuit 1', 'RMX Choco Island 1']

Peach__Wintertime_ = race_tool('Peach__Wintertime_', 'High-End', Peach__Wintertime__3items, Peach__Wintertime__2items, Peach__Wintertime__lv3_courses, Peach__Wintertime__lv6_courses)


#Baby_Peach__Cherub_
# https://game8.co/games/mariokarttour/archives/278438

Baby_Peach__Cherub__3items = ['Yoshi Circuit R/T', 'Donut Plains 1R', 'Frappe Snowland R/T', 'Mario Circuit', 'Yoshi Circuit T', 'Donut Plains 2', 'Donut Plains 2R', 'Choco Island 2', 'Paris Promenade 2', 'Paris Promenade 2R/T', 'SNES Rainbow Road R', 'RMX Choco Island 2T', 'Choco Island 1T', 'Choco Island 1R', 'RMX Choco Island 1R', 'London Loop 2R', 'Mario Circuit 2R/T', 'RMX Rainbow Road 2T']

Baby_Peach__Cherub__2items = ['Choco Island 1', 'Vancouver Velocity', 'Vancouver Velocity R/T', 'SNES Rainbow Road R/T', 'RMX Choco Island 2R', 'RMX Choco Island 2', 'DK Pass', 'DK Pass T', 'Frappe Snowland T', 'Paris Promenade 2R', 'Paris Promenade 2T', 'RMX Choco Island 1', 'RMX Rainbow Road 2R']

Baby_Peach__Cherub__lv3_courses = ['DK Pass T', 'SNES Rainbow Road R/T']

Baby_Peach__Cherub__lv6_courses = ['Frappe Snowland T', 'Choco Island 1']

Baby_Peach__Cherub_ = race_tool('Baby_Peach__Cherub_', 'High-End', Baby_Peach__Cherub__3items, Baby_Peach__Cherub__2items, Baby_Peach__Cherub__lv3_courses, Baby_Peach__Cherub__lv6_courses)


#Rosalina__Aurora_
# https://game8.co/games/mariokarttour/archives/279954

Rosalina__Aurora__3items = ['Frappe Snowland T', 'Frappe Snowland R', 'Vancouver Velocity', 'Vancouver Velocity R', 'Vancouver Velocity R/T', 'Mario Circuit T', 'DS Rainbow Road', 'DS Rainbow Road R', 'Vanilla Lake 1R/T', 'Choco Mountain T', 'Choco Mountain R', 'RMX Mario Circuit 1R', 'RMX Rainbow Road 2R', 'Berlin Byways 2R', 'DS Rainbow Road R/T', 'London Loop 2R', 'RMX Rainbow Road 1']

Rosalina__Aurora__2items = ['Paris Promenade', 'Frappe Snowland', 'Vancouver Velocity T', 'DK Pass', 'Frappe Snowland R/T', 'SNES Rainbow Road R/T', 'Vanilla Lake 1R', 'London Loop 2', 'Choco Mountain', 'RMX Mario Circuit 1T', 'RMX Rainbow Road 2T', 'Berlin Byways 2R/T', 'RMX Rainbow Road 1R', 'London Loop 2T', 'London Loop 2R/T']

Rosalina__Aurora__lv3_courses = ['Frappe Snowland R/T', 'Frappe Snowland']

Rosalina__Aurora__lv6_courses = ['DK Pass']

Rosalina__Aurora_ = race_tool('Rosalina__Aurora_', 'High-End', Rosalina__Aurora__3items, Rosalina__Aurora__2items, Rosalina__Aurora__lv3_courses, Rosalina__Aurora__lv6_courses)


#Wario__Hiker_
# https://game8.co/games/mariokarttour/archives/279955

Wario__Hiker__3items = ['Vanilla Lake 1R', 'DK Pass R', 'DK Pass T', 'Vancouver Velocity R', "Luigi's Mansion", "Luigi's Mansion R", 'Rock Rock Mountain', 'DK Pass R/T', 'DK Summit T', 'Dino Dino Jungle T', 'Kalimari Desert R', 'Choco Mountain', 'Paris Promenade T']

Wario__Hiker__2items = ['Vanilla Lake 1T', 'Vanilla Lake 1', "Bowser's Castle 1", 'DK Pass', 'Vancouver Velocity T', 'Rock Rock Mountain R', 'Koopa Troopa Beach', 'Cheep Cheep Lagoon R/T', 'Dino Dino Jungle R/T', 'Waluigi Pinball R/T', 'Ghost Valley 1R/T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1T', 'RMX Mario Circuit 1R', 'RMX Choco Island 2', 'Paris Promenade R/T']

Wario__Hiker__lv3_courses = ['Vanilla Lake 1', "Bowser's Castle 1"]

Wario__Hiker__lv6_courses = ['DK Pass', 'RMX Mario Circuit 1R']

Wario__Hiker_ = race_tool('Wario__Hiker_', 'High-End', Wario__Hiker__3items, Wario__Hiker__2items, Wario__Hiker__lv3_courses, Wario__Hiker__lv6_courses)


#Mario__Classic_
# https://game8.co/games/mariokarttour/archives/281092

Mario__Classic__3items = ['RMX Mario Circuit 1T', 'RMX Mario Circuit 1', 'Mario Circuit 1', 'RMX Mario Circuit 1R', 'Mario Circuit 2R/T', 'Mario Circuit 2', 'London Loop T', 'Mario Circuit 2T', 'London Loop R/T', 'Sunset Wilds R', 'RMX Rainbow Road 1R/T', 'RMX Mario Circuit 1R/T']

Mario__Classic__2items = ['Mario Circuit 1R/T', 'Mario Circuit 3T', 'Mario Circuit 3', 'Donut Plains 1', 'London Loop', 'Donut Plains 1T', 'London Loop R', 'Maple Treeway T', 'Maple Treeway R', 'Mario Circuit 3R/T', 'Sunset Wilds T', 'Sunset Wilds R/T', 'London Loop 2', 'Mario Circuit 2R', 'London Loop 2T', 'Kalimari Desert R/T', 'Vanilla Lake 1', 'Vanilla Lake 1T', 'Donut Plains 1R/T', 'Merry Mountain', 'Koopa Troopa Beach 2']

Mario__Classic__lv3_courses = ['Mario Circuit 2R', 'Vanilla Lake 1']

Mario__Classic__lv6_courses = ['Mario Circuit 3', 'Donut Plains 1T']

Mario__Classic_ = race_tool('Mario__Classic_', 'High-End', Mario__Classic__3items, Mario__Classic__2items, Mario__Classic__lv3_courses, Mario__Classic__lv6_courses)


#Luigi__Classic_
# https://game8.co/games/mariokarttour/archives/281112

Luigi__Classic__3items = ["Luigi's Mansion R", 'Mario Circuit 3T', 'Mario Circuit R/T', 'Mario Circuit 2T', "Luigi's Mansion R/T", 'Mario Circuit 2R', 'London Loop', 'London Loop T', 'Paris Promenade', 'Maple Treeway T', 'Sunset Wilds', 'Merry Mountain', 'Donut Plains 1R/T']

Luigi__Classic__2items = ['Koopa Troopa Beach 2T', 'RMX Mario Circuit 1', 'Toad Circuit R', "Luigi's Mansion", "Luigi's Mansion T", 'Waluigi Pinball R', 'Mario Circuit T', 'Kalimari Desert R', 'Mario Circuit 1T', 'Donut Plains 1', 'Paris Promenade R/T', 'Frappe Snowland R', 'London Loop R', 'Koopa Troopa Beach', 'London Loop R/T', 'Maple Treeway', 'Sunset Wilds R', 'Berlin Byways 2', 'Berlin Byways 2R', 'Vanilla Lake 1R', 'Merry Mountain T', 'DK Summit', 'DK Summit T']

Luigi__Classic__lv3_courses = ['Mario Circuit 1T', 'Frappe Snowland R']

Luigi__Classic__lv6_courses = ['Toad Circuit R', 'Vanilla Lake 1R']

Luigi__Classic_ = race_tool('Luigi__Classic_', 'High-End', Luigi__Classic__3items, Luigi__Classic__2items, Luigi__Classic__lv3_courses, Luigi__Classic__lv6_courses)


#Baby_Rosalina__Detective_
# https://game8.co/games/mariokarttour/archives/282822

Baby_Rosalina__Detective__3items = ['Frappe Snowland', 'Frappe Snowland R', 'Yoshi Circuit R/T', "Luigi's Mansion R/T", 'Vancouver Velocity T', 'London Loop R', 'Berlin Byways 2R/T', 'Berlin Byways 2R', 'Paris Promenade 2', 'Shy Guy Bazaar T', 'Daisy Hills R/T', 'RMX Mario Circuit 1T', 'London Loop 2', 'London Loop 2R', 'London Loop 2R/T', 'RMX Choco Island 2R', 'Tokyo Blur T', 'Tokyo Blur R', 'Tokyo Blur 2T', 'Tokyo Blur 2', 'RMX Choco Island 1']

Baby_Rosalina__Detective__2items = ['Mario Circuit 2R', 'Donut Plains 1R', 'Vancouver Velocity R', 'Berlin Byways 2', 'Berlin Byways 2T', 'Paris Promenade 2R', "Luigi's Mansion T", 'London Loop 2T', 'RMX Mario Circuit 1R', 'RMX Choco Island 1R', 'Tokyo Blur 2R', 'Tokyo Blur', 'RMX Mario Circuit 1R/T', 'Daisy Hills']

Baby_Rosalina__Detective__lv3_courses = ['Daisy Hills', 'RMX Mario Circuit 1R/T']

Baby_Rosalina__Detective__lv6_courses = ["Luigi's Mansion T", 'RMX Choco Island 1R']

Baby_Rosalina__Detective_ = race_tool('Baby_Rosalina__Detective_', 'High-End', Baby_Rosalina__Detective__3items, Baby_Rosalina__Detective__2items, Baby_Rosalina__Detective__lv3_courses, Baby_Rosalina__Detective__lv6_courses)


#Black_Yoshi
# https://game8.co/games/mariokarttour/archives/285889

Black_Yoshi_3items = ['Koopa Troopa Beach 2T', 'Toad Circuit', 'Sunset Wilds', 'Sunset Wilds T', 'Paris Promenade 2', 'Donut Plains 2R', 'Choco Mountain T', 'Tokyo Blur 3R', 'Tokyo Blur 3T', 'Ghost Valley 1R', 'Ghost Valley 1T', 'DK Summit R', 'Donut Plains 1R/T', 'RMX Mario Circuit 1R/T', 'Daisy Hills', 'Yoshi Circuit R', 'Daisy Hills T', 'DK Pass R/T', 'Rock Rock Mountain T', 'Daisy Hills R/T']

Black_Yoshi_2items = ['Daisy Hills R', 'Yoshi Circuit T', 'Toad Circuit R', 'Dino Dino Jungle T', 'Sunset Wilds R', 'Ghost Valley 1', 'Berlin Byways 2T', 'Berlin Byways 2R', 'Donut Plains 2T', 'Choco Mountain', 'RMX Choco Island 1', 'Tokyo Blur 3', 'DK Summit', 'Yoshi Circuit', 'Toad Circuit R/T', 'Rock Rock Mountain', 'Yoshi Circuit R/T', 'Rock Rock Mountain R']

Black_Yoshi_lv3_courses = ['Yoshi Circuit', 'Daisy Hills R']

Black_Yoshi_lv6_courses = ['Ghost Valley 1', 'Choco Mountain']

Black_Yoshi = race_tool('Black_Yoshi', 'High-End', Black_Yoshi_3items, Black_Yoshi_2items, Black_Yoshi_lv3_courses, Black_Yoshi_lv6_courses)


#Yoshi__Egg_Hunt_
# https://game8.co/games/mariokarttour/archives/285890

Yoshi__Egg_Hunt__3items = ['RMX Mario Circuit 1R/T', 'Yoshi Circuit', 'Yoshi Circuit R', 'Daisy Hills', 'Sunset Wilds R', 'RMX Mario Circuit 1R', 'Mario Circuit 2R', 'Mario Circuit 2', 'Tokyo Blur T', 'Tokyo Blur R', 'Yoshi Circuit R/T', 'Dino Dino Jungle R/T', 'Cheep Cheep Lagoon R/T', 'Maple Treeway T']

Yoshi__Egg_Hunt__2items = ['Tokyo Blur R/T', 'Maple Treeway R', 'Daisy Hills T', 'Daisy Hills R', 'Yoshi Circuit T', 'Donut Plains 1R/T', 'Dino Dino Jungle T', 'Sunset Wilds', 'Cheep Cheep Lagoon', 'Cheep Cheep Lagoon T', 'Mario Circuit 2T', 'Tokyo Blur 3', 'Daisy Hills R/T', 'Toad Circuit R/T', "Luigi's Mansion R/T", 'Choco Island 2R/T']

Yoshi__Egg_Hunt__lv3_courses = ['Dino Dino Jungle T', 'Mario Circuit 2T']

Yoshi__Egg_Hunt__lv6_courses = ['Donut Plains 1R/T', 'Cheep Cheep Lagoon T']

Yoshi__Egg_Hunt_ = race_tool('Yoshi__Egg_Hunt_', 'High-End', Yoshi__Egg_Hunt__3items, Yoshi__Egg_Hunt__2items, Yoshi__Egg_Hunt__lv3_courses, Yoshi__Egg_Hunt__lv6_courses)


#Builder_Mario
# https://game8.co/games/mariokarttour/archives/286539

Builder_Mario_3items = ['Koopa Troopa Beach 2T', 'Tokyo Blur R/T', 'London Loop R/T', 'Sunset Wilds T', 'Los Angeles Laps R/T', 'Los Angeles Laps T', 'Kalimari Desert T', 'RMX Mario Circuit 1T', 'RMX Choco Island 1R', 'Mario Circuit 1T', "Bowser's Castle 1T", 'Mario Circuit 1R/T', 'Mario Circuit R/T', 'Choco Island 2R/T']

Builder_Mario_2items = ['Paris Promenade T', "Bowser's Castle 2R/T", 'Rock Rock Mountain T', 'Choco Island 1T', 'Daisy Hills T', 'Toad Circuit T', 'DK Summit T', 'Mario Circuit 2R/T', 'RMX Mario Circuit 1R/T', 'RMX Choco Island 1', 'Daisy Hills R/T', 'Vanilla Lake 1R/T', 'Maple Treeway T']

Builder_Mario_lv3_courses = ['Daisy Hills R/T', 'Daisy Hills T']

Builder_Mario_lv6_courses = ['Toad Circuit T', 'Choco Island 1T']

Builder_Mario = race_tool('Builder_Mario', 'High-End', Builder_Mario_3items, Builder_Mario_2items, Builder_Mario_lv3_courses, Builder_Mario_lv6_courses)


#Builder_Toad
# https://game8.co/games/mariokarttour/archives/286542

Builder_Toad_3items = ['Vancouver Velocity T', 'New York Minute 3R/T', 'New York Minute 3T', 'Dino Dino Jungle T', 'RMX Rainbow Road 1R/T', 'Yoshi Circuit T', 'Toad Circuit T', 'Cheep Cheep Lagoon T', 'Tokyo Blur 3T', 'Ghost Valley 1T', 'Toad Circuit R/T', 'Choco Island 2R/T', 'Vanilla Lake 1R/T', 'DK Summit T', 'RMX Rainbow Road 1T', 'Merry Mountain T']

Builder_Toad_2items = ['Kalimari Desert 2T', 'Paris Promenade T', 'Waluigi Pinball T', 'Frappe Snowland T', 'RMX Choco Island 1T', 'Donut Plains 1T', 'RMX Choco Island 1R', 'Choco Island 1T', 'SNES Rainbow Road R/T', 'Shy Guy Bazaar R/T', 'Mario Circuit 3R/T', 'DK Pass R/T', 'RMX Choco Island 1']

Builder_Toad_lv3_courses = ['Shy Guy Bazaar R/T', 'RMX Choco Island 1T']

Builder_Toad_lv6_courses = ['Waluigi Pinball T', 'RMX Choco Island 1']

Builder_Toad = race_tool('Builder_Toad', 'High-End', Builder_Toad_3items, Builder_Toad_2items, Builder_Toad_lv3_courses, Builder_Toad_lv6_courses)


#Dry_Bones__Gold_
# https://game8.co/games/mariokarttour/archives/286541

Dry_Bones__Gold__3items = ["Bowser's Castle 1", "Bowser's Castle 1R", 'Choco Island 1', 'Koopa Troopa Beach 2', "Bowser's Castle 2", "Bowser's Castle 2T", "Bowser's Castle 2R/T", 'Vanilla Lake 1R/T', "Bowser's Castle 1R/T", 'Neo Bowser City R/T', 'RMX Rainbow Road 1R', 'Ghost Valley 1R/T', 'SNES Rainbow Road R/T', 'Vancouver Velocity', 'New York Minute 3', 'Kalimari Desert 2']

Dry_Bones__Gold__2items = ["Bowser's Castle 1T", 'Koopa Troopa Beach 2T', 'RMX Choco Island 1T', "Bowser's Castle 2R", 'Choco Island 1R', 'Merry Mountain T', 'Waluigi Pinball R', 'Merry Mountain', 'Kalimari Desert R', 'Kalimari Desert', 'RMX Rainbow Road 1', "Luigi's Mansion R/T", 'Yoshi Circuit R/T', 'Shy Guy Bazaar R/T', 'Choco Island 2R/T', 'Waluigi Pinball R/T', 'Dino Dino Jungle R/T', 'Vancouver Velocity R', 'New York Minute 3R', 'Kalimari Desert 2R']

Dry_Bones__Gold__lv3_courses = ["Bowser's Castle 2R", 'SNES Rainbow Road']

Dry_Bones__Gold__lv6_courses = ['Ghost Valley 1', 'Koopa Troopa Beach 2R']

Dry_Bones__Gold_ = race_tool('Dry_Bones__Gold_', 'High-End', Dry_Bones__Gold__3items, Dry_Bones__Gold__2items, Dry_Bones__Gold__lv3_courses, Dry_Bones__Gold__lv6_courses)


#Daisy__Fairy_
# https://game8.co/games/mariokarttour/archives/286865

Daisy__Fairy__3items = ['Mario Circuit R', 'DS Rainbow Road', 'Vanilla Lake 1R/T', 'Choco Island 2R/T', 'Vanilla Lake 1', 'Vanilla Lake 1R', 'Sunset Wilds R', 'RMX Choco Island 1', 'RMX Choco Island 1', 'RMX Mario Circuit 1T', 'RMX Choco Island 2', 'Choco Island 2', 'Choco Island 2R', 'Tokyo Blur T', "Luigi's Mansion", 'Maple Treeway']

Daisy__Fairy__2items = ['RMX Choco Island 1R', 'Daisy Hills T', 'Mario Circuit 1T', 'Daisy Hills R', 'Koopa Troopa Beach R/T', 'Sunset Wilds T', 'Sunset Wilds', 'Yoshi Circuit R', 'Choco Island 2T', 'DS Rainbow Road R/T', 'Tokyo Blur', 'Tokyo Blur R', 'Yoshi Circuit R/T', 'Mario Circuit 1R/T', 'Maple Treeway T']

Daisy__Fairy__lv3_courses = ['Daisy Hills R', 'Koopa Troopa Beach R/T']

Daisy__Fairy__lv6_courses = ['RMX Choco Island 1R', 'Yoshi Circuit R']

Daisy__Fairy_ = race_tool('Daisy__Fairy_', 'High-End', Daisy__Fairy__3items, Daisy__Fairy__2items, Daisy__Fairy__lv3_courses, Daisy__Fairy__lv6_courses)


#Funky_Kong
# https://game8.co/games/mariokarttour/archives/288930

Funky_Kong_3items = ['Vanilla Lake 1T', 'Dino Dino Jungle', 'Los Angeles Laps R/T', 'Paris Promenade 2T', 'Paris Promenade 2R', 'Rock Rock Mountain R', 'Rock Rock Mountain T', 'Cheep Cheep Lagoon T', 'Cheep Cheep Lagoon R', 'RMX Choco Island 2R', 'Choco Mountain R', 'New York Minute 3R', 'DK Pass']

Funky_Kong_2items = ['Dino Dino Jungle T', 'Vanilla Lake 1', "Bowser's Castle 2T", 'DK Pass R', 'DK Pass T', 'Toad Circuit R', 'Donut Plains 2T', 'New York Minute 3', 'New York Minute 3T', 'Cheep Cheep Lagoon', 'Rock Rock Mountain', 'Waluigi Pinball R/T', 'Choco Mountain', 'Royal Raceway T']

Funky_Kong_lv3_courses = ["Bowser's Castle 2T", 'Waluigi Pinball R/T']

Funky_Kong_lv6_courses = ['Cheep Cheep Lagoon', 'Royal Raceway T']

Funky_Kong = race_tool('Funky_Kong', 'High-End', Funky_Kong_3items, Funky_Kong_2items, Funky_Kong_lv3_courses, Funky_Kong_lv6_courses)


#Dixie_Kong
# https://game8.co/games/mariokarttour/archives/288929

Dixie_Kong_3items = ['Maple Treeway', 'London Loop', 'Cheep Cheep Lagoon', 'Cheep Cheep Lagoon R', 'Donut Plains 1', 'Donut Plains 1T', 'RMX Choco Island 1R', 'RMX Choco Island 1T', 'Daisy Hills', 'Daisy Hills R', 'Daisy Hills T', 'Royal Raceway R', 'Vanilla Lake 1', 'Kalimari Desert 2R']

Dixie_Kong_2items = ['Choco Island 1', 'Donut Plains 2', 'Donut Plains 2T', 'Maple Treeway R', 'Choco Island 1R', 'Tokyo Blur R/T', 'London Loop R/T', 'New York Minute 3', 'New York Minute 3T', 'Royal Raceway', 'DK Pass', 'RMX Choco Island 1', 'Kalimari Desert 2', 'Dino Dino Jungle T', 'Choco Island 2R/T']

Dixie_Kong_lv3_courses = ['Choco Island 2R/T', 'Royal Raceway']

Dixie_Kong_lv6_courses = ['Choco Island 1', 'Kalimari Desert 2']

Dixie_Kong = race_tool('Dixie_Kong', 'High-End', Dixie_Kong_3items, Dixie_Kong_2items, Dixie_Kong_lv3_courses, Dixie_Kong_lv6_courses)


#Mario__Chef_
# https://game8.co/games/mariokarttour/archives/289728

Mario__Chef__3items = ['Choco Island 1', "Luigi's Mansion", 'RMX Mario Circuit 1', 'Donut Plains 1', 'Paris Promenade 2', 'Choco Mountain', 'Choco Mountain R', 'RMX Choco Island 1R', 'RMX Choco Island 1', 'Donut Plains 1R/T', 'Mario Circuit R', 'Tokyo Blur 3', 'Mario Circuit 3R/T', 'DK Summit R']

Mario__Chef__2items = ['Royal Raceway T', 'Royal Raceway R', 'Berlin Byways 2R', 'Berlin Byways 2', 'Donut Plains 1T', 'Tokyo Blur 3T', 'Choco Island 1R', 'Choco Island 1T', 'Choco Mountain R', 'Choco Island 1T', 'Mario Circuit', 'Mario Circuit 2', 'Mario Circuit 3', "Luigi's Mansion R/T", 'DK Summit']

Mario__Chef__lv3_courses = ['Donut Plains 1T', 'Mario Circuit 2']

Mario__Chef__lv6_courses = ['Choco Island 1T', 'Mario Circuit 3']

Mario__Chef_ = race_tool('Mario__Chef_', 'High-End', Mario__Chef__3items, Mario__Chef__2items, Mario__Chef__lv3_courses, Mario__Chef__lv6_courses)


#Dry_Bowser__Gold_
# https://game8.co/games/mariokarttour/archives/289729

Dry_Bowser__Gold__3items = ['Neo Bowser City', 'Neo Bowser City T', 'Waluigi Pinball T', 'Waluigi Pinball R', 'DS Rainbow Road R', 'DS Rainbow Road T', 'Dino Dino Jungle', 'Dino Dino Jungle T', 'Airship Fortress R', 'Airship Fortress', "Luigi's Mansion T", 'Choco Island 1T', 'Rock Rock Mountain R', "Rosalina's Ice World T", 'Kalimari Desert R', "Bowser's Castle 2R/T", 'RMX Rainbow Road 1R', 'Vancouver Velocity R']

Dry_Bowser__Gold__2items = ['Neo Bowser City R', 'Waluigi Pinball', 'DS Rainbow Road', 'Dino Dino Jungle R', 'RMX Rainbow Road 1R/T', 'Choco Island 1', 'Rock Rock Mountain T', 'Kalimari Desert', 'Kalimari Desert T', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1T', 'Vancouver Velocity']

Dry_Bowser__Gold__lv3_courses = ['Kalimari Desert T', 'Waluigi Pinball']

Dry_Bowser__Gold__lv6_courses = ['Neo Bowser City R', 'RMX Rainbow Road 1']

Dry_Bowser__Gold_ = race_tool('Dry_Bowser__Gold_', 'High-End', Dry_Bowser__Gold__3items, Dry_Bowser__Gold__2items, Dry_Bowser__Gold__lv3_courses, Dry_Bowser__Gold__lv6_courses)


#Peach__Wedding_
# https://game8.co/games/mariokarttour/archives/290569

Peach__Wedding__3items = ['London Loop', 'Shy Guy Bazaar', 'RMX Mario Circuit 1R/T', 'Berlin Byways 2T', 'Royal Raceway', 'Royal Raceway R', 'RMX Mario Circuit 1', 'SNES Rainbow Road', 'SNES Rainbow Road R', 'Sunset Wilds T', 'Los Angeles Laps R', 'RMX Mario Circuit 1R/T', 'Toad Circuit T', 'Donut Plains 1', 'Donut Plains 1R', 'Daisy Hills R', 'RMX Choco Island 2', 'RMX Choco Island 2T', 'RMX Rainbow Road 2']

Peach__Wedding__2items = ['Shy Guy Bazaar R', 'Waluigi Pinball R', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', 'Berlin Byways 2', 'Royal Raceway T', 'Sunset Wilds', 'Los Angeles Laps', 'Los Angeles Laps R/T', 'Toad Circuit', "Luigi's Mansion R/T", 'Mario Circuit 1R/T', 'Daisy Hills', 'RMX Choco Island 2R']

Peach__Wedding__lv3_courses = ['Toad Circuit', 'Daisy Hills']

Peach__Wedding__lv6_courses = ['Shy Guy Bazaar R', 'Koopa Troopa Beach 2']

Peach__Wedding_ = race_tool('Peach__Wedding_', 'High-End', Peach__Wedding__3items, Peach__Wedding__2items, Peach__Wedding__lv3_courses, Peach__Wedding__lv6_courses)


#Rosalina__Swimwear_
# https://game8.co/games/mariokarttour/archives/291190

Rosalina__Swimwear__3items = ['Koopa Troopa Beach', 'Los Angeles Laps T', 'Koopa Troopa Beach R/T', 'SNES Rainbow Road R/T', 'Yoshi Circuit R/T', 'Donut Plains 1T', 'Frappe Snowland R', 'Choco Island 1', 'Choco Island 1T', 'Royal Raceway R', 'Royal Raceway T', 'Koopa Troopa Beach 2', 'RMX Rainbow Road 1']

Rosalina__Swimwear__2items = ['Los Angeles Laps', 'RMX Rainbow Road 1R/T', 'Daisy Hills R/T', 'Mario Circuit R/T', 'RMX Mario Circuit 1R', 'Donut Plains 1R', 'Choco Island 1R', 'Choco Mountain T', 'Choco Mountain R', 'SNES Rainbow Road', 'SNES Rainbow Road T', 'DS Rainbow Road', 'Koopa Troopa Beach 2R', 'RMX Rainbow Road 1R', 'Koopa Troopa Beach 2T', 'Koopa Troopa Beach R', 'Royal Raceway', 'RMX Rainbow Road 2R', 'RMX Rainbow Road 2']

Rosalina__Swimwear__lv3_courses = ['DS Rainbow Road', 'Mario Circuit R/T']

Rosalina__Swimwear__lv6_courses = ['Choco Mountain T', 'RMX Mario Circuit 1R']

Rosalina__Swimwear_ = race_tool('Rosalina__Swimwear_', 'High-End', Rosalina__Swimwear__3items, Rosalina__Swimwear__2items, Rosalina__Swimwear__lv3_courses, Rosalina__Swimwear__lv6_courses)


#Mario__Swimwear_
# https://game8.co/games/mariokarttour/archives/291191

Mario__Swimwear__3items = ['Mario Circuit 1R', 'Los Angeles Laps', 'Los Angeles Laps R', 'Airship Fortress', 'Mario Circuit 2T', 'Mario Circuit 3', 'Mario Circuit R/T', 'RMX Mario Circuit 1', 'RMX Mario Circuit 1R', 'Vanilla Lake 1R/T', 'Koopa Troopa Beach 2T', 'Koopa Troopa Beach 2R', 'Cheep Cheep Lagoon', 'RMX Choco Island 1R']

Mario__Swimwear__2items = ['Mario Circuit 2', 'Mario Circuit 3R', 'Mario Circuit 3T', 'Airship Fortress R', 'Airship Fortress T', 'Koopa Troopa Beach R/T', 'Cheep Cheep Lagoon R/T', 'Mario Circuit 1', 'Mario Circuit 1T', 'Cheep Cheep Lagoon T', 'Cheep Cheep Lagoon R', 'Koopa Troopa Beach T', 'Koopa Troopa Beach 2']

Mario__Swimwear__lv3_courses = ['Cheep Cheep Lagoon R', 'Mario Circuit 1T']

Mario__Swimwear__lv6_courses = ['Airship Fortress T', 'Airship Fortress R']

Mario__Swimwear_ = race_tool('Mario__Swimwear_', 'High-End', Mario__Swimwear__3items, Mario__Swimwear__2items, Mario__Swimwear__lv3_courses, Mario__Swimwear__lv6_courses)


#Toadette__Explorer_
# https://game8.co/games/mariokarttour/archives/291842

Toadette__Explorer__3items = ['Kalimari Desert R', 'Choco Island 2T', 'Kalimari Desert R/T', 'Rock Rock Mountain', 'Sunset Wilds R/T', 'Daisy Hills', 'Daisy Hills R', 'Choco Island 2T', 'Royal Raceway', 'Royal Raceway R', 'Choco Mountain T', 'Toad Circuit', 'Toad Circuit R', 'DK Summit', 'Koopa Troopa Beach T', 'Kalimari Desert 2R']

Toadette__Explorer__2items = ['Rock Rock Mountain R', 'Kalimari Desert 2T', 'Kalimari Desert 2', 'Sunset Wilds', 'Sunset Wilds T', 'Choco Island 2R/T', 'Choco Island 2R', "Luigi's Mansion T", 'Vanilla Lake 1R', 'Choco Island 1', 'Kalimari Desert R', 'Sunset Wilds R', 'Koopa Troopa Beach R', 'Dino Dino Jungle R/T', 'DS Rainbow Road R/T', 'Choco Mountain R', 'Dino Dino Jungle', 'Dino Dino Jungle R', 'Toad Circuit T']

Toadette__Explorer__lv3_courses = ['Dino Dino Jungle', 'DS Rainbow Road R/T']

Toadette__Explorer__lv6_courses = ['Choco Mountain R', 'Kalimari Desert 2']

Toadette__Explorer_ = race_tool('Toadette__Explorer_', 'High-End', Toadette__Explorer__3items, Toadette__Explorer__2items, Toadette__Explorer__lv3_courses, Toadette__Explorer__lv6_courses)


#Captain_Toad
# https://game8.co/games/mariokarttour/archives/291841

Captain_Toad_3items = ['Kalimari Desert 2T', 'Sunset Wilds R', "Bowser's Castle 1", 'Toad Circuit R/T', 'Choco Mountain R', 'Choco Mountain', 'Toad Circuit T', 'Koopa Troopa Beach 2', 'RMX Choco Island 1R', 'Cheep Cheep Lagoon T', 'Mario Circuit 3R', 'Cheep Cheep Lagoon R', 'RMX Choco Island 2', 'DK Summit R', 'Merry Mountain']

Captain_Toad_2items = ['Kalimari Desert 2', 'Kalimari Desert 2R', 'Kalimari Desert R/T', 'Airship Fortress T', 'Airship Fortress', "Bowser's Castle 1R", 'Choco Mountain T', 'Royal Raceway T', 'Ghost Valley 1R', 'Cheep Cheep Lagoon', 'DK Summit', 'Merry Mountain T']

Captain_Toad_lv3_courses = ['Cheep Cheep Lagoon R/T', "Bowser's Castle 1R"]

Captain_Toad_lv6_courses = ['Airship Fortress', 'Kalimari Desert 2']

Captain_Toad = race_tool('Captain_Toad', 'High-End', Captain_Toad_3items, Captain_Toad_2items, Captain_Toad_lv3_courses, Captain_Toad_lv6_courses)


#Nabbit
# https://game8.co/games/mariokarttour/archives/292308

Nabbit_3items = ["Rosalina's Ice World", "Rosalina's Ice World R", 'Frappe Snowland', 'Choco Island 1', 'Choco Island 1T', 'Choco Island 2', 'Choco Island 2R', 'Tokyo Blur 2', 'RMX Choco Island 1', 'Tokyo Blur 2R', 'Los Angeles Laps R/T', 'Waluigi Pinball R/T', 'Frappe Snowland R/T', 'DK Summit T', 'Mario Circuit 1', 'Kalimari Desert 2T', 'Kalimari Desert 2R', 'Choco Mountain T']

Nabbit_2items = ['Airship Fortress T', 'Airship Fortress R', 'Choco Island 2T', 'Los Angeles Laps R', "Luigi's Mansion T", 'Sunset Wilds R/T', 'Choco Island 2R/T', 'DK Summit R', 'Mario Circuit 1R', 'Kalimari Desert 2', 'Choco Mountain']

Nabbit_lv3_courses = ['Toad Circuit T', "Luigi's Mansion T"]

Nabbit_lv6_courses = ['Choco Mountain', 'Airship Fortress T']

Nabbit = race_tool('Nabbit', 'High-End', Nabbit_3items, Nabbit_2items, Nabbit_lv3_courses, Nabbit_lv6_courses)


#Wario__Cowboy_
# https://game8.co/games/mariokarttour/archives/292309

Wario__Cowboy__3items = ["Luigi's Mansion R/T", 'Neo Bowser City R', 'Airship Fortress T', 'Tokyo Blur 3T', 'Donut Plains 1R/T', 'Tokyo Blur T', 'Merry Mountain T', 'RMX Choco Island 2', 'Kalimari Desert 2T', 'Kalimari Desert 2', 'Donut Plains 1R', 'Donut Plains 1']

Wario__Cowboy__2items = ['Airship Fortress R', 'Airship Fortress', 'Daisy Hills', 'RMX Rainbow Road 1R/T', 'Tokyo Blur 3', 'Tokyo Blur 3R', 'Tokyo Blur', "Luigi's Mansion", "Luigi's Mansion T", 'Tokyo Blur R', 'DK Summit T', 'Choco Mountain', 'Dino Dino Jungle', 'Kalimari Desert 2R']

Wario__Cowboy__lv3_courses = ['Dino Dino Jungle', "Luigi's Mansion T"]

Wario__Cowboy__lv6_courses = ['Kalimari Desert 2R', 'Airship Fortress R']

Wario__Cowboy_ = race_tool('Wario__Cowboy_', 'High-End', Wario__Cowboy__3items, Wario__Cowboy__2items, Wario__Cowboy__lv3_courses, Wario__Cowboy__lv6_courses)


#Bowser_Jr__Pirate_
# https://game8.co/games/mariokarttour/archives/292672

Bowser_Jr__Pirate__3items = ['Airship Fortress R', 'Airship Fortress', 'Kalimari Desert 2', 'Neo Bowser City T', 'Tokyo Blur', 'Tokyo Blur R', "Bowser's Castle 1R/T", 'Cheep Cheep Lagoon R/T', 'Los Angeles Laps R/T', 'Ghost Valley 1R/T', "Bowser's Castle 2T", 'Vanilla Lake 1R', 'Vanilla Lake 1T', 'RMX Rainbow Road 1T', 'Paris Promenade 2']

Bowser_Jr__Pirate__2items = ['Frappe Snowland T', 'Neo Bowser City', 'Airship Fortress T', 'Tokyo Blur T', 'Koopa Troopa Beach 2', 'Koopa Troopa Beach 2R', 'Neo Bowser City R/T', 'Los Angeles Laps T', 'RMX Rainbow Road 1', 'RMX Rainbow Road 1R', 'Vanilla Lake 1', 'RMX Choco Island 2T', 'RMX Choco Island 2R', 'RMX Choco Island 2', 'Paris Promenade 2R']

Bowser_Jr__Pirate__lv3_courses = ['Neo Bowser City', 'Koopa Troopa Beach 2R']

Bowser_Jr__Pirate__lv6_courses = ['Frappe Snowland T', 'RMX Rainbow Road 1']

Bowser_Jr__Pirate_ = race_tool('Bowser_Jr__Pirate_', 'High-End', Bowser_Jr__Pirate__3items, Bowser_Jr__Pirate__2items, Bowser_Jr__Pirate__lv3_courses, Bowser_Jr__Pirate__lv6_courses)


#King_Bob_omb
# https://game8.co/games/mariokarttour/archives/292673

King_Bob_omb_3items = ["Bowser's Castle 1T", 'DK Pass', 'DK Pass T', "Luigi's Mansion R", 'Koopa Troopa Beach 2T', 'Sunset Wilds', "Rosalina's Ice World", "Bowser's Castle 2", "Bowser's Castle 2T", 'DK Summit', 'Choco Mountain', 'Donut Plains 2', 'Berlin Byways 2', 'Berlin Byways 2R/T', 'Airship Fortress T', 'Airship Fortress R']

King_Bob_omb_2items = ["Luigi's Mansion T", 'Tokyo Blur 3T', 'Tokyo Blur 3R', 'Koopa Troopa Beach 2R', "Bowser's Castle 1R/T", 'RMX Choco Island 1R', 'RMX Choco Island 1T', 'Los Angeles Laps', 'Los Angeles Laps R', 'Sunset Wilds T', 'Sunset Wilds R', 'Waluigi Pinball', 'Waluigi Pinball T', 'Shy Guy Bazaar R/T', 'Merry Mountain', 'Merry Mountain R', 'Choco Mountain T', 'Choco Mountain R', 'RMX Choco Island 2T', 'Donut Plains 2R', "Rosalina's Ice World R", 'Airship Fortress', 'Ghost Valley 1T', 'Ghost Valley 1R']

King_Bob_omb_lv3_courses = ['Toad Circuit T', 'Ghost Valley 1R']

King_Bob_omb_lv6_courses = ['Choco Mountain R', 'RMX Choco Island 1R']

King_Bob_omb = race_tool('King_Bob_omb', 'High-End', King_Bob_omb_3items, King_Bob_omb_2items, King_Bob_omb_lv3_courses, King_Bob_omb_lv6_courses)


#Daisy__Yukata_
# https://game8.co/games/mariokarttour/archives/293911

Daisy__Yukata__3items = ['Tokyo Blur 3R', 'Tokyo Blur 3', 'Waluigi Pinball R', 'Koopa Troopa Beach 2T', 'Ghost Valley 1R/T', 'Airship Fortress', 'Tokyo Blur', 'Koopa Troopa Beach R/T', 'Daisy Hills R/T', 'RMX Rainbow Road 1T', 'RMX Rainbow Road 1R', 'Shy Guy Bazaar R', 'Donut Plains 1R/T', 'Shy Guy Bazaar R/T']

Daisy__Yukata__2items = ['Tokyo Blur T', 'Koopa Troopa Beach 2R', 'Kalimari Desert R', 'London Loop R/T', 'London Loop R', 'London Loop R', 'Cheep Cheep Lagoon R/T', 'Los Angeles Laps', 'Los Angeles Laps T', 'Shy Guy Bazaar T', 'Shy Guy Bazaar', 'RMX Rainbow Road 1', 'Daisy Hills T', 'Tokyo Blur 3T', 'Koopa Troopa Beach 2']

Daisy__Yukata__lv3_courses = ['Koopa Troopa Beach 2R', 'Shy Guy Bazaar']

Daisy__Yukata__lv6_courses = ['Kalimari Desert', 'Koopa Troopa Beach 2']

Daisy__Yukata_ = race_tool('Daisy__Yukata_', 'High-End', Daisy__Yukata__3items, Daisy__Yukata__2items, Daisy__Yukata__lv3_courses, Daisy__Yukata__lv6_courses)


#Mario__SNES_
# https://game8.co/games/mariokarttour/archives/296084

Mario__SNES__3items = ['Tokyo Blur R/T', 'New York Minute 3', 'Yoshi Circuit', 'Yoshi Circuit T', 'Mario Circuit 1R/T', 'Berlin Byways 2T', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 1', 'Royal Raceway T', 'SNES Rainbow Road T', 'RMX Rainbow Road 2T', 'Ghost Valley 1R/T', 'Choco Island 2T']

Mario__SNES__2items = ['SNES Rainbow Road', 'SNES Rainbow Road R', 'Choco Island 2', 'Tokyo Blur T', 'New York Minute 3R/T', 'New York Minute 3R', 'Yoshi Circuit R', 'Los Angeles Laps', 'Los Angeles Laps R', 'Los Angeles Laps T', 'RMX Rainbow Road 1T', 'Mario Circuit 1', 'Mario Circuit 1T', 'Vanilla Lake 1T', 'RMX Mario Circuit 1', 'DK Summit T', 'Berlin Byways 2R']

Mario__SNES__lv3_courses = ['Mario Circuit 1', 'Yoshi Circuit R']

Mario__SNES__lv6_courses = ['Vanilla Lake 1T', 'RMX Rainbow Road 1T']

Mario__SNES_ = race_tool('Mario__SNES_', 'High-End', Mario__SNES__3items, Mario__SNES__2items, Mario__SNES__lv3_courses, Mario__SNES__lv6_courses)


#Donkey_Kong_Jr__SNES_
# https://game8.co/games/mariokarttour/archives/296085

Donkey_Kong_Jr__SNES__3items = ['Los Angeles Laps R', 'Los Angeles Laps T', 'Frappe Snowland R/T', 'Waluigi Pinball', 'Waluigi Pinball T', 'DK Summit R', 'Choco Mountain', 'Choco Mountain R', 'RMX Rainbow Road 1T', 'Royal Raceway R', "Bowser's Castle 1T", 'Choco Island 1R', 'Tokyo Blur T', 'Tokyo Blur R', 'Mario Circuit 3', 'Berlin Byways 2R/T']

Donkey_Kong_Jr__SNES__2items = ['SNES Rainbow Road T', 'SNES Rainbow Road R/T', 'Waluigi Pinball R', 'DS Rainbow Road R/T', 'DK Summit T', 'Choco Mountain T', 'RMX Rainbow Road 1R', 'Shy Guy Bazaar T', 'Shy Guy Bazaar R', 'Tokyo Blur R/T', 'Choco Island 1T', 'New York Minute 3', 'New York Minute 3R/T', 'New York Minute 3T', 'Mario Circuit 3R', 'Donut Plains 1R', 'Donut Plains 1', 'Los Angeles Laps R/T']

Donkey_Kong_Jr__SNES__lv3_courses = ['Donut Plains 1', 'Donut Plains 1R']

Donkey_Kong_Jr__SNES__lv6_courses = ['Waluigi Pinball R', 'RMX Rainbow Road 1R']

Donkey_Kong_Jr__SNES_ = race_tool('Donkey_Kong_Jr__SNES_', 'High-End', Donkey_Kong_Jr__SNES__3items, Donkey_Kong_Jr__SNES__2items, Donkey_Kong_Jr__SNES__lv3_courses, Donkey_Kong_Jr__SNES__lv6_courses)


#Mario__Sunshine_
# https://game8.co/games/mariokarttour/archives/297368

Mario__Sunshine__3items = ['Los Angeles Laps', 'RMX Rainbow Road 1T', 'Kalimari Desert 2', 'RMX Choco Island 1T', 'RMX Mario Circuit 1R/T', 'Donut Plains 2T', 'Koopa Troopa Beach', 'Koopa Troopa Beach T', 'Choco Island 2R', 'Choco Island 2T', 'RMX Rainbow Road 2T', 'Tokyo Blur R/T', 'Paris Promenade T', 'London Loop T', 'Vancouver Velocity T', 'New York Minute 3T']

Mario__Sunshine__2items = ['London Loop R/T', 'Vancouver Velocity', 'New York Minute 3', 'Donut Plains 2R', 'RMX Mario Circuit 1R', 'RMX Mario Circuit 1', 'Koopa Troopa Beach R', 'Mario Circuit R', 'Choco Island 2', 'SNES Rainbow Road R', 'Los Angeles Laps R/T', 'SNES Rainbow Road T', 'Los Angeles Laps R', 'RMX Choco Island 1', 'Cheep Cheep Lagoon R/T', 'Kalimari Desert 2T', 'RMX Rainbow Road 1', 'Choco Mountain T', 'Tokyo Blur T', 'Paris Promenade R']

Mario__Sunshine__lv3_courses = ['Kalimari Desert 2T', 'Choco Mountain T']

Mario__Sunshine__lv6_courses = ['Cheep Cheep Lagoon R/T', 'SNES Rainbow Road R']

Mario__Sunshine_ = race_tool('Mario__Sunshine_', 'High-End', Mario__Sunshine__3items, Mario__Sunshine__2items, Mario__Sunshine__lv3_courses, Mario__Sunshine__lv6_courses)


#Shy_Guy__Gold_
# https://game8.co/games/mariokarttour/archives/304783

Shy_Guy__Gold__3items = ['Shy Guy Bazaar T', 'Shy Guy Bazaar R', 'SNES Rainbow Road R/T', 'Maple Treeway T', 'Neo Bowser City R/T', 'Maple Treeway R', "Bowser's Castle 1R/T", "Rosalina's Ice World", 'DK Summit T', 'DS Rainbow Road T', 'Airship Fortress', 'Airship Fortress T', 'Vancouver Velocity R', 'Tokyo Blur T', 'Tokyo Blur R', 'Berlin Byways 2R', 'Sunset Wilds']

Shy_Guy__Gold__2items = ['Sunset Wilds R', 'Maple Treeway', "Bowser's Castle 2R/T", 'Shy Guy Bazaar', 'Frappe Snowland', 'Vancouver Velocity', 'DK Summit R', 'Choco Island 1R', 'New York Minute 3', 'New York Minute 3T', 'London Loop', 'London Loop R/T', 'Vancouver Velocity', 'Cheep Cheep Lagoon R', 'Berlin Byways 2', 'Kalimari Desert 2R', 'Kalimari Desert 2T']

Shy_Guy__Gold__lv3_courses = ['DS Rainbow Road R', 'Choco Island 1R']

Shy_Guy__Gold__lv6_courses = ['Shy Guy Bazaar', 'Maple Treeway']

Shy_Guy__Gold_ = race_tool('Shy_Guy__Gold_', 'High-End', Shy_Guy__Gold__3items, Shy_Guy__Gold__2items, Shy_Guy__Gold__lv3_courses, Shy_Guy__Gold__lv6_courses)


#King_Boo__Gold_
# https://game8.co/games/mariokarttour/archives/305314

King_Boo__Gold__3items = ['SNES Rainbow Road R/T', 'DS Rainbow Road', 'Merry Mountain R', 'Vanilla Lake 1T', 'RMX Rainbow Road 1', 'Koopa Troopa Beach 2R', 'Kalimari Desert 2T', 'Kalimari Desert 2R', 'Maple Treeway R', 'Choco Island 2', "Luigi's Mansion"]

King_Boo__Gold__2items = ['SNES Rainbow Road T', 'SNES Rainbow Road R', "Luigi's Mansion R", 'DS Rainbow Road R/T', 'Maple Treeway', 'Ghost Valley 1R/T', 'Airship Fortress', 'Airship Fortress R', "Bowser's Castle 1R/T", "Rosalina's Ice World R", 'Merry Mountain R', 'Merry Mountain', 'DK Summit', 'DS Rainbow Road R', 'Merry Mountain T', 'Paris Promenade 2', 'Donut Plains 2R', 'RMX Rainbow Road 2R', 'Koopa Troopa Beach 2T', 'Sunset Wilds', 'Kalimari Desert 2']

King_Boo__Gold__lv3_courses = ['Airship Fortress R', 'Airship Fortress']

King_Boo__Gold__lv6_courses = ['SNES Rainbow Road T', 'Maple Treeway']

King_Boo__Gold_ = race_tool('King_Boo__Gold_', 'High-End', King_Boo__Gold__3items, King_Boo__Gold__2items, King_Boo__Gold__lv3_courses, King_Boo__Gold__lv6_courses)


#Mario__Halloween_
# https://game8.co/games/mariokarttour/archives/305316

Mario__Halloween__3items = ['RMX Mario Circuit 1R/T', 'Sunset Wilds R/T', 'Mario Circuit 1', 'Mario Circuit 1R', 'Mario Circuit 3', 'Neo Bowser City R', 'Mario Circuit T', 'DK Summit R', 'Merry Mountain T', 'Maple Treeway', "Luigi's Mansion R", "Luigi's Mansion T", 'RMX Rainbow Road 2T']

Mario__Halloween__2items = ['Mario Circuit 1R/T', 'Donut Plains 2R', 'Mario Circuit 1T', 'Berlin Byways 2R', 'Berlin Byways 2', 'Mario Circuit', 'Mario Circuit R', 'Neo Bowser City T', 'Sunset Wilds', 'Sunset Wilds T', 'DK Summit', 'Merry Mountain', 'RMX Mario Circuit 1', 'DS Rainbow Road R/T', 'Maple Treeway T', 'Maple Treeway R', 'Kalimari Desert', 'Frappe Snowland', 'Frappe Snowland R']

Mario__Halloween__lv3_courses = ['Kalimari Desert', 'Frappe Snowland']

Mario__Halloween__lv6_courses = ['DS Rainbow Road R/T', 'Maple Treeway T']

Mario__Halloween_ = race_tool('Mario__Halloween_', 'High-End', Mario__Halloween__3items, Mario__Halloween__2items, Mario__Halloween__lv3_courses, Mario__Halloween__lv6_courses)


#Peach__Halloween_
# https://game8.co/games/mariokarttour/archives/305315

Peach__Halloween__3items = ['SNES Rainbow Road R/T', 'Neo Bowser City R/T', 'Paris Promenade 2T', 'Royal Raceway', 'Royal Raceway T', "Rosalina's Ice World R", 'Berlin Byways 2', 'Merry Mountain', 'Maple Treeway T', "Luigi's Mansion T", 'Frappe Snowland', 'Airship Fortress', 'RMX Rainbow Road 2', 'Mario Circuit 2T']

Peach__Halloween__2items = ['Sunset Wilds R/T', 'RMX Rainbow Road 1R/T', 'Paris Promenade 2', 'Waluigi Pinball R/T', 'Royal Raceway R', 'Sunset Wilds T', 'Sunset Wilds R', "Rosalina's Ice World", 'Berlin Byways 2R', 'Merry Mountain R', 'DS Rainbow Road R', 'Maple Treeway', "Luigi's Mansion R", 'Frappe Snowland R', 'DS Rainbow Road R/T', 'Maple Treeway R', 'Airship Fortress R', 'Mario Circuit 2R', 'Mario Circuit 2']

Peach__Halloween__lv3_courses = ['DS Rainbow Road R/T', 'Maple Treeway R']

Peach__Halloween__lv6_courses = ["Luigi's Mansion R", 'Frappe Snowland R']

Peach__Halloween_ = race_tool('Peach__Halloween_', 'High-End', Peach__Halloween__3items, Peach__Halloween__2items, Peach__Halloween__lv3_courses, Peach__Halloween__lv6_courses)


#Peach__Explorer_
# https://game8.co/games/mariokarttour/archives/305956

Peach__Explorer__3items = ['Sunset Wilds R/T', 'Dino Dino Jungle R/T', 'Kalimari Desert R/T', "Rosalina's Ice World", 'Maple Treeway R', 'Sunset Wilds', 'Kalimari Desert 2', 'Royal Raceway T', 'Kalimari Desert 2T', 'Dino Dino Jungle R']

Peach__Explorer__2items = ['Mario Circuit R/T', 'Toad Circuit R/T', 'Vanilla Lake 1R/T', 'Choco Mountain R', 'Yoshi Circuit', 'Merry Mountain T', 'Maple Treeway T', 'Merry Mountain R', 'Kalimari Desert 2R', 'Dino Dino Jungle', 'Dino Dino Jungle T', 'Royal Raceway', 'Sunset Wilds T']

Peach__Explorer__lv3_courses = ['Kalimari Desert 2R', 'Dino Dino Jungle T']

Peach__Explorer__lv6_courses = ['Sunset Wilds T', 'Dino Dino Jungle']

Peach__Explorer_ = race_tool('Peach__Explorer_', 'High-End', Peach__Explorer__3items, Peach__Explorer__2items, Peach__Explorer__lv3_courses, Peach__Explorer__lv6_courses)


#Builder_Luigi
# https://game8.co/games/mariokarttour/archives/309241

Builder_Luigi_3items = ['Paris Promenade 2T', "Rosalina's Ice World T", 'Berlin Byways 2T', 'Daisy Hills T', 'Dino Dino Jungle T', 'Shy Guy Bazaar R/T', 'RMX Mario Circuit 1T', 'Choco Island 1T', 'Maple Treeway T', 'Waluigi Pinball T', 'Airship Fortress T', 'RMX Rainbow Road 1R/T', 'Sunset Wilds R/T', 'Cheep Cheep Lagoon R/T', 'Koopa Troopa Beach R/T']

Builder_Luigi_2items = ['Ghost Valley 1R/T', 'RMX Mario Circuit 1R/T', 'Vanilla Lake 1R/T', 'Yoshi Circuit R/T', 'Shy Guy Bazaar T', "Bowser's Castle 2T", 'Berlin Byways 2R/T', 'DK Summit T', 'RMX Choco Island 2T', 'DS Rainbow Road T', 'Merry Mountain T', 'Kalimari Desert T', 'Koopa Troopa Beach 2T', "Luigi's Mansion R/T", 'Toad Circuit R/T']

Builder_Luigi_lv3_courses = ['Vanilla Lake 1R/T', 'Yoshi Circuit R/T']

Builder_Luigi_lv6_courses = ["Luigi's Mansion R/T", 'Ghost Valley 1R/T']

Builder_Luigi = race_tool('Builder_Luigi', 'High-End', Builder_Luigi_3items, Builder_Luigi_2items, Builder_Luigi_lv3_courses, Builder_Luigi_lv6_courses)


#Bowser__Santa_
# https://game8.co/games/mariokarttour/archives/311464

Bowser__Santa__3items = ["Bowser's Castle 2R", 'Royal Raceway', 'Frappe Snowland', 'Merry Mountain', 'Maple Treeway', 'Maple Treeway T', 'Waluigi Pinball T', 'RMX Rainbow Road 2', 'RMX Rainbow Road 1R/T', 'Vanilla Lake 1', 'Shy Guy Bazaar', 'Vanilla Lake 1R']

Bowser__Santa__2items = ["Bowser's Castle 2", "Rosalina's Ice World", "Rosalina's Ice World R", 'DK Summit', 'DK Summit R', 'Merry Mountain R', 'DS Rainbow Road T', 'Shy Guy Bazaar R/T', 'DK Pass R/T', 'Dino Dino Jungle R/T', 'SNES Rainbow Road T', 'SNES Rainbow Road R/T', 'Donut Plains 2', 'RMX Rainbow Road 2T', 'Donut Plains 2R', 'RMX Rainbow Road 2R', 'Waluigi Pinball R']

Bowser__Santa__lv3_courses = ['DS Rainbow Road T', 'Dino Dino Jungle R/T']

Bowser__Santa__lv6_courses = ['Merry Mountain R', 'Shy Guy Bazaar R/T']

Bowser__Santa_ = race_tool('Bowser__Santa_', 'High-End', Bowser__Santa__3items, Bowser__Santa__2items, Bowser__Santa__lv3_courses, Bowser__Santa__lv6_courses)


#Fire_Rosalina
# https://game8.co/games/mariokarttour/archives/314372

Fire_Rosalina_3items = ["Rosalina's Ice World", 'RMX Rainbow Road 1', 'Sunset Wilds T', 'RMX Rainbow Road 1R/T', 'Maple Treeway T', 'Kalimari Desert 2R', 'Yoshi Circuit', 'Airship Fortress R', 'Airship Fortress T', 'RMX Rainbow Road 2R']

Fire_Rosalina_2items = ['Donut Plains 2T', "Rosalina's Ice World R", 'Merry Mountain T', 'Merry Mountain', 'SNES Rainbow Road', 'RMX Rainbow Road 1R', "Bowser's Castle 2", 'Kalimari Desert 2', "Bowser's Castle 2T", 'Berlin Byways 2T', 'Berlin Byways 2R/T', 'DK Summit', 'DK Summit T', 'RMX Rainbow Road 2', 'RMX Rainbow Road 2T', 'Vanilla Lake 1R', 'Vanilla Lake 1T']

Fire_Rosalina_lv3_courses = ["Rosalina's Ice World R", 'Merry Mountain']

Fire_Rosalina_lv6_courses = ['SNES Rainbow Road R', "Bowser's Castle 2"]

Fire_Rosalina = race_tool('Fire_Rosalina', 'High-End', Fire_Rosalina_3items, Fire_Rosalina_2items, Fire_Rosalina_lv3_courses, Fire_Rosalina_lv6_courses)


#Lakitu__Party_Time_
# https://game8.co/games/mariokarttour/archives/315369

Lakitu__Party_Time__3items = ['Merry Mountain T', 'Paris Promenade 2T', 'Paris Promenade 2R', 'Donut Plains 2T', 'RMX Rainbow Road 2', 'Waluigi Pinball', 'Waluigi Pinball R', 'RMX Rainbow Road 1R', "Rosalina's Ice World", 'Yoshi Circuit T', 'Kalimari Desert T', "Bowser's Castle 2T", 'RMX Choco Island 2T', 'Mario Circuit 3T', 'Mario Circuit 3R', 'Berlin Byways 2R']

Lakitu__Party_Time__2items = ['Mario Circuit 3', 'DK Summit R', "Bowser's Castle 2R", 'RMX Choco Island 2R', 'RMX Rainbow Road 2R', 'Kalimari Desert', 'Waluigi Pinball T', 'RMX Rainbow Road 1T', "Rosalina's Ice World T", 'Shy Guy Bazaar', "Rosalina's Ice World R", 'Merry Mountain R', 'Donut Plains 2', 'Berlin Byways 2']

Lakitu__Party_Time__lv3_courses = ['RMX Rainbow Road 2R', 'RMX Rainbow Road 1T']

Lakitu__Party_Time__lv6_courses = ['Kalimari Desert', "Rosalina's Ice World R"]

Lakitu__Party_Time_ = race_tool('Lakitu__Party_Time_', 'High-End', Lakitu__Party_Time__3items, Lakitu__Party_Time__2items, Lakitu__Party_Time__lv3_courses, Lakitu__Party_Time__lv6_courses)


#Luigi__Lederhosen_
# https://game8.co/games/mariokarttour/archives/316097

Luigi__Lederhosen__3items = ['Shy Guy Bazaar', 'Merry Mountain', 'Donut Plains 2R', 'Mario Circuit 1T', 'Choco Mountain', 'DK Summit T', 'Choco Mountain R', 'RMX Choco Island 2T', 'Airship Fortress', 'Kalimari Desert 2', 'Berlin Byways 2', 'Berlin Byways 2R/T', 'Mario Circuit 1T']

Luigi__Lederhosen__2items = ['Shy Guy Bazaar T', 'Donut Plains 2', 'Donut Plains 2T', 'Berlin Byways 2R', 'Mario Circuit 1', 'Waluigi Pinball', 'Waluigi Pinball T', 'Kalimari Desert 2T', 'Airship Fortress T', 'DK Summit R', 'Choco Island 1', 'Sunset Wilds R/T', 'RMX Choco Island 2R']

Luigi__Lederhosen__lv3_courses = ['Waluigi Pinball T', 'Airship Fortress T']

Luigi__Lederhosen__lv6_courses = ['Mario Circuit 1', 'Waluigi Pinball']

Luigi__Lederhosen_ = race_tool('Luigi__Lederhosen_', 'High-End', Luigi__Lederhosen__3items, Luigi__Lederhosen__2items, Luigi__Lederhosen__lv3_courses, Luigi__Lederhosen__lv6_courses)


#Cat_Peach
# https://game8.co/games/mariokarttour/archives/317071

Cat_Peach_3items = ['Donut Plains 2', 'RMX Rainbow Road 1R/T', 'Merry Mountain', 'Kalimari Desert 2', 'Maple Treeway', "Rosalina's Ice World T", 'Sunset Wilds R/T', 'RMX Rainbow Road 2', 'RMX Choco Island 2']

Cat_Peach_2items = ['Royal Raceway', 'Royal Raceway R', 'Donut Plains 2T', 'Maple Treeway T', 'Merry Mountain', 'Mario Circuit 2T']

Cat_Peach_lv3_courses = ['Royal Raceway R', 'Maple Treeway T']

Cat_Peach_lv6_courses = ['Donut Plains 2T', 'Merry Mountain T']

Cat_Peach = race_tool('Cat_Peach', 'High-End', Cat_Peach_3items, Cat_Peach_2items, Cat_Peach_lv3_courses, Cat_Peach_lv6_courses)


#Cat_Toad
# https://game8.co/games/mariokarttour/archives/317070

Cat_Toad_3items = ['Donut Plains 2R', 'RMX Rainbow Road 1R/T', 'Paris Promenade 2R', 'Paris Promenade 2R', 'Sunset Wilds R/T', "Rosalina's Ice World R", "Bowser's Castle 2R", 'Dino Dino Jungle', 'Merry Mountain R']

Cat_Toad_2items = ['Shy Guy Bazaar T', 'Shy Guy Bazaar R', 'Koopa Troopa Beach R/T', 'Donut Plains 2', 'Paris Promenade 2', 'Merry Mountain', 'Yoshi Circuit R', "Rosalina's Ice World", 'Dino Dino Jungle T', 'Donut Plains 2T']

Cat_Toad_lv3_courses = ['Shy Guy Bazaar R', 'Paris Promenade 2']

Cat_Toad_lv6_courses = ['Donut Plains 2', 'Merry Mountain']

Cat_Toad = race_tool('Cat_Toad', 'High-End', Cat_Toad_3items, Cat_Toad_2items, Cat_Toad_lv3_courses, Cat_Toad_lv6_courses)


#Pauline__Rose_
# https://game8.co/games/mariokarttour/archives/317797

Pauline__Rose__3items = ['RMX Choco Island 2T', 'Donut Plains 2T', 'Choco Island 1T', 'Donut Plains 2R', 'DS Rainbow Road R/T', 'Maple Treeway', 'RMX Rainbow Road 2', 'RMX Rainbow Road 2T']

Pauline__Rose__2items = ['Frappe Snowland T', 'Choco Island 1', 'RMX Choco Island 2', 'Donut Plains 2', 'Choco Mountain', 'Choco Mountain R', 'RMX Choco Island 2R', 'Maple Treeway R']

Pauline__Rose__lv3_courses = ['Choco Island 1', 'Maple Treeway R']

Pauline__Rose__lv6_courses = ['Donut Plains 2', 'RMX Choco Island 2']

Pauline__Rose_ = race_tool('Pauline__Rose_', 'High-End', Pauline__Rose__3items, Pauline__Rose__2items, Pauline__Rose__lv3_courses, Pauline__Rose__lv6_courses)


#Penguin_Toad
# https://game8.co/games/mariokarttour/archives/321004

Penguin_Toad_3items = ['DK Summit T', 'Vanilla Lake 1T', 'RMX Rainbow Road 2T', 'RMX Choco Island 2T', 'Frappe Snowland T', 'Vanilla Lake 1R', 'DK Summit R', "Rosalina's Ice World"]

Penguin_Toad_2items = ['DK Summit R', 'Frappe Snowland', 'Frappe Snowland T', 'Vanilla Lake 1R', "Rosalina's Ice World", "Rosalina's Ice World T"]

Penguin_Toad_lv3_courses = []

Penguin_Toad_lv6_courses = []

Penguin_Toad = race_tool('Penguin_Toad', 'High-End', Penguin_Toad_3items, Penguin_Toad_2items, Penguin_Toad_lv3_courses, Penguin_Toad_lv6_courses)


#Mario__Racing_
# https://game8.co/games/mariokarttour/archives/322565

Mario__Racing__3items = ['Mario Circuit 1R', 'RMX Mario Circuit 1R/T', 'Mario Circuit 1R/T', 'Toad Circuit T', 'Tokyo Blur 4']

Mario__Racing__2items = ['Mario Circuit 1', 'RMX Mario Circuit 1T', 'RMX Mario Circuit 1', 'Toad Circuit R', 'Tokyo Blur 4R/T', 'Tokyo Blur 4R']

Mario__Racing__lv3_courses = ['Toad Circuit R', 'RMX Mario Circuit 1T']

Mario__Racing__lv6_courses = ['Mario Circuit 1', 'Tokyo Blur 4R/T']

Mario__Racing_ = race_tool('Mario__Racing_', 'High-End', Mario__Racing__3items, Mario__Racing__2items, Mario__Racing__lv3_courses, Mario__Racing__lv6_courses)


#Penguin_Luigi
# https://game8.co/games/mariokarttour/archives/275773

Penguin_Luigi_3items = ['DK Pass R/T', 'London Loop R', 'Mario Circuit 2R/T', 'RMX Rainbow Road 1R/T', 'Waluigi Pinball R/T', 'DK Pass', 'Frappe Snowland T', 'Rock Rock Mountain R', 'Donut Plains 2T', "Rosalina's Ice World T", 'Mario Circuit R/T', 'RMX Choco Island 1R', 'DK Pass R', 'Merry Mountain', 'RMX Rainbow Road 1T', 'RMX Mario Circuit 1R', 'Koopa Troopa Beach 2', 'Mario Circuit 2R/T', 'Berlin Byways 2T', 'Berlin Byways 2R', 'Vanilla Lake 1']

Penguin_Luigi_2items = ['London Loop', 'London Loop R/T', 'DS Rainbow Road R/T', 'Royal Raceway R', 'Paris Promenade T', 'Paris Promenade R/T', "Luigi's Mansion R/T", 'Donut Plains 2R', 'Paris Promenade 2T', 'Frappe Snowland R/T', 'Vancouver Velocity R', "Luigi's Mansion R", 'Rock Rock Mountain', 'Frappe Snowland R', 'Koopa Troopa Beach 2T', 'RMX Rainbow Road 2R']

Penguin_Luigi_lv3_courses = ["Luigi's Mansion R", 'DS Rainbow Road R/T']

Penguin_Luigi_lv6_courses = ['Rock Rock Mountain', 'Koopa Troopa Beach 2T']

Penguin_Luigi = race_tool('Penguin_Luigi', 'High-End', Penguin_Luigi_3items, Penguin_Luigi_2items, Penguin_Luigi_lv3_courses, Penguin_Luigi_lv6_courses)


#Diddy_Kong
# https://game8.co/games/mariokarttour/archives/270447

Diddy_Kong_3items = ['Dino Dino Jungle R', 'Toad Circuit R', 'Rock Rock Mountain R', 'New York Minute 2R/T']

Diddy_Kong_2items = ['Neo Bowser City R/T', 'Choco Island 2T', 'Mario Circuit 3', 'Tokyo Blur R/T', 'London Loop T', 'New York Minute 2', 'Koopa Troopa Beach R', 'Koopa Troopa Beach T', 'Rock Rock Mountain', 'New York Minute R', 'Waluigi Pinball R', 'New York Minute R/T', 'Tokyo Blur 2', 'Mario Circuit 2R/T']

Diddy_Kong_lv3_courses = ['Neo Bowser City R/T']

Diddy_Kong_lv6_courses = ['Koopa Troopa Beach R']

Diddy_Kong = race_tool('Diddy_Kong', 'Super', Diddy_Kong_3items, Diddy_Kong_2items, Diddy_Kong_lv3_courses, Diddy_Kong_lv6_courses)


#Donkey_Kong
# https://game8.co/games/mariokarttour/archives/270446

Donkey_Kong_3items = ['Dino Dino Jungle', 'Rock Rock Mountain', 'Waluigi Pinball R', 'New York Minute 3R', 'DK Pass']

Donkey_Kong_2items = ['RMX Rainbow Road 1T', "Bowser's Castle 2R/T", 'Vanilla Lake 1R/T', 'DK Pass T', 'New York Minute 3R/T', 'Dino Dino Jungle R', 'Dino Dino Jungle T', 'Tokyo Blur R', 'RMX Choco Island 2T', 'Koopa Troopa Beach R', 'Rock Rock Mountain R', 'New York Minute', 'New York Minute T', 'New York Minute 3', 'Merry Mountain R']

Donkey_Kong_lv3_courses = ['Vanilla Lake 1R/T']

Donkey_Kong_lv6_courses = ['RMX Rainbow Road 1T']

Donkey_Kong = race_tool('Donkey_Kong', 'Super', Donkey_Kong_3items, Donkey_Kong_2items, Donkey_Kong_lv3_courses, Donkey_Kong_lv6_courses)


#Bowser
# https://game8.co/games/mariokarttour/archives/270445

Bowser_3items = ['Dino Dino Jungle T', "Bowser's Castle 1", "Bowser's Castle 1T", "Bowser's Castle 2R", "Bowser's Castle 2R/T", 'DS Rainbow Road T', 'Neo Bowser City']

Bowser_2items = ['RMX Rainbow Road 1T', 'Kalimari Desert', "Bowser's Castle 2", 'SNES Rainbow Road T', "Bowser's Castle 1R/T", "Bowser's Castle 1R", 'Rock Rock Mountain R', 'New York Minute T', 'Kalimari Desert R/T', 'DS Rainbow Road R']

Bowser_lv3_courses = ['Kalimari Desert R/T']

Bowser_lv6_courses = ["Bowser's Castle 1R"]

Bowser = race_tool('Bowser', 'Super', Bowser_3items, Bowser_2items, Bowser_lv3_courses, Bowser_lv6_courses)


#Toadette
# https://game8.co/games/mariokarttour/archives/270444

Toadette_3items = ['Mario Circuit 3R', 'Daisy Hills R', 'Toad Circuit']

Toadette_2items = ['Mario Circuit 1R/T', 'Tokyo Blur 2R/T', 'Toad Circuit R/T', 'RMX Rainbow Road 1', 'Kalimari Desert 2T', 'Mario Circuit', 'Toad Circuit T', 'Maple Treeway T', 'Donut Plains 1', 'Paris Promenade', 'Daisy Hills', 'Mario Circuit 3', 'Koopa Troopa Beach', 'Mario Circuit T', 'Toad Circuit R', 'Mario Circuit 1R/T', 'Choco Island 1R', 'DS Rainbow Road R', 'DK Summit R']

Toadette_lv3_courses = ['Toad Circuit R/T']

Toadette_lv6_courses = ['Mario Circuit T']

Toadette = race_tool('Toadette', 'Super', Toadette_3items, Toadette_2items, Toadette_lv3_courses, Toadette_lv6_courses)


#Toad
# https://game8.co/games/mariokarttour/archives/270443

Toad_3items = ['Mario Circuit R', 'Mario Circuit 1R/T', 'Toad Circuit R/T', 'Donut Plains 1R', 'Toad Circuit', 'Rock Rock Mountain T']

Toad_2items = ["Luigi's Mansion", 'Koopa Troopa Beach', 'Paris Promenade R', 'Toad Circuit T', 'Mario Circuit 3', 'Mario Circuit 1', 'Mario Circuit 1T', 'Ghost Valley 1', 'Ghost Valley 1R', 'New York Minute 2T', 'London Loop 2R', "Rosalina's Ice World", 'Frappe Snowland R']

Toad_lv3_courses = ['Mario Circuit 1T']

Toad_lv6_courses = ['Koopa Troopa Beach']

Toad = race_tool('Toad', 'Super', Toad_3items, Toad_2items, Toad_lv3_courses, Toad_lv6_courses)


#Daisy
# https://game8.co/games/mariokarttour/archives/270442

Daisy_3items = ['RMX Choco Island 1T', 'Daisy Hills', 'Daisy Hills T', 'Cheep Cheep Lagoon R', 'Shy Guy Bazaar R']

Daisy_2items = ['Daisy Hills R/T', 'Kalimari Desert 2', 'Yoshi Circuit T', 'Mario Circuit T', 'Toad Circuit', 'Shy Guy Bazaar T', 'Paris Promenade R', 'Paris Promenade 2', 'New York Minute 3', 'New York Minute 3R/T', 'Shy Guy Bazaar R/T', 'DK Summit']

Daisy_lv3_courses = ['Shy Guy Bazaar R/T']

Daisy_lv6_courses = ['Shy Guy Bazaar T']

Daisy = race_tool('Daisy', 'Super', Daisy_3items, Daisy_2items, Daisy_lv3_courses, Daisy_lv6_courses)


#Yoshi
# https://game8.co/games/mariokarttour/archives/270441

Yoshi_3items = ['RMX Choco Island 1T', 'Yoshi Circuit R/T', 'Rock Rock Mountain', 'Yoshi Circuit', 'Yoshi Circuit T']

Yoshi_2items = ['London Loop 2R', 'New York Minute 2', 'Dino Dino Jungle', 'Dino Dino Jungle R', 'Yoshi Circuit R', 'Maple Treeway R', 'Maple Treeway', 'DK Pass R', 'London Loop R', 'Frappe Snowland R/T', 'Royal Raceway']

Yoshi_lv3_courses = ['Frappe Snowland R/T']

Yoshi_lv6_courses = ['Dino Dino Jungle R']

Yoshi = race_tool('Yoshi', 'Super', Yoshi_3items, Yoshi_2items, Yoshi_lv3_courses, Yoshi_lv6_courses)


#Peach
# https://game8.co/games/mariokarttour/archives/270440

Peach_3items = ['Mario Circuit 1T', "Luigi's Mansion R", 'Mario Circuit 3R/T', 'Koopa Troopa Beach R', 'Koopa Troopa Beach T', 'Yoshi Circuit R']

Peach_2items = ['RMX Rainbow Road 2R', 'Kalimari Desert 2T', 'Toad Circuit T', 'Mario Circuit R', 'Mario Circuit 1R', 'Cheep Cheep Lagoon T', 'Shy Guy Bazaar', 'Mario Circuit', 'London Loop R/T', 'Paris Promenade', 'Frappe Snowland R/T', 'Vancouver Velocity R/T', 'Paris Promenade 2']

Peach_lv3_courses = ['Frappe Snowland R/T']

Peach_lv6_courses = ['Mario Circuit R']

Peach = race_tool('Peach', 'Super', Peach_3items, Peach_2items, Peach_lv3_courses, Peach_lv6_courses)


#Mario
# https://game8.co/games/mariokarttour/archives/270432

Mario_3items = ['RMX Rainbow Road 2R', 'Mario Circuit 3R/T', 'Mario Circuit T', 'Koopa Troopa Beach', 'Mario Circuit 1', 'Cheep Cheep Lagoon T']

Mario_2items = ['RMX Rainbow Road 2T', 'Koopa Troopa Beach R', 'Yoshi Circuit R', 'Mario Circuit 1R', 'Shy Guy Bazaar R', 'Yoshi Circuit', 'DK Pass', 'London Loop R', 'Yoshi Circuit R/T', 'London Loop R', 'New York Minute 3R']

Mario_lv3_courses = ['Yoshi Circuit R/T']

Mario_lv6_courses = ['Koopa Troopa Beach R']

Mario = race_tool('Mario', 'Super', Mario_3items, Mario_2items, Mario_lv3_courses, Mario_lv6_courses)


#Rosalina
# https://game8.co/games/mariokarttour/archives/270725

Rosalina_3items = ['RMX Rainbow Road 2R', 'Cheep Cheep Lagoon', 'Paris Promenade R/T', 'DK Pass R', 'SNES Rainbow Road R/T', 'New York Minute 3T', 'Mario Circuit R', 'SNES Rainbow Road']

Rosalina_2items = ['RMX Rainbow Road 1', 'RMX Rainbow Road 1R', 'RMX Rainbow Road 2', 'Mario Circuit 3T', 'Paris Promenade R', 'Donut Plains 1R/T', 'DS Rainbow Road', 'New York Minute 3R/T', 'Neo Bowser City R', 'SNES Rainbow Road R', 'Mario Circuit 2', 'Choco Island 2R', 'London Loop 2T']

Rosalina_lv3_courses = ['SNES Rainbow Road R']

Rosalina_lv6_courses = ['Mario Circuit 3T']

Rosalina = race_tool('Rosalina', 'Super', Rosalina_3items, Rosalina_2items, Rosalina_lv3_courses, Rosalina_lv6_courses)


#Wario
# https://game8.co/games/mariokarttour/archives/270724

Wario_3items = ['DK Pass T', 'Choco Island 2T', 'Los Angeles Laps R', 'Kalimari Desert R', 'Kalimari Desert T', 'Koopa Troopa Beach 2R']

Wario_2items = ['Neo Bowser City', 'RMX Rainbow Road 1R', 'Rock Rock Mountain T', 'Vanilla Lake 1R/T', 'Dino Dino Jungle T', "Bowser's Castle 2R/T", 'Los Angeles Laps', 'Choco Island 2', 'Los Angeles Laps R/T', 'Los Angeles Laps T', 'Mario Circuit 3', 'Mario Circuit 3R', 'New York Minute 3R', 'New York Minute 2R', 'New York Minute 2T', "Luigi's Mansion R/T", 'Tokyo Blur 2R']

Wario_lv3_courses = ["Luigi's Mansion R/T"]

Wario_lv6_courses = ["Bowser's Castle 2R/T"]

Wario = race_tool('Wario', 'Super', Wario_3items, Wario_2items, Wario_lv3_courses, Wario_lv6_courses)


#Bowser_Jr
# https://game8.co/games/mariokarttour/archives/270723

Bowser_Jr_3items = ['Neo Bowser City', 'Neo Bowser City T', "Bowser's Castle 1R", "Bowser's Castle 2R/T", 'Choco Island 2R', 'Paris Promenade T', 'Cheep Cheep Lagoon T', 'Kalimari Desert R/T', 'Vanilla Lake 1T']

Bowser_Jr_2items = ["Bowser's Castle 1T", 'Mario Circuit 2T', 'Cheep Cheep Lagoon', 'Neo Bowser City R', 'DS Rainbow Road R']

Bowser_Jr_lv3_courses = ["Bowser's Castle 1T"]

Bowser_Jr_lv6_courses = ['Mario Circuit 2T']

Bowser_Jr = race_tool('Bowser_Jr', 'Super', Bowser_Jr_3items, Bowser_Jr_2items, Bowser_Jr_lv3_courses, Bowser_Jr_lv6_courses)


#Lakitu
# https://game8.co/games/mariokarttour/archives/270722

Lakitu_3items = ['Toad Circuit T', 'Mario Circuit 2T', 'London Loop 2R', 'Tokyo Blur 3R', 'Ghost Valley 1T', 'Waluigi Pinball T', 'Paris Promenade T', 'Mario Circuit 3T', 'London Loop R', 'Merry Mountain R']

Lakitu_2items = ['Dino Dino Jungle R', 'Rock Rock Mountain R', 'Tokyo Blur', 'Tokyo Blur T', 'Cheep Cheep Lagoon', 'Mario Circuit 2', 'London Loop 2', "Bowser's Castle 2R/T", 'RMX Choco Island 2R', 'Tokyo Blur 2T']

Lakitu_lv3_courses = ["Bowser's Castle 2R/T"]

Lakitu_lv6_courses = ['Mario Circuit 2']

Lakitu = race_tool('Lakitu', 'Super', Lakitu_3items, Lakitu_2items, Lakitu_lv3_courses, Lakitu_lv6_courses)


#Luigi
# https://game8.co/games/mariokarttour/archives/271645

Luigi_3items = ["Luigi's Mansion", "Luigi's Mansion T", 'Ghost Valley 1', 'DK Pass T', 'Cheep Cheep Lagoon T', 'RMX Mario Circuit 1R/T', 'Waluigi Pinball R/T', 'New York Minute 3R']

Luigi_2items = ['RMX Rainbow Road 2T', 'RMX Rainbow Road 2', "Luigi's Mansion R", 'Waluigi Pinball R', "Luigi's Mansion R/T", 'Paris Promenade 2T', 'Paris Promenade 2', 'New York Minute 2R', 'New York Minute 3', "Rosalina's Ice World R"]

Luigi_lv3_courses = ["Luigi's Mansion R/T"]

Luigi_lv6_courses = ['Waluigi Pinball R']

Luigi = race_tool('Luigi', 'Super', Luigi_3items, Luigi_2items, Luigi_lv3_courses, Luigi_lv6_courses)


#Waluigi
# https://game8.co/games/mariokarttour/archives/271646

Waluigi_3items = ['Neo Bowser City R', 'Rock Rock Mountain', "Bowser's Castle 1R/T", 'Los Angeles Laps T', 'Shy Guy Bazaar R/T', 'Waluigi Pinball', 'DS Rainbow Road R']

Waluigi_2items = ['RMX Rainbow Road 1R', 'Waluigi Pinball R', 'Kalimari Desert 2R', 'Waluigi Pinball T', 'Kalimari Desert 2', 'Kalimari Desert', 'London Loop 2T', 'Paris Promenade', 'Waluigi Pinball R/T', 'New York Minute 2R/T']

Waluigi_lv3_courses = ['Waluigi Pinball R']

Waluigi_lv6_courses = ['Kalimari Desert']

Waluigi = race_tool('Waluigi', 'Super', Waluigi_3items, Waluigi_2items, Waluigi_lv3_courses, Waluigi_lv6_courses)


#King_Boo
# https://game8.co/games/mariokarttour/archives/271647

King_Boo_3items = ['Ghost Valley 1R', 'Tokyo Blur 2R', 'Shy Guy Bazaar', "Luigi's Mansion", "Luigi's Mansion R/T", 'Ghost Valley 1R/T']

King_Boo_2items = ['DK Pass R', 'Choco Island 2T', 'Waluigi Pinball', 'Ghost Valley 1', 'Ghost Valley 1T', "Bowser's Castle 2", 'Paris Promenade T', 'Airship Fortress R', 'Airship Fortress', 'Frappe Snowland T']

King_Boo_lv3_courses = ['Choco Island 2T']

King_Boo_lv6_courses = ["Bowser's Castle 2"]

King_Boo = race_tool('King_Boo', 'Super', King_Boo_3items, King_Boo_2items, King_Boo_lv3_courses, King_Boo_lv6_courses)


#Toad__Pit_Crew_
# https://game8.co/games/mariokarttour/archives/272257

Toad__Pit_Crew__3items = ['Mario Circuit 1', 'Mario Circuit 2', 'Mario Circuit 2T', 'Mario Circuit T', 'Mario Circuit 3', 'Tokyo Blur', "Rosalina's Ice World R"]

Toad__Pit_Crew__2items = ['Merry Mountain R', 'Yoshi Circuit', 'Mario Circuit 3T', 'Toad Circuit', 'Toad Circuit T', 'Paris Promenade T', 'Mario Circuit 3R/T', 'RMX Mario Circuit 1R/T', 'Sunset Wilds', 'Tokyo Blur T', 'Tokyo Blur R', 'RMX Choco Island 2', 'Tokyo Blur 3T', 'RMX Rainbow Road 1T']

Toad__Pit_Crew__lv3_courses = ['Mario Circuit 3R/T']

Toad__Pit_Crew__lv6_courses = ['RMX Mario Circuit 1R/T']

Toad__Pit_Crew_ = race_tool('Toad__Pit_Crew_', 'Super', Toad__Pit_Crew__3items, Toad__Pit_Crew__2items, Toad__Pit_Crew__lv3_courses, Toad__Pit_Crew__lv6_courses)


#Black_Shy_Guy
# https://game8.co/games/mariokarttour/archives/273757

Black_Shy_Guy_3items = ['Sunset Wilds R', 'DK Pass R', 'Cheep Cheep Lagoon', 'Ghost Valley 1T', 'Ghost Valley 1R/T', 'Mario Circuit 1R']

Black_Shy_Guy_2items = ['DK Pass T', "Luigi's Mansion R/T", 'Tokyo Blur', 'Tokyo Blur R', 'Sunset Wilds', 'Tokyo Blur', 'Tokyo Blur R', 'Airship Fortress T', 'Airship Fortress R', 'Paris Promenade 2R/T', "Rosalina's Ice World T", 'Paris Promenade 2R', "Rosalina's Ice World R", 'Mario Circuit 1T', 'Shy Guy Bazaar', 'Shy Guy Bazaar R', 'Choco Island 2', 'DK Pass R/T', 'Daisy Hills T']

Black_Shy_Guy_lv3_courses = ["Luigi's Mansion R/T"]

Black_Shy_Guy_lv6_courses = ['Choco Island 2']

Black_Shy_Guy = race_tool('Black_Shy_Guy', 'Super', Black_Shy_Guy_3items, Black_Shy_Guy_2items, Black_Shy_Guy_lv3_courses, Black_Shy_Guy_lv6_courses)


#Red_Koopa__Freerunning_
# https://game8.co/games/mariokarttour/archives/274702

Red_Koopa__Freerunning__3items = ['Donut Plains 1T', 'Toad Circuit T', 'Mario Circuit', 'London Loop', 'Paris Promenade 2R/T', 'Mario Circuit 1R/T', 'Cheep Cheep Lagoon R', 'Koopa Troopa Beach 2R', 'Koopa Troopa Beach R/T']

Red_Koopa__Freerunning__2items = ['London Loop 2R', 'London Loop R', 'Yoshi Circuit T', 'Mario Circuit 2', 'Mario Circuit 3R/T', 'RMX Mario Circuit 1R/T', 'Airship Fortress R', 'Toad Circuit', 'Choco Island 2T', 'Mario Circuit 1', 'Tokyo Blur 2R', 'Toad Circuit R/T']

Red_Koopa__Freerunning__lv3_courses = ['Mario Circuit 3R/T']

Red_Koopa__Freerunning__lv6_courses = ['Yoshi Circuit T']

Red_Koopa__Freerunning_ = race_tool('Red_Koopa__Freerunning_', 'Super', Red_Koopa__Freerunning__3items, Red_Koopa__Freerunning__2items, Red_Koopa__Freerunning__lv3_courses, Red_Koopa__Freerunning__lv6_courses)


#Birdo
# https://game8.co/games/mariokarttour/archives/275175

Birdo_3items = ['Donut Plains 2R', "Bowser's Castle 2R", "Bowser's Castle 2T", 'Choco Island 1T', 'Dino Dino Jungle R/T', 'DS Rainbow Road T', 'Frappe Snowland R/T', 'Vancouver Velocity T', 'Choco Island 2R/T']

Birdo_2items = ['Frappe Snowland T', 'London Loop 2T', 'DS Rainbow Road R/T', 'Los Angeles Laps R/T', 'Los Angeles Laps R', 'Donut Plains 2T', 'Choco Island 1R', 'Ghost Valley 1R/T', 'DS Rainbow Road', "Luigi's Mansion R", 'Waluigi Pinball T', 'New York Minute 2', 'New York Minute 2T', 'Vancouver Velocity', 'Tokyo Blur 2T', 'DK Pass R/T']

Birdo_lv3_courses = ['Ghost Valley 1R/T']

Birdo_lv6_courses = ['Waluigi Pinball T']

Birdo = race_tool('Birdo', 'Super', Birdo_3items, Birdo_2items, Birdo_lv3_courses, Birdo_lv6_courses)


#Red_Yoshi
# https://game8.co/games/mariokarttour/archives/275392

Red_Yoshi_3items = ['Daisy Hills R/T', 'Yoshi Circuit', 'Tokyo Blur 2T', 'Rock Rock Mountain T', 'Maple Treeway R', 'Tokyo Blur 2R/T', 'Yoshi Circuit R/T', 'London Loop T', 'Dino Dino Jungle R/T', 'Koopa Troopa Beach 2R']

Red_Yoshi_2items = ['RMX Choco Island 1T', 'Maple Treeway T', 'Yoshi Circuit R', 'London Loop 2', 'London Loop 2R/T', 'Donut Plains 1T', 'Donut Plains 1R', 'London Loop', 'London Loop R/T', 'Tokyo Blur R/T', 'Frappe Snowland R', 'Koopa Troopa Beach 2T', 'Frappe Snowland T', 'Vanilla Lake 1', 'Mario Circuit 2R/T', 'Mario Circuit 2R', 'Daisy Hills', 'Rock Rock Mountain']

Red_Yoshi_lv3_courses = ['Donut Plains 1R']

Red_Yoshi_lv6_courses = ['Mario Circuit 2R/T']

Red_Yoshi = race_tool('Red_Yoshi', 'Super', Red_Yoshi_3items, Red_Yoshi_2items, Red_Yoshi_lv3_courses, Red_Yoshi_lv6_courses)


#Pink_Shy_Guy
# https://game8.co/games/mariokarttour/archives/278437

Pink_Shy_Guy_3items = ['Tokyo Blur 2', 'Shy Guy Bazaar R/T', 'London Loop 2R/T', 'Shy Guy Bazaar T', 'Kalimari Desert T', 'Paris Promenade R', 'Frappe Snowland', 'Paris Promenade 2T', 'Ghost Valley 1']

Pink_Shy_Guy_2items = ['Kalimari Desert 2R', 'Tokyo Blur', 'Tokyo Blur 3', 'Cheep Cheep Lagoon R/T', 'Choco Island 2R/T', 'Choco Mountain', 'Choco Mountain T', 'Kalimari Desert R', 'Shy Guy Bazaar', 'Donut Plains 1R/T', 'Paris Promenade', 'Paris Promenade R/T', 'RMX Mario Circuit 1T', 'RMX Mario Circuit 1R', 'Mario Circuit 2R/T', 'Paris Promenade 2', 'Paris Promenade 2R/T', 'Ghost Valley 1R', 'SNES Rainbow Road']

Pink_Shy_Guy_lv3_courses = ['Cheep Cheep Lagoon R/T']

Pink_Shy_Guy_lv6_courses = ['Mario Circuit 2R/T']

Pink_Shy_Guy = race_tool('Pink_Shy_Guy', 'Super', Pink_Shy_Guy_3items, Pink_Shy_Guy_2items, Pink_Shy_Guy_lv3_courses, Pink_Shy_Guy_lv6_courses)


#Birdo__Light_Blue_
# https://game8.co/games/mariokarttour/archives/279953

Birdo__Light_Blue__3items = ['Mario Circuit 2R/T', 'Vancouver Velocity', 'Vancouver Velocity R/T', 'Ghost Valley 1R', 'Mario Circuit 3T', 'DS Rainbow Road', 'Frappe Snowland T', 'Frappe Snowland T']

Birdo__Light_Blue__2items = ['Cheep Cheep Lagoon R/T', 'Ghost Valley 1R/T', 'Donut Plains 1T', "Bowser's Castle 2T", 'RMX Mario Circuit 1R', 'Donut Plains 1R/T', 'Airship Fortress R', 'Waluigi Pinball T', 'Vancouver Velocity R', 'Vancouver Velocity T', 'Koopa Troopa Beach R/T', 'Koopa Troopa Beach 2T', 'Koopa Troopa Beach 2R', 'Koopa Troopa Beach 2', 'DK Summit R']

Birdo__Light_Blue__lv3_courses = ['Koopa Troopa Beach R/T']

Birdo__Light_Blue__lv6_courses = ['Donut Plains 1R/T']

Birdo__Light_Blue_ = race_tool('Birdo__Light_Blue_', 'Super', Birdo__Light_Blue__3items, Birdo__Light_Blue__2items, Birdo__Light_Blue__lv3_courses, Birdo__Light_Blue__lv6_courses)


#Hammer_Bro
# https://game8.co/games/mariokarttour/archives/285092

Hammer_Bro_3items = ['Mario Circuit 3R/T', 'Paris Promenade 2R', "Bowser's Castle 1R/T", 'Kalimari Desert R/T', 'Donut Plains 1T', 'Kalimari Desert', 'Toad Circuit']

Hammer_Bro_2items = ['Choco Mountain R', 'Los Angeles Laps T', 'Los Angeles Laps R', 'Mario Circuit 2R/T', 'Dino Dino Jungle R/T', "Bowser's Castle 2T", "Bowser's Castle 2", "Bowser's Castle 2R", 'Donut Plains 1', 'Koopa Troopa Beach', 'Koopa Troopa Beach R', 'Toad Circuit T', 'DS Rainbow Road T']

Hammer_Bro_lv3_courses = ['Dino Dino Jungle R/T']

Hammer_Bro_lv6_courses = ['Koopa Troopa Beach']

Hammer_Bro = race_tool('Hammer_Bro', 'Super', Hammer_Bro_3items, Hammer_Bro_2items, Hammer_Bro_lv3_courses, Hammer_Bro_lv6_courses)


#Boomerang_Bro
# https://game8.co/games/mariokarttour/archives/285093

Boomerang_Bro_3items = ['Cheep Cheep Lagoon R/T', 'Rock Rock Mountain T', 'Donut Plains 1', 'RMX Mario Circuit 1R', 'RMX Mario Circuit 1T']

Boomerang_Bro_2items = ['Mario Circuit 2R/T', 'Vancouver Velocity', 'Vancouver Velocity T', 'Donut Plains 1R/T', 'Neo Bowser City T', 'Neo Bowser City', 'Rock Rock Mountain R', 'Rock Rock Mountain', 'DS Rainbow Road T', "Bowser's Castle 2", 'Donut Plains 1T', 'Donut Plains 1R', 'Kalimari Desert T', "Bowser's Castle 2R", 'Kalimari Desert R', 'Dino Dino Jungle R']

Boomerang_Bro_lv3_courses = ['Kalimari Desert T']

Boomerang_Bro_lv6_courses = ['Kalimari Desert R']

Boomerang_Bro = race_tool('Boomerang_Bro', 'Super', Boomerang_Bro_3items, Boomerang_Bro_2items, Boomerang_Bro_lv3_courses, Boomerang_Bro_lv6_courses)


#Ice_Bro
# https://game8.co/games/mariokarttour/archives/285094

Ice_Bro_3items = ['Vanilla Lake 1R/T', 'DK Pass R/T', 'Vancouver Velocity', 'Vancouver Velocity R', 'Neo Bowser City', 'Vanilla Lake 1R', "Bowser's Castle 2", 'Frappe Snowland', 'Frappe Snowland R', 'Frappe Snowland T']

Ice_Bro_2items = ['Frappe Snowland R/T', 'DS Rainbow Road R/T', "Rosalina's Ice World T", 'Vancouver Velocity R/T', 'Mario Circuit 3R', 'Donut Plains 1', "Bowser's Castle 2T", 'Kalimari Desert T', 'DK Pass R', 'DK Pass T', 'Koopa Troopa Beach T', 'DK Pass']

Ice_Bro_lv3_courses = ['Koopa Troopa Beach T']

Ice_Bro_lv6_courses = ['Mario Circuit 3R']

Ice_Bro = race_tool('Ice_Bro', 'Super', Ice_Bro_3items, Ice_Bro_2items, Ice_Bro_lv3_courses, Ice_Bro_lv6_courses)


#Fire_Bro
# https://game8.co/games/mariokarttour/archives/285095

Fire_Bro_3items = ["Bowser's Castle 2R", 'Shy Guy Bazaar R', "Bowser's Castle 2R/T", "Bowser's Castle 1R/T", 'Airship Fortress R', "Bowser's Castle 1R", "Bowser's Castle 2", "Bowser's Castle 2T"]

Fire_Bro_2items = ['Kalimari Desert', 'Dino Dino Jungle', 'Dino Dino Jungle T', 'Donut Plains 1R', 'Sunset Wilds R', 'Neo Bowser City', 'Neo Bowser City T', 'Airship Fortress T', 'RMX Choco Island 1R', 'DS Rainbow Road T']

Fire_Bro_lv3_courses = ['Dino Dino Jungle T']

Fire_Bro_lv6_courses = ['Donut Plains 1R']

Fire_Bro = race_tool('Fire_Bro', 'Super', Fire_Bro_3items, Fire_Bro_2items, Fire_Bro_lv3_courses, Fire_Bro_lv6_courses)


#Birdo__Yellow_
# https://game8.co/games/mariokarttour/archives/285888

Birdo__Yellow__3items = ['Kalimari Desert 2T', 'Paris Promenade R', 'London Loop R/T', 'Kalimari Desert R/T', 'Cheep Cheep Lagoon', 'RMX Choco Island 1', 'Shy Guy Bazaar R/T']

Birdo__Yellow__2items = ['Choco Island 2T', 'Choco Island 2R/T', 'Waluigi Pinball R/T', 'Royal Raceway', 'Maple Treeway R', 'Sunset Wilds R/T', 'Paris Promenade', 'Paris Promenade R/T', 'London Loop', 'Daisy Hills', 'Daisy Hills R', 'Rock Rock Mountain T', 'Donut Plains 1R/T', 'Choco Island 2R', 'Cheep Cheep Lagoon R', 'Cheep Cheep Lagoon T']

Birdo__Yellow__lv3_courses = ['Choco Island 2T']

Birdo__Yellow__lv6_courses = ['Waluigi Pinball R/T']

Birdo__Yellow_ = race_tool('Birdo__Yellow_', 'Super', Birdo__Yellow__3items, Birdo__Yellow__2items, Birdo__Yellow__lv3_courses, Birdo__Yellow__lv6_courses)


#Monty_Mole
# https://game8.co/games/mariokarttour/archives/286864

Monty_Mole_3items = ["Bowser's Castle 2", 'Dino Dino Jungle R', 'Mario Circuit 1T', 'RMX Choco Island 1T', 'Donut Plains 1', 'Donut Plains 1R', 'Koopa Troopa Beach 2']

Monty_Mole_2items = ['Choco Island 1', 'RMX Choco Island 1R', 'Dino Dino Jungle', "Bowser's Castle 2R", 'Toad Circuit R', 'Koopa Troopa Beach R/T', 'RMX Choco Island 1', 'Choco Island 1T', 'Choco Island 1R', 'Donut Plains 1T', 'Koopa Troopa Beach 2R']

Monty_Mole_lv3_courses = ['Koopa Troopa Beach R/T']

Monty_Mole_lv6_courses = ['Toad Circuit R']

Monty_Mole = race_tool('Monty_Mole', 'Super', Monty_Mole_3items, Monty_Mole_2items, Monty_Mole_lv3_courses, Monty_Mole_lv6_courses)


#Penguin_Luigi
# https://game8.co/games/mariokarttour/archives/275773

Penguin_Luigi_3items = ['DK Pass R/T', 'London Loop R', 'Mario Circuit 2R/T', 'RMX Rainbow Road 1R/T', 'Waluigi Pinball R/T', 'DK Pass', 'Frappe Snowland T', 'Rock Rock Mountain R', 'Donut Plains 2T', "Rosalina's Ice World T", 'Mario Circuit R/T', 'RMX Choco Island 1R', 'DK Pass R', 'Merry Mountain', 'RMX Rainbow Road 1T', 'RMX Mario Circuit 1R', 'Koopa Troopa Beach 2', 'Mario Circuit 2R/T', 'Berlin Byways 2T', 'Berlin Byways 2R', 'Vanilla Lake 1']

Penguin_Luigi_2items = ['London Loop', 'London Loop R/T', 'DS Rainbow Road R/T', 'Royal Raceway R', 'Paris Promenade T', 'Paris Promenade R/T', "Luigi's Mansion R/T", 'Donut Plains 2R', 'Paris Promenade 2T', 'Frappe Snowland R/T', 'Vancouver Velocity R', "Luigi's Mansion R", 'Rock Rock Mountain', 'Frappe Snowland R', 'Koopa Troopa Beach 2T', 'RMX Rainbow Road 2R']

Penguin_Luigi_lv3_courses = ["Luigi's Mansion R", 'DS Rainbow Road R/T']

Penguin_Luigi_lv6_courses = ['Rock Rock Mountain', 'Koopa Troopa Beach 2T']

Penguin_Luigi = race_tool('Penguin_Luigi', 'High-End', Penguin_Luigi_3items, Penguin_Luigi_2items, Penguin_Luigi_lv3_courses, Penguin_Luigi_lv6_courses)


#Dry_Bones
# https://game8.co/games/mariokarttour/archives/270439

Dry_Bones_3items = ["Bowser's Castle 1T", 'Shy Guy Bazaar T']

Dry_Bones_2items = ["Bowser's Castle 1", "Bowser's Castle 1R", 'Cheep Cheep Lagoon R', 'Cheep Cheep Lagoon T', 'London Loop R/T', 'Kalimari Desert', 'Vanilla Lake 1R/T', "Bowser's Castle 2R/T", 'Choco Island 2T', 'RMX Mario Circuit 1R']

Dry_Bones_lv3_courses = []

Dry_Bones_lv6_courses = ["Bowser's Castle 1"]

Dry_Bones = race_tool('Dry_Bones', 'Normal', Dry_Bones_3items, Dry_Bones_2items, Dry_Bones_lv3_courses, Dry_Bones_lv6_courses)


#Shy_Guy
# https://game8.co/games/mariokarttour/archives/270438

Shy_Guy_3items = ['Shy Guy Bazaar']

Shy_Guy_2items = ['Dino Dino Jungle', "Bowser's Castle 1", "Bowser's Castle 1R", 'Shy Guy Bazaar T', 'Daisy Hills R/T', 'Ghost Valley 1R', 'DK Pass', 'London Loop R', 'SNES Rainbow Road', 'Ghost Valley 1R/T']

Shy_Guy_lv3_courses = []

Shy_Guy_lv6_courses = ['Daisy Hills R/T']

Shy_Guy = race_tool('Shy_Guy', 'Normal', Shy_Guy_3items, Shy_Guy_2items, Shy_Guy_lv3_courses, Shy_Guy_lv6_courses)


#Koopa_Troopa
# https://game8.co/games/mariokarttour/archives/270437

Koopa_Troopa_3items = ['Koopa Troopa Beach', 'Cheep Cheep Lagoon R/T']

Koopa_Troopa_2items = ['London Loop', 'Mario Circuit 1R/T', 'Choco Island 2', 'Mario Circuit T', 'Tokyo Blur R', 'Koopa Troopa Beach 2', "Bowser's Castle 1T", 'Koopa Troopa Beach R', 'Koopa Troopa Beach T', 'Cheep Cheep Lagoon', 'Cheep Cheep Lagoon R']

Koopa_Troopa_lv3_courses = []

Koopa_Troopa_lv6_courses = ['Mario Circuit T']

Koopa_Troopa = race_tool('Koopa_Troopa', 'Normal', Koopa_Troopa_3items, Koopa_Troopa_2items, Koopa_Troopa_lv3_courses, Koopa_Troopa_lv6_courses)


#Baby_Daisy
# https://game8.co/games/mariokarttour/archives/270436

Baby_Daisy_3items = ['Bubble+', ' Bubble+.1', 'Bubble+', "Increases the Bubble's movement speed."]

Baby_Daisy_2items = ['Daisy Hills R/T', 'Daisy Hills T', 'Choco Island 2R/T (Lv 6)', 'Kalimari Desert T', 'Choco Island 2R', 'Tokyo Blur R/T', 'Daisy Hills R', 'Koopa Troopa Beach T', 'Toad Circuit R', 'Mario Circuit 1R', 'Cheep Cheep Lagoon', 'Shy Guy Bazaar', 'Choco Island 2R/T']

Baby_Daisy_lv3_courses = []

Baby_Daisy_lv6_courses = []

Baby_Daisy = race_tool('Baby_Daisy', 'Normal', Baby_Daisy_3items, Baby_Daisy_2items, Baby_Daisy_lv3_courses, Baby_Daisy_lv6_courses)


#Baby_Peach
# https://game8.co/games/mariokarttour/archives/270435

Baby_Peach_3items = ['Bubble+', ' Bubble+.1', 'Bubble+', "Increases the Bubble's movement speed."]

Baby_Peach_2items = ['Cheep Cheep Lagoon', 'DS Rainbow Road (Lv 6)', 'Choco Island 2', 'RMX Rainbow Road 2R', 'London Loop 2R', 'Tokyo Blur', 'Ghost Valley 1', 'Tokyo Blur T', 'Vanilla Lake 1R/T', 'DS Rainbow Road', 'Daisy Hills R', 'Koopa Troopa Beach R', 'Mario Circuit 1R', 'DK Pass R']

Baby_Peach_lv3_courses = []

Baby_Peach_lv6_courses = []

Baby_Peach = race_tool('Baby_Peach', 'Normal', Baby_Peach_3items, Baby_Peach_2items, Baby_Peach_lv3_courses, Baby_Peach_lv6_courses)


#Baby_Mario
# https://game8.co/games/mariokarttour/archives/270434

Baby_Mario_3items = ['Waluigi Pinball', 'Mario Circuit 1T']

Baby_Mario_2items = ['Yoshi Circuit', 'Waluigi Pinball T', 'Vanilla Lake 1R/T', 'Daisy Hills R', 'Koopa Troopa Beach', 'Toad Circuit', 'Toad Circuit T', 'RMX Mario Circuit 1', 'DK Pass', 'DK Pass T']

Baby_Mario_lv3_courses = []

Baby_Mario_lv6_courses = ['Vanilla Lake 1R/T']

Baby_Mario = race_tool('Baby_Mario', 'Normal', Baby_Mario_3items, Baby_Mario_2items, Baby_Mario_lv3_courses, Baby_Mario_lv6_courses)


#Baby_Rosalina
# https://game8.co/games/mariokarttour/archives/270721

Baby_Rosalina_3items = ['Bubble+', ' Bubble+.1', 'Bubble+', "Increases the Bubble's movement speed."]

Baby_Rosalina_2items = ['SNES Rainbow Road T', 'Choco Island 2T', 'Choco Island 2R/T (Lv 6)', 'Ghost Valley 1', "Luigi's Mansion T", 'Frappe Snowland', 'Yoshi Circuit R', 'Mario Circuit 2T', 'London Loop 2', 'DS Rainbow Road', 'Choco Island 2R/T', 'DK Pass', 'SNES Rainbow Road R', 'SNES Rainbow Road R/T', 'London Loop']

Baby_Rosalina_lv3_courses = []

Baby_Rosalina_lv6_courses = []

Baby_Rosalina = race_tool('Baby_Rosalina', 'Normal', Baby_Rosalina_3items, Baby_Rosalina_2items, Baby_Rosalina_lv3_courses, Baby_Rosalina_lv6_courses)


#Iggy
# https://game8.co/games/mariokarttour/archives/270720

Iggy_3items = ['Choco Island 2R']

Iggy_2items = ['Tokyo Blur 2R/T', 'DK Pass R', 'Ghost Valley 1T', "Bowser's Castle 1T", 'Koopa Troopa Beach T', 'Kalimari Desert R', 'Neo Bowser City T', 'Rock Rock Mountain T', 'Mario Circuit 2', 'Mario Circuit 2R', 'Paris Promenade T', "Bowser's Castle 2R/T"]

Iggy_lv3_courses = []

Iggy_lv6_courses = ["Bowser's Castle 1T"]

Iggy = race_tool('Iggy', 'Normal', Iggy_3items, Iggy_2items, Iggy_lv3_courses, Iggy_lv6_courses)


#Larry
# https://game8.co/games/mariokarttour/archives/270719

Larry_3items = ['Kalimari Desert R', 'Kalimari Desert R/T']

Larry_2items = ['Cheep Cheep Lagoon R', 'Rock Rock Mountain T', 'Kalimari Desert T', 'Neo Bowser City', 'Neo Bowser City T', 'Paris Promenade R', 'Paris Promenade R/T', 'Mario Circuit 3T', 'Cheep Cheep Lagoon R/T']

Larry_lv3_courses = []

Larry_lv6_courses = ['Cheep Cheep Lagoon R/T']

Larry = race_tool('Larry', 'Normal', Larry_3items, Larry_2items, Larry_lv3_courses, Larry_lv6_courses)


#Lemmy
# https://game8.co/games/mariokarttour/archives/270718

Lemmy_3items = ['Bubble+', ' Bubble+.1', 'Bubble+', "Increases the Bubble's movement speed."]

Lemmy_2items = ['SNES Rainbow Road R', 'Mario Circuit 2T', 'Cheep Cheep Lagoon R', 'DS Rainbow Road', 'Vanilla Lake 1', 'DS Rainbow Road T (Lv 6)', "Bowser's Castle 1R", 'SNES Rainbow Road', 'Toad Circuit R', 'Choco Island 2T', "Bowser's Castle 2R/T", 'DS Rainbow Road T']

Lemmy_lv3_courses = []

Lemmy_lv6_courses = []

Lemmy = race_tool('Lemmy', 'Normal', Lemmy_3items, Lemmy_2items, Lemmy_lv3_courses, Lemmy_lv6_courses)


#Ludwig
# https://game8.co/games/mariokarttour/archives/270717

Ludwig_3items = ["Bowser's Castle 1", 'Kalimari Desert', 'Kalimari Desert R/T', 'Neo Bowser City R/T']

Ludwig_2items = ['Yoshi Circuit R/T', 'Shy Guy Bazaar R', 'Choco Mountain T', 'Choco Mountain R', 'SNES Rainbow Road', 'Tokyo Blur 2T', 'RMX Mario Circuit 1R', 'Airship Fortress T']

Ludwig_lv3_courses = []

Ludwig_lv6_courses = ['Yoshi Circuit R/T']

Ludwig = race_tool('Ludwig', 'Normal', Ludwig_3items, Ludwig_2items, Ludwig_lv3_courses, Ludwig_lv6_courses)


#Morton
# https://game8.co/games/mariokarttour/archives/270716

Morton_3items = ['Kalimari Desert']

Morton_2items = ["Bowser's Castle 1R/T", "Bowser's Castle 1", 'Dino Dino Jungle R/T', 'Kalimari Desert T', 'Mario Circuit 3R', 'Neo Bowser City T', 'Rock Rock Mountain', 'Mario Circuit 2R', 'Donut Plains 1T', 'Kalimari Desert R/T', 'Airship Fortress', 'Koopa Troopa Beach 2T', 'Koopa Troopa Beach 2R']

Morton_lv3_courses = []

Morton_lv6_courses = ['Dino Dino Jungle R/T']

Morton = race_tool('Morton', 'Normal', Morton_3items, Morton_2items, Morton_lv3_courses, Morton_lv6_courses)


#Roy
# https://game8.co/games/mariokarttour/archives/270715

Roy_3items = ['Kalimari Desert T', 'Dino Dino Jungle R/T']

Roy_2items = ['London Loop T', "Bowser's Castle 1R/T", 'Kalimari Desert', 'Kalimari Desert R', 'Mario Circuit 2T', 'Neo Bowser City R', 'Dino Dino Jungle R', 'Koopa Troopa Beach T', 'RMX Mario Circuit 1R', 'Kalimari Desert R/T', 'RMX Choco Island 1R', 'RMX Choco Island 1']

Roy_lv3_courses = []

Roy_lv6_courses = ["Bowser's Castle 1R/T"]

Roy = race_tool('Roy', 'Normal', Roy_3items, Roy_2items, Roy_lv3_courses, Roy_lv6_courses)


#Wendy
# https://game8.co/games/mariokarttour/archives/270714

Wendy_3items = ['Choco Island 2']

Wendy_2items = ['Cheep Cheep Lagoon R', 'Choco Mountain', 'Choco Mountain R', 'Daisy Hills T', 'Mario Circuit', 'Mario Circuit T', 'Neo Bowser City R', "Bowser's Castle 2", "Bowser's Castle 2R", 'Waluigi Pinball R/T', 'Paris Promenade 2R', 'DS Rainbow Road T', 'Choco Island 2R/T']

Wendy_lv3_courses = []

Wendy_lv6_courses = ["Bowser's Castle 2R"]

Wendy = race_tool('Wendy', 'Normal', Wendy_3items, Wendy_2items, Wendy_lv3_courses, Wendy_lv6_courses)


#Baby_Luigi
# https://game8.co/games/mariokarttour/archives/271644

Baby_Luigi_3items = ["Luigi's Mansion R", "Luigi's Mansion R/T", 'Paris Promenade 2R']

Baby_Luigi_2items = ['RMX Mario Circuit 1T', "Luigi's Mansion", 'Waluigi Pinball', 'Daisy Hills T', 'Mario Circuit 1R', 'Paris Promenade 2R/T', 'Donut Plains 1R/T', 'Waluigi Pinball R/T', 'New York Minute 3T', 'New York Minute 3R', 'DK Pass R', 'Mario Circuit R/T']

Baby_Luigi_lv3_courses = []

Baby_Luigi_lv6_courses = ['Waluigi Pinball R/T']

Baby_Luigi = race_tool('Baby_Luigi', 'Normal', Baby_Luigi_3items, Baby_Luigi_2items, Baby_Luigi_lv3_courses, Baby_Luigi_lv6_courses)


#Penguin_Luigi
# https://game8.co/games/mariokarttour/archives/275773

Penguin_Luigi_3items = ['DK Pass R/T', 'London Loop R', 'Mario Circuit 2R/T', 'RMX Rainbow Road 1R/T', 'Waluigi Pinball R/T', 'DK Pass', 'Frappe Snowland T', 'Rock Rock Mountain R', 'Donut Plains 2T', "Rosalina's Ice World T", 'Mario Circuit R/T', 'RMX Choco Island 1R', 'DK Pass R', 'Merry Mountain', 'RMX Rainbow Road 1T', 'RMX Mario Circuit 1R', 'Koopa Troopa Beach 2', 'Mario Circuit 2R/T', 'Berlin Byways 2T', 'Berlin Byways 2R', 'Vanilla Lake 1']

Penguin_Luigi_2items = ['London Loop', 'London Loop R/T', 'DS Rainbow Road R/T', 'Royal Raceway R', 'Paris Promenade T', 'Paris Promenade R/T', "Luigi's Mansion R/T", 'Donut Plains 2R', 'Paris Promenade 2T', 'Frappe Snowland R/T', 'Vancouver Velocity R', "Luigi's Mansion R", 'Rock Rock Mountain', 'Frappe Snowland R', 'Koopa Troopa Beach 2T', 'RMX Rainbow Road 2R']

Penguin_Luigi_lv3_courses = ["Luigi's Mansion R", 'DS Rainbow Road R/T']

Penguin_Luigi_lv6_courses = ['Rock Rock Mountain', 'Koopa Troopa Beach 2T']

Penguin_Luigi = race_tool('Penguin_Luigi', 'High-End', Penguin_Luigi_3items, Penguin_Luigi_2items, Penguin_Luigi_lv3_courses, Penguin_Luigi_lv6_courses)

