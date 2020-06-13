import tkinter   
from PIL import ImageTk,Image
import time
import numpy as np

root = tkinter.Tk()  

image_home = './images/'  
size = 0
canvas = tkinter.Canvas(root, width = 1000, height = 1000)  
canvas.pack()

def generate_movement(step):
        movement = np.random.randint(-1000,1000,size =(2,2))/1000
        ones = np.array([np.ones(2).tolist()]).T
        denom = np.matmul(np.square(movement),ones)
        denom = np.sqrt(denom)

        movement = step*movement/denom
        return movement

class Characters :
    def __init__(self, species, name, position):
        self.species = species
        self.name = name
    
    def create_image(self):
        global iteration,coordinates

        movement = generate_movement(5)
        coordinates = coordinates + movement
        
        firefly_image = image_home + self.species
        photo = ImageTk.PhotoImage(Image.open(firefly_image))

        label = tkinter.Label(root)
        label.image = photo
        label.pack()

        canvas.delete('all')
        newimg = canvas.create_image(coordinates[0][0],coordinates[0][1], image=photo)
        newimg = canvas.create_image(coordinates[1][0],coordinates[1][1], image=photo)
        canvas.after(10,self.create_image)

    def init_iteration(self):
        global iteration,coordinates
        coordinates  = np.random.randint(500, size=(2, 2))
        iteration = 1

    def create_character(self):
        iteration = 1
        self.init_iteration()
        canvas.itemconfig(self.name)
        canvas.after(1000,self.create_image)

bee1 = Characters('bee.png','bee1',[100,100])
bee1.create_character()

bee2 = Characters('bee.png','bee2',[500,500])
bee2.create_character()

root.mainloop()