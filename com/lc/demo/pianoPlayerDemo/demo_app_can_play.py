from piano_player import Player

# 设置曲谱
sheet_music = (
    ('C4', 0.5), ('D4', 0.5), ('E4', 0.5), ('C4', 0.5),  # 两只老虎
    ('C4', 0.5), ('D4', 0.5), ('E4', 0.5), ('C4', 0.5),  # 两只老虎
    ('E4', 0.5), ('F4', 0.5), ('G4', 1),  # 跑得快
    ('E4', 0.5), ('F4', 0.5), ('G4', 1),  # 跑得快
    ('G4', 0.25), ('A4', 0.25), ('G4', 0.25), ('F4', 0.25), ('E4', 0.5), ('C4', 0.5),  # 一只没有耳朵
    ('G4', 0.25), ('A4', 0.25), ('G4', 0.25), ('F4', 0.25), ('E4', 0.5), ('C4', 0.5),  # 一只没有尾巴
    ('D4', 0.5), ('G3', 0.5), ('C4', 1),  # 真奇怪
    ('D4', 0.5), ('G3', 0.5), ('C4', 1)  # 真奇怪
)

Player.play_many(sheet_music)
