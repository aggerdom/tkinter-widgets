__author__ = 'alex'
import tkinter as tk
from itertools import cycle


class MyText(tk.Text):
    """Extends tk.Text to add scrollbars.

    .. py:function::
        MyText(master[, scrollbars=xy])

        @param master:
        @type master: tk.Frame
        @param scrollbars: Controls which scrollbars to include

            "x"
                creates scrollbar in x direction

            "y"
                creates scrollbar in y direction

            "xy"
                creates both x and y scrollbars

            None
                creates no scrollbars
        @type scrollbars: [str | None]
        @return: textwidget
        @rtype: tk.Text
    """

    def __init__(self, master, packside="left", scrollbars="xy", wrap=tk.NONE, ):
        """
        Constructor for MyText

         MyText(master[, scrollbars=
        """

        tk.Text.__init__(self, master)
        self.master = master
        self.scrollbarflag = scrollbars
        self.add_scrollbars()
        self.config(wrap=wrap)
        self.pack(fill="both", side=packside, expand=True)

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

    def clear_text(self):
        """Clears all text from the text widget"""
        self.delete("1.0", "end")


colorcycle = cycle(["red", "green", "blue"])
from functools import partial


def framefactory(master, text=None):
    """

    :param master: widget to place the frame into
    :type master:
    :param text: controls whether the frame will have
    :type text:
    :return:
    :rtype:
    """
    master = master
    if text is not None:
        labeltext = text
        frametype = partial(tk.LabelFrame, text=labeltext)
    else:
        frametype = tk.Frame
    return frametype


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


if __name__ == '__main__':
    root = tk.Tk()
    base = ScrollFrame(root)
    base.pack()
    base.add_scrollbars()
    text = tk.Text(base)
    text.pack()
    root.mainloop()
