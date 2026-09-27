import pygame

class Button():
    def __init__(this, base_image, hovering_image, x_pos, y_pos):
        this.base_image = base_image
        this.hovering_image = hovering_image
        this.x_pos = x_pos
        this.y_pos = y_pos
        this.rect = this.base_image.get_rect(center=(this.x_pos, this.y_pos))

    def checkForInput(this, position):
        if position[0] in range(this.rect.left, this.rect.right) and position[1] in range(this.rect.top, this.rect.bottom):
            return True
        return False
    
    def getRect(this):
        return this.rect
    def getSurface(this):
        return this.base_image
    
        #(source: Surface, dest: RectLike = (0, 0), area: RectLike | None = None, special_flags: int = 0)

