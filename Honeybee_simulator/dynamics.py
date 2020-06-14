import tkinter   
from PIL import ImageTk,Image
import numpy as np

root = tkinter.Tk()  

image_home = './images/'  
size = 0
canvas = tkinter.Canvas(root, width = 1000, height = 1000)  
canvas.pack()
global_time = 0

firefly_image = image_home + 'bee.png'
flower_image = image_home + 'flowers.png'
background_image = image_home + 'scenery.png'

def generate_landing_movement(target,position):
        global global_time
        movement = (target-position)/10
        return movement

def generate_8_movement(step):
        global global_time
        ones = np.array([np.ones(2).tolist()]).T

        theta = 30* np.cos(global_time/400)

        movement = np.matmul(ones,np.array([[np.sin(theta),np.cos(theta)]]))
        movement = np.random.randint(0,10)/10*step*movement
        global_time += 1
        return movement

def generate_random_movement(step):
        movement = np.random.randint(-1000,1000,size =2)/1000
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
        global iteration,coordinates,images

        images = []  
        
        movement = generate_random_movement(10)
        coordinates[0] = np.abs(coordinates[0] + movement)
        del movement
        
        movement = generate_random_movement(10)
        coordinates[1] = np.abs(coordinates[1] + movement)
        del movement

        bee = ImageTk.PhotoImage(Image.open(firefly_image))
        
        image = Image.open(flower_image)
        image = image.resize((100, 100), Image.ANTIALIAS)
        flower = ImageTk.PhotoImage(image)

        image = Image.open(background_image)
        image = image.resize((1000, 1000), Image.ANTIALIAS)
        scenery = ImageTk.PhotoImage(image)
        
        images.append(bee)
        images.append(flower)
        images.append(scenery)

        canvas.delete('all')

        canvas.create_image(500,500, image=scenery)

        canvas.create_image(coordinates[2][0],coordinates[2][1], image=flower)
        canvas.create_image(coordinates[3][0],coordinates[3][1], image=flower)
        canvas.create_image(coordinates[4][0],coordinates[4][1], image=flower)

        canvas.create_image(coordinates[0][0],coordinates[0][1], image=bee)
        canvas.create_image(coordinates[1][0],coordinates[1][1], image=bee)


        del flower, bee, scenery, image
        
        label = tkinter.Label(root)
        label.image = images
        label.pack()

        del images

        canvas.after(5,self.create_image)

    def init_iteration(self):
        global iteration,coordinates
        coordinates  = np.array([np.random.randint(500, size=2),np.random.randint(500, size=2),np.array([500,600]),np.array([700,600]),np.array([300,600])])
        iteration = 1

    def create_character(self):
        self.init_iteration()
        canvas.itemconfig(self.name)
        canvas.after(1000,self.create_image)

bee1 = Characters('bee.png','bee1',[100,100])
bee1.create_character()

root.mainloop()