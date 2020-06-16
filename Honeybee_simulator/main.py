import tkinter
from PIL import ImageTk, Image
import numpy as np

root = tkinter.Tk()

image_home = './images/'
canvas_dimensions = {'x':1000, 'y':600}

no_of_bees = 3

canvas = tkinter.Canvas(root, width=canvas_dimensions['x'], height=canvas_dimensions['y'])
canvas.pack()

label = tkinter.Label(root)
global_time = 0

firefly_image = image_home + 'firefly.png'
flower_image = image_home + 'flowers.png'
background_image = image_home + 'nightScene.png'

coordinates = []
images_in_frame = []

static_images = []
dynamic_images = []
phase_vector = np.random.randint(0,7,size = no_of_bees)

def create_images(image_file, x=500,y=500, scaling_factor = 1, type_ = 'static'):
    global images_in_frame, static_images, dynamic_images
    image = Image.open(image_file)
    width, height = image.size

    new_width = int(np.rint(scaling_factor*width))
    new_height = int(np.rint(scaling_factor*height))

    image = image.resize((new_width, new_height), Image.ANTIALIAS)
    photoImage = ImageTk.PhotoImage(image)
    images_in_frame.append(photoImage)

    if(type_ =='static'):
        static_images.append(photoImage)
    else:
        dynamic_images.append(photoImage)
    canvas.create_image(x,y, image=photoImage)

def landing_motion(target, position):
    global global_time
    movement = (target-position)/10
    return movement

def random_motion(step):
    theta = np.random.randint(0, 360+90)
    theta = theta * np.pi/180
    y_step_random = step * 1 if np.sin(theta) > 0 else step* -1
    x_step_random = step * 1 if np.cos(theta) > 0 else step* -1
    movement = step*np.array([x_step_random,y_step_random]).T
    del theta
    return movement

def hovering_motion(current_position, center = np.array([500,500]), axis = 0, step = 1, period = 1, phase = 0):
    global global_time
    theta = global_time * np.pi/180
    x_step_periodic = 500 + 400 * np.cos(phase + theta/(2*period))
    y_step_periodic = 400 + 100 * np.sin(phase + theta/period)
    movement = np.array([x_step_periodic,y_step_periodic])
    return movement
    
def simulate():
    global coordinates,images_in_frame, canvas, static_images, dynamic_images, global_time  
    images_in_frame.clear()
    dynamic_images.clear()
    label.config(image='')
    global_time = global_time + 1
    for i in range(0,no_of_bees):
        movement = hovering_motion(coordinates[i],step = 2, phase = phase_vector[i])
        coordinates[i] = movement
        del movement
    images_in_frame = static_images + dynamic_images
    for i in range(0,no_of_bees):
        create_images(firefly_image, coordinates[i][0],coordinates[i][1], scaling_factor= 0.1, type_= 'dynamic')
    label.image = images_in_frame
    label.pack()
    canvas.after(5,simulate)

def init_iteration():
    global coordinates
    coordinates = np.array(np.random.randint(500, size=(no_of_bees,2)))
    
def create_character():
    init_iteration()
    canvas.after(1000,simulate)

create_images(background_image, y=300, scaling_factor=1)
create_character()

root.mainloop()
