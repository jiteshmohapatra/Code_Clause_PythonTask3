import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.text = tk.Text(root, wrap="word", undo=True)
        self.text.pack(expand="yes", fill="both")
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)

    def new_file(self):
        self.root.title("Simple Text Editor")
        self.text.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.root.title(f"Simple Text Editor - {file_path}")
            with open(file_path, "r") as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.root.title(f"Simple Text Editor - {file_path}")
            with open(file_path, "w") as file:
                file.write(self.text.get(1.0, tk.END))

def main():
    root = tk.Tk()
    root.geometry("600x400")
    editor = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
