import tkinter
from PIL import ImageTk, Image
import numpy as np

root = tkinter.Tk()

image_home = './images/'
size = 0
canvas = tkinter.Canvas(root, width=1000, height=1000)
canvas.pack()

label = tkinter.Label(root)
global_time = 0

firefly_image = image_home + 'firefly.png'
flower_image = image_home + 'flowers.png'
background_image = [image_home + 'nightScene.png']

coordinates = []
images_in_frame = []


scenery = []

def static_images(image_files):
    global images_in_frame, scenery
    for image_file in image_files:
        image = Image.open(image_file)
        image = image.resize((1000, 1000), Image.ANTIALIAS)
        scenery.append(ImageTk.PhotoImage(image))

static_images(background_image)
canvas.create_image(500,500, image=scenery)


def generate_landing_movement(target, position):
        global global_time
        movement = (target-position)/10
        return movement


def generate_8_movement(step):
        global global_time
        ones = np.array([np.ones(2).tolist()]).T
        theta = 30 * np.cos(global_time/400)
        movement = np.matmul(ones, np.array([[np.sin(theta), np.cos(theta)]]))
        movement = np.random.randint(0, 10)/10*step*movement
        global_time += 1
        del theta, ones
        return movement


def generate_random_movement(step):
        movement = np.random.randint(-1000, 1000, size=2)/1000
        ones = np.array([np.ones(2).tolist()]).T
        denom = np.matmul(np.square(movement), ones)
        denom = np.sqrt(denom)
        movement = step*movement/denom
        del ones, denom
        return movement

def create_image():
    
    global coordinates,images_in_frame, canvas    

    images_in_frame.clear()
    label.config(image='')

    for i in range(0,6):
        movement = generate_random_movement(5)
        coordinates[i] = np.abs(coordinates[i] + movement)
        del movement

    bee = ImageTk.PhotoImage(Image.open(firefly_image))
    
    image = Image.open(flower_image)
    image = image.resize((100, 100), Image.ANTIALIAS)
    flower = ImageTk.PhotoImage(image)

    images_in_frame.append(bee)
    images_in_frame.append(flower)
    images_in_frame.append(scenery)

    canvas.create_image(coordinates[6][0],coordinates[6][1], image=flower)
    canvas.create_image(coordinates[7][0],coordinates[7][1], image=flower)
    canvas.create_image(coordinates[8][0],coordinates[8][1], image=flower)

    canvas.create_image(coordinates[0][0],coordinates[0][1], image=bee)
    canvas.create_image(coordinates[1][0],coordinates[1][1], image=bee)
    canvas.create_image(coordinates[2][0],coordinates[2][1], image=bee)
    canvas.create_image(coordinates[3][0],coordinates[3][1], image=bee)
    canvas.create_image(coordinates[4][0],coordinates[4][1], image=bee)
    canvas.create_image(coordinates[5][0],coordinates[5][1], image=bee)

    del flower, bee
    label.image = images_in_frame
    label.pack()

    canvas.after(5,create_image)

def init_iteration():
    global coordinates
    coordinates  = np.array([np.random.randint(500, size=2),np.random.randint(500, size=2),np.random.randint(500, size=2),
                   np.random.randint(500, size=2),np.random.randint(500, size=2),np.random.randint(500, size=2),
                   np.array([500,600]),np.array([700,600]),np.array([300,600])])
    
def create_character():
    init_iteration()
    canvas.after(1000,create_image)

create_character()
root.mainloop()
