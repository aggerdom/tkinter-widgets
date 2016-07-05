# tkinter-widgets

Collection of tkinter widgets and helper functions for things such as setting a window to always on top

# Widgets

- PinButton
    - Button to pin the window containing the widget to be always on top
- TTKPinButton
    - ttk version of PinButton, looks slightly nicer

- AlphaSlider(tk.Scale):
    - Slider to control the transparency of the containing window.
        > alphacontrol = AlphaSlider(root,from_=20,to=100)



# Useful resources for tkinter development

## General Tkinter

- [TkDocs](http://www.tkdocs.com/index.html)
- [Effbot Tkinterbook](http://effbot.org/tkinterbook)
- [Thinking Tkinter](http://thinkingtkinter.sourceforge.net/)
- [(New Mexico Tech) Tkinter 8.5 reference: a GUI for Python](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html)
- [Tutorials Point](http://www.tutorialspoint.com/python/tk_menu.htm)
- [Unpythonic.net: Tkinter Wiki](http://tkinter.unpythonic.net/wiki/)


## Tix

- [PythonDocs: tix](https://docs.python.org/3.3/library/tkinter.tix.html)


### ttk stuff

- [PythonDocs: ttk](https://docs.python.org/3/library/tkinter.ttk.html)
- [Colors with names (tcl docs)](http://wiki.tcl.tk/16166)


### Misc

[Structuring Tkinter App](http://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application)

Todo:

- Bitmap Pin Image for PinButton

# Mixins for development
- Widget Explorer
    - Description: Tool window that displays information about the widget the mouse is over
    - Needs:
        - Way of getting a handle for the window the cursor is over (preferably not using focus follows mouse)
- Helpers to embed widets in canvas
- Stuff for treeview
- Devhelp toplevel with resources and docs from around the net
- 

<!-- http://python-3-patterns-idioms-test.readthedocs.io/en/latest/index.html -->