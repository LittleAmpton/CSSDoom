from xml.etree import ElementTree as ET
from math import floor, ceil
from CssStyle import Style, set_elem_style
from helper import Pos, get_room_index
from globals import Settings, Textures

class Connection:
    def __init__(self, between, pos, arrows, name):
        self._name = name
        first = 0
        if get_room_index(between[0]) > get_room_index(between[1]):
            first = 1
        second = int(not first)
        self.rooms = (between[first], between[second])
        self.pos = (Pos(pos[first][0], pos[first][1]), \
                    Pos(pos[second][0], pos[second][1]))
        self.arrows = (arrows[first], arrows[second])
        self.name = name

    def getIndexDiff(self):
        return get_room_index(self.rooms[1]) - get_room_index(self.rooms[0])

    def createArrow(self, index):
        arrow_element = ET.Element('div')
        arrow_style = Style().pos_independent().size_connector().\
                x(self.pos[index].x).y(self.pos[index].y).\
                z(Settings.z_indexes['arrows'])
        if self.arrows[index] is not None:
            arrow_style.bg_tex( Textures.arrows[ self.arrows[index] ] )
        set_elem_style(arrow_element, arrow_style)
        return arrow_element

    def createBlockers(self):
        room1_index = get_room_index(self.rooms[0])
        room2_index = get_room_index(self.rooms[1])
        x1 = self.pos[0].x
        x2 = self.pos[1].x
        y1 = self.pos[0].y
        y2 = self.pos[1].y
        x_diff = x1 - x2
        if x_diff == 0: x_diff = 1
        y_diff = y1 - y2
        if y_diff == 0: y_diff = 1
        i_diff = self.getIndexDiff()
        w = Settings.game_width
        h = Settings.game_height
        b = Settings.sbar_height
        s = Settings.connection_size
        x_min = (x1 -  w) * (i_diff / x_diff) + room1_index
        y_min = (y1 - (h + b)) * (i_diff / y_diff) + room1_index
        x_max = (s + x1) * i_diff / x_diff + room1_index
        y_max = (s + y1) * i_diff / y_diff + room1_index
        if (x_min > x_max): x_min,x_max = x_max,x_min
        if (y_min > y_max): y_min,  y_max = y_max,y_min
        x_min = floor(x_min) + 1
        x_max = ceil(x_max) - 1
        y_min = floor(y_min) + 1
        y_max = ceil(y_max) - 1
        index_min = max(x_min, y_min)
        index_max = min(x_max, y_max)
        for i in range(max(0, index_min), min(index_max+1,len(Settings.rooms))):
            if i not in range(get_room_index(self.rooms[0]) + 1, get_room_index(self.rooms[1])):
                continue
            blocker = ET.Element('div')
            style = Style().pos_independent().size_connector().z(Settings.z_indexes['blockers']).\
                    xy_blocker(i, self.pos, room1_index, room2_index)
            if Settings.debug_connections:
                style.bg_color('blue').opacity(0.5)
            set_elem_style(blocker, style)
            Settings.rooms[i].elem.append(blocker)

    def createElement(self):
        det = ET.Element('details')
        shape = ET.SubElement(det, 'summary')

        room1_index = get_room_index(self.rooms[0])
        room2_index = get_room_index(self.rooms[1])
        index_diff = room2_index - room1_index
        if room2_index <= get_room_index('start'):
            det.set('open', '')

        style = Style().pos_independent().size_connector().no_arrow().\
                xy_connector(self.pos, room1_index, room2_index).z(Settings.z_indexes['connections']).\
                cursor_pointer()
        if Settings.debug_connections:
            style.bg_color('red').opacity(0.5)
            shape.text = self.name
        set_elem_style(shape, style)

        padder = ET.SubElement(det, 'div')
        set_elem_style(padder, Style().width(index_diff))
        return det


