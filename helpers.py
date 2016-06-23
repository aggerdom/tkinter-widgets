import tkinter as tk

# ============== Functions to get information about widgets

def get_window_of_widget(widget):
    """Find the window that contains a widget"""
    containing_window = widget.winfo_toplevel()
    return containing_window

# ============== Functions to control window properties

def make_always_on_top(tkwindow):
    tkwindow.wm_attributes('-topmost', 1)

def make_not_always_on_top(tkwindow):
    tkwindow.wm_attributes('-topmost', 0)

def toggle_always_on_top(tkwindow):
    is_on = tkwindow.wm_attributes('-topmost')
    if is_on:
        tkwindow.wm_attributes('-topmost', 0)
    else:
        tkwindow.wm_attributes('-topmost', 1)


def adjust_alpha(tkwindow, percentage, minval = 0.2):
    change = percentage
    curval = tkwindow.wm_attributes('-alpha')
    newval = curval + change
    if newval > 1:
        tkwindow.wm_attributes('-alpha', 1.0)
    elif newval < minval:
        tkwindow.wm_attributes('-alpha', minval)
    else:
        tkwindow.wm_attributes('-alpha', newval)



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
        if 'label' not in kwargs:
            kwargs['label'] = 'Opacity'
        tk.Scale.__init__(self,master,*args,**kwargs)
        self.containing_window = self.winfo_toplevel()
        self.set(self.get_alpha_of_window()) # set the default slider value
        # make the slider set the window alpha
        self.config(command = lambda e:self.update_value(self.get()/100))

    def get_alpha_of_window(self):
        wm_status = self.containing_window.wm_attributes()
        cur_alpha = wm_status[wm_status.index('-alpha') + 1]
        return cur_alpha

    def update_value(self,new_alpha):
        self.containing_window.wm_attributes('-alpha',new_alpha
