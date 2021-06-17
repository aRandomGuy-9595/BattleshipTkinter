import tkinter as tk
from PIL import Image, ImageTk


class LoginPage(tk.Frame):
	
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

		image = Image.open(self.config.logo_path)
		image_w, image_h = image.size
		ratio = image_w/self.config.side
		image = image.resize((int(image_w//ratio//1),int(image_h//ratio//1)))

		self.logo = ImageTk.PhotoImage(image)
		self.label_logo = tk.Label(self.main_frame, image=self.logo)
		self.label_logo.pack(pady=5)

		self.label_userid = tk.Label(self.main_frame, text="User ID", font=("Times New Roman", 20, "bold"), bg="white", fg="black")
		self.label_userid.pack(pady=5)

		self.var_userid = tk.StringVar()
		self.entry_userid = tk.Entry(self.main_frame, font=("Times New Roman", 16, "bold"), textvariable=self.var_userid)
		self.entry_userid.pack(pady=5)

		self.label_password = tk.Label(self.main_frame, text="Password", font=("Times New Roman", 20, "bold"), bg="white", fg="black")
		self.label_password.pack(pady=5)

		self.var_password = tk.StringVar()
		self.entry_password = tk.Entry(self.main_frame, font=("Times New Roman", 16, "bold"), show="*", textvariable=self.var_password)
		self.entry_password.pack(pady=5)

		self.btn_login = tk.Button(self.main_frame, text="Verify", font=("Times New Roman", 20, "bold"), command=lambda:self.game.auth_login())
		self.btn_login.pack(pady=5)

