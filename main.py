import pygame
from pygame.locals import *
import sys
import os

pygame.init()
piece_height, piece_width = (64, 64)

screen = pygame.display.set_mode((piece_height * 11, piece_width * 11))
pygame.display.set_caption("shogi_app")

# piece_imgフォルダの中身のファイル名を変数名にして、６４ｘ６４の画像に変換
for file in os.listdir("./piece_img"):
    globals()[file[:-4]] = pygame.transform.scale(pygame.image.load(f"piece_img/{file}"), (64, 64))

syokei = (
    ([kyou, 2], [kei, 2], [gin, 2], [kin, 2], [gyoku, 2], [kin, 2], [gin, 2], [kei, 2], [kyou, 2]),
    (0, [hi, 2], 0, 0, 0, 0, 0, [kaku, 2], 0),
    ([fu, 2], [fu, 2], [fu, 2], [fu, 2], [fu, 2], [fu, 2], [fu, 2], [fu, 2], [fu, 2]),
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0),
    ([fu, 1], [fu, 1], [fu, 1], [fu, 1], [fu, 1], [fu, 1], [fu, 1], [fu, 1], [fu, 1]),
    (0, [hi, 1], 0, 0, 0, 0, 0, [kaku, 1], 0),
    ([kyou, 1], [kei, 1], [gin, 1], [kin, 1], [gyoku, 1], [kin, 1], [gin, 1], [kei, 1], [kyou, 1])

)

running = True
while running:
    screen.fill((0, 0, 0))
    banmen = pygame.Surface((64 * 9, 64 * 9))
    banmen.fill((255, 255, 153))
    for i in range(9):
        pygame.draw.line(banmen, (0, 0, 0), (64* i, 0), (64 * i, 576))
        pygame.draw.line(banmen, (0, 0, 0), (0, 64 * i), (576, 64 * i))
    pygame.draw.line(banmen, (0, 0, 0), (128, 128), (128, 600))
    screen.blit(banmen, (64, 64))

    # for i in range(1, 10):
    #     for k in range(1, 10):
    #         screen.blit(tokin, (64 * i, 64 * k))
    for row in syokei:
        for c, column in enumerate(row):
            if column:
                if column[1] == 2:
                    img = pygame.transform.rotate(column[0], 180)
                else:
                    img = column[0]
                screen.blit(img, (64 * (c + 1), 64 * (syokei.index(row) + 1)))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            sys.exit()
    pygame.display.update()
