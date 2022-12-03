from globals import Settings

class CssParam:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def __str__(self):
        return '{0}:{1};'.format(self._name, self._value)

class Style:
    def __init__(self):
        self._params = {}

    # styles
    def bg_color(self, color_name): self._params['background'] = CssParam('background', color_name); return self
    def bg_tex(self, tex): self._params['background'] = CssParam('background', 'url(\'{0}\')'.format(tex)); return self
    def opacity(self, val): self._params['opacity'] = CssParam('opacity', str(val)); return self
    def z(self, zindex): self._params['z'] = CssParam('z-index', str(zindex)); return self
    def no_overflow(self): self._params['overflow'] = CssParam('overflow', 'hidden'); return self
    def inlineflex(self): self._params['display'] = CssParam('display', 'inline-flex'); return self
    def center_items(self): self._params['align-items'] = CssParam('align-items', 'center'); return self
    def cursor_pointer(self): self._params['cursor'] = CssParam('cursor','pointer'); return self
    def pos_independent(self): self._params['position'] = CssParam('position', 'absolute'); return self
    def pos_dependent(self): self._params['position'] = CssParam('position', 'relative'); return self
    def width(self, size): self._params['width'] = CssParam('width', '{0}px'.format(size)); return self
    def width_full(self): self._params['width'] = CssParam('width', '100%'); return self
    def height(self, size): self._params['height'] = CssParam('height', '{0}px'.format(size)); return self
    def left(self, pos): self._params['left'] = CssParam('left', '{0}px'.format(pos)); return self
    def top(self, pos): self._params['top'] = CssParam('top', '{0}px'.format(pos)); return self
    def no_arrow(self): self._params['list-style'] = CssParam('list-style', 'none'); return self
    def padr(self, val): self._params['padding-right'] = CssParam('padding-right', '{0}px'.format(val)); return self
    def padb(self, val): self._params['padding-bottom'] = CssParam('padding-bottom', '{0}px'.format(val)); return self
    def padbf(self): self._params['padding-bottom'] = CssParam('padding-bottom', 'calc(100% * -1)'); return self
    def marginr(self, val): self._params['margin-right'] = CssParam('margin-right', '{0}px'.format(val)); return self
    def squarewithparent(self): self._params['padding-bottom'] = CssParam('padding-bottom', '100%'); return self
    def prevent_shifting(self):
        #self._params['top'] = CssParam('top', 'calc(100% * -1)');
        self._params['left'] = CssParam('left', 'calc(100% * -601)');
        return self;
    def x(self, pos): return self.left(pos);
    def y(self, pos): return self.top(pos);
    def move_y_with_counter(self, offset):
        self._params['top'] = CssParam('top', 'calc({1}px - (100%*{0}))'.\
                format(1 * (Settings.total_height), offset))
        return self

    def move_xy_with_screen(self):
        self._params['left'] = CssParam('left', 'calc(100%*{0})'.\
                format(2 * Settings.game_width))
        self._params['top'] = CssParam('top', 'calc(100%*{0})'.\
                format(2 * (Settings.game_height + Settings.sbar_height)))
        return self

    def xy_blocker(self, i, pos, room1, room2):
        i_diff = room2 - room1
        x_diff = pos[0].x - pos[1].x
        y_diff = pos[0].y - pos[1].y
        self.x(pos[0].x - (i - room1) * (x_diff/i_diff))
        self.y(pos[0].y - (i - room1) * (y_diff/i_diff))
        return self

    def xy_connector(self, pos, room1, room2):
        i_diff = room2 - room1
        x_diff = pos[0].x - pos[1].x
        y_diff = pos[0].y - pos[1].y
        self._params['left'] = CssParam( 'left', 'calc({0}px - ((100% - {1}px) * {2}) + (( max(100%, {1}px) - min(100%, {3}px ))*10000) )'.\
                format(pos[0].x, room1, x_diff/i_diff, room2) )
        self._params['top'] = CssParam( 'top', 'calc({0}px - ( (100% - {1}px) * {2}) )'.\
                format(pos[0].y, room1, y_diff/i_diff) )
        return self

    def size_connector(self):
        self._params['width'] = CssParam('width', '{0}px'.\
                format(Settings.connection_size))
        self._params['height'] = CssParam('height', '{0}px'.\
                format(Settings.connection_size))
        return self

    def disp_center_flex(self):
        self._params['display'] = CssParam('display', 'flex')
        self._params['flex-direction'] = CssParam('flex-direction', 'column')
        self._params['align-items'] = CssParam('align-items', 'center')
        return self

    def screen_pos(self, i):
        self._params['left'] = CssParam('left',\
                'calc(({0}px * {1}) - (100% * {0}))'.\
                format(Settings.game_width, i))
        self._params['top'] = CssParam('top', '0')
        return self

    def y_var_offset(self, offset, screen):
        self._params['top'] = CssParam('top', 'calc((100% * {0}) + {1}px)'.\
                format(Settings.game_height,\
                offset - 2 * (Settings.game_height + Settings.sbar_height) * screen))
        return self

    def x_var_offset(self, offset, screen):
        self._params['left'] = CssParam('left', 'calc((100% * {0}) + {1}px)'.\
                format(Settings.game_width,\
                offset - (2 * Settings.game_width * screen)))
        return self

    def __str__(self):
        style_value = str()
        params = list(self._params.values())
        if 'background' in self._params:
            params += [ CssParam('background-size', 'cover') ] 
            params += [ CssParam('background-position', 'center') ]
        for param in params:
            if param:
                style_value += str(param)
        return style_value

def set_elem_style(elem, style):
    elem.set('style', str(style))
