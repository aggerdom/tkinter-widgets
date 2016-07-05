import tkinter as tk

class TranparentBase(tk.Toplevel):
    def __init__(self,master,*args,trans_color="#2b4404",**kwargs):
        tk.Toplevel.__init__(self, master, *args, **kwargs)
        self.tranparent_color = trans_color
        self.overrideredirect(True)
        self.lift()
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-transparentcolor", self.tranparent_color)
        self.add_close_button()

    def add_close_button(self,bg='grey'):
        self.closebutton = tk.Button(self,text="X",bg=bg,command=lambda:self.destroy())
        self.closebutton.pack(side='right')

class TransCanv(tk.Canvas):
    def __init__(self,master,*args,trans_color="#2b4404",**kwargs):
        tk.Canvas.__init__(self, master, *args, **kwargs)
        self.trans_color=trans_color
        self.bind('<Button-1>', self.draw_transparent_pixel)

    def draw_transparent_pixel(self,event,*args,**kwargs):
        x = event.x
        y = event.y
        self.create_rectangle(x,y,x+100,y+100,fill=self.trans_color)


def test():
    root = tk.Tk()
    root.withdraw()
    drawwin = TranparentBase(root)
    drawcanv = TransCanv(drawwin,bg="green")
    drawcanv.pack()
    drawcanv.create_rectangle(3,3,3,3)
    root.mainloop()

test()
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