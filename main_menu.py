import tkinter as tk 

class MainMenu(tk.Frame):
	
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

		self.btn_play = tk.Button(self.main_frame, text="Play Game", font=("Times New Roman", 20, "bold"), command=lambda:self.game.create_board())
		self.btn_play.pack(pady=5)

		self.btn_exit = tk.Button(self.main_frame, text="Quit", font=("Times New Roman", 20, "bold"), command=lambda:self.game.exit())
		self.btn_exit.pack(pady=5)