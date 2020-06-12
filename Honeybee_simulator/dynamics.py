import tkinter   
from PIL import ImageTk,Image
import time
import numpy as np

root = tkinter.Tk()  
canvas = tkinter.Canvas(root, width = 1000, height = 1000)  
canvas.pack()
image_home = './images/'
firefly_image = image_home + 'firefly.png'
photo = ImageTk.PhotoImage(Image.open(firefly_image))  
size = 0

label = tkinter.Label(root, image=photo)
label.pack()
    
def create_image():
        global iteration,x_,y
        if(iteration>100):
            iteration = 0
        iteration = iteration + 1
        n1 = np.random.randint(1000)/1000
        n2 = np.random.randint(1000)/1000
        denom = np.sqrt(n1*n1 + n2*n2)
        coord = x + 10*n1/denom, y + 10*n2/denom
        label.configure(image = photo)
        label.image = photo
        canvas.delete('all')
        newimg = canvas.create_image(coord, image=photo)
        canvas.after(100,create_image)

def init_iteration():
    global iteration,x,y
    iteration = 1
    x = 100
    y = 100

iteration = 1
init_iteration()
canvas.after(1000,create_image)
root.mainloop()