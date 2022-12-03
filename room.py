from xml.etree import ElementTree as ET
from globals import Settings
from CssStyle import Style, set_elem_style

class Room:
    def __init__(self, name, tex, enemies, items, interactives):
        self.name = name
        self.tex = tex
        self.enemies = enemies
        self.items = items
        self.interactives = interactives

    def set_index(self, index):
        self.index = index

    def generate_element(self):
        self.elem = ET.Element('div')
        bg_style = Style().bg_tex(self.tex).pos_independent().\
                width(Settings.game_width).height(Settings.game_height).\
                screen_pos(self.index)
        if self.name == 'finish':
            bg_style.z(Settings.z_indexes['tally'])
        set_elem_style(self.elem, bg_style)
        for inter in self.interactives:
            self.elem.append(inter.generate_element())
        return self.elem
