import tkinter as tk
import sys

from config import Config
from ship import Ship
from player import Player
from board import Board
from loginPage import LoginPage
from endscreen import EndScreen
from main_menu import MainMenu

class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config

		super().__init__()
		self.title(self.config.app_title)
		self.geometry(self.config.screen)
		self.create_container()
		self.pages = {}
		self.create_endScreen()
		self.create_mainMenu()
		self.create_loginPage()

	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)
		self.game.createanswer()
		#self.start_time = self.game_statistic.get_current_time()

	def create_loginPage(self):
		self.pages['loginPage'] = LoginPage(self.container, self)

	def create_mainMenu(self):
		self.pages['mainMenu'] = MainMenu(self.container, self)

	def create_endScreen(self):
		self.pages['endScreen'] = EndScreen(self.container, self)

	def change_page(self, page):
		page = self.pages[page]
		page.tkraise()

	def auth_login(self):
		userid = self.pages['loginPage'].var_userid.get()
		password = self.pages['loginPage'].var_password.get()
		match = self.config.login(userid, password)
		if match:
			self.change_page('mainMenu')

	def exit(self):
		sys.exit()


class Battleship:

	def __init__(self):
		self.config = Config()
		self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)

	def check_answer(self):
		ship = self.ship.location
		player = self.player.location
		if ship == player:
			return True
		else:
			return False

	def button_clicked(self, pos_x, pos_y):
		self.player.current_location(pos_x, pos_y)
		win = self.check_answer()
		self.window.pages['board'].change_img_button(pos_x, pos_y, win)
		if win:
			self.window.change_page('endScreen')

	def run(self):
		self.window.mainloop()

	def createanswer(self):
		self.ship.setup_location()
		print(self.ship.location)


if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()