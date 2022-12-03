class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Size:
    def __init__(self, w, h):
        self.w = w
        self.h = h

def generate_container():
    from xml.etree import ElementTree as ET
    from CssStyle import Style, set_elem_style
    # two tags because the second ones makes width == height
    width_container = ET.Element('div')
    set_elem_style(width_container, Style().inlineflex().pos_independent())
    height_container = ET.SubElement(width_container, 'div')
    set_elem_style(height_container, Style().inlineflex().squarewithparent())
    return (width_container, height_container)
    
def get_room(name):
    from globals import Settings
    return next(room for room in Settings.rooms if room.name == name)

def get_room_index(name):
    return get_room(name).index
