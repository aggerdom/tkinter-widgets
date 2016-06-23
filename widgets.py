from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
    import tkMessageBox as messagebox
    # import tkColorChooser as colorchooser
    # import tkCommonDialog as commondialog
    # import tkFont as font
elif version_info.major >= 3:
    import tkinter as tk
    from tkinter import messagebox
    # from tkinter import colorchooser
    # from tkinter import commondialog
    # from tkinter import font


class PinButton(tk.Button):
    """Button to pin the window containing the widget to
    be always on top"""

    def __init__(self, master, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)
        self.master = master
        self.containing_window = self.winfo_toplevel()
        self.config(command=lambda: self.toggle_always_on_top(self.containing_window))

    @staticmethod
    def toggle_always_on_top(tkwindow):
        is_on = tkwindow.wm_attributes('-topmost')
        if is_on:
            tkwindow.wm_attributes('-topmost', 0)
        else:
            tkwindow.wm_attributes('-topmost', 1)

class AlphaSlider(tk.Scale):
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
        tk.Scale.__init__(self,master,*args,**kwargs)
        self.containing_window = self.winfo_toplevel()
        self.set(100)
        self._alpha = 100
        # make the slider set the window alpha
        self.config(command = lambda e:setattr(self,'alpha', self.get()))
    
    @property
    def alpha(self):
        return self._alpha
    
    @alpha.setter
    def alpha(self,value):
        if type(value) == int:
            # dealing with value specified as a percentage
            new_alpha = value/100.0
        elif type(value)==float and (0 <= value <= 1):
            new_alpha = value
        else:
            raise ValueError("Alpha value for window must either be float (0 < v < 1) or an integer percentage")
        self.containing_window.wm_attributes('-alpha',new_alpha)
        self._alpha = value

class TTKAlphaSlider(ttk.Scale):
    """
    ttk version of the AlphaSlider widget that controls the transparency of the containing window.

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
        self.set(100) # set the intitial value
        self._alpha = 100
        # make the slider set the window alpha
        self.config(command = lambda e: setattr(self,'alpha', int(self.get())))
    
    @property
    def alpha(self):
        return self._alpha
    
    @alpha.setter
    def alpha(self,value):
        if type(value) == int:
            # dealing with value specified as a percentage
            new_alpha = value/100.0
        elif type(value)==float and (0 <= value <= 1):
            new_alpha = value
        else:
            raise ValueError("Alpha value for window must either be float (0 < v < 1) or an integer percentage")
        self.containing_window.wm_attributes('-alpha',new_alpha)
        self._alpha = value
