import tkinter as tk
from tkinter import ttk
from collections import defaultdict
import re
import ctypes

from tkinterwidgets.helpers import (get_window_stack, get_window_of_widget,
                                    destroy_root)


def _traverse(widget):
    """ Used for helping to create TreeView of widgets in a program.
    Returns an iterator of (parentwidget, childwidget) of any widgets
    that have the provided widget as an ancestor.
    """
    for child in widget.children.values():
        yield (widget, child)
        yield from _traverse(child)


class ScrollFrame(tk.Frame):
    def __init__(self, master, text=None, scrollbarflag="y"):
        tk.Frame.__init__(self, master)
        self.scrollbarflag = scrollbarflag
        self.master = master
        if text is not None:
            self.labeltext = text
            self.frametype = tk.LabelFrame
        else:
            self.frametype = tk.Frame
        self.frametype.__init__(self, master)

    def add_scrollbars(self):
        """Checks whether x or y are in """
        if self.scrollbarflag is None:
            return
        configdict = dict()
        if "x" in self.scrollbarflag:
            self.xscrollbar = tk.Scrollbar(self.master, orient=tk.HORIZONTAL)
            self.xscrollbar.pack(side="bottom", fill="x")
            self.xscrollbar.config(command=self.xview)
            configdict.update(dict(xscrollcommand=self.xscrollbar.set))
        if "y" in self.scrollbarflag:
            self.yscrollbar = tk.Scrollbar(self.master)
            self.yscrollbar.pack(side="right", fill="y")
            self.yscrollbar.config(command=self.yview)
            configdict.update(dict(yscrollcommand=self.yscrollbar.set))
        self.config(**configdict)


def get_info_from_widget(w):
    info = dict()
    info['is_leaf'] = w.children == {}
    for key, value in w.config():
        info['config/{}'.format(key)] = str(value)
    return info


def create_info_frame(widget, master):
    info_frame = tk.Frame(master)
    leafs = [(oid, w) for w in widget.children.items() if w.children == {}]
    nodes = [(oid, w) for w in widget.children.items() if w.children == {}]
    for id, widget in leafs:
        text = "{}:{}".format()
    for id, widget in nodes:
        has_children = len(widget.children) != 0
        widget_type = str(type(widget))
        frame = tk.LabelFrame(self.mainframe, text=id)
        frame.pack()
        has_children = tk.Label(frame, text="Has Children: {}".format(has_children))
        has_children.pack()


class Inspector(tk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        tk.Toplevel.__init__(self, master, *args, **kwargs)
        self.title('Inspector')
        self.mainframe = ScrollFrame(self)
        self.mainframe.pack(expand=True, fill='both')
        self.subframes = []
        self.wm_attributes('-toolwindow', 1)
        # for debugging
        self.populate_frame()

    def populate_frame(self):
        root = self.nametowidget('.')
        for id, widget in root.children.items():
            has_children = len(widget.children) != 0
            widget_type = str(type(widget))
            frame = tk.LabelFrame(self.mainframe, text=id)
            frame.pack()
            has_children = tk.Label(frame, text="Has Children: {}".format(has_children))
            has_children.pack()

    def add_subframe(self, label=None):
        if label:
            subframe = tk.LabelFrame(self.mainframe, text=label)
        else:
            subframe = tk.LabelFrame(self.mainframe)
        subframe.pack(fill='X')
        self.subframes.append(subframe)


class InspectorPopup(tk.Toplevel):
    def __init__(self, master):
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
