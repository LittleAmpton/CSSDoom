from xml.etree import ElementTree as ET
from CssStyle import Style, set_elem_style
from helper import generate_container
from globals import Settings

class Interactive:
    def __init__(self, pos, size, tex):
        self.pos = pos
        self.size = size
        self.tex = tex

    def generate_element(self):
        con = generate_container()
        container = con[0]
        subcontainer = con[1]
        det = ET.SubElement(subcontainer, 'details')
        summary = ET.SubElement(det, 'summary')
        set_elem_style(summary, Style().pos_independent().x(self.pos.x).\
                move_y_with_counter(self.pos.y).width(self.size.w).\
                height(self.size.h).bg_tex(self.tex).no_arrow().\
                cursor_pointer().z(Settings.z_indexes['interactives']))
        padder = ET.SubElement(det, 'div')
        set_elem_style(padder, Style().width(1))
        return container
