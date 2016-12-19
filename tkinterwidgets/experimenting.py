import tkinter as tk

# Q1: Can we find a master list of widgets?
# Q2: Can we repack a widget in another window
# Q3: Can you clone/deepcopy a widget? A window?
# Q4: What methods can be easily lifted to a getter/setter api?
# Q5: How should I emphasise the inspected widget (needs developed inspector.py)

# Q6: Does widget opacity follow parent or window it is packed in
# Answer: Not in a strait forwards way
def q6():
    root = tk.Tk()
    root.withdraw()
    # setup host
    hostwindow = tk.Toplevel(root)
    hostwindow.title('host')
    hostframe = tk.LabelFrame(hostwindow,text='hostframe')
    hostframe.pack()
    # setup parent
    parentwindow = tk.Toplevel(root)
    parentwindow.title('parent')
    testlabel = tk.Label(parentwindow,text="Can you see me?")
    testlabel.pack(in_=hostframe)
    # _tkinter.TclError: can't pack .6740336.6794192 inside .6615408.6617200
    root.mainloop()

class PopUp(tk.Toplevel):
    def __init__(self,master,*args,**kwargs):
        tk.Toplevel.__init__(self, master, *args, **kwargs)
        self.transparent_color = 'white'
        # set the background to the color to make transparent
        self.config(bg=self.transparent_color)
        self.closebutton = tk.Button(self,text="X",bg="grey",command=lambda:self.destroy())
        self.closebutton.pack(side='right')
        self.overrideredirect(True)
        self.lift()
        self.wm_attributes('-topmost',True)
        self.wm_attributes("-transparentcolor", self.transparent_color)


# http://stackoverflow.com/a/22106858
# Todo: Adapt this to use a canvas with the transparency color, and add drawing methods
def example_of_transparent_window():
    root = tk.Tk()
    root.config(bg='white')
    closebutton = tk.Button(root,text="X",bg="grey",command=lambda:root.destroy())
    closebutton.pack(side='right')
    label = tk.Label(root, text="I'm a label", bg='white')
    label2 = tk.Label(root, text="Im not transparent",bg='yellow')
    label2.pack()
    root.overrideredirect(True)
    root.geometry("+250+250")
    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-transparentcolor", "white")
    label.pack()
    root.mainloop()

# How to use virtual events
def virtual_events():
    root = tk.Tk()
    root.bind("<<foo>>",print('foo'))
    root.mainloop()


if __name__ == '__main__':
    # q6()
    # example_of_transparent_window()
    virtual_events()