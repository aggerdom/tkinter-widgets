import tkinter as tk

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

