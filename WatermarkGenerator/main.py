from tkinter import *
from tkinter import filedialog
from PIL import Image, EpsImagePlugin
#must have Ghostscript downloaded for working with postscript image files (external to python)

GREY = "#cdd1d1"
BLUE = "#e1F7F7"
WATERMARK_COLOR = "#A1A1A1"
FONT_NAME = "Calibri"
FONT_SIZE = 13
PHOTO_WIDTH = None
PHOTO_HEIGHT = None
PHOTO_IMAGE = None #This is necessary because tkinter doesn't save this image within the function
CANVAS_WIDTH = None
CANVAS_HEIGHT = None

# ---------------------------- Image Functions ------------------------------- #
def upload_image():
    global PHOTO_WIDTH, PHOTO_HEIGHT, PHOTO_IMAGE
    PHOTO_WIDTH = int(width_input.get())
    PHOTO_HEIGHT = int(height_input.get())
    if PHOTO_WIDTH > 900:
        CANVAS_WIDTH = 900
    else:
        CANVAS_WIDTH = PHOTO_WIDTH
    if PHOTO_HEIGHT > 500:
        CANVAS_HEIGHT = 500
    else:
        CANVAS_HEIGHT = PHOTO_HEIGHT
    canvas.configure(width=CANVAS_WIDTH, height=CANVAS_HEIGHT,highlightthickness=0,
                     scrollregion=(0, 0, PHOTO_WIDTH, PHOTO_HEIGHT)) #,
    filename = filedialog.askopenfilename()
    PHOTO_IMAGE = PhotoImage(file=filename)
    canvas.create_image((0, 0), image = PHOTO_IMAGE, anchor = "nw")

def clear_image():
    global PHOTO_WIDTH, PHOTO_HEIGHT
    PHOTO_WIDTH = None
    PHOTO_HEIGHT = None
    width_input.delete(0, "end")
    width_input.insert(0, "0")
    height_input.delete(0, "end")
    height_input.insert(0, "0")
    canvas.delete("all")

def add_watermark():
    watermark_text = canvas.create_text(int(PHOTO_WIDTH/2), int(PHOTO_HEIGHT/2), text = "WATERMARK",
                                        font = (FONT_NAME, int(PHOTO_WIDTH/10), "bold"), fill = WATERMARK_COLOR)

def save_image():
    canvas.update()
    EpsImagePlugin.gs_binary = r"C:\Program Files\gs\gs10.06.0\bin\gswin64.exe"
    filesave = filedialog.asksaveasfilename(defaultextension=".ps")
    canvas.postscript(file=filesave, colormode='color', width = PHOTO_WIDTH, height = PHOTO_HEIGHT)
    ps_img = Image.open(filesave)
    filesave = filesave.replace(".ps","")
    ps_img.save(filesave + ".png")
# ---------------------------------------------------------------------------- #

window = Tk()
window.title("Watermark Generator")
window.config(padx = 100, pady = 50, bg=BLUE)

#Directions text
directions_label = Label(text="Enter image dimensions:", font = (FONT_NAME,FONT_SIZE), background=BLUE)
directions_label.grid(column=1, row=0, columnspan = 2)

spacer0 = Label(text="     ", font = (FONT_NAME,FONT_SIZE), background=BLUE)
spacer0.grid(column=0, row=1, columnspan = 4)

#Width label
width_label = Label(text="Width:", font = (FONT_NAME,FONT_SIZE), background=BLUE, width = 10)
width_label.grid(column=0, row = 2, sticky = "e")

#Width input
width_input = Entry(width=15, font = (FONT_NAME,FONT_SIZE))
width_input.insert(0, "0")
width_input.grid(column=1, row=2, columnspan = 1,sticky = "w")

#Height label
height_label = Label(text="Height:", font = (FONT_NAME,FONT_SIZE), background=BLUE, width = 10)
height_label.grid(column=2, row = 2, sticky = "e")

#Height input
height_input = Entry(width=15, font = (FONT_NAME,FONT_SIZE))
height_input.insert(0, "0")
height_input.grid(column=3, row=2, columnspan = 1, sticky = "w")

spacer1 = Label(text="     ", font = (FONT_NAME,FONT_SIZE), background=BLUE)
spacer1.grid(column=0, row=3, columnspan = 4)

#upload button
upload_button = Button(text = "Upload Image", command = upload_image, bg = "white", width = 15, font = (FONT_NAME,FONT_SIZE))
upload_button.grid(column=0, row=4, columnspan = 2)

#clear button
clear_button = Button(text = "Clear Image", command = clear_image, bg = "white", width = 15, font = (FONT_NAME,FONT_SIZE))
clear_button.grid(column=3, row=4, columnspan = 2)

#canvas widget allows layering of widgets
h = Scrollbar(window, orient="horizontal")
v = Scrollbar(window, orient="vertical")
canvas = Canvas(window, width=500, height=400, bg=BLUE, highlightthickness=0,scrollregion=(0, 0, 50, 40),
                yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview
canvas.grid(column=1, row=5, columnspan=4)
h.grid(column=1, row=6, columnspan=4, sticky=("w","e"))
v.grid(column=0, row=5, sticky=("n","s","e"))
window.grid_columnconfigure(0, weight=2)
window.grid_rowconfigure(5, weight=2)

#add watermark button
watermark_button = Button(text = "Add Watermark", command = add_watermark, bg="white", width = 15, font = (FONT_NAME,FONT_SIZE))
watermark_button.grid(column=0, row=7, columnspan = 2)

#save button
save_button = Button(text = "Save Image", command = save_image, bg="white", width = 15, font = (FONT_NAME,FONT_SIZE))
save_button.grid(column=3, row=7, columnspan = 2)

window.mainloop()