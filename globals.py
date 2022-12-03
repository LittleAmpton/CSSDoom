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
            Counter(Pos(200, 406), 16, None, False),
            Counter(Pos(450, 100), 16, 'finish', True)
        ]
        Settings.item_counters = [
            Counter(Pos(350, 406), 15, None, False),
            Counter(Pos(450, 138), 15, 'finish', True)
        ]

    def create_rooms():
        from clickables import Counter, Zombieman, Shotgunguy, Imp,\
                GArmor, BArmor, Medikit, Stimpack, HBonus, ABonus
        from interactives import Interactive
        from helper import Pos, Size
        from room import Room
        # in order!
        Settings.rooms = [
                Room('armor', 'https://staging.cohostcdn.org/attachment/f17ab89b-66b6-4b61-97ee-0c27f08737dc/bg_armor.png', [
                        Shotgunguy(Pos(177, 154), 1.28),
                        Shotgunguy(Pos(346, 164), 1.5),
                    ], [
                        GArmor(Pos(283, 199), 0.79)
                    ], []),
                Room('stairs', 'https://staging.cohostcdn.org/attachment/5f789f5d-f920-45c6-9257-d55c13958295/bg_stairs.png', [
                        Shotgunguy(Pos(133, 163), 1.3),
                        Shotgunguy(Pos(300, 179), 1.6),
                    ], [
                        HBonus(Pos(138, 232), 0.9),
                        HBonus(Pos(452, 232), 0.9),
                    ], []),
                Room('start', 'https://staging.cohostcdn.org/attachment/1bc7b949-9ccc-4122-90fa-04a60f835818/bg_start.png', [], [], []),
                Room('hall1', 'https://staging.cohostcdn.org/attachment/050875ef-0c6a-402a-9a10-81eed7fc982f/bg_hall1.png', [], [
                        ABonus(Pos(248, 251), 1),
                    ], []),
                Room('door1', 'https://staging.cohostcdn.org/attachment/a6c0a87f-1737-4776-8714-92483544af93/bg_door1.png', [], [], [
                        Interactive(Pos(227-20, 62), Size(243, 254), 'https://staging.cohostcdn.org/attachment/6683e47a-6b20-405c-ad70-3fb49dc199e1/int_door1.png') ]
                ),
                Room('comp', 'https://staging.cohostcdn.org/attachment/5d3e2c20-9d60-4cb0-8041-edf1e7e5682b/bg_comp.png', [
                        Zombieman(Pos(194, 142), 0.67),
                        Zombieman(Pos(255, 149), 1.11)
                    ], [
                        ABonus(Pos(103, 228), 0.63),
                        ABonus(Pos(141, 213), 0.60),
                    ], []),
                Room('hall2', 'https://staging.cohostcdn.org/attachment/6deb6a8a-6c00-4066-9324-86a572c2e419/bg_hall2.png', [
                        Shotgunguy(Pos(194, 189), 1)
                    ], [
                        HBonus(Pos(186, 256), 0.75),
                        HBonus(Pos(202, 243), 0.64),
                    ], []),
                Room('acid', 'https://staging.cohostcdn.org/attachment/508a12bb-b64b-47c2-bbde-aa688be92aae/bg_acid.png', [
                        Shotgunguy(Pos(376, 142), 1.93),
                        Zombieman(Pos(262, 177), 1),
                        Zombieman(Pos(349, 169), 0.58),
                        Imp(Pos(167, 97), 0.42),
                    ], [], []),
                Room('door2', 'https://staging.cohostcdn.org/attachment/bcbe116a-9903-4168-9029-0804a1d0ca3d/bg_door2.png', [
                    ], [], [
                        Interactive(Pos(146-20,116), Size(211, 160), 'https://staging.cohostcdn.org/attachment/b8a449fa-4003-4d46-ae25-94f8aadefbbd/int_door2.png'),
                        Interactive(Pos(423-20,0), Size(216, 400), 'https://staging.cohostcdn.org/attachment/e6b51998-50bf-4047-9015-4467fb168f4f/int_secret.png'),
                    ]),
                Room('secret1', 'https://staging.cohostcdn.org/attachment/13038e84-2cfd-4fbb-b468-eae7f4e8c61f/bg_secret1.png', [
                        Shotgunguy(Pos(279, 249), 0.75)
                    ], [], []),
                Room('secret2', 'https://staging.cohostcdn.org/attachment/ad1c55b9-c10b-440c-bcf0-8b1f7f73cd43/bg_secret2.png', [], [
                        Medikit(Pos(126, 268), 1.66),
                    ], []),
                Room('secret3', 'https://staging.cohostcdn.org/attachment/fdf49c5a-00b7-4880-b8a4-d61800775546/bg_secret3.png', [], [
                        BArmor(Pos(243, 255), 1.19)
                    ], []),
                Room('to_exit', 'https://staging.cohostcdn.org/attachment/da0082f9-c35a-4d4e-b18c-546247bd6d01/bg_toexit.png', [
                        Imp(Pos(77, 143), 1.41)], [], []),
                Room('exit_left', 'https://staging.cohostcdn.org/attachment/26055cf4-68ee-4a3d-a8fc-5ce6ce128ab3/bg_exleft.png', [
                        Zombieman(Pos(432, 177), 1.46)
                    ], [
                        ABonus(Pos(379, 236), 0.59),
                        ABonus(Pos(347, 233), 0.59),
                        Stimpack(Pos(195, 267), 1),
                    ], []),
                Room('exit_right', 'https://staging.cohostcdn.org/attachment/09dd38da-1e25-49b9-ba9d-4ed0d8caf4ad/bg_exright.png', [
                        Shotgunguy(Pos(118, 155), 1.39)
                    ], [
                        Stimpack(Pos(227, 230), 0.57),
                        Medikit(Pos(252, 224), 0.68),
                    ], []),
                Room('door3', 'https://staging.cohostcdn.org/attachment/f81d3c66-3bcb-4f05-aac8-1c4f2b137f52/bg_door3.png', [
                        Imp(Pos(243, 151), 1),
                    ], [], [
                        Interactive(Pos(224-20,91), Size(190, 242), 'https://staging.cohostcdn.org/attachment/456077f7-2a22-48eb-b847-ae16075b5b4b/int_door3.png'),
                    ]),
                Room('exit', 'https://staging.cohostcdn.org/attachment/bdb44b20-00a4-4c20-a285-7d18f7849b99/bg_exit.png', [], [], []),
                Room('finish', 'https://staging.cohostcdn.org/attachment/3df39923-4fb6-4bc1-bf02-fbf6dec98df8/finish.png', [], [], []),
                ]
        i = 0
        for room in Settings.rooms:
            room.index = i
            i += 1

class Textures:
    arrows = {
            'left': 'https://staging.cohostcdn.org/attachment/151648ce-3536-46c1-9f4f-31e0970c4946/arrow_left.png',
            'right': 'https://staging.cohostcdn.org/attachment/84a1c70b-c4ba-41bd-963c-2382f7273f10/arrow_right.png',
            'up': 'https://staging.cohostcdn.org/attachment/5fbe1385-d15c-4b3c-893c-fafc213e7b30/arrow_up.png',
            'back': 'https://staging.cohostcdn.org/attachment/84e9a6c8-94d9-421b-b6e8-6e0c8a52fc61/arrow_back.png'
            }
    sbar = 'https://staging.cohostcdn.org/attachment/a8956119-aded-42d7-8594-f38662e8ef42/sbar.png'
    numbers = [
            'https://staging.cohostcdn.org/attachment/f1851eee-253c-4455-8ca5-42eb11b161be/num0.png',
            'https://staging.cohostcdn.org/attachment/8da8dff3-ae54-40d3-8a72-d2eab68c5399/num1.png',
            'https://staging.cohostcdn.org/attachment/bf1e48e0-22d3-4d2f-8f66-0e2a57f25af7/num2.png',
            'https://staging.cohostcdn.org/attachment/481fde31-b89f-4555-b060-dc08f01587e1/num3.png',
            'https://staging.cohostcdn.org/attachment/a9ac6031-984f-4c15-bff5-b73e561d539a/num4.png',
            'https://staging.cohostcdn.org/attachment/14f5bfea-db29-4761-a356-bd8e8aa35468/num5.png',
            'https://staging.cohostcdn.org/attachment/ea994178-98b6-441a-9c06-87155b58ee5e/num6.png',
            'https://staging.cohostcdn.org/attachment/d05f38b2-08db-462c-8f7b-eedfba8024b8/num7.png',
            'https://staging.cohostcdn.org/attachment/55eeb001-fce5-4e32-86b8-b615bddd0dfd/num8.png',
            'https://staging.cohostcdn.org/attachment/0337552a-6088-4493-9752-fbede209d400/num9.png',
            'https://staging.cohostcdn.org/attachment/769774a3-c3ff-45ce-a5d5-0009ba2a6654/nump.png'
            ]
    pistol = 'https://staging.cohostcdn.org/attachment/8a62750a-4a2a-474b-873e-b2e64e9830dd/pistol.png'
    monsters = {
            'zombie-alive':'https://staging.cohostcdn.org/attachment/ad4169d6-13b6-44fe-8595-9316418fa3f7/zombie1.png',
            'zombie-dead':'https://staging.cohostcdn.org/attachment/65d58d67-9c46-4c69-82d8-5751bf6a7538/zombie2.png',
            'shotgun-alive':'https://staging.cohostcdn.org/attachment/f23f7e34-fc6e-456d-87cb-38cde82c35ff/shotgun1.png',
            'shotgun-dead':'https://staging.cohostcdn.org/attachment/5686193d-5c98-4b6f-b66a-fa0d0977e0ca/shotgun2.png',
            'imp-alive':'https://staging.cohostcdn.org/attachment/88decbf8-96bf-445e-9ecf-fccae5873455/imp1.png',
            'imp-dead':'https://staging.cohostcdn.org/attachment/53648759-61b4-4fcb-b6a3-7ea2a8979fa2/imp2.png'
            }
    items = {
            'garmor':'https://staging.cohostcdn.org/attachment/45493e42-44f3-4f78-9e51-34f4f67c7592/garmor.png',
            'barmor':'https://staging.cohostcdn.org/attachment/0ad79883-abc0-416b-80ac-6751be96701d/barmor.png',
            'stimpack':'https://staging.cohostcdn.org/attachment/7b4c9db2-d9a2-4b5d-8e75-26e5a9eec250/stimpack.png',
            'medikit':'https://staging.cohostcdn.org/attachment/c837de01-c768-4711-a959-838aa1cfa1e7/medikit.png',
            'hbonus':'https://staging.cohostcdn.org/attachment/981dc729-7168-4f11-891b-43a7be4030bf/hbonus.png',
            'abonus':'https://staging.cohostcdn.org/attachment/034e154b-bd64-41a2-8675-fcfaef6a5985/abonus.png'
            }

