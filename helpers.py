import tkinter as tk
from PIL import ImageTk, Image

def make_tk_image(imagepath):
    """
    Opens and reads in an image to display in tk widgets.
    Example:
        >>> root = tk.Tk()
        >>> img=make_tk_image(imagepath)
        >>> label=tk.Label(root,image=img)
        >>> label.pack()
    """
    return ImageTk.PhotoImage(Image.open(imagepath))


def get_root(widget):
    """Takes any tkinter widget and returns the root"""
    return widget.nametowidget('.')


def true_terminate(widget):
    """Exits tkinter and then exits python application"""
    widget.nametowidget('.').destroy()
    from sys import exit
    exit()


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

# TODO: Add multiscreen support

def get_screensize():
    """Return the size of the window
    Returns: (width, height) tuple"""
    root = tk.Tk()
    root.withdraw()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    return (width, height)

# ============== Functions to get information about widgets


def get_window_of_widget(widget):
    """Find the window that contains a widget"""
    containing_window = widget.winfo_toplevel()
    return containing_window


def get_window_stack(window):
    """Takes a root node, and returns a list of windows
    from bottom of the window stack to the top of the window stack.

    C.F. http://www.tkdocs.com/tutorial/windows.html
    """
    root = window.nametowidget('.')
    stackorder = root.tk.eval('wm stackorder ' + str(root)).split()
    stackorder = [root.nametowidget(w) for w in stackorder]
    return stackorder


def window_is_above(w1, w2):
    """
    Returns whether window w1 is above window w2 in the window stackorder.
    Credit: c.f. http://www.tkdocs.com/tutorial/windows.html
    """
    root = w1.nametowidget('.')  # find the root window to get full stackorder
    return (root.tk.eval('wm stackorder ' + str(w1) + ' isabove ' + str(w2))) == '1'

def get_bindings(widget):
    # See further http://tkinter.unpythonic.net/wiki/Events
    bindings = defaultdict(dict)
    for tag in widget.bindtags():
        bindings[tag] = dict()
        for binding in widget.bind_class(tag):
            bindings[tag][binding] = []
            bound_function_string = widget.bind(binding)
            if len(bound_function_string) > 0:
                bound_funcs = get_bound_functions(bound_function_string)
                bindings[tag][binding].extend(bound_funcs)
    return bindings


def get_bound_functions(current_callback: str):
    """
    After getting the Tcl code for a procedure associated with a widget using
    `widget.bind(<SomeEvent>)` passing the code to this function will return a
    handle for any python callbacks bound to that event.

    The naming convention used in tkinter as of current is of the form
          "id(<CallWrapper Instance>)"  + function_name

    Luckily however on cpython implementations, the id is it's memory address.
    So we can take the Tcl code used by the command, and then use its memory address to get the CallWrapper
    and return its function handle.

    ======== Examples of commands defined in tkinter.

    ::
      'if {"[4560616<lambda> %# %b %f %h %k %s %t %w %x %y %A %E %K %N %W %T %X %Y %D]" == "break"} break\n'
      'if {"[7780752on_right_press %# %b %f %h %k %s %t %w %x %y %A %E %K %N %W %T %X %Y %D]" == "break"} break\n"
    """

    segments = [seg for seg in current_callback.split("\n") if seg != '']

    # Find functions bound in the callback
    found_callbacks = []

    for segment in segments:
        match = re.search(r'if {"\[(\d+)([^\ ]+)', segment)
        address = match.group(1)
        fname = match.group(2)

        # Address -> CallWrapper
        callwrapper = ctypes.cast(int(address), ctypes.py_object).value.__self__
        found_callbacks.append(callwrapper.func)

    return found_callbacks


def destroy_root(widget):
    widget.nametowidget('.').destroy()


# ============== Functions to control window properties

def make_always_on_top(tkwindow):
    tkwindow.wm_attributes('-topmost', 1)


def make_not_always_on_top(tkwindow):
    tkwindow.wm_attributes('-topmost', 0)


def toggle_always_on_top(tkwindow):
    opposite_state = tkwindow.wm_attributes('-topmost') == False
    tkwindow.wm_attributes('-topmost', opposite_state)


def adjust_alpha(tkwindow, percentage, minval=0.2):
    change = percentage
    curval = tkwindow.wm_attributes('-alpha')
    newval = curval + change
    if newval > 1:
        tkwindow.wm_attributes('-alpha', 1.0)
    elif newval < minval:
        tkwindow.wm_attributes('-alpha', minval)
    else:
        tkwindow.wm_attributes('-alpha', newval)
