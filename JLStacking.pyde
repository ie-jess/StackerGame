paddleX = 250
paddleY = 750
movingRight = True
stackerX = random(100, 400)
stackerY = 100
level = 0
gameOver = False

def  setup():
    size(500, 800)
    textSize (24)
    rectMode(CENTER)
    
def draw():
    #tryna add this dumb shit as a new starting page D;
#    global gameStart
#    if(gameStart == False):
#        restart()
#    else:
#        startingPage()
        
    
    global gameOver
    if(gameOver == True):
        fill(0,0,0)
        rect (250, 400, 500, 800)
        fill (255,255,255)
        text ("GAME OVER", 175, 400)
        text ("Thanks for playing!", 135, 450)
    else:
        background(0)
        movePaddle()
        drawPaddle()
        drawStacker()
        moveStacker()
        checkForCatch()
        showScore()
       
#def startingPage():
#    background(0)
#    text ("Stack Bricks!", 175, 400)
#    text ("Click space to start game.", 135, 450)
#    if (startGame == True):
        
    
    
        
def showScore():
    fill (255)
    text ("Level: " + str(level), 400, 30)
    
def checkForCatch():
    global paddleX, paddleY, stackerX, stackerY, level, gameOver
    if (level == 0):
        if (stackerY > 705 and dist(stackerX, stackerY, paddleX, paddleY)<40):
            level = 1
            stackerY = random(-200, -100)
            stackerX = random (100, 400) 
    if (level == 1):
        if (stackerY > 635 and stackerY < 650 and dist(paddleX, paddleY, stackerX, stackerY)<110):
            level = 2
            stackerY = random(-200, -100)
            stackerX = random (100, 400) 
    if (level == 2):
        if (stackerY > 565 and stackerY < 580 and dist(paddleX, paddleY, stackerX, stackerY)<180):
            level = 3
            stackerY = random(-200, -100)
            stackerX = random (100, 400) 
    if (level == 3):
        if (stackerY > 495 and stackerY < 510 and dist(paddleX, paddleY, stackerX, stackerY)<250):
            level = 4
            stackerY = random(-200, -100)
            stackerX = random (100, 400)
        
            
def drawStacker():
    global stackerX, stackerY, level
    if (level == 0):
        fill (0, 0, 255)
        rect(stackerX, stackerY, 70, 70)
    elif (level == 1):
        fill (0, 255, 0)
        rect(stackerX, stackerY, 70, 70)
    elif (level == 2):
        fill (255, 0, 255)
        rect(stackerX, stackerY, 70, 70)
    elif (level == 3):
        fill (0, 255, 255)
        rect(stackerX, stackerY, 70, 70)
    
    
def drawPaddle():
    global paddleX, paddleY
    fill(255, 0, 0)
    rect(paddleX, paddleY, 100, 30)
    if (level >= 1):
        fill(0, 0, 255)
        rect (paddleX, paddleY-50, 70, 70)
    if (level >= 2):
        fill(0, 255, 0)
        rect (paddleX, paddleY-120, 70, 70)
    if (level >= 3):
        fill (255, 0, 255)
        rect (paddleX, paddleY-190, 70, 70)
    if (level >= 4):
       fill (0, 255, 255)
       rect (paddleX, paddleY-260, 70, 70)
    
def movePaddle():
    global paddleX, movingRight, level
    if(movingRight == True):
        if (level == 0):
           paddleX = paddleX + 2
        elif (level == 1):
            paddleX = paddleX + 3
        elif (level == 2):
            paddleX = paddleX + 4
        elif (level == 3):
            paddleX = paddleX + 5
    else:
        if (level == 0):
           paddleX = paddleX - 2
        elif (level == 1):
            paddleX = paddleX - 3
        elif (level == 2):
            paddleX = paddleX - 4
        elif (level == 3):
            paddleX = paddleX - 5
    if(paddleX > 500):
        paddleX = 0
    if(paddleX < 0):
        paddleX = 500 
        
def moveStacker():
    global stackerY, gameOver, level
    if (level == 0):
        stackerY = stackerY + 3
    elif (level == 1):
        stackerY = stackerY + 5
    elif (level == 2):
        stackerY = stackerY + 8
    elif (level == 3):
        stackerY = stackerY + 10
    elif (level == 4):
        gameOver = True
    if (stackerY > 800):
        gameOver = True
        
#def restart():
#    global gameOver
#    gameOver = False
        
   
def mousePressed():
    global movingRight
    if(mouseButton == RIGHT):
        movingRight = True
    if(mouseButton == LEFT):
        movingRight = False
        
#def keyPressed():
#    if(key == 'r'):
#        restart()
#    if(key == ' '):
#        startGame = True
        
