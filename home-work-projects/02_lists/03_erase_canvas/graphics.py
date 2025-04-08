"""
Simple graphics library for creating interactive canvas with basic shapes
"""

import tkinter as tk
from typing import List, Tuple, Optional, Any

class Canvas:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.mouse_x = 0
        self.mouse_y = 0
        self.last_click_x = 0
        self.last_click_y = 0
        
        self.canvas.bind('<Motion>', self._update_mouse_position)
        self.canvas.bind('<Button-1>', self._update_last_click)
        self.root.update()

    def create_rectangle(self, x1: int, y1: int, x2: int, y2: int, color: str) -> int:
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')

    def set_color(self, shape_id: int, color: str) -> None:
        self.canvas.itemconfig(shape_id, fill=color)

    def moveto(self, shape_id: int, x: int, y: int) -> None:
        bbox = self.canvas.bbox(shape_id)
        if bbox:
            current_x, current_y = bbox[0], bbox[1]
            dx, dy = x - current_x, y - current_y
            self.canvas.move(shape_id, dx, dy)
        self.root.update()

    def find_overlapping(self, x1: int, y1: int, x2: int, y2: int) -> Tuple[int, ...]:
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def wait_for_click(self) -> None:
        self.root.update()
        while not hasattr(self, '_clicked'):
            self.root.update()
        delattr(self, '_clicked')

    def get_mouse_x(self) -> int:
        return self.mouse_x

    def get_mouse_y(self) -> int:
        return self.mouse_y

    def get_last_click(self) -> Tuple[int, int]:
        return (self.last_click_x, self.last_click_y)

    def _update_mouse_position(self, event: Any) -> None:
        self.mouse_x = event.x
        self.mouse_y = event.y

    def _update_last_click(self, event: Any) -> None:
        self.last_click_x = event.x
        self.last_click_y = event.y
        self._clicked = True