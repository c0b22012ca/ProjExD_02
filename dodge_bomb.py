
import random
import sys

import pygame as pg

de = {pg.K_UP:((0,-1)),#移動の辞書
          pg.K_DOWN:((0,+1)),
          pg.K_LEFT:((-1,0)),
          pg.K_RIGHT:((+1,0))}

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    tmr = 0

    kk_rct = kk_img.get_rect()#rectクラスの生成と値ゲット
    kk_rct.center = 900,400

    bb_img = pg.Surface((20,20))
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)
    bb_img.set_colorkey((0,0,0))
    bb_x = random.randint(0,1600)
    bb_y = random.randint(0,900)
    vx = +1
    vy = +1
    bb_rect = bb_img.get_rect()#rectクラスの生成と値ゲット
    bb_rect.center = bb_x,bb_y#rectクラスのcenterインスタンスの変更
    bb_rect.move_ip(vx,vy)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        key_lst = pg.key.get_pressed()
        for k,v in de.items():#kが押されたキー、ｖが移動方向
            if key_lst[k]:
                kk_rct.move_ip(v)

        bb_rect.move_ip(vx,vy)
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        screen.blit(bb_img,bb_rect)
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()