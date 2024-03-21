from tkinter import *
import tkinter.messagebox as msg
import random
import string

class PasswordGenerator(Tk):

    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        app_width = 500
        app_height = 200
        set_x = int((screen_width / 2) - (app_width / 2))
        set_y = int((screen_height / 2) - (app_height / 2))
        self.geometry(f'{app_width}x{app_height}+{set_x}+{set_y}')
        self.title("Password Generator")
        self.resizable(False, False)
    
        self.app_heading_frame = self.create_app_heading_frame()
        self.create_heading_label()
        self.size_input_frame = self.create_size_input_frame()
        self.create_password_size_label()
        self.password_size_entry = self.create_password_size_entry()
        self.button_frame = self.create_button_frame()
        self.create_generate_button()
        
    def create_app_heading_frame(self):
        
        frame = Frame(self, height = 50, bg = "#2b2e30")
        frame.pack(fill = X)
        return frame

    def create_heading_label(self):
        
        label = Label(self.app_heading_frame, text = "Password Generator", font = ("Helvetica", 23, "bold"), fg = "#F0FFFF", bg = "#2b2e30")
        label.pack()

    def create_size_input_frame(self):
        
        frame = Frame(self, bg = "#e5e7ea", height = 300, padx = 20, pady = 20)
        frame.pack(fill = BOTH)
        return frame

    def create_password_size_label(self):
        
        label = Label(self.size_input_frame, text = "Set Password Size -", font = ("Helvetica", 16), bg = "#e5e7ea", fg = "#000000")
        label.pack(side = LEFT, padx = (0, 10))

    def create_password_size_entry(self):
        
        entry = Entry(self.size_input_frame, width = 20, fg = "#1e4976", font = ("Helvetica", 13))
        entry.pack(side = LEFT,  ipady = 2, ipadx = 2)
        return entry

    def create_button_frame(self):
        
        frame = Frame(self, bg="#e5e7ea", height=100, padx=20, pady=20)
        frame.pack(fill=BOTH)
        return frame

    def show_generate_password_window(self, size, password):
        
        show_generated_password_popup_window = Toplevel(self)
        show_generated_password_popup_window.geometry("700x215")
        show_generated_password_popup_window.resizable(False, False)
        show_generated_password_popup_window.title(f"Your Generated Password")
        label = Label(show_generated_password_popup_window, text = f"GENERATED PASSWORD", fg = "#000000", font = ("Helvetica", 16, 'bold'))
        label.pack()
        pass_view = Text(show_generated_password_popup_window, height = 3, width = 70, fg = "#000000", bg = "#e5e7ea", font = ("Helvetica", 15))
        pass_view.insert(END, password)
        pass_view.config(state = DISABLED)
        pass_view.pack()
        btn_close = Button(show_generated_password_popup_window, text = "Close", width = 13, bd = 0, bg = "#FF3030", fg = "#030303", font = ("Helvetica", 13, "bold"), command = show_generated_password_popup_window.destroy)
        btn_close.pack(side = RIGHT, padx = (0, 20))
        show_generated_password_popup_window.mainloop()

    def create_generate_button(self):
        
        button = Button(self.button_frame, text = "GENERATE PASSWORD", bg = "#007FFF", fg = "#000000", font = ("Helvetica", 12, "bold"), borderwidth = 0, cursor = "hand2", padx = 20, pady = 5, command = lambda: self.collect_password(self.password_size_entry.get()))
        button.pack()
        
    def generate_security_password(self, size):
        
        characters = string.ascii_letters + string.digits + string.punctuation
        pwd = ''.join(random.choice(characters) for _ in range(size))
        return pwd

    def collect_password(self, size):
        
        try:
            size = int(size)
            if size > 99 or size < 9:
                msg.showwarning(title = "WARNING",message = "Password size must be less than 100 and greater than 8")
            elif size <= 100 or size >= 8:
                password = self.generate_security_password(int(size))
                self.show_generate_password_window(size, password)
                
        except Exception as e:
            msg.showwarning(title = "WARNING", message = "Kindly enter the integer number to proceed forward.")

    def run(self):
        
        self.mainloop()

if __name__ == '__main__':
    app = PasswordGenerator()
    app.run()
    