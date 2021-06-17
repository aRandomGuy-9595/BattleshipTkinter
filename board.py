import tkinter as tk
from PIL import Image, ImageTk


class Board(tk.Frame):

	def __init__(self, parent, Game):

		self.game = Game
		self.config = Game.config
		super().__init__(parent)
		self.configure(bg="white")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)
		self.create_mainframe()
		self.update_board()

	def update_board(self):
		self.create_board()
		self.show_board()
		self.create_button_board()
		self.show_button_board()

	def create_mainframe(self):
		self.mainframe = tk.Frame(self, height=self.config.side, width=self.config.side, bg="black")
		self.mainframe.pack(expand=True)

	def create_board(self):
		self.frame_rows = []
		color = 696969

		n_row, n_column = self.config.row, self.config.column
		row_height, row_width = self.config.side//n_row, self.config.side

		for i in range(n_row):
			row_color = f"#{color}"
			frame = tk.Frame(self.mainframe, height=row_height, width=row_width, bg=row_color)
			self.frame_rows.append(frame)
			color += 500

	def show_board(self):
		for frame in self.frame_rows:
			frame.pack()

	def put_and_resize_photo(self, realimg, scale):
		n_column = self.config.column
		button_width = self.config.side//n_column-10

		image = Image.open(realimg)
		image_w, image_h = image.size
		ratio = image_w/button_width
		image = image.resize((int(image_w//ratio//scale), int(image_h//ratio//scale)))
		return ImageTk.PhotoImage(image)

	def change_img_button(self,pos_x, pos_y, win):
		if win:
			img = self.beforeflip
		else:
			img = self.afterflip
		self.button_board[pos_x][pos_y].configure(image=img)

	def create_button_board(self):
		self.button_board = []
		n_row, n_column = self.config.row, self.config.column
		button_height, button_width = self.config.side//n_row-10, self.config.side//n_column-10

		self.beforeflip = self.put_and_resize_photo(realimg=self.config.beforeflip, scale=2)

		self.afterflip = self.put_and_resize_photo(realimg=self.config.afterflip, scale=3)

		self.tempimg = self.put_and_resize_photo(realimg=self.config.tempimg, scale=2)


		for i in range(n_row):
			row = []
			for j in range(n_column):
				button = tk.Button(self.frame_rows[i], bg="pink", image=self.beforeflip,height=button_height, width=button_width, command=lambda x=i, y=j :self.game.button_clicked(x, y))
				row.append(button)
			self.button_board.append(row)

	def show_button_board(self):
		n_row, n_column = self.config.row, self.config.column
		for i in range(n_row):
			for j in range(n_column):
				self.button_board[i][j].pack(side="left")
