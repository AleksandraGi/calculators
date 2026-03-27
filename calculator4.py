# https://www.youtube.com/watch?v=QZPv1y2znZo

import tkinter as tk

LIGHT_GRAY = '#F5F5F5'

class Calculator:
    def __init__(self):
        """
        Properties of the window
        """
        # --- WINDOW ---
        self.window = tk.Tk()                   # main window of the app
        self.window.geometry("375x667")         # size of the window (width x height (pixels))
        self.window.resizable(0,0)              # is resizable? (width, height (0=False, 1=True))
        self.window.title("Calculator")         # title of the window
    
        # --- DISPLAY AND BUTTONS FRAMES ---
        self.display_frame = self.create_display_frame()        # create frame for display (call a function)
        self.buttons_frame = self.create_buttons_frame()        # create frame for buttons (call a function)

    def create_display_frame(self):
        """
        """
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)        # creates window with height and colour
        frame.pack(expand=True, fill="both")                            # putting frame into window (without it frame would be in memory but not displayed) (add the frame to window and allow it to expand everywhere is space)
                                                                        # expand=True - frame expands and takes extra space
                                                                        # fill="both" - if there's space the frame expands where is space in both  directions
        return frame
    
    def create_buttons_frame(self):
        """
        """
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame        



    def run(self):
        """
        Running the app
        """
        self.window.mainloop()      # runs main loop of the window app (app opens window, waits for user's actions and reacts with those actions, close the app)

if __name__ == "__main__":
    """
    Run code only if the file is run directly (python calculator4.py in bash)
    Or if the code is imported into another file 
    """
    calc = Calculator()     # create object of the class (only def __init__())
    calc.run()              # run the object (use its property (def run()))