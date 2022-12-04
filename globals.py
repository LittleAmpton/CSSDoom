from collections import OrderedDict

class Settings:
    game_width = 600
    game_height = 400
    sbar_height = 64
    pistol_width = 114
    pistol_height = 124
    pistol_x = 300 - 57
    pistol_y = 400 - 124
    total_height = game_height + sbar_height
    connection_size = 100
    debug_connections = False
    debug_positions = False

    z_indexes = {
            'arrows':1,
            'connections':2,
            'blockers':3,
            'items':4,
            'enemies':5,
            'interactives':6,
            'pistol':7,
            'tally':8,
            'counters':9,
            }

    def init():
        Settings.create_rooms()
        Settings.create_connections()
        Settings.create_clickable_counters()

    def create_connections():
        from connection import Connection
        Settings.connections = [
                Connection(('start' , 'stairs') , ((20 , 150), (50, 275)), ('left', 'back'), 'to stairs') ,
                Connection(('stairs', 'armor')  , ((255, 75) , (50, 275)), ('up'  , 'back'), 'to armor')  ,

                Connection(('start' , 'hall1'), ((260, 160), (50, 275)), ('up'  , 'back'), 'to hallway'),
                Connection(('hall1' , 'door1') , ((320, 160), (50, 275)), ('up', 'back'), 'to door1') ,
                Connection(('door1' , 'comp') , ((320, 170), (50, 275)), ('right', 'back'), 'to comp') ,
                Connection(('comp' , 'hall2') , ((480, 170), (50, 275)), ('up', 'back'), 'to hall2') ,
                Connection(('hall2' , 'acid') , ((280, 170), (50, 275)), ('up', 'back'), 'to acid') ,
                Connection(('acid' , 'door2') , ((390, 150), (50, 275)), ('up', 'back'), 'to door2') ,
                Connection(('door2' , 'secret1') , ((490, 180), (450, 275)), ('right', 'back'), 'to secret1') ,
                Connection(('secret1' , 'secret2') , ((280, 200), (450, 275)), ('up', 'back'), 'to secret2') ,
                Connection(('secret2' , 'secret3') , ((310,  70), (450, 275)), ('up', 'back'), 'to secret3') ,

                Connection(('door2' , 'to_exit') , ((190, 160), (50, 275)), ('up', 'back'), 'to to_exit') ,
                Connection(('to_exit' , 'exit_left') , ((50, 150), (50, 275)), ('left', 'back'), 'to exit_left') ,
                Connection(('to_exit' , 'exit_right') , ((450, 150), (50, 275)), ('right', 'back'), 'to exit_right') ,
                Connection(('to_exit' , 'door3') , ((255, 160), (50, 275)), ('up', 'back'), 'to door3') ,
                Connection(('door3' , 'exit') , ((255, 160), (50, 275)), ('up', 'back'), 'to exit') ,
                Connection(('exit' , 'finish') , ((275, 160), (50, 275)), (None, None), 'to finish') ,
                ]

    def create_clickable_counters():
        from clickables import Clickable, Counter
        from helper import Pos
        Settings.enemy_counters = [
            Counter(Pos(200, 406), 14, None, False),
            Counter(Pos(450, 100), 14, 'finish', True)
        ]
        Settings.item_counters = [
            Counter(Pos(350, 406), 13, None, False),
            Counter(Pos(450, 138), 13, 'finish', True)
        ]

    def create_rooms():
        from clickables import Counter, Zombieman, Shotgunguy, Imp,\
                GArmor, BArmor, Medikit, Stimpack, HBonus, ABonus
        from interactives import Interactive
        from helper import Pos, Size
        from room import Room
        # in order!
        Settings.rooms = [
                Room('armor', 'https://ifmn.neocities.org/bg_armor.png', [
                        Shotgunguy(Pos(177, 154), 1.28),
                        Shotgunguy(Pos(346, 164), 1.5),
                    ], [
                        GArmor(Pos(283, 199), 0.79)
                    ], []),
                    Room('stairs', 'https://ifmn.neocities.org/bg_stairs.png', [
                        Shotgunguy(Pos(300, 179), 1.6),
                    ], [
                        HBonus(Pos(138, 232), 0.9),
                        HBonus(Pos(452, 232), 0.9),
                    ], []),
                    Room('start', 'https://ifmn.neocities.org/bg_start.png', [], [], []),
                    Room('hall1', 'https://ifmn.neocities.org/bg_hall1.png', [], [
                        ABonus(Pos(248, 251), 1),
                    ], []),
                    Room('door1', 'https://ifmn.neocities.org/bg_door1.png', [], [], [
                        Interactive(Pos(227-20, 62), Size(243, 254), 'https://ifmn.neocities.org/int_door1.png') ]
                ),
                    Room('comp', 'https://ifmn.neocities.org/bg_comp.png', [
                        Zombieman(Pos(194, 142), 0.67),
                        Zombieman(Pos(255, 149), 1.11)
                    ], [
                        ABonus(Pos(103, 228), 0.63),
                        ABonus(Pos(141, 213), 0.60),
                    ], []),
                    Room('hall2', 'https://ifmn.neocities.org/bg_hall2.png', [
                        Shotgunguy(Pos(194, 189), 1)
                    ], [
                        HBonus(Pos(186, 256), 0.75),
                    ], []),
                    Room('acid', 'https://ifmn.neocities.org/bg_acid.png', [
                        Shotgunguy(Pos(376, 142), 1.93),
                        Zombieman(Pos(349, 169), 0.58),
                        Imp(Pos(167, 97), 0.42),
                    ], [], []),
                    Room('door2', 'https://ifmn.neocities.org/bg_door2.png', [
                    ], [], [
                        Interactive(Pos(146-20,116), Size(211, 160), 'https://ifmn.neocities.org/int_door2.png'),
                        Interactive(Pos(423-20,0), Size(216, 400), 'https://ifmn.neocities.org/int_secret.png'),
                    ]),
                    Room('secret1', 'https://ifmn.neocities.org/bg_secret1.png', [
                        Shotgunguy(Pos(279, 249), 0.75)
                    ], [], []),
                    Room('secret2', 'https://ifmn.neocities.org/bg_secret2.png', [], [
                        Medikit(Pos(126, 268), 1.66),
                    ], []),
                Room('secret3', 'https://ifmn.neocities.org/bg_secret3.png', [], [
                        BArmor(Pos(243, 255), 1.19)
                    ], []),
                Room('to_exit', 'https://ifmn.neocities.org/bg_toexit.png', [
                        Imp(Pos(77, 143), 1.41)], [], []),
                Room('exit_left', 'https://ifmn.neocities.org/bg_exleft.png', [
                        Zombieman(Pos(432, 177), 1.46)
                    ], [
                        ABonus(Pos(379, 236), 0.59),
                        Stimpack(Pos(195, 267), 1),
                    ], []),
                Room('exit_right', 'https://ifmn.neocities.org/bg_exright.png', [
                        Shotgunguy(Pos(118, 155), 1.39)
                    ], [
                        Stimpack(Pos(227, 230), 0.57),
                        Medikit(Pos(252, 224), 0.68),
                    ], []),
                Room('door3', 'https://ifmn.neocities.org/bg_door3.png', [
                        Imp(Pos(243, 151), 1),
                    ], [], [
                        Interactive(Pos(224-20,91), Size(190, 242), 'https://ifmn.neocities.org/int_door3.png'),
                    ]),
                Room('exit', 'https://ifmn.neocities.org/bg_exit.png', [], [], []),
                Room('finish', 'https://ifmn.neocities.org/finish.png', [], [], []),
                ]
        i = 0
        for room in Settings.rooms:
            room.index = i
            i += 1

class Textures:
    arrows = {
            'left': 'https://ifmn.neocities.org/arrow_left.png',
            'right': 'https://ifmn.neocities.org/arrow_right.png',
            'up': 'https://ifmn.neocities.org/arrow_up.png',
            'back': 'https://ifmn.neocities.org/arrow_back.png'
            }
    sbar = 'https://ifmn.neocities.org/sbar.png'
    numbers = [
            'https://ifmn.neocities.org/num0.png', 'https://ifmn.neocities.org/num1.png', 'https://ifmn.neocities.org/num2.png', 'https://ifmn.neocities.org/num3.png',
            'https://ifmn.neocities.org/num4.png', 'https://ifmn.neocities.org/num5.png', 'https://ifmn.neocities.org/num6.png', 'https://ifmn.neocities.org/num7.png',
            'https://ifmn.neocities.org/num8.png', 'https://ifmn.neocities.org/num9.png', 'https://ifmn.neocities.org/nump.png'
            ]
    pistol = 'https://ifmn.neocities.org/pistol.png'
    monsters = {
            'zombie-alive':'https://ifmn.neocities.org/zombie1.png',
            'zombie-dead':'https://ifmn.neocities.org/zombie2.png',
            'shotgun-alive':'https://ifmn.neocities.org/shotgun1.png',
            'shotgun-dead':'https://ifmn.neocities.org/shotgun2.png',
            'imp-alive':'https://ifmn.neocities.org/imp1.png',
            'imp-dead':'https://ifmn.neocities.org/imp2.png'
            }
    items = {
            'garmor':'https://ifmn.neocities.org/garmor.png',
            'barmor':'https://ifmn.neocities.org/barmor.png',
            'stimpack':'https://ifmn.neocities.org/stimpack.png',
            'medikit':'https://ifmn.neocities.org/medikit.png',
            'hbonus':'https://ifmn.neocities.org/hbonus.png',
            'abonus':'https://ifmn.neocities.org/abonus.png'
            }

