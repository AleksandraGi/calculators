# Source: https://www.youtube.com/watch?v=QZPv1y2znZo

import tkinter as tk

# --- COLOURS AND FONTS ---
LIGHT_GRAY = "#F5F5F5"                  # background colour used in the display area
LABEL_COLOUR = '#25265E'                # text colour used on labels and buttons
WHITE = '#FFFFFF'                       # button background colour for digit buttons
OFF_WHITE = '#F8FAFF'                   # button background colour for operator / special buttons
LIGHT_BLUE = '#CCEDFF'                  # background colour for the "=" button

SMALL_FONT_STYLE = ("Arial", 16)            # font used for the smaller top label
LARGE_FONT_STYLE = ("Arial", 40, "bold")    # font used for the main display label
DIGIT_FONT_STYLE = ("Arial", 24, "bold")    # font used for digit buttons
DEFAULT_FONT_STYLE = ("Arial", 20)          # font used for operator and special buttons


class Calculator:
    def __init__(self):
        """
        Create the calculator window
        Initialize its main properties (expressions, create frames, labels, buttons and key bindings)
        """
        # --- WINDOW ---
        self.window = tk.Tk()                   # create the main application window
        self.window.geometry("375x667")         # set window size: width x height (pixels)
        self.window.resizable(0,0)              # disable resizing: (width=False, height=False)
        self.window.title("Calculator")         # set the title shown in the title bar
    
        # --- EXPRESSIONS SHOWN ON THE SCREEN ---
        self.total_expression  = ""            # stores the full expression (e.g. "12 + 7")
        self.current_expression = ""           # stores the current number / current visible input (e.g."56")

        # --- DISPLAY AND BUTTONS FRAMES ---
        self.display_frame = self.create_display_frame()            # create the top frame used for the calculator display

        self.total_label, self.label = self.create_display_labels() # create two labels inside the display frame:
                                                                    #   1. total_label    ->  smaller top line
                                                                    #   2. label          ->  bigger main line

        # --- BUTTON POSITIONS ---
        self.digits ={
            7: (1, 1),  8: (1, 2),  9: (1, 3),
            4: (2, 1),  5: (2, 2),  6: (2, 3),
            1: (3, 1),  2: (3, 2),  3: (3, 3),
            0: (4, 2),  '.': (4,1)
        }                                           # dictionary that tells the program where each digit button should be places
                                                    #   key - button text
                                                    #   value - (row, column) inside the grid layout

        self.operations = {
            "/": "\u00F7", 
            "*": "\u00D7", 
            "-": "-", 
            "+": "+"}           # dictionary of math operators
                                #   key - operator used in python
                                #   value - symbol shown on screen

        # --- BUTTON FRAME ---
        self.buttons_frame = self.create_buttons_frame()        # create the bottom frame where calculator buttons will be placed

        self.buttons_frame.rowconfigure(0, weight=1)            # configurate row 0 seperately because it contains special buttons

        for x in range(1, 5):                                   # configurate rows 1-4 and columns 1-4 so buttons expand evenly
            self.buttons_frame.rowconfigure(x, weight=1)        # make each row expandable
            self.buttons_frame.columnconfigure(x, weight=1)     # make each column expandable

        # --- CREATE BUTTONS ---
        self.create_digit_buttons()         # create number buttons (0-9 and ".")
        self.create_operator_buttons()      # create operator buttons (+, -, /, *)
        self.create_special_buttons()       # create C, =, power and sqrt buttons

        # --- KEYBOARD SUPPORT ---
        self.bind_keys()                    # allow keyboard input


    def bind_keys(self):
        """
        Bind keyboard keys to calculator actions
        """
        self.window.bind("<Return>", lambda event: self.evaluate())                             # wneh Enter is pressed, call evaluate()

        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))  # for every digit key and ".", bind keyboard input to add_to_expression()
                                                                                                # digit=key stores the current loop value inside the lambda

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))   # bind operator keys (+, -, /, *) to append_operator()


    def create_special_buttons(self):
        """
        Create all special buttons
        """
        self.create_clear_button()      # C
        self.create_equals_button()     # =
        self.create_square_button()     # x²
        self.create_sqrt_button()       # √x


    def create_display_labels(self):
        """
        Create the two labels displayed in the display area
            total_label -> shows the full expression
            label       -> shows the current input / current number        
        """
        total_label = tk.Label(
            self.display_frame,             # parent widget: this label will be inside display_frame
            text=self.total_expression,     # text shown in the label at the start
            anchor=tk.E,                    # align text to the east (right side)
            bg=LIGHT_GRAY,                  # background colour
            fg=LABEL_COLOUR,                # text colour
            padx=24,                        # horizontal inner padding
            font=SMALL_FONT_STYLE)          # smaller font style for the top label
        
        total_label.pack(expand=True, fill="both")  # add the label to the frame and let it expand to fill available space

        label = tk.Label(                   
            self.display_frame,             # parent widget: this label will be inside display_frame
            text=self.current_expression,   # text shown in the label at the start
            anchor=tk.E,                    # align text to the right side
            bg=LIGHT_GRAY,                  # background colour
            fg=LABEL_COLOUR,                # text colour
            padx=24,                        # horizontal inner padding
            font=LARGE_FONT_STYLE)          # font style for the main larger label
        
        label.pack(expand=True, fill="both")    # add the label to the frame and let it expand to fill available space

        return total_label, label           # return both labels so they can be saved as object attributes


    def create_display_frame(self):
        """
        Create the upper frame of the calculator. This frame will contain the labels used as the calculator display
        """
        frame = tk.Frame(
            self.window,        # parent widget: frame will be inside the main window
            height=221,         # frame height in pixels
            bg=LIGHT_GRAY)      # frame background colour
        frame.pack(expand=True, fill="both")    # pack() places the frame inside the window (without it frame would be in memory but not displayed) (add the frame to window and allow it to expand everywhere is space)
                                                #   expand=True -> allows the frame to take extra available space
                                                #   fill="both" -> lets the frame stretch horizontally and vertically
       
        return frame            # return the created frame
    

    def add_to_expression(self, value):
        """
        Add a digit or decimal point to the current expression
        """
        self.current_expression += str(value)   # convert value to string and add it to the end of the current expression
        self.update_label()                     # refresh the main display label so the new value becomes visible


    def create_digit_buttons(self):
        """
        Create digit buttons based on the positions stored in self.digits
        """
        for digit, grid_value in self.digits.items():
            button = tk.Button(
                self.buttons_frame,                         # parent widget: button will be inside buttons_frame
                text=str(digit),                            # button text (e.g. "7")
                bg=WHITE,                                   # background colour
                fg=LABEL_COLOUR,                            # text colour
                font=DIGIT_FONT_STYLE,                      # font used on digit buttons
                borderwidth=0,                              # remove border
                command=lambda x=digit: self.add_to_expression(x)   # when button is clicked, add this digit to current_expression
                                                                    # x=digit stores the current digit from the loop
            )

            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)    # place the button in the grid
                                                                                    # sticky=tk.NSEW makes the button stretch in all directions


    def append_operator(self, operator):
        """
        Move the current expression to the total expression and add an operator
        """
        self.current_expression += operator                 # add the operator to the current expression (e.g. "12" -> "12+")
        self.total_expression += self.current_expression    # move the current part into the full expression
        self.current_expression = ""                        # clear current_expression so the user can type the next number
        self.update_total_label()                           # update the smaller top label with the full expression
        self.update_label()                                 # clear or update the main display label


    def create_operator_buttons(self):
        """
        Create operator buttons (+, -, /, *)
        """
        i = 0       # row 0 because operator buttons will be places in column 4
        for operator, symbol in self.operations.items():
            button = tk.Button(
                self.buttons_frame,                         # parent widget
                text=symbol,                                # pretty symbol shown on the button
                bg=OFF_WHITE,                               # background colour
                fg=LABEL_COLOUR,                            # text colour
                font=DEFAULT_FONT_STYLE,                    # font style
                borderwidth=0,                              # remove border
                command=lambda x=operator: self.append_operator(x)) # when clicked, add the real operator to the expression
            button.grid(row=i, column=4, sticky=tk.NSEW)    # place operator in the last column, one below another
            i += 1  # move to the next row for the next operator button


    def clear(self):
        """
        Clear both expressions and reset the display
        """
        self.current_expression = ""    # remove current input
        self.total_expression = ""      # remove full expression
        self.update_label()             # clear main display label
        self.update_total_label()       # clear top display label


    def create_clear_button(self):
        """
        Create the clear button 'C'
        """
        button = tk.Button(
            self.buttons_frame,                 # parent widget
            text="C",                           # button text
            bg=OFF_WHITE,                       # background colour
            fg=LABEL_COLOUR,                    # text colour
            font=DEFAULT_FONT_STYLE,            # font style
            borderwidth=0,                      # remove border
            command=self.clear                  # call clear() when clicked
        )

        button.grid(row=0, column=1, sticky=tk.NSEW)    # place the button in row 0, column 1


    def square(self):
        """
        Square the current expression
        """
        self.current_expression = str(eval(f"{self.current_expression}**2"))    # evaluate current_expression squared (e.g. 5 -> 25)
        self.update_label()     # show the result on the main display


    def create_square_button(self):
        """
        Create the square button (x^2)
        """
        button = tk.Button(
            self.buttons_frame,                 # parent widget
            text="x\u00b2",                     # unicode for "x²"
            bg=OFF_WHITE,                       # background colour
            fg=LABEL_COLOUR,                    # text colour
            font=DEFAULT_FONT_STYLE,            # font style
            borderwidth=0,                      # remove border
            command=self.square                 # call square() when clicked
        )

        button.grid(row=0, column=2, sticky=tk.NSEW)    # place the button in row 0, column 2


    def sqrt(self):
        """
        Calculate the square root of the current expression
        """
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))  # calculate square root by raising the number to the power of 0.5
        self.update_label()     # show the result on the main display


    def create_sqrt_button(self):
        """
        Create the square root button (√x)
        """
        button = tk.Button(
            self.buttons_frame,                 # parent widget
            text="\u221ax",                     # unicode for "√x"
            bg=OFF_WHITE,                       # background colour
            fg=LABEL_COLOUR,                    # text colour
            font=DEFAULT_FONT_STYLE,            # font style
            borderwidth=0,                      # remove border
            command=self.sqrt                   # call sqrt() when clicked
        )

        button.grid(row=0, column=3, sticky=tk.NSEW)    # place the button in row 0, column 3


    def evaluate(self):
        """
        Evaluate the full math expression and show the result
        """
        self.total_expression += self.current_expression    # add the last typed number to the full expression
        self.update_total_label()                           # show the full expression in the top label becore calculating

        try:
            self.current_expression = str(eval(self.total_expression))  # calculate the result of the full expression
            self.total_expression = ""                                  # clear the top expression after successful calculation
        except Exception as e:
            self.current_expression = "Error"                           # if something is wrong (e.g. invalid expression), show "Error"
        finally:
            self.update_label()                                         # update the main display no matter what happened


    def create_equals_button(self):
        """
        Create the equals button (=)
        """
        button = tk.Button(
            self.buttons_frame,                 # parent widget
            text="=",                           # button text
            bg=LIGHT_BLUE,                      # background colour
            fg=LABEL_COLOUR,                    # text colour
            font=DEFAULT_FONT_STYLE,            # font style
            borderwidth=0,                      # remove border
            command=self.evaluate               # call evaluate() when clicked
        )

        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)  # place the button in row 4, column 3; columnspan=2 makes it cover two columns 


    def create_buttons_frame(self):
        """        
        Create the lower frame of the calculator. This frame will later contain all calculator buttons
        """
        frame = tk.Frame(self.window)           # create a frame inside the main window
        frame.pack(expand=True, fill="both")    # place it in the window and allow it to stretch
        
        return frame                            # return the created frame


    def update_total_label(self):
        """
        Update the smaller top label with the full expression. Replace python operators with math symbols
        """
        expression = self.total_expression                              # create a local copy of the full expression
        for operator, symbol in self.operations.items():                
            expression = expression.replace(operator, f" {symbol} ")    # replace "/", "*" etc. with "÷", "×" etc. for display only
        self.total_label.config(text=expression)                        # change the text shown in the top label


    def update_label(self):
        """
        Update the main label with the current expression. Limit the visible text to 11 characters
        """
        self.label.config(text=self.current_expression[:11])    # show only the first 11 characters so the display doesn't overflow


    def run(self):
        """
        Start the calculator app
        """
        self.window.mainloop()  # start tkinter's main event loop:
                                # the window appears, waits for the user actions,
                                # reacts to clicks, typing, closing the window, etc.


if __name__ == "__main__":
    """
    Run this part only when the file is executed directly (example: python calculator4.py)    
    This block will not run automatically if the file is imported into another file
    """
    calc = Calculator()     # create an object (instance) of the Calculator class 
    calc.run()              # start the application by calling its run() method