from xml.etree import ElementTree as ET
from CssStyle import Style, set_elem_style
from helper import generate_container, get_room, get_room_index
from globals import Settings, Textures
from connection import Connection

def generate_rooms(container):
    for room in Settings.rooms:
        container.append(room.generate_element())
    generate_connections(container)

def generate_connections(container):
    for connection in Settings.connections:
        connection_button = connection.createElement()
        container.append(connection_button)
        get_room(connection.rooms[0]).elem.append(connection.createArrow(0))
        get_room(connection.rooms[1]).elem.append(connection.createArrow(1))
        blockers = connection.createBlockers()
        #for blocker in blockers:
        #    container.append(blocker)

def generate_monsters(container):
    breaker = ET.SubElement(container, 'div')
    set_elem_style(breaker, Style().inlineflex().pos_independent().\
            move_xy_with_screen())
    con = generate_container()
    breaker.append(con[0])
    subcontainer = con[1]
    # GROSS HACK
   # set_elem_style(subcontainer, Style().inlineflex().squarewithparent().\
   #         pos_independent().prevent_shifting())

    for room in Settings.rooms:
        for enemy in room.enemies:
            enemy.set_screen(room.index)
            enemy_element = enemy.create_element()
            subcontainer.append(enemy_element)

    for counter in Settings.enemy_counters:
        counter_element = counter.create_element()
        subcontainer.append(counter_element)

def generate_pickups(container):
    breaker = ET.SubElement(container, 'div')
    set_elem_style(breaker, Style().inlineflex().pos_independent().\
            move_xy_with_screen())
    con = generate_container()
    breaker.append(con[0])
    subcontainer = con[1]
    # GROSS HACK
    #set_elem_style(subcontainer, Style().inlineflex().squarewithparent().\
    #        pos_independent().prevent_shifting())

    for room in Settings.rooms:
        for item in room.items:
            item.set_screen(room.index)
            item_element = item.create_element()
            subcontainer.append(item_element)

    for counter in Settings.item_counters:
        counter_element = counter.create_element()
        subcontainer.append(counter_element)

def create_statusbar(root):
    sbar = ET.SubElement(root, 'div')
    style = Style().pos_independent().x(0).y(Settings.game_height).\
            width(Settings.game_width).height(Settings.sbar_height).\
            bg_tex(Textures.sbar)
    set_elem_style(sbar, style)

def create_pistol(root):
    pistol = ET.SubElement(root, 'div')
    style = Style().pos_independent().x(Settings.pistol_x).\
            y(Settings.pistol_y).width(Settings.pistol_width).\
            height(Settings.pistol_height).bg_tex(Textures.pistol).z(Settings.z_indexes['pistol'])
    set_elem_style(pistol, style)

def generate_game():
    root_center = ET.Element('div')
    set_elem_style(root_center, Style().width_full().disp_center_flex())

    root_frame = ET.SubElement(root_center, 'div')
    frame_style = Style().width(Settings.game_width).\
            height(Settings.game_height + Settings.sbar_height)
    if not Settings.debug_positions:
        frame_style.no_overflow()
    set_elem_style(root_frame, frame_style)

    root = ET.SubElement(root_frame, 'div')
    set_elem_style(root, Style().inlineflex().pos_dependent().top(0).left(0).\
            padr(Settings.game_width).\
            padb(Settings.game_height + Settings.sbar_height))

    root.append(ET.Comment('statusbar'))
    create_statusbar(root)
    create_pistol(root)
    con = generate_container()
    root.append(con[0])
    container = con[1]
    container.append(ET.Comment('rooms'))
    generate_rooms(container)
    container.append(ET.Comment('monsters'))
    generate_monsters(container)
    container.append(ET.Comment('pickups'))
    generate_pickups(container)

    print("Wszystko git")
    with open('output.html', 'wb') as f:
        f.write(ET.tostring(root_center, method='html'))

Settings.init()
generate_game()
