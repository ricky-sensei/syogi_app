import pygame
from pygame.locals import *
import sys
import os

"""
スクリプト内の符号はｘ：左から０−８ ｙ：上から０−８で統一

"""
pygame.init()
piece_height, piece_width = (64, 64)

screen = pygame.display.set_mode((piece_height * 11, piece_width * 11))
pygame.display.set_caption("shogi_app")

# piece_imgフォルダの中身のファイル名を変数名にして、６４ｘ６４の画像に変換
for file in os.listdir("./piece_img"):
    globals()[file[:-4]] = pygame.transform.scale(pygame.image.load(f"piece_img/{file}"), (64, 64))

banmen = [
    [[kyou, 2], [kei, 2], [gin, 2], [kin, 2], [gyoku, 2], [kin, 2], [gin, 2], [kei, 2], [kyou, 2]],
    [0, [hi, 2], 0, 0, 0, 0, 0, [kaku, 2], 0],
    [[fu, 2], [fu, 2], [fu, 2], [fu, 2], [fu, 2], [fu, 2], [fu, 2], [fu, 2], [fu, 2]],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [[fu, 1], [fu, 1], [fu, 1], [fu, 1], [fu, 1], [fu, 1], [fu, 1], [fu, 1], [fu, 1]],
    [0, [kaku, 1], 0, 0, 0, 0, 0, [hi, 1], 0],
    [[kyou, 1], [kei, 1], [gin, 1], [kin, 1], [gyoku, 1], [kin, 1], [gin, 1], [kei, 1], [kyou, 1]]
]

running = True
selected = False
selected_index_x = None
selected_index_y = None
screen.fill((0, 0, 0))
syougiban = pygame.Surface((64 * 9, 64 * 9))
syougiban.fill((255, 255, 153))

for i in range(9):
    pygame.draw.line(syougiban, (0, 0, 0), (64 * i, 0), (64 * i, 576))
    pygame.draw.line(syougiban, (0, 0, 0), (0, 64 * i), (576, 64 * i))
while running:
    screen.blit(syougiban, (64, 64))
    for r, row in enumerate(banmen):
        for c, column in enumerate(row):
            if column:
                if column[1] == 2:
                    img = pygame.transform.rotate(column[0], 180)
                else:
                    img = column[0]
                screen.blit(img, (64 * (c + 1), 64 * (banmen.index(row) + 1)))
                if (c, r) == (selected_index_x, selected_index_y):
                    pygame.draw.rect(screen, (255, 0, 0), (64 * (c + 1), 64 * (banmen.index(row) + 1), 64, 64), 1)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if selected:
                selected = False
                moveto_pos_x, moveto_pos_y = pygame.mouse.get_pos()
                moveto_index_x = moveto_pos_x // 64 - 1
                moveto_index_y = moveto_pos_y // 64 - 1
                banmen[moveto_index_y][moveto_index_x] = banmen[selected_index_y][selected_index_x]
                banmen[selected_index_y][selected_index_x] = 0
            else:
                selected = True
                selected_pos_x, selected_pos_y = pygame.mouse.get_pos()
                selected_index_x = selected_pos_x // 64 - 1
                selected_index_y = selected_pos_y // 64 - 1
                print(selected_index_x, selected_index_y)

    pygame.display.update()
