import tkinter as tk
from PIL import ImageTk, Image

def make_tk_image(imagepath):
    """
    Opens and reads in an image to display in tk widgets.
    Example:
        >>> root = tk.Tk()
        >>> img=make_tk_image(imagepath)
        >>> label=tk.Label(root,image=img)
        >>> label.pack()
    """
    return ImageTk.PhotoImage(Image.open(imagepath))

def get_root(widget):
    """Takes any tkinter widget and returns the root"""
    return widget.nametowidget('.')

def true_terminate(widget):
    """Exits tkinter and then exits python application"""
    widget.nametowidget('.').destroy()
    from sys import exit
    exit()


def get_clipboard_contents():
    """Helper function to get the current contents of the clipboard as a string """
    root = tk.Tk()
    root.withdraw()
    cliptext = root.clipboard_get()
    root.destroy()
    return cliptext


def clip_filter():
    """
    Generator that will yield the contents of the clipboard
    only if the contents of the clipboard have changed since next
    was previously called from the generator.
    """
    old_contents = get_clipboard_contents()
    yield old_contents
    while True:
        new_contents = get_clipboard_contents()
        if new_contents != old_contents:
            old_contents = new_contents
            yield old_contents
        else:
            yield None

# TODO: Add multiscreen support
# use
def get_screensize():
    """Return the size of the window
    Returns: (width, height) tuple"""
    root=tk.Tk()
    root.withdraw()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    return (width,height)

# ============== Functions to get information about widgets

def get_window_of_widget(widget):
    """Find the window that contains a widget"""
    containing_window = widget.winfo_toplevel()
    return containing_window

def get_window_stack(window):
    """Takes a root node, and returns a list of windows
    from bottom of the window stack to the top of the window stack.

    C.F. http://www.tkdocs.com/tutorial/windows.html
    """
    root = window.nametowidget('.')
    stackorder = root.tk.eval('wm stackorder '+str(root)).split()
    stackorder = [root.nametowidget(w) for w in stackorder]
    return stackorder

def window_is_above(w1,w2):
    """
    Returns whether window w1 is above window w2 in the window stackorder.
    Credit: c.f. http://www.tkdocs.com/tutorial/windows.html
    """
    root = w1.nametowidget('.') # find the root window to get full stackorder
    return (root.tk.eval('wm stackorder '+str(w1)+' isabove '+str(w2))) == '1'

def destroy_root(widget):
    widget.nametowidget('.').destroy()


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

