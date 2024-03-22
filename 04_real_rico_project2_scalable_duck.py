"""
    Draws a scalable duck using a created
    duck function that takes in 4 parameters.
    
    FILE NAME: 04_real_rico_project2_scalable_duck.py
    AUTHOR: Lisette Real Rico
    DATE: Oct 6, 2023
    Course: COMP 1351
    Assignment: Project 2
    Collaborators: NONE
"""
import dudraw

def duck(left_x:float, bottom_y:float, width:float, height:float) -> None:
    """
    Function that draws a duck with a violet hat. Doesn't return a value.
    Takes in 4 variables:
        left_x -> gives x coordinate of bottom left corner of drawing
        bottom_y -> gives y coordinate of bottom left corner of drawing
        width -> x scale of the drawing
        height -> y scale of the drawing
    """

    #DRAWS BEAK (orange w/ dark red line for separation)
    dudraw.set_pen_color_rgb(255, 120, 80)
    dudraw.filled_triangle(left_x+0.75*width, bottom_y+0.7*height,
                           left_x+0.75*width, bottom_y+0.55*height,
                           left_x+0.85*width, bottom_y+0.6*height)
    dudraw.set_pen_color(dudraw.DARK_RED)
    dudraw.line(left_x+0.85*width, bottom_y+0.6*height,
                left_x+0.75*width, bottom_y+0.6*height)
    
    #DRAWS TAIL (yellow)
    dudraw.set_pen_color(dudraw.YELLOW)
    dudraw.filled_triangle(left_x+0.15*width, bottom_y+0.5*height, 
                           left_x+0.3*width, bottom_y+0.53*height,
                           left_x+0.22*width, bottom_y+0.35*height)

    #DRAWS BODY & HEAD (yellow)
    dudraw.filled_ellipse(left_x+0.5*width, bottom_y+0.4*height, 0.3*width, 0.2*height) #body
    dudraw.filled_ellipse(left_x+0.65*width, bottom_y+0.63*height, width*0.15, height*0.15) #head

    #DRAWS WING (yellow w/ orange shadow & black outline)
    dudraw.set_pen_color(dudraw.ORANGE)
    dudraw.filled_triangle(left_x+0.5*width, bottom_y+0.48*height,
                           left_x+0.35*width, bottom_y+0.40*height,
                           left_x+0.5*width, bottom_y+0.35*height) #shadow
    dudraw.set_pen_color(dudraw.YELLOW)
    dudraw.filled_triangle(left_x+0.5*width, bottom_y+0.48*height,
                           left_x+0.38*width, bottom_y+0.411*height,
                           left_x+0.5*width, bottom_y+0.359*height) #wing
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.set_pen_width(width*0.005)
    dudraw.line(left_x+0.5*width, bottom_y+0.48*height,
                left_x+0.35*width, bottom_y+0.4*height) #outline
    dudraw.line(left_x+0.5*width, bottom_y+0.35*height,
                left_x+0.35*width, bottom_y+0.4*height) #outline
    
    #EYE (black)
    dudraw.filled_ellipse(left_x+0.75*width, bottom_y+0.65*height, width*0.02, height*0.02)

    #HAT (violet)
    dudraw.set_pen_color(dudraw.VIOLET)
    dudraw.filled_rectangle(left_x+0.65*width, bottom_y+0.7*height, width*0.2, height*0.01) #rim of hat
    dudraw.filled_elliptical_sector(left_x+0.65*width, bottom_y+0.7*height, width*0.17, height*0.15, 0, 180) #top of hat


def main():
    dudraw.set_canvas_size(900,900)
    dudraw.clear(dudraw.LIGHT_GRAY)

    #Draw four copies of your drawing at different locations and with different sizes
    # dudraw.set_x_scale(0, 900)
    # dudraw.set_y_scale(0, 900)
    # duck(25, 25, 225, 225)
    # duck(25, 375, 200, 50)
    # duck(375, 275, 50, 200)
    # duck(375, 125, 50, 50)

    # Draw four copies of my drawing at different locations and with different sizes
    duck(0.05, 0.05, 0.45, 0.45)
    duck(0.05, 0.75, 0.4, 0.1)
    duck(0.75, 0.55, 0.1, 0.4)
    duck(0.75, 0.25, 0.1, 0.1)
    
    dudraw.show(float('inf'))

if __name__ == '__main__':
    main()