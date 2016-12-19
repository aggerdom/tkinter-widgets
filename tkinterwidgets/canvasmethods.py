import tkinter as tk
from operator import attrgetter

def apply(f,*args,**kwargs):
    return f(*args,**kwargs)

class MyCanv(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        tk.Canvas.__init__(self, master, *args, **kwargs)
        self.bind("<Enter>", lambda e: print("Enter"))
        self.bind("<Button-1>",lambda e: apply(self.create_rectangle(get_)
        # self.create_arc
        # self.create_bitmap
        # self.create_image
        # self.create_line
        # self.create_oval
        # self.create_triangle
        # self.create_polygon
        # self.create_rectangle
        # self.create_text
        # self.create_window

    def draw_bounding_box(self,id):
        bbox_coords = self.bbox(id)
        bbox = self.create_rectangle(*bbox_coords,dash=(3,5))
        return bbox

    def create_circle(self, center_x, center_y,
                      radius, disabledwidth=1):
        x0, y0 = center_x - radius, center_y - radius
        x1, y1 = center_x + radius, center_y + radius
        x1, y1 = x1-disabledwidth, y1-disabledwidth
        return self.create_oval(x0,y0,x1,y1)

    def create_equilateral_triangle(self,centerx,centery,
                                    height,*args,rotation=0,**kwargs):
        raise NotImplementedError

if __name__ == '__main__':
    root = tk.Tk()
    canv = MyCanv(root)
    canv.pack()
    inspect = Inspector(root)
    canv.mainloop()
