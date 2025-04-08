"""
🎨 The Magical Canvas Eraser 🎨
=============================
A magical tool that transforms blue cells into white space!
Draw with erasure and create art through removal.
=============================
"""

from graphics import Canvas
import time
import random
import keyboard  

# Canvas dimensions and styling
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

# Color palettes
CELL_COLORS = ['royal blue', 'steel blue', 'cornflower blue', 'dodger blue']
ERASER_COLORS = ['pink', 'hot pink', 'deep pink']

def create_gradient_grid(canvas: Canvas) -> None:
    """Creates a beautiful gradient grid of blue cells"""
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            color = random.choice(CELL_COLORS)
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, color)

def animate_eraser(canvas: Canvas, eraser: int) -> None:
    """Makes the eraser pulse with different colors"""
    canvas.set_color(eraser, random.choice(ERASER_COLORS))

def erase_objects(canvas: Canvas, eraser: int) -> None:
    """Creates a magical erasing effect"""
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    overlapping = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    for obj in overlapping:
        if obj != eraser:
            canvas.set_color(obj, 'white')

def main():
    print("✨ Welcome to the Magical Canvas Eraser! ✨")
    print("Click anywhere to summon your magical eraser...")
    print("Press 'q' to quit the program\n")
    
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    create_gradient_grid(canvas)
    
    canvas.wait_for_click()
    x, y = canvas.get_last_click()
    
    eraser = canvas.create_rectangle(
        x, y, x + ERASER_SIZE, y + ERASER_SIZE, 
        random.choice(ERASER_COLORS)
    )
    
    print("🎨 Your magical eraser has appeared!")
    print("Move it around to create your masterpiece...")
    print("Remember: Press 'q' to exit\n")
    
    while True:
        if keyboard.is_pressed('q'):  # Check if 'q' is pressed
            print("Thanks for creating art! Goodbye! ✨")
            break
            
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        erase_objects(canvas, eraser)
        animate_eraser(canvas, eraser)
        time.sleep(0.05)

if __name__ == '__main__':
    main()