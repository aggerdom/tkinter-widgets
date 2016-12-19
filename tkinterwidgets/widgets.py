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
    from tkinter import ttk
    # from tkinter import colorchooser
    # from tkinter import commondialog
    # from tkinter import font

from tkinterwidgets.helpers import *


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

class PinLabel(tk.Label):
    """Label to pin the window containing the widget to
    be always on top.

    Usage:
        >>> root = tk.Tk()
        >>> pinlabel = PinLabel(root)
        >>> pinlabel.pack()
    """

    def __init__(self, master, *args, img='icons/PinIcon.png', **kwargs):
        tk.Label.__init__(self, master, *args, **kwargs)
        self.master = master
        self.containing_window = self.winfo_toplevel()
        self.img = make_tk_image(img)
        self.config(image=self.img)
        self.bind('<Button-1>', lambda e: self.toggle_always_on_top())
        self.style()

    def style(self):
        cur_relief = self.config('relief')[-1]
        self.bind("<Enter>",lambda e: self.config(relief='raised'))
        self.bind('<Leave>',lambda e: self.config(relief=cur_relief))


    def toggle_always_on_top(self):
        is_on = self.containing_window.wm_attributes('-topmost')
        if is_on:
            self.containing_window.wm_attributes('-topmost', 0)
        else:
            self.containing_window.wm_attributes('-topmost', 1)


class AlphaSlider(tk.Scale):
    """
    Slider to control the transparency of the containing window.

    > alphacontrol = AlphaSlider(root,from_=20,to=100)

    """

    def __init__(self, master, *args, **kwargs):
        # Set the slider scale, orientation, and label if unspecified
        if 'from_' not in kwargs:
            kwargs['from_'] = 20
        if 'to' not in kwargs:
            kwargs['to'] = 100
        if 'orient' not in kwargs:
            kwargs['orient'] = tk.HORIZONTAL
        tk.Scale.__init__(self, master, *args, **kwargs)
        self.containing_window = self.winfo_toplevel()
        self.set(100)
        self._alpha = 100
        # make the slider set the window alpha
        self.config(command=lambda e: setattr(self, 'alpha', self.get()))

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        if type(value) == int:
            # dealing with value specified as a percentage
            new_alpha = value / 100.0
        elif type(value) == float and (0 <= value <= 1):
            new_alpha = value
        else:
            raise ValueError("Alpha value for window must either be float (0 < v < 1) or an integer percentage")
        self.containing_window.wm_attributes('-alpha', new_alpha)
        self._alpha = value


class TTKAlphaSlider(ttk.Scale):
    """
    ttk version of the AlphaSlider widget that controls the transparency of the containing window.

    > alphacontrol = AlphaSlider(root,from_=20,to=100)

    """

    def __init__(self, master, *args, **kwargs):
        # Set the slider scale, orientation, and label if unspecified
        if 'from_' not in kwargs:
            kwargs['from_'] = 20
        if 'to' not in kwargs:
            kwargs['to'] = 100
        if 'orient' not in kwargs:
            kwargs['orient'] = tk.HORIZONTAL
        ttk.Scale.__init__(self, master, *args, **kwargs)
        self.containing_window = self.winfo_toplevel()
        self.set(100)  # set the intitial value
        self._alpha = 100
        # make the slider set the window alpha
        self.config(command=lambda e: setattr(self, 'alpha', int(self.get())))

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        if type(value) == int:
            # dealing with value specified as a percentage
            new_alpha = value / 100.0
        elif type(value) == float and (0 <= value <= 1):
            new_alpha = value
        else:
            raise ValueError("Alpha value for window must either be float (0 < v < 1) or an integer percentage")
        self.containing_window.wm_attributes('-alpha', new_alpha)
        self._alpha = value


# TODO
class UrlLabel(tk.Label):
    """Label that opens a url when clicked"""

    def __init__(self, master, url, text=None, **kwargs):
        raise NotImplementedError
        if text == None:
            kwargs['text'] = url
        tk.Label.__init__(self, master, **kwargs)
        self.url = url
        self.color = 'blue'
        command = lambda: webbrowser.open(url)


class KillButton(tk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        tk.Toplevel.__init__(self, master, *args, **kwargs)
        make_always_on_top(self)
        root = self.nametowidget('.')
        self.title('Killbutton')
        root.bind('<<KillButtonHidden>>', self.lift)
        self.killbutton = tk.Button(self, text='Terminate', command=lambda: true_terminate(self), bg='red')
        self.killbutton.pack()

    def kill_tkinter(self):
        self.nametowidget('.').destroy()

    def kill_app(self):
        # Close tkinter so the tcl runtime terminates
        self.kill_tkinter()
        # Kill the python interpreter
        from sys import exit
        exit()


if __name__ == '__main__':
    root = tk.Tk()
    killbutton = KillButton(root)
    root.mainloop()
