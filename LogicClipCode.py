import tkinter as tk
import os

icon_path = os.path.abspath("icons8-null-symbol-96.ico")

texts = [    ["AND | ∧", "OR | ∨", "NOT | ¬"],
    ["XOR | ⊕", "IMPLIES | ⇒", "IF AND ONLY IF | ⇔"],
    ["MEMBER | ∈", "SUBSET | ⊆", "NOT A SUBSET | ⊄"],
    ["THERE EXISTS | ∃", "FOR ALL | ∀", "ARROW | →"],
    ["","NULL | ⊥",""]
]

INFO = """

Welcome to Logic Clip!

This program provides you with a simple and easy-to-use interface for working with Boolean algebra, which is a fundamental part of computer science and digital electronics.

Boolean algebra is a branch of algebra that deals with logical operations and values, which are typically represented as True or False, or 1 or 0. In Boolean algebra, logical operations such as AND, OR, NOT, XOR, IMPLIES, and IF AND ONLY IF are used to manipulate and analyze logical values and expressions.

Here are some basic identities of Boolean algebra:

    Identity laws: a ∨ 0 = a, a ∧ 1 = a
    Complement laws: a ∨ ¬a = 1, a ∧ ¬a = 0
    Commutative laws: a ∨ b = b OR a, a ∧ b = b ∧ a
    Associative laws: a ∨ (b ∨ c) = (a ∨ b) OR c, a ∧ (b ∧ c) = (a ∧ b) ∧ c
    Distributive laws: a ∧ (b ∨ c) = (a ∧ b) OR (a ∧ c), a OR (b ∧ c) = (a ∨ b) ∧ (a ∨ c)
    De Morgan's laws: ¬(a ∧ b) = ¬a ∨ ¬b, ¬(a ∨ b) = ¬a ∧ ¬b

Now, here are some definitions of the logical operations used in this program:

    ∧: AND: returns True if both operands are True
    ∨: OR: returns True if at least one of the operands is True
    ¬: NOT: returns the opposite value of the operand
    ⊕: XOR: returns True if exactly one of the operands is True
    ⇒: IMPLIES: returns False if the first operand is True and the second operand is False; otherwise, returns True
    ⇔: IF AND ONLY IF: returns True if both operands have the same truth value; otherwise, returns False
    ∃: THERE EXISTS: Indicates the existence of at least one object satisfying a given condition
    ∀: FOR ALL: Indicates that a given condition holds true for all objects in a set
    ⊥: NULL: Represents a null or undefined value.

If you have any questions or feedback about this program, please feel free to contact us. Thank you for using Logic Clip!

"""

class TextGrid(tk.Frame):
    def __init__(self, parent, texts):
        tk.Frame.__init__(self, parent)
        self.texts = texts
        self.text_areas = []
        self.create_widgets()

    def create_widgets(self):
        max_width = max(len(text) for row in self.texts for text in row) + 1
        max_height = 7  # set the max height for the temp text area
        self.maxwidth = max_width * 3  # update the max width of the temp text area
        self.maxheight = max_height

        # Create the text areas
        for i, row in enumerate(self.texts):
            for j, text in enumerate(row):
                text_area = tk.Text(self, width=max_width, height=1, wrap=tk.NONE, highlightthickness=0)
                text_area.insert("end", text)
                text_area.configure(state='disabled')
                text_area.bind("<Button-1>", lambda e, ta=text_area: ta.tag_add("sel", "1.0", "end"))
                text_area.grid(row=i, column=j)
    
        # Create temporary text area and buttons frame
        temp_frame = tk.Frame(self, width=self.maxwidth, height=self.maxheight)
        temp_frame.grid(row=len(self.texts), column=0, columnspan=max(len(row) for row in self.texts))

        # Create temporary text area
        temp_scrollbar = tk.Scrollbar(temp_frame)
        temp_scrollbar.pack(side="left", fill="y")

        self.temp_text = tk.Text(temp_frame, wrap="word", yscrollcommand=temp_scrollbar.set, width=max_width * 3, height=max_height)
        self.temp_text.pack(side="left", fill="both", expand=True)

        temp_scrollbar.config(command=self.temp_text.yview)
        
        # Create copy and delete and info buttons
        button_frame = tk.Frame(temp_frame, width=50, height=self.maxheight)
        button_frame.pack(side="right")

        copy_button = tk.Button(button_frame, text="COPY", width=4, command=self.copy_text, bg="#4CAF50", fg="white")
        copy_button.pack(side="top")

        delete_button = tk.Button(button_frame, text="DEL", width=4, command=self.clear_text, bg="#F44336", fg="white")
        delete_button.pack(side="top")

        info_button = tk.Button(button_frame, text="INFO", width=4, command=self.show_info, bg="#2196F3", fg="white")
        info_button.pack(side="top")

        # Set focus to temporary text area
        self.temp_text.focus_set()

    def copy_text(self):
        self.clipboard_clear()
        text = self.temp_text.get("1.0", "end")
        self.clipboard_append(text)

    def clear_text(self):
        self.temp_text.delete("1.0", "end")
        
    def show_info(self):
        info_window = tk.Toplevel(self)
        info_window.title("Information")
        info_window.geometry("600x500")
        info_window.iconbitmap(icon_path)
        info_window.configure(background='white')
        info_label = tk.Label(info_window, text=INFO, wraplength=580, background='white')
        info_label.pack()
        
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Logic Clip")
    root.iconbitmap(icon_path)
    root.resizable(False, False)

    text_grid = TextGrid(root, texts)
    text_grid.pack()

    root.mainloop()
