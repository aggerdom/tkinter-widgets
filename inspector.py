import tkinter as tk
from helpers import get_window_stack, get_window_of_widget, destroy_root

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
