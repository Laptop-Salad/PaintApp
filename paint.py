import tkinter
from tkinter import messagebox
from PIL import Image, ImageDraw

# Variables
brush = False
brush_colour = "black"
img_brush_colour = (0,0,0)
brush_size = 5
filename = ""

colours = [
    ["yellow"],
    ["orange"],
    ["red"],
    ["blue"],
    ["purple"],
    ["pink"],
    ["black"],
    ["green"],
    ["brown"],
    ["grey"],
    ["white"]
]

rgb_colours = {
    "yellow": [(255,255,0)],
    "orange": [(255,69,0)],
    "red": [(255,0,0)],
    "blue": [(0,0,255)],
    "purple": [(128,0,128)],
    "pink": [(255,182,193)],
    "black": [(0,0,0)],
    "green": [(0,255,0)],
    "brown": [(128,0,0)],
    "grey": [(128,128,128)],
    "white": [(255,255,255)]
}

# Functions
def save_img():
    global filename
    name = filename_entry.get()
    
    if len(name) == 0:
        messagebox.showerror("Filename Error", "ERROR: Cannot save image without a name")
        return
        
    image_name = name + ".png"
    img.save(image_name, "PNG")

    messagebox.showinfo("Image Saved", "Image Saved")
    
    
def change_colour(colour):
    global brush_colour
    
    brush_colour = colour[0]
    
def toggle_brush(event):
    global brush
    brush = not brush

def change_brush_size(size):
    global brush_size
    brush_size += size

    brush_size_lbl.config(text=brush_size)

def draw(event):
    if brush:
        x1, y1 = event.x, event.y
        x2, y2 = x1+brush_size, y1+brush_size
        
        canvas.create_oval(x1, y1, x2, y2, fill=brush_colour, outline=brush_colour)
        draw = ImageDraw.Draw(img)
        draw.ellipse((x1, y1, x2, y2), rgb_colours[brush_colour][0], None, (brush_size*10))


# Create frame
root = tkinter.Tk()
root.title('Paint')
root.geometry('600x600')

# Create and place canvas
canvas = tkinter.Canvas(root, bg="white")
canvas.grid(column=1, row=1, columnspan=20, rowspan=20)

# Create image
img = Image.new("RGB", (400, 300), (255,255,255))

# Create and place buttons
buttons = []
col = 2
rw = 22
for i in range(len(colours)):
    button = tkinter.Button(root, bg=colours[i], command=lambda colour=colours[i]: change_colour(colour))
    button.grid(column=col, row=rw)
    col += 1
    buttons.append(button)

# Place other buttons
brush_size_lbl = tkinter.Label(root, text=brush_size)
brush_size_lbl.grid(column=4, row=24, columnspan=3)

dec_brush_size = tkinter.Button(root, text="-", command=lambda size=-1: change_brush_size(size))
dec_brush_size.grid(column=2, row=24)

inc_brush_size = tkinter.Button(root, text="+", command=lambda size=1: change_brush_size(size))
inc_brush_size.grid(column=3, row=24)

filename_entry = tkinter.Entry(root)
filename_entry.grid(column=2, row=26, columnspan=4)

save = tkinter.Button(root, text="Save as PNG", command=save_img)
save.grid(column=6, row=26, columnspan=4)

# Bind motion event to canvas (drawing as long as brush in on)
canvas.bind('<Motion>', draw)

# Bind button event to canvas (turning brush on/off)
canvas.bind('<ButtonPress>', toggle_brush)

# Mainloop
root.mainloop()

