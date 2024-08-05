import tkinter as tk
from tkinter import ttk, font

BLACK = "#FFFFFF"
WHITE = "#000000"
DARK_GREY = "#141414"
BUTTON_WIDTH = 10
BUTTON_HEIGHT = 5

class CalculatorApp:
    def __init__(self, window) -> None:
        self.window = window
        self.window.title("Calculator")
        self.ans = None

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure('TButton', background=DARK_GREY, 
                             foreground='white', borderwidth=0.1)
        self.style.map("TButton", background=[("active", "darkgreen")])
        self.window.geometry("312x500")
        self.window.resizable(False, False)
        
        self.T = tk.Text(self.window, bg=WHITE, fg="#0000FF",
                         height=2.54, width=24, font=("Yu Gothic Bold", 40))
        self.T.pack()  

        self.button_setup()

    def get_display_text(self):
        return self.T.get("1.0", tk.END).strip()

    def set_display_text(self, text):
        self.T.delete("1.0", tk.END)
        self.T.insert(tk.END, text)

    def insert_num(self, num):
        text = self.get_display_text()
        if len(text) < 8:
            self.T.insert(tk.END, num)

    def insert_decimal(self, decimal):
            self.T.insert(tk.END, decimal)

    def insert_operation(self, operation):
        text = self.get_display_text()
        if text and text[-1] in '/*-+':
            self.set_display_text(text[:-1] + operation)
        else:
            self.T.insert(tk.END, operation)

    def wipe_screen(self, _=None):
        self.T.delete("1.0", tk.END)

    def change_signs(self, _=None):
        text = self.get_display_text()
        if text.startswith('-'):
            self.set_display_text(text[1:])
        else: 
            self.set_display_text('-' + text)

    def evaluate(self, _=None):
        try:
            text = self.get_display_text()
            answer = eval(text)
            self.set_display_text(str(answer))

        except Exception:
            self.set_display_text("Error")

    def percentage(self, _=None):
        try:
            text = self.get_display_text()
            result = eval(text) / 100
            self.set_display_text(str(result))
        except Exception:
            self.set_display_text("Error")

    def button_setup(self):
        frame_style = ttk.Style()
        frame_style.configure('CustomFrame.TFrame', background='black')
        input_frame = ttk.Frame(window, style='CustomFrame.TFrame')
    
        # Button grid in list
        buttons = [
            ('AC', 0, 0, self.wipe_screen), ('+/-', 0, 1, self.change_signs), 
            ('%', 0, 2, self.percentage), ('/', 0, 3, self.insert_operation),
            ('7', 1, 0, self.insert_num), ('8', 1, 1, self.insert_num), 
            ('9', 1, 2, self.insert_num), ('*', 1, 3, self.insert_operation),
            ('4', 2, 0, self.insert_num), ('5', 2, 1, self.insert_num), 
            ('6', 2, 2, self.insert_num), ('-', 2, 3, self.insert_operation),
            ('1', 3, 0, self.insert_num), ('2', 3, 1, self.insert_num), 
            ('3', 3, 2, self.insert_num), ('+', 3, 3, self.insert_operation),
            ('.', 4, 2, self.insert_decimal), ('=', 4, 3, self.evaluate)
        ]

        for (text, row, column, command) in buttons:
            btn = ttk.Button(master = input_frame, text = text, 
                             style = 'TButton', width=BUTTON_WIDTH, 
                             command = lambda t = text, c = command: c(t))
            btn.grid(row=row, column=column, padx=2.5, pady=1, ipady = 5)


        btn = ttk.Button(master = input_frame, text = '0', style = 'TButton', 
                         command = lambda t = '0', c = self.insert_num: c(t))
        btn.grid(row = 4, column = 0, columnspan=2, 
                 sticky='ew', padx=2.5, pady=1, ipady = 5)

        for i in range(5): 
            input_frame.grid_rowconfigure(i, weight=1)
        for i in range(3):  
            input_frame.grid_columnconfigure(i, weight=0)
        input_frame.pack(fill=tk.BOTH, expand=True)

# make Button widgets that calls wipe_screen() and saves returned into variable 'saved'

if __name__ == "__main__":
    window = tk.Tk()
    app = CalculatorApp(window)
    window.mainloop()


    
