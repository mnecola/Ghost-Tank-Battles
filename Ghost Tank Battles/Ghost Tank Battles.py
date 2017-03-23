from gamelib import *



game = Game(800,600,"Game")



greenline = []
blackline = []
blueline = []
blackbox = []

for times in range(3):
    blackline.append(Image("images\\blackline.png",game))
    greenline.append(Image("images\\greenline.png",game))
    blueline.append(Image("images\\blueline.png",game))
    blackbox.append(Image("images\\black box.jpg",game))
    
    
for b in blackline:
    x = randint(50,700)
    y = randint(50, 530)
    b.moveTo(x,y)
    
for g in greenline:
    x = randint(50,700)
    y = randint(50, 530)
    g.moveTo(x,y)
    
for bl in blueline:
    x = randint(50,700)
    y = randint(50, 530)
    bl.moveTo(x,y)

for bb in blackbox:
    x = randint(50,700)
    y = randint(50, 530)
    bb.moveTo(x,y)

bullet2 = Image("images\\bullet2.png",game)
bullet1 = Image("images\\bullet1.png",game)
tank = Image("images\\tank1.png",game)
tank2 = Image("images\\tank2.png",game)
count = 0
tank.draw()
tank2.draw()


game.drawText("Ghost Tank Battles",game.width/4 ,game.height/4,Font(blue,90,yellow))
game.drawText("Press [SPACE] to Start",game.width/2 + 80,game.height - 50,Font(yellow,40,green))
game.update()#add an update
game.wait(K_SPACE)#add wait time



explosion = Animation("images\\explosion.png",22,game, 285/5, 320/5)
explosion.visible = False

plasma = Animation("images\\plasmaball1.png",11,game,352/11,32)
plasma.visible = False

plasma2 = Animation("images\\plasmaball1.png",11,game,352/11,32)
plasma2.visible = False



tank.moveTo(720,550)
tank2.moveTo(30,30)

while not game.over:
    
    game.processInput()
    
    game.clearBackground(white)
    bullet2.move()
    bullet1.move()
    tank.move()
    tank2.move()
    explosion.draw(False) #False makes the animation play only once
    plasma.move()
    plasma2.move()

#Tank 1
 
    if keys.Pressed[K_LEFT]:
        tank.rotateBy(3,"left")
        
    if keys.Pressed[K_RIGHT]:
        tank.rotateBy(3,"right")
 
    if keys.Pressed[K_UP]:
        tank.forward(2)
    else:
        tank.speed *= 0.99

    if keys.Pressed[K_DOWN]:
        tank.forward(-2)

    if keys.Pressed[K_m]:
        bullet1.visible = True
        bullet1.moveTo(tank.x,tank.y)
        bullet1.setSpeed(3 , tank.getAngle())

    
    if bullet2.collidedWith(tank):
            tank.visible=False
            explosion.visible = True
            explosion.moveTo(tank2.x,tank2.y)
            game.over = True
    
    for b in blackline:
        if bullet1.collidedWith(b,"rectangle"):
            bullet1.visible = False
            explosion.visible = True
            explosion.moveTo(bullet1.x,bullet1.y)

    for bl in blueline:
        if bullet1.collidedWith(bl,"rectangle"):
            bullet1.visible = False
            explosion.visible = True
            explosion.moveTo(bullet1.x,bullet1.y)

    for g in greenline:
        if bullet1.collidedWith(g,"rectangle"):
            bullet1.visible = False
            explosion.visible = True
            explosion.moveTo(bullet1.x,bullet1.y)

    for bb in blackbox:
        if bullet1.collidedWith(bb,"rectangle"):
            bullet1.visible = False
            explosion.visible = True
            explosion.moveTo(bullet1.x,bullet1.y)

#Tank 2
    
    if keys.Pressed[K_a]:
        tank2.rotateBy(3,"left")
        
    if keys.Pressed[K_d]:
         tank2.rotateBy(3,"right")
 
    if keys.Pressed[K_w]:
        tank2.forward(2)
    else:
        tank2.speed *= 0.99

    if keys.Pressed[K_s]:
        tank2.forward(-2)

    if keys.Pressed[K_q]:
        bullet2.visible = True
        bullet2.moveTo(tank2.x,tank2.y)
        bullet2.setSpeed(3 , tank2.getAngle())


    if count>=20:
        game.over =True

    for b in blackline:
        b.draw()
        

    for g in greenline:
        g.draw()
        
    for bl in blueline:
        bl.draw()
        
    for bb in blackbox:
        bb.draw()
    
    if bullet1.collidedWith(tank2):
            tank2.visible=False
            explosion.visible = True
            explosion.moveTo(tank2.x,tank2.y)
            game.over = True
            
    for b in blackline:
        if bullet2.collidedWith(b,"rectangle"):
            bullet2.visible = False
            explosion.visible = True
            explosion.moveTo(bullet2.x,bullet2.y)

    for bl in blueline:
        if bullet2.collidedWith(bl,"rectangle"):
            bullet2.visible = False
            explosion.visible = True
            explosion.moveTo(bullet2.x,bullet2.y)

    for g in greenline:
        if bullet2.collidedWith(g,"rectangle"):
            bullet2.visible = False
            explosion.visible = True
            explosion.moveTo(bullet2.x,bullet2.y)

    for bb in blackbox:
        if bullet2.collidedWith(bb,"rectangle"):
            bullet2.visible = False
            explosion.visible = True
            explosion.moveTo(bullet2.x,bullet2.y)
    
    game.update(60)


game.drawText("Game Over",game.width/4,game.height/3,Font(green,90,yellow))
game.drawText("Press [ESC] to Exit",game.width/2 + 80,game.height - 50,Font(yellow,40,green))
game.update()
game.wait(K_ESCAPE)




    
    
game.quit()
