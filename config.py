import json

class Config:

	def __init__(self):

		self.app_title = "Battleship"
		self.row = 5
		self.column = 5
		base = 160
		ratio = 5
		self.side = base*ratio
		self.screen = f"{self.side}x{self.side}+500+500"
		self.beforeflip = "img/maxresdefaultt.jpg"
		self.afterflip = "img/maxresdefault.jpg"
		self.tempimg = "img/giphy.gif"
		self.logo_path = "img/giphy.gif"
		self.users_path = "json/users.json"


	def load_userData(self, users_path):
		with open(users_path, "r") as json_data:
			userData = json.load(json_data)
		return userData


	def login(self, userid, password):
		users = self.load_userData(self.users_path)
		if userid in users:
			if password == users[userid]["password"]:
				return True
			else:
				return False
		else:
			return False

