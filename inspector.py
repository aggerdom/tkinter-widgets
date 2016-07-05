import tkinter as tk

# Todo: Validation function to determine that a window is root
def is_root(root):
    return True

def get_window_stack(root):
    """Takes a root node, and returns a list of windows
    from bottom of the window stack to the top of the window stack.

    C.F. http://www.tkdocs.com/tutorial/windows.html
    """
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

class InspectorPopup(tk.Toplevel):
    def __init__(self,master):
        pass
    def get_widget_with_focus(self):
        return w.focus_get()
    def set_focus_to_follow_mouse(self):
        w.tk_focusFollowsMouse()
    def undo_focus_follow_mouse(self):
        m = "I have yet to find a good way of undoing this, " \
            "and John Shipman's Tkinter reference suggests there is not" \
            "one, but for now I'm leaving this here for further research"
        raise NotImplementedError(m)
