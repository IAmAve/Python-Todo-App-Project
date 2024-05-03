import tkinter as tk
from gui.main_window import MainWindow

# Create main application window
root = tk.Tk()
root.title("TODO App")

# Initialize main window
main_window = MainWindow(root)

# Start the main event loop
root.mainloop()