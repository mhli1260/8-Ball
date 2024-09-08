from vectors import Vec
from ball import Ball
# from stick import Stick
import math
from cmu_112_graphics import *

#initializes all variables
def appStarted(app):
    app.timerDelay = 10
    app.timerCount = 0
    app.seconds = 0
    app.totalTime = 300
    app.timer = False

    #initializing main variables
    app.count = 0
    app.radius = 10
    app.mass = 300
    app.cueStickX = 200 + app.radius + 10
    app.cueStickY = app.height / 2 + app.radius
    app.dragX = 0
    app.dragY = 0
    app.angle = 0
    app.margin = 20
    app.startStick = 500
    app.endStick = 20000
    app.stickx1 = 0
    app.stickx2 = 0
    app.sticky1 = 0
    app.sticky2 = 0
    app.winner = ''
    app.showStick = True
    app.playerTurn = True
    app.TitleScreen = True
    app.MainScreen = False
    app.WinnerScreen = False
    app.ChallengeWin = True
    app.Challenge = False
    app.DirectionScreen = False
    app.ChallengeScreen = False
    app.player = 0
    app.playercount = True
    app.playcount = 0
    app.length = 16
    app.turn = True
    app.player1 = ''
    app.player2 = ''
    #15-122 Animations Part 4 Notes
    #I found my image from: https://www.google.com/url?sa=i&url=https%3A%2F%2F\
    #www.govtech.com%2Feducation%2Fhigher-ed%2Fhow-to-avoid-being-behind-the-\
    #it-eight-ball&psig=AOvVaw306SHsKUWB_v6MUMA5hB5U&ust=1670524184116000&sour\
    #ce=images&cd=vfe&ved=0CA4QjRxqFwoTCJCyiNaR6PsCFQAAAAAdAAAAABAE
    app.image = Image.open('8 ball background.jpeg')
    app.image2 = app.scaleImage(app.image, 4)

    #creating ball objects
    app.ball1 = Ball(780, 310, 0, 'red', 0, True, 15)
    app.ball2 = Ball(190 , 300 , 0, 'white', 0, False, 0) #white cue ball
    app.ball3 = Ball(800, 300, 0, 'green4', 0, False, 6)
    app.ball4 = Ball(800, 320, 0, 'maroon', 0, True, 16)
    app.ball5 = Ball(800, 260, 0, 'blue', 0, True, 10)
    app.ball6 = Ball(760, 300, 0, 'black', 0, False, 8)
    app.ball7 = Ball(740, 310, 0, 'dark orange', 0, True, 13)
    app.ball8 = Ball(740, 290, 0, 'dark orange', 0, False, 5)
    app.ball9 = Ball(720, 300, 0, 'yellow', 0, True, 9)
    app.ball10 = Ball(800, 280, 0, 'green4', 0, True, 14)  
    app.ball11 = Ball(800, 340, 0, 'purple', 0, True, 12)
    app.ball12 = Ball(780, 290, 0, 'purple', 0, False, 4)
    app.ball13 = Ball(780, 270, 0, 'blue', 0, False, 2)
    app.ball14 = Ball(780, 330, 0, 'yellow', 0, False, 1)
    app.ball15 = Ball(760, 280, 0, 'maroon', 0, False, 7)
    app.ball16 = Ball(760, 320, 0, 'red', 0, False, 3)
    app.balls = [app.ball1, app.ball2, app.ball3, app.ball4, app.ball5, 
    app.ball6, app.ball7, app.ball8, app.ball9, app.ball10,
    app.ball11, app.ball12, app.ball13, app.ball14, app.ball15, app.ball16] 
    app.stripe = [app.ball1, app.ball4, app.ball5, app.ball7, app.ball9, 
    app.ball10, app.ball11, app.ball6]
    app.stripe2 = [app.ball1, app.ball4, app.ball5, app.ball7, app.ball9, 
    app.ball10, app.ball11, app.ball6]
    app.solid = [app.ball3, app.ball16, app.ball8, app.ball12, app.ball13, 
    app.ball14, app.ball15, app.ball6]
    app.solid2 = [app.ball3, app.ball16, app.ball8, app.ball12, app.ball13, 
    app.ball14, app.ball15, app.ball6]

#returns True if balls collided, False if not
def isHit(app, ball, ball1):
    dividend = (ball1.pos.x - ball.pos.x)**2 + (ball1.pos.y - ball.pos.y)**2
    distance = math.sqrt(dividend)
    
    if distance <= app.radius * 2:
        return True
    return False

#calculates ball collisions
#I learned the physics behind how collisions work from: 
# https://www.youtube.com/watch?v=lul_-MjnGuk
def collision(app, balla, ballb):
    dx = ballb.pos.x - balla.pos.x
    dy = ballb.pos.y - balla.pos.y
    
    if isHit(app, balla, ballb) == True:
        angle = math.atan2(dy,dx)
        aX = 0 
        aY = 0
        bX = dx*math.cos(angle) + dy*math.sin(angle)
        bY = dy*math.cos(angle) - dx*math.sin(angle)

        #calculating change in angles
        vela_x = balla.vel.x*math.cos(angle) + balla.vel.y*math.sin(angle)
        vela_y = balla.vel.y*math.cos(angle) - balla.vel.x*math.sin(angle)
        velb_x = ballb.vel.x*math.cos(angle) + ballb.vel.y*math.sin(angle)
        velb_y = ballb.vel.y*math.cos(angle) - ballb.vel.x*math.sin(angle)

        temp = vela_x 
        vela_x = (2*app.mass*velb_x)/(app.mass*2)
        velb_x = (2*app.mass*temp)/(app.mass*2)

        totalVel = abs(vela_x) + abs(velb_x)
        cross = (app.radius * 2) - abs(aX-bX)
        if (totalVel == 0):
            totalVel = 0.000000000001
        aX = aX + vela_x/totalVel*cross
        bX = bX + velb_x/totalVel*cross
     
        #updating positions!
        changea = Vec(balla.pos.x + aX*math.cos(angle)-aY*math.sin(angle), 
        balla.pos.y + aY*math.cos(angle)+aX*math.sin(angle), 0)
        changeb = Vec(balla.pos.x + bX*math.cos(angle)-bY*math.sin(angle), 
        balla.pos.y + bY*math.cos(angle)+bX*math.sin(angle), 0)
        balla.pos = changea
        ballb.pos = changeb

        #updating velocities!
        changea = Vec(vela_x*math.cos(angle) - vela_y*math.sin(angle),
        vela_y*math.cos(angle) + vela_x*math.sin(angle), 0)
        changeb = Vec(velb_x*math.cos(angle) - velb_y*math.sin(angle),
        velb_y*math.cos(angle) + velb_x*math.sin(angle), 0)
        balla.vel = changea
        ballb.vel = changeb

#removes ball from list of balls when it reaches a hole
def socket(app, ball):
    if 140 <= ball.pos.y <= 170:
        if 90 <= ball.pos.x <= 120 or \
            485 <= ball.pos.x + app.radius*2 <= 515 or \
            485 <= ball.pos.x <= 515 or \
            880 <= ball.pos.x + app.radius*2 <= 910:
                app.balls.remove(ball)
                if app.MainScreen == True:
                    if ball.color == "black":
                        app.WinnerScreen = True
                        app.MainScreen = False
                        if app.playercount == False:
                            app.winner = app.player1
                        else:
                            app.winner = app.player2
                    else:
                        if ball.color == "white":
                            pass
                        elif ball.stripes == True:
                            app.stripe2.remove(ball)
                        else:
                            app.solid2.remove(ball)
                        if app.playercount == True and ball.stripes == True:
                            app.turn = True 
                        elif app.playercount == False and ball.stripes == False:
                            app.turn = True
                
    elif 430 <= ball.pos.y + app.radius*2 <= 460:
        if 90 <= ball.pos.x <= 120 or \
            485 <= ball.pos.x + app.radius*2 <= 515 or \
            485 <= ball.pos.x <= 515 or \
            880 <= ball.pos.x + app.radius*2 <= 910:
                app.balls.remove(ball)
                if app.MainScreen == True:
                    if ball.color == "black":
                        app.WinnerScreen = True
                        app.MainScreen = False
                        if app.playercount == False:
                            app.winner = app.player1
                        else:
                            app.winner = app.player2
                    else:

                        if ball.color == "white":
                            pass
                        elif ball.stripes == True:
                            app.stripe2.remove(ball)
                        else:
                            app.solid2.remove(ball)
                        if app.playercount == True and ball.stripes == False:
                            app.turn = False 
                        elif app.playercount == False and ball.stripes == True:
                            app.turn = False
                
#updates ball positions
def move(app, ball):
    #change position every time move is called based on ball velocity
    if app.stickx2 - app.stickx1 < 0:
        ball.pos.x += ball.vel.x
        ball.pos.y += ball.vel.y
    else:
        ball.pos.x += ball.vel.x
        ball.pos.y += ball.vel.y
    
    #friction!!
    
    ball.vel.x *= 0.9
    ball.vel.y *= 0.9
    if ball.vel.x < 0 and ball.vel.y < 0:
        ball.vel.x = 0
        ball.vel.y = 0

    #accounts for change in direction if ball hits the edge of the table
    if (ball.pos.x > 920 - app.radius*2 - app.margin):
        ball.pos.x = 920 - app.radius*2 - app.margin
        ball.vel.x = -ball.vel.x
    if (ball.pos.x < 80 + app.radius*2):
        ball.pos.x = 80 + app.radius*2
        ball.vel.x = -ball.vel.x
    if (ball.pos.y > 450 - app.radius*2):
        ball.pos.y = 450 - app.radius*2
        ball.vel.y = -ball.vel.y
    if (ball.pos.y < 150 + app.radius*2 - app.margin):
        ball.pos.y = 150 + app.radius*2 - app.margin
        ball.vel.y = -ball.vel.y

#draws pool table
def drawTable(app, canvas):
    #main table
    canvas.create_rectangle(100, 150, 900, 450, fill = "dark green",
    outline = 'dark green')
    #border
    canvas.create_rectangle(100, 130, 920, 150, fill = 'saddle brown',
    outline = 'saddle brown')
    canvas.create_rectangle(80, 130, 100, 470, fill = 'saddle brown', 
    outline = 'saddle brown')
    canvas.create_rectangle(100, 450, 920, 470, fill = 'saddle brown', 
    outline = 'saddle brown')
    canvas.create_rectangle(900, 150, 920, 450, fill = 'saddle brown', 
    outline = 'saddle brown')
    #sockets
    canvas.create_oval(90, 140, 120, 170, fill = 'black')
    canvas.create_oval(485, 140, 515, 170, fill = 'black')
    canvas.create_oval(880, 140, 910, 170, fill = 'black')
    canvas.create_oval(90, 430, 120, 460, fill = 'black')
    canvas.create_oval(485, 430, 515, 460, fill = 'black')
    canvas.create_oval(880, 430, 910, 460, fill = 'black')

#draws each ball
def drawBalls(app, canvas):
    for ball in app.balls:
        canvas.create_oval(ball.pos.x, ball.pos.y, ball.pos.x + app.radius * 2, 
        ball.pos.y + app.radius * 2, fill = ball.color)
        textColor = 'black'
        if ball.color == 'white' or ball.color == 'black':
            textColor = 'white'
        if ball.stripes == True:
            canvas.create_rectangle(ball.pos.x + 5, ball.pos.y + 3, 
            ball.pos.x + 15, ball.pos.y + 17, fill = 'white', outline = 'white')
            canvas.create_arc(ball.pos.x + 6, ball.pos.y+1, ball.pos.x + 14, 
            ball.pos.y + 5, fill = 'white', outline = 'white', extent = 180)
            canvas.create_arc(ball.pos.x + 6, ball.pos.y+17, ball.pos.x + 14, 
            ball.pos.y + 19 , fill = 'white', outline = 'white', extent = -180)
        canvas.create_text(ball.pos.x + app.radius, ball.pos.y + app.radius, 
        text = f'{ball.number}', fill = textColor, font = ('Arial','10','bold'))

#draws cue stick
def drawStick(app, canvas):
    if app.showStick == True:
        startX = -1 * app.radius - math.cos(app.angle) * 25 
        startY = -1 * app.radius - math.sin(app.angle) * 25
        endX = -1 * app.radius - math.cos(app.angle) * 120 
        endY = -1 * app.radius - math.sin(app.angle) * 120 
        
        canvas.create_line(app.ball2.pos.x + startX + app.radius * 2, 
        app.ball2.pos.y + startY + app.radius * 2, 
        app.ball2.pos.x + endX + app.radius * 2, 
        app.ball2.pos.y + endY + app.radius*2, width = 10, 
        fill = 'saddle brown')

#lets cue stick follow mouse
def mouseMoved(app, event):
    app.cueStickX = event.x
    app.cueStickY = event.y
    app.angle = math.atan2(app.ball2.pos.y - app.cueStickY, 
    app.ball2.pos.x - app.cueStickX)
    if app.angle < 0:
        app.angle = 2*math.pi + app.angle

#gets mouse click position
def mousePressed(app, event):
    app.stickx1 = event.x
    app.sticky1 = event.y

#gets mouse release position for drag function   
def mouseReleased(app, event):
    app.stickx2 = event.x
    app.sticky2 = event.y
    dividend = (app.stickx2 - app.stickx1)**2 + (app.sticky2 - app.sticky1)**2
    distance = math.sqrt(dividend)
    app.showStick = False
    app.startStick = 20
    app.endStick = 100

    #changes starting cueball velocity based on drag distance
    if app.sticky2 - app.sticky1 < 0:
        if distance <= 5:
            app.ball2.vel = Vec(0,0,0)
        elif distance <= 10:
            app.ball2.vel = Vec(5*math.cos(app.angle), 
            abs(5*math.sin(app.angle)), 0)
        elif distance <= 50:
            app.ball2.vel = Vec(10*math.cos(app.angle), 
            abs(10*math.sin(app.angle)), 0)
        elif distance <= 100:
            app.ball2.vel = Vec(50*math.cos(app.angle), 
            abs(50*math.sin(app.angle)), 0)
        else: 
            app.ball2.vel = Vec(140*math.cos(app.angle), 
            abs(140*math.sin(app.angle)), 0)
    elif app.stickx2 - app.stickx1 > 0:
        if distance <= 5:
            app.ball2.vel = Vec(0,0,0)
        elif distance <= 10:
            app.ball2.vel = Vec(5*math.cos(app.angle), 
            5*math.sin(app.angle), 0)
        elif distance <= 50:
            app.ball2.vel = Vec(10*math.cos(app.angle), 
            10*math.sin(app.angle), 0)
        elif distance <= 100:
            app.ball2.vel = Vec(50*math.cos(app.angle), 
            50*math.sin(app.angle), 0)
        else: 
            app.ball2.vel = Vec(140*math.cos(app.angle), 
            140*math.sin(app.angle), 0)
    else: 
        if distance <= 5:
            app.ball2.vel = Vec(0,0,0)
        elif distance <= 10:
            app.ball2.vel = Vec(5*math.cos(app.angle), 
            5*math.sin(app.angle), 0)
        elif distance <= 50:
            app.ball2.vel = Vec(10*math.cos(app.angle), 
            10*math.sin(app.angle), 0)
        elif distance <= 100:
            app.ball2.vel = Vec(50*math.cos(app.angle), 
            50*math.sin(app.angle), 0)
        else: 
            app.ball2.vel = Vec(140*math.cos(app.angle), 
            140*math.sin(app.angle), 0)
    app.player = -1
    
#key functions
def keyPressed(app, event):
    if (event.key == 'd'):
        app.DirectionScreen = True
        app.TitleScreen = False
    if (event.key == 'b'):
        app.DirectionScreen = False
        app.TitleScreen = True
    if (event.key == 'p'):
        app.TitleScreen = False
        app.DirectionScreen = False
        app.MainScreen = True
        app.player1 = app.getUserInput("Player 1 name: ")
        app.player2 = app.getUserInput("Player 2 name: ")
    if (event.key == 'c'):
        app.TitleScreen = False
        app.ChallengeScreen = True
        app.timer = True
        app.Challenge = True
    if (event.key == 'r'):
        app.TitleScreen = True
        app.ChallengeScreen = False
        app.MainScreen = False
        app.WinnerScreen = False
        app.totalTime = 300
        app.ball1 = Ball(780, 310, 0, 'red', 0, True, 15)
        app.ball2 = Ball(190 , 300 , 0, 'white', 0, False, 0) #white cue ball
        app.ball3 = Ball(800, 300, 0, 'green4', 0, False, 6)
        app.ball4 = Ball(800, 320, 0, 'maroon', 0, True, 16)
        app.ball5 = Ball(800, 260, 0, 'blue', 0, True, 10)
        app.ball6 = Ball(760, 300, 0, 'black', 0, False, 8)
        app.ball7 = Ball(740, 310, 0, 'dark orange', 0, True, 13)
        app.ball8 = Ball(740, 290, 0, 'dark orange', 0, False, 5)
        app.ball9 = Ball(720, 300, 0, 'yellow', 0, True, 9)
        app.ball10 = Ball(800, 280, 0, 'green4', 0, True, 14)  
        app.ball11 = Ball(800, 340, 0, 'purple', 0, True, 12)
        app.ball12 = Ball(780, 290, 0, 'purple', 0, False, 4)
        app.ball13 = Ball(780, 270, 0, 'blue', 0, False, 2)
        app.ball14 = Ball(780, 330, 0, 'yellow', 0, False, 1)
        app.ball15 = Ball(760, 280, 0, 'maroon', 0, False, 7)
        app.ball16 = Ball(760, 320, 0, 'red', 0, False, 3)
        app.balls = [app.ball1, app.ball2, app.ball3, app.ball4, app.ball5, 
        app.ball6, app.ball7, app.ball8, app.ball9, app.ball10,
        app.ball11, app.ball12, app.ball13, app.ball14, app.ball15, app.ball16] 
        app.stripe = [app.ball1, app.ball4, app.ball5, app.ball7, app.ball9, 
        app.ball10, app.ball11, app.ball6]
        app.stripe2 = [app.ball1, app.ball4, app.ball5, app.ball7, app.ball9, 
        app.ball10, app.ball11, app.ball6]
        app.solid = [app.ball3, app.ball16, app.ball8, app.ball12, app.ball13, 
        app.ball14, app.ball15, app.ball6]
        app.solid2 = [app.ball3, app.ball16, app.ball8, app.ball12, app.ball13, 
        app.ball14, app.ball15, app.ball6]

#calculates time
def timer(app):
    app.timerCount += 1
    if app.timerCount % 100 == 0:
        app.totalTime -= 1
    if app.totalTime == 0:
        app.WinnerScreen = True
        app.ChallengeScreen = False
        if len(app.balls) > 1:
            app.ChallengeWin = False
        elif len(app.balls) == 1:
            app.ChallengeWin = True

#loop for all functions
def timerFired(app): 
    if app.timer == True:
        timer(app)
    for ball in app.balls:
        move(app, ball)
        socket(app, ball)

    for i in range(len(app.balls)-1):
        for j in range(i+1,len(app.balls)):
            collision(app, app.balls[i], app.balls[j])
    app.count = 0
    for ball in app.balls:
        if ball.vel.x < 1 and ball.vel.y < 1:
            app.count += 1
                
    if app.count == len(app.balls):
        app.player += 1
        app.showStick = True
        if app.player == 0:
            if app.length == len(app.balls):
                if app.turn == True:
                    app.playcount+=1
                    
                else:
                    
                    remainder = 5 - app.playcount % 5
                    app.playcount += remainder
                    app.turn = True
                         
            app.length = len(app.balls)
            if app.playcount % 5 == 0:
                if app.playercount == True:
                    app.playercount = False
                else:
                    app.playercount = True
    if app.MainScreen == True:
        #checks for stripe balls out of remaining balls
        app.count = 0
        for balls in app.stripe:
            if balls not in app.balls:
                app.count += 1
        if app.count == 8:
            app.winner = 'stripes'
            app.WinnerScreen = True
            app.MainScreen = False
        #checks for solid balls out of remaining balls
        app.count = 0
        for balls in app.solid:
            if balls not in app.balls:
                app.count += 1
        if app.count == 8:
            app.winner = 'solids'
            app.WinnerScreen = True
            app.MainScreen = False
    elif app.ChallengeScreen == True:
        if len(app.balls) == 1:
            app.ChallengeScreen = False
            app.WinnerScreen = True

    if app.ball2 not in app.balls:
        app.balls.append(app.ball2)
        app.ball2.pos.x = 190
        app.ball2.pos.y = 300
        app.ball2.vel.x = 0
        app.ball2.vel.y = 0
        if app.playercount == True:
            app.playercount = False
        else:
            app.playercount = True
        app.playcount += 1
       
#draws main game screen
def drawMainScreen(app, canvas):
    if app.MainScreen == True:
        drawTable(app, canvas)
        drawBalls(app, canvas)
        drawStick(app, canvas)
        
        if app.playercount == True:
            canvas.create_text(app.width/2, app.height*(1/6), 
            text = f"{app.player1}'s turn: striped", font = ("Arial", '28'))
        else:
            canvas.create_text(app.width/2, app.height*(1/6), 
            text = f"{app.player2}'s turn: solid", font = ("Arial", '28'))
        canvas.create_text(100, 100, 
        text = f"{app.player1}'s balls left: {len(app.stripe2)}")
        canvas.create_text(900, 100, 
        text = f"{app.player2}'s balls left: {len(app.solid2)}")

#draws challenge game screen
def drawChallengeScreen(app, canvas):
    if app.ChallengeScreen == True:
        drawTable(app, canvas)
        drawBalls(app, canvas)
        drawStick(app, canvas)
        minutes = app.totalTime // 60
        seconds = app.totalTime % 60
        if seconds == 0:
            canvas.create_text(app.width/2, app.height*(1/6) - 30, 
            text = f"0{minutes}:00", font = ("Arial", '28', 'bold'))
        elif seconds < 10:
            canvas.create_text(app.width/2, app.height*(1/6) - 30, 
            text = f"0{minutes}:0{seconds}", font = ("Arial", '28', 'bold'))
        elif minutes == 0: 
            canvas.create_text(app.width/2, app.height*(1/6) - 30, 
            text = f"00:{seconds}", font = ("Arial", '28', 'bold'))
        else: 
            canvas.create_text(app.width/2, app.height*(1/6) - 30, 
            text = f"0{minutes}:{seconds}", font = ("Arial", '28', 'bold'))
        canvas.create_text(app.width/2, app.height*(1/6), 
        text = f'Balls remaining: {len(app.balls) - 1}', font = ("Arial", '20'))
    
#draws title screen             
def drawTitleScreen(app, canvas):
    if app.TitleScreen == True:
        canvas.create_image(app.width/2, app.height/2, 
        image = ImageTk.PhotoImage(app.image2))
        canvas.create_text(app.width/2, app.height*(1/5), text = "8-ball Pool", 
        font = ('Arial','50','bold'), fill = 'white')
        canvas.create_rectangle(app.width/2 - 220, app.height*(1/3.4) - 20, 
        app.width/2 + 220, app.height*(1/3.4) + 20, fill = 'black')
        canvas.create_text(app.width/2, app.height*(1/3.4), 
        text = "press d for directions", font = ("Arial", '28', 'bold'),
        fill = 'white')
        canvas.create_rectangle(app.width/2 - 220, app.height*(1/2.6) - 20, 
        app.width/2 + 220, app.height*(1/2.6) + 20, fill = 'black')
        canvas.create_text(app.width/2, app.height*(1/2.6),
        text = 'press p to play 2 player game', font = ("Arial", '28', 'bold'), 
        fill = 'white')
        canvas.create_rectangle(app.width/2 - 220, app.height*(1/2.1) - 20, 
        app.width/2 + 220, app.height*(1/2.1) + 20, fill = 'black')
        canvas.create_text(app.width/2, app.height*(1/2.1),
        text = 'press c to play challenge mode', 
        font = ("Arial", '28', 'bold'), fill = 'white')

#draws directions page
def drawDirection(app, canvas):
    if app.DirectionScreen == True:
        canvas.create_rectangle(0,0,app.width, app.height, fill = 'dark green')
        
        #directions for 2 player game
        canvas.create_text(app.width/2,app.height*(1/6)-3,text = '2 player'+\
            ' directions:', 
            font = ('Arial','24','bold'))
        canvas.create_text(app.width/2,app.height*(1/6)+25,text='--> Player 1'+\
            ' Goal: to get all striped balls into the sockets.', 
            font = ('Arial','18','bold'))
        canvas.create_text(app.width/2, app.height*(1/6) + 50 , 
        text = '--> Player 2 Goal: to get all solid balls into the sockets.', 
        font = ('Arial','18','bold'))
        canvas.create_text(app.width/2,app.height*(1/6)+75,text="--> After"+\
        " getting all assigned balls in the sockets,"+ \
        " the player must also get the 8 ball into one of the 6 sockets.", 
        font = ('Arial','18','bold'))
        canvas.create_text(app.width/2,app.height*(1/6)+100,text="--> In" + \
        " order to shoot a the cue ball, drag the mouse away from the ball" , 
        font = ('Arial','18','bold'))
        canvas.create_text(app.width/2, app.height*(1/6) + 125, text = \
         "in the opposite direction of where you want the ball to go in.", 
         font = ('Arial','18','bold'))
        canvas.create_text(app.width/2, app.height*(1/6) + 150, 
        text = "--> Release mouse when ready to shoot.", 
        font = ('Arial','18','bold'))
        canvas.create_text(app.width/2, app.height*(1/6) + 175, 
        text = "--> Each player gets 5 shots per turn.", 
        font = ('Arial','18','bold'))
        canvas.create_text(app.width/2, app.height*(1/6) + 200, 
        text = "--> Press p to play 2 player game!", 
        font = ('Arial','18','bold'))

        #directions for 1 player game
        canvas.create_text(app.width/2, app.height*(1/6) + 247, 
        text = 'Single player directions: ', font = ('Arial','24','bold'))
        canvas.create_text(app.width/2, app.height*(1/6) + 275,
        text = "Goal: get all the balls, excluding the cueball, into one of"+\
            " the 6 sockets.", font = ('Arial','18','bold'))
        canvas.create_text(app.width/2, app.height*(1/6) + 300,
        text = "Follow the same directions above to shoot the cueball.", 
        font = ('Arial','18','bold'))
        canvas.create_text(app.width/2, app.height*(1/6) + 325, 
        text = "Beware! You have a 5 minute time limit...", 
        font = ('Arial','18','bold'))
        canvas.create_text(app.width/2, app.height*(1/6) + 350,
        text = "Press c to play single player game!", 
        font = ('Arial','18','bold'))
        
        #back function
        canvas.create_text(app.width/2, app.height*(1/6) + 400,
        text = "Press b to go back.", 
        font = ('Arial','18','bold'))
        
#draws game winner screen
def drawWinnerScreen(app, canvas):
    if app.WinnerScreen == True:
        canvas.create_rectangle(0,0,app.width, app.height, fill = 'grey')
        if app.Challenge == True:
            if app.ChallengeWin == True:
                canvas.create_text(app.width/2, app.height/2, 
                text = 'You win!', font = ('Arial','40','bold'))
            else:
                canvas.create_text(app.width/2, app.height/2, 
                text = 'You lose!', font = ('Arial','40','bold'))
        else:
            canvas.create_text(app.width/2, app.height/2, 
            text = f'{app.winner} wins!', font = ('Arial','40','bold'))

#draws everything!
def redrawAll(app, canvas):
    drawTitleScreen(app, canvas)
    drawMainScreen(app, canvas)
    drawWinnerScreen(app, canvas)
    drawDirection(app, canvas)
    drawChallengeScreen(app, canvas)
 
def run8ball():
    runApp(width=1000, height=600)

run8ball()
    

    
