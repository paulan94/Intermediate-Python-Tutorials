#OOP Review using sentdex's Intermediate Python Programming Tutorial
#Paul An 9/4/17

import random
import pygame
from blob_class import Blob
import numpy as np

# num blobs
STARTING_BLUE_BLOBS = 20
STARTING_RED_BLOBS = 12
STARTING_GREEN_BLOBS = 20

#gameboard
WIDTH = 800
HEIGHT = 600

#colors
WHITE = (255, 255, 255) # R G B
BLUE = (0 , 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#init game board display
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


class BlueBlob(Blob):
    
    #colors as tuples just incase we want to call from other locations
    def __init__(self, x_boundary, y_boundary, movement_range):
        Blob.__init__(self, (0 , 0, 255), x_boundary, y_boundary, movement_range=movement_range)

    def __add__(self, other_blob):
        if other_blob.color == (255, 0, 0):
            self.size -= other_blob.size
            other_blob.size -= self.size
        elif other_blob.color == (0, 255, 0):
            self.size += other_blob.size
            other_blob.size = 0
        elif other_blob.color == (0, 0, 255):
            pass
        else:
            raise ExceptionError('Tried to combine one or multiple blobs of unsupported colors') 
        

class RedBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (255 , 0, 0), x_boundary, y_boundary)

class GreenBlob(Blob):
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0 , 255, 0), x_boundary, y_boundary)


def is_touching(b1,b2):
    return np.linalg.norm(np.array([b1.x,b1.y]) - np.array([b2.x,b2.y])) < (b1.size + b2.size)
        
def handle_collisions(blob_list):
    blues, reds, greens = blob_list #list of 3 dicts
    for blue_id, blue_blob in blues.copy().items(): #only copy if u want to modify
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                if blue_blob == other_blob:
                    pass
                else:
                    if is_touching(blue_blob, other_blob):
                        blue_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        if blue_blob.size <= 0:
                            del blues[blue_id]
    return blues, reds, greens
                        
#PEP8 says 1 line of space for functions, and 2 for classes
def draw_environment(blob_list):
    blues, reds, greens = handle_collisions(blob_list)
    game_display.fill(WHITE)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x,blob.y], blob.size)
            blob.move()
            
            blob.check_bounds()
                
    pygame.display.update()
    return blues, reds, greens
 

def main():
    blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT, (-7,8)) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))

##    print ('Blue blob size {} red sizez {}'.format(blue_blobs[0].size, red_blobs[0].size))
##    blue_blobs[0] + red_blobs[0]
##    print ('Blue blob size {} red sizez {}'.format(blue_blobs[0].size, red_blobs[0].size))
## 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        blue_blobs, red_blobs, green_blobs = draw_environment([blue_blobs, red_blobs, green_blobs])
        clock.tick(60)

if __name__ == "__main__":
    main()

    
