from tkinter import *
from PIL import Image, ImageTk, ImageFile

def resize_image(width: int, height: int, image: ImageFile) -> ImageTk.PhotoImage:
    resized_image = image.resize((width, height), Image.Resampling.LANCZOS)
    converted_image = ImageTk.PhotoImage(resized_image)
    return converted_image

root = Tk()
root.geometry("1280x720")

page1_image = resize_image(400, 400, Image.open("images/page1.png"))
page1_story = ("Rudolph, lost and confused, stumbled through the desolate Martian landscape. "
               "His nose, usually a beacon of holiday cheer, was now a flickering ember in the alien twilight. "
               "He'd taken a wrong turn during a particularly foggy Christmas Eve and somehow ended up… here."
               "Suddenly, a hulking figure materialized from the swirling red dust. It was Venom, the alien symbiote, "
               "stranded after a failed attempt to hitch a ride on a departing rover. 'Tasty reindeer,' "
               "Venom hissed, its long tongue flicking out. Rudolph, despite his gentle nature, was no coward. "
               "'I wouldn't try that if I were you,' he warned, 'I've got a powerful kick!'")


page2_image = resize_image(400, 400, Image.open("images/page2.png"))
page3_image = resize_image(400, 400, Image.open("images/page3.png"))

pages = {
    "1": page1_image,
    "2": page2_image,
    "3": page3_image
}


# Canvas for the image
image_canvas = Canvas(root, width=400, height=400)  # Set canvas size
image_canvas.create_image(200, 200, image=page1_image, anchor="center")
image_canvas.grid(row=0, column=0, columnspan=2, pady=20)  # Span 2 columns

# Label for "Page 1"
current_page = 1
page_label = Label(root, text=f'Page {current_page}')
page_label.grid(row=1, column=0, columnspan=2)

# Textbox for the story
story_textbox = Label(root, text=page1_story, wraplength=400, justify="center")  # wrap=WORD for word wrapping
story_textbox.grid(row=2, column=0, columnspan=2, pady=20)

# Buttons
prev_page_button = Button(text="Previous Page", command=lambda: print("Placeholder function, not yet implemented!"))
prev_page_button.grid(row=3, column=0, sticky="ew")  # Expand horizontally
next_page_button = Button(text="Next Page", command=lambda: print("Placeholder function, not yet implemented!"))
next_page_button.grid(row=3, column=1, sticky="ew")  # Expand horizontally

# Configure rows and columns for proper spacing and centering
root.rowconfigure(0, weight=1)  # Give weight to the image row
root.rowconfigure(2, weight=1)  # Give weight to the textbox row
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.mainloop()