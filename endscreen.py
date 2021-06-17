import tkinter as tk
from tkinter import ttk

class EndScreen(tk.Frame):
	
	def __init__(self, parent, Game):
		
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="white")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)


		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self, width=self.config.side, height=self.config.side, bg="white")
		self.main_frame.pack(expand=True)

		#BUTTON
		self.label_youwin = tk.Label(self.main_frame, text="You Win!!!", font=("Times New Roman", 69, "bold"), bg="white", fg="black")
		self.label_youwin.pack(pady=5)

		self.label_youwin1 = tk.Label(self.main_frame, text="", font=("Times New Roman", 20, "bold"), bg="white", fg="black")
		self.label_youwin1.pack(pady=5)

		self.btn_playagain = tk.Button(self.main_frame, text="Play Again?", font=("Times New Roman", 20, "bold"), command=lambda:self.game.create_board())
		self.btn_playagain.pack(pady=5)

		self.btn_mainMenu = tk.Button(self.main_frame, text="Menu", font=("Times New Roman", 20, "bold"), command=lambda:self.game.change_page('mainMenu'))
		self.btn_mainMenu.pack(pady=5)

		self.btn_exit = tk.Button(self.main_frame, text="Quit", font=("Times New Roman", 20, "bold"), command=lambda:self.game.exit())
		self.btn_exit.pack(pady=5)
