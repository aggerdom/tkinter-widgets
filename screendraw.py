import tkinter as tk
from widgets import *
from helpers import (adjust_alpha,destroy_root,
                     get_window_of_widget,make_always_on_top,
                     make_not_always_on_top, get_root,
                     get_screensize)
import pyautogui


class TranparentBase(tk.Toplevel):
    def __init__(self, master, *args, trans_color="#2b4404", **kwargs):
        tk.Toplevel.__init__(self, master, *args, **kwargs)
        self.tranparent_color = trans_color
        self.overrideredirect(True)
        self.lift()
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-transparentcolor", self.tranparent_color)
        self.add_close_button()
        self.make_fullscreen()

    def add_close_button(self, bg='grey'):
        self.closebutton = tk.Button(self, text="X", bg=bg, command=lambda: destroy_root(self))
        self.closebutton.pack(side='right')

    def make_fullscreen(self,actually_fullscreen=False):
        w,h = get_screensize()
        self.geometry('%dx%d-0-30'%(w,h))


class TransCanv(tk.Canvas):
    def __init__(self, master, *args, trans_color="#2b4404", **kwargs):
        tk.Canvas.__init__(self, master, *args, **kwargs)
        self.trans_color = trans_color
        self.make_canvas_transparent()
        self.bind('<Button-1>', self.draw_rect)
        self.bind('<Button-3>', self.click_through)
        self.bind("<space>",lambda e:pyautogui.click(duration=2))
        self.bind('<Enter>',lambda e:print('Entering'))
        self.bind('<Enter>',lambda e:self.update_idletasks())
        self.bind('<Leave>',lambda e:print('leaving'))
        self.bind('<Button-1>', lambda e: print('b1'), add='+')
        self.bind('<Button-3>', lambda e: print('b3'), add='+')
        # self.bind('<Button-3>', lambda e: self.update_idletasks, add='+')

    def make_canvas_transparent(self):
        self['bg'] = self.trans_color

    def draw_rect(self, event, *args, fill='green', **kwargs):
        x = event.x
        y = event.y
        self.create_rectangle(x, y, x + 100, y + 100, fill=fill)

    def draw_transparent_pixel(self, event, *args, **kwargs):
        x = event.x
        y = event.y
        self.create_rectangle(x, y, x + 100, y + 100,
                              fill=self.trans_color)

    def click_through(self,event):
        win = get_window_of_widget(self)
        win.state("withdrawn")
        get_root(self).after_idle(lambda: win.state('normal'))
        try:
            pyautogui.click(clicks=2)
            pyautogui.typewrite("e")
            print('clicked through')
        except PermissionError:
            print('click through failed')

def test():
    root = tk.Tk()
    root.withdraw()
    kill_button = KillButton(root)
    drawwin = TranparentBase(root)
    drawcanv = TransCanv(drawwin, bg="green")
    drawcanv.pack(expand=True,fill='both')
    drawcanv.create_rectangle(3, 3, 3, 3)
    root.mainloop()

# Todo: Adapt this to use a canvas with the transparency color, and add drawing methods
def example_of_transparent_window():
    root = tk.Tk()
    root.config(bg='white')
    closebutton = tk.Button(root, text="X", bg="grey", command=lambda: root.destroy())
    closebutton.pack(side='right')
    label = tk.Label(root, text="I'm a label", bg='white')
    label2 = tk.Label(root, text="Im not transparent", bg='yellow')
    label2.pack()
    root.overrideredirect(True)
    root.geometry("+250+250")
    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-transparentcolor", "white")
    label.pack()
    root.mainloop()


if __name__ == '__main__':
    # canv = tk.Canvas()
    # canv.bind("<Button-1>",lambda e:print("Button 1"))
    # canv.bind('<Button-3>',lambda e:print("Button 3"))
    # canv['bg']='yellow'
    # canv.pack()
    # canv.mainloop()
    test()
