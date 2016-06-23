import tkinter as tk
from tkinter import messagebox, ttk

# ==============================================================
# Helper Functions
# ==============================================================

from PIL import ImageTk, Image
def make_tk_image(imagepath):
    """ 
    Opens and reads in an image to display in tk widgets. Using for example
        img=make_tk_image(imagepath)
        label=tk.Label(foo,img=image)
    """
    return ImageTk.PhotoImage(Image.open(imagepath))

# ===============================================================
# Useful Buttons
# ===============================================================

class PinButton(tk.Button):
    """Button to pin the window containing a widget to
    be always on top"""

    def __init__(self, master, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)
        self.master = master
        self.containing_window = self.winfo_toplevel()
        self.config(command=lambda: self.toggle_always_on_top(self.containing_window))

    @staticmethod
    def toggle_always_on_top(tkwindow):
        wm_status = tkwindow.wm_attributes()
        is_on = wm_status[wm_status.index('-topmost') + 1] == 1
        if is_on:
            tkwindow.wm_attributes('-topmost', 0)
        else:
            tkwindow.wm_attributes('-topmost', 1)

class AlphaSlider(ttk.Scale):
    """
    Slider to control the transparency of the containing window.
    > alphacontrol = AlphaSlider(root,from_=20,to=100)
    """

    def __init__(self, master,*args,**kwargs):
        # Set the slider scale, orientation, and label if unspecified
        if 'from_' not in kwargs:
            kwargs['from_'] = 20
        if 'to' not in kwargs:
            kwargs['to'] = 100
        if 'orient' not in kwargs:
            kwargs['orient'] = tk.HORIZONTAL
        ttk.Scale.__init__(self,master,*args,**kwargs)
        self.containing_window = self.winfo_toplevel()
        # self.set(self.get_alpha_of_window()) # set the default slider value
        # make the slider set the window alpha
        self.config(command = lambda e:self.update_value(int(self.get())/100))
        self.set(100)

    def get_alpha_of_window(self):
        wm_status = self.containing_window.wm_attributes()
        cur_alpha = wm_status[wm_status.index('-alpha') + 1]
        return cur_alpha

    def update_value(self,new_alpha):
        self.containing_window.wm_attributes('-alpha',new_alpha)



# ================================================================

class Navbar(tk.LabelFrame):
    """Navigation panel on the left side of the main page"""

    def __init__(self, parent, *args, **kwargs):
        tk.LabelFrame.__init__(self, parent, *args, **kwargs)
        tk.Label(self, text="this is the labelframe").pack()

# ================================================================

class Toolbar(tk.LabelFrame):
    """Ribbon at the top of the main page"""

    def __init__(self, parent, *args, **kwargs):
        tk.LabelFrame.__init__(self, parent, *args, **kwargs)
        self.backButton = tk.Button(self, text="BACK", command=self.on_back_button)
        self.forwardButton = tk.Button(self, text="FORWARD", command=self.on_forward_button)
        self.backButton.pack(side='left', expand=False)
        self.forwardButton.pack(side='left', expand=False)

    def on_back_button(self):
        raise NotImplementedError

    def on_forward_button(self):
        raise NotImplementedError

# ================================================================

class Statusbar(tk.LabelFrame):
    """Bar at the bottom of the main page that
    displays the  current status of various aspects of the state"""

    def __init__(self, parent, *args, **kwargs):
        tk.LabelFrame.__init__(self, parent, *args, **kwargs)
        self.pinButton = PinButton(self,text='Pin window')
        self.pinButton.pack(side='right')
        self.alphacontrol = AlphaSlider(self)
        self.alphacontrol.pack(side='right')

# ================================================================

class Main(tk.LabelFrame):
    """Body window of the main program"""

    def __init__(self, parent, *args, **kwargs):
        """Constructor for the main program window"""
        tk.LabelFrame.__init__(self, parent, *args, **kwargs)

# ================================================================

class MainApplication(tk.Frame):
    """Highest level in the main program window"""

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # ============== Subparts of the App Go Here
        self.statusbar = Statusbar(self, text="Statusbar")
        self.toolbar = Toolbar(self, text="Toolbar")
        self.navbar = Navbar(self, text="NavBar")
        self.main = Main(self, text="Main")

        self.statusbar.pack(side="bottom", fill="x")
        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)

        # ============== Add the menubar

        self.menubar = menubar = tk.Menu(self.parent)
        self.parent.config(menu=self.menubar)

        # Add file menu
        self.filemenu = tk.Menu(menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open", command=self.on_menu_openfile)
        self.filemenu.add_command(label="Save", command=self.on_menu_savefile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.parent.quit)

        # Add View Menu
        self.viewMenu = tk.Menu(menubar, tearoff=0)
        self.menubar.add_cascade(label="View", menu=self.viewMenu)

        # Add Edit Menu
        self.editmenu = tk.Menu(menubar, tearoff=0)
        self.editmenu.add_command(label="Cut", command=self.on_menu_cut)
        self.editmenu.add_command(label="Copy", command=self.on_menu_copy)
        self.editmenu.add_command(label="Paste", command=self.on_menu_paste)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        # Add Help Menu
        self.helpmenu = tk.Menu(menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.on_menu_about)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

    def on_menu_openfile(self):
        raise NotImplementedError

    def on_menu_savefile(self):
        raise NotImplementedError

    def on_menu_cut(self):
        raise NotImplementedError

    def on_menu_copy(self):
        raise NotImplementedError

    def on_menu_paste(self):
        raise NotImplementedError

    def on_menu_about(self):
        raise NotImplementedError

# ================================================================

def main():
    root = tk.Tk()
    mainapp = MainApplication(root)
    mainapp.pack(side=tk.TOP, fill="both", expand=True)
    root.mainloop()


if __name__ == '__main__':
    main()