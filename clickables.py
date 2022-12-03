from xml.etree import ElementTree as ET
from CssStyle import Style, set_elem_style
from helper import get_room_index, Pos, Size
from globals import Settings, Textures

class Clickable:
    def __init__(self, pos):
        self.pos = pos
        self.size = Size(50, 50)
        self.tex1 = None
        self.tex2 = None

    def set_screen(self, screen):
        self.screen = screen

    def create_element(self):
        container = ET.Element('div')
        set_elem_style(container, Style().pos_dependent())
        elem_details = ET.Element('details')
        #set_elem_style(elem_details, Style().padbf())

        elem_clickable = ET.Element('summary')
        elem_style = Style().pos_independent().\
                left(self.pos.x).y_var_offset(self.pos.y, self.screen).\
                x_var_offset(self.pos.x, self.screen).no_arrow().cursor_pointer().\
                z(Settings.z_indexes['enemies'])
        if self.tex1 is None:
            elem_style.bg_color('green').width(50).height(50)
        else:
            elem_style.bg_tex(self.tex1).width(self.size.w).height(self.size.h)
        set_elem_style(elem_clickable, elem_style)

        if self.tex2 is not None:
            elem_frame = ET.Element('div')
            frame_style = Style().pos_independent().left(self.pos.x).\
                    y_var_offset(self.pos.y, self.screen).\
                    x_var_offset(self.pos.x - Settings.game_width, self.screen).bg_tex(self.tex2).\
                    width(self.size.w).height(self.size.h)
            set_elem_style(elem_frame, frame_style)

        elem_padder = ET.Element('div')
        set_elem_style(elem_padder, Style().width(1).pos_dependent())

        elem_details.append(elem_clickable)
        if self.tex2 is not None:
            elem_details.append(elem_frame)
        elem_details.append(elem_padder)
        container.append(elem_details)
        return container

class TexturedClickable(Clickable):
    def __init__(self, pos, size, tex1, tex2):
        super().__init__(pos)
        self.size = size
        self.tex1 = tex1
        self.tex2 = tex2

def Zombieman(pos, scale):
    return TexturedClickable(pos, Size(94 * scale, 110 * scale),
                Textures.monsters['zombie-alive'], Textures.monsters['zombie-dead'])

def Shotgunguy(pos, scale):
    return TexturedClickable(pos, Size(104 * scale, 110 * scale),
                Textures.monsters['shotgun-alive'], Textures.monsters['shotgun-dead'])

def Imp(pos, scale):
    return TexturedClickable(pos, Size(116 * scale, 114 * scale),
                Textures.monsters['imp-alive'], Textures.monsters['imp-dead'])

def GArmor(pos, scale):
    return TexturedClickable(pos, Size(62 * scale, 34 * scale),
                Textures.items['garmor'], None)

def BArmor(pos, scale):
    return TexturedClickable(pos, Size(62 * scale, 34 * scale),
                Textures.items['barmor'], None)

def Stimpack(pos, scale):
    return TexturedClickable(pos, Size(28 * scale, 30 * scale),
                Textures.items['stimpack'], None)

def Medikit(pos, scale):
    return TexturedClickable(pos, Size(56 * scale, 38 * scale),
                Textures.items['medikit'], None)

def HBonus(pos, scale):
    return TexturedClickable(pos, Size(28 * scale, 36 * scale),
                Textures.items['hbonus'], None)

def ABonus(pos, scale):
    return TexturedClickable(pos, Size(32 * scale, 30 * scale),
                Textures.items['abonus'], None)

def create_number_element(number):
    elem = ET.Element('div')
    set_elem_style(elem, Style().width(28).height(32).\
            bg_tex(Textures.numbers[number]).marginr(1))
    return elem

class Counter:
    def __init__(self, pos, n, screen, percent):
        self.pos = pos
        self.screen = screen
        self.percent = percent
        self.n = n

    def create_numbers_column(self, index):
        subcontainer = ET.Element('div')
        set_elem_style(subcontainer, Style().pos_independent().
                x(self.pos.x - (2 * index * Settings.game_width)).
                move_y_with_counter(self.pos.y - (2 * index * (Settings.total_height))).\
                z(Settings.z_indexes['counters']) )

        if self.percent is True:
            numbers = [x * 100 / (self.n) for x in range(0, self.n + 1)]
        else:
            numbers = range(0, self.n+1)
        
        i = 0
        for num in numbers:
            num_cont = ET.Element('div')
            set_elem_style(num_cont, Style().inlineflex().pos_independent().\
                    y(i * (Settings.game_height + Settings.sbar_height)))
            for n in str(int(num)):
                elem = create_number_element(int(n))
                num_cont.append(elem)
            if self.percent is True:
                num_cont.append(create_number_element(10))
            subcontainer.append(num_cont)
            i += 1
        return subcontainer

    def create_element(self):
        container = ET.Element('div')
        if self.screen is None:
            for i in range(0, len(Settings.rooms)):
                column = self.create_numbers_column(i)
                container.append(column)
        else:
            index = get_room_index(self.screen)
            column = self.create_numbers_column(index)
            container.append(column)
        return container
