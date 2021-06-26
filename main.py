from tkinter import *
from tkinter import font
from tkinter import ttk

# # # # # # # # # # # GUI CONFIG # # # # # # # # # # #  #

# configure the symbols and positions of buttons in pad
BTN_SYM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=', '.', '<-', 'C']
BTN_POS = ((4, 1), (3, 1), (3, 2), (3, 3), (2, 1), (2, 2), (2, 3), (1, 1),
           (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (0, 4), (0, 3))
BTN_SQCE = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '<plus>',
            '<minus>', '<asterisk>', '<slash>', '<Return>', '<period>', '<BackSpace>']


def format_seq(z):
    if z == 'plus':
        return '+'
    elif z == 'minus':
        return '-'
    elif z == 'asterisk':
        return '*'
    elif z == 'slash':
        return '/'
    elif z == 'Return':
        return '='
    elif z == 'BackSpace':
        return '<-'
    else:
        return z


# creat the root
root = Tk()
root.title("Calculatrix")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(width=250, height=250)
root.maxsize(width=500, height=500)

# configure  the main frame
main_frame = ttk.Frame(root, padding=(5, 5, 5, 5))
main_frame.grid(column=0, row=0, sticky=(N, S, E, W))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)

# configure the dispaly frame
dispaly_frame = ttk.Frame(main_frame, padding=(5, 5, 5, 5))
dispaly_frame.grid(row=0, column=0, sticky=(N, S, E, W))
dispaly_frame.columnconfigure(0, weight=1)
dispaly_frame.rowconfigure(0, weight=1)
dispaly_frame.rowconfigure(1, weight=1)

# configure the pad frame
pad_frame = ttk.Frame(main_frame, padding=(5, 5, 5, 5))
pad_frame.grid(row=1, column=0, sticky=(N, S, E, W))
for i in [0, 1, 2, 3, 4]:
    pad_frame.rowconfigure(i, weight=1)
    pad_frame.columnconfigure(i, weight=1)

# create the buttons
btn_list = []
for i in range(18):
    btn = ttk.Button(pad_frame, text=BTN_SYM[i], command=lambda j=BTN_SYM[i]: btn_call(j))
    btn.grid(row=BTN_POS[i][0], column=BTN_POS[i][1], sticky=(N, S, E, W))
    btn_list.append(btn)

# configure fonts
entry_font = font.Font(family='Helvetica', name='entryFont', size=16, weight='bold')

# create equation display
equation_display = ttk.Label(dispaly_frame, text="0")
equation_display.grid(row=0, column=0, sticky=(N, S, E))

# create entry display
entry_display = ttk.Label(dispaly_frame, text="0", font=entry_font)
entry_display.grid(row=1, column=0, sticky=(N, S, E))

# bind events from the keyboard to the button pad callback
for i in range(17):
    root.bind(BTN_SQCE[i], lambda e: btn_call(format_seq(e.keysym)))

# change the style of the app
# s = ttk.Style()
# print(s.theme_names())
# s.theme_use('vista')
# print(s.theme_use())


# # # # # # # # # # # # CALLBACKS CONFIG # # # # # # # # # # # #
x = ['0']
y = ['0']
r = []
o = ""


def calculate():
    """ """
    global x
    global y
    global o
    global r

    r = list(str(eval(''.join(x) + o + ''.join(y))))
    x.clear()
    x.extend(r)
    y = ['0']
    o = ""


def number_call(nbr):
    global r
    if o == "":
        if x == ['0'] or r != []:
            x.clear()
            r = []
        x.append(nbr)
        entry_display.config(text=''.join(x))
    else:
        if y == ['0']:
            y.clear()
        y.append(nbr)
        entry_display.config(text=''.join(y))


def operation_call(op):
    global o

    if o != "" or y != ['0']:
        calculate()
        entry_display.config(text=''.join(x))
    o = op
    equation_display.config(text=''.join(x) + o)


def return_call():

    if y != ['0']:
        equation_display.config(text=''.join(x) + o + ''.join(y) + '=')
        calculate()
        entry_display.config(text=''.join(r))


def back_call():
    if o == "":
        if x != ['0'] and len(x) > 0:
            x.pop()
            entry_display.config(text=''.join(x))
    elif y != ['0'] and len(y) > 0:
        y.pop()
        entry_display.config(text=''.join(y))


def clear_call():
    global x
    global y
    global o
    global r
    x = ['0']
    y = ['0']
    o = ""
    r = []
    equation_display.config(text='0')
    entry_display.config(text='0')


def btn_call(tag):
    if tag in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        number_call(tag)
    elif tag in ['+', '-', '*', '/']:
        operation_call(tag)
    elif tag == '=':
        return_call()
    elif tag == '<-':
        back_call()
    elif tag == 'C':
        clear_call()


root.mainloop()
