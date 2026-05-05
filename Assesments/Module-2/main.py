import tkinter as tk
from gui import MiniBlogApp

def main():
    root = tk.Tk()
    app = MiniBlogApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
