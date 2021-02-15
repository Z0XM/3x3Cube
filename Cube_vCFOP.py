import pygame

from Assets.Colors import *
from Assets.Z import *

def SetCube_buttons(X=300, Y=70):
    for piece in range(9):
        Cube_buttons[5][piece].change(x=X+(piece%3)*65, y=Y+(piece//3)*65)
    Y+=210
    for piece in range(9):
        Cube_buttons[1][piece].change(x=X+(piece%3)*65, y=Y+(piece//3)*65)
    Y+=210
    for piece in range(9):
        Cube_buttons[0][piece].change(x=X+(piece%3)*65, y=Y+(piece//3)*65)
    X-=210
    Y-=210
    for piece in range(9):
        Cube_buttons[2][piece].change(x=X+(piece%3)*65, y=Y+(piece//3)*65)
    X+=2*210
    for piece in range(9):
        Cube_buttons[4][piece].change(x=X+(piece%3)*65, y=Y+(piece//3)*65)
    X+=210
    for piece in range(9):
        Cube_buttons[3][piece].change(x=X+(piece%3)*65, y=Y+(piece//3)*65)

def DisplayCube_buttons():
    for side in range(6):
        for piece in range(9):
            Cube_buttons[side][piece].create(screen)

def ConvertCubeToData():
    code={White:'w', Blue:'b', Green:'g', Orange:'o', Red:'r', Yellow:'y'}
    
    for side in range(6):
        Cube[side][0]=code[Cube_buttons[side][0].bg_color]
        Cube[side][1]=code[Cube_buttons[side][1].bg_color]
        Cube[side][2]=code[Cube_buttons[side][2].bg_color]
        Cube[side][3]=code[Cube_buttons[side][5].bg_color]
        Cube[side][4]=code[Cube_buttons[side][8].bg_color]
        Cube[side][5]=code[Cube_buttons[side][7].bg_color]
        Cube[side][6]=code[Cube_buttons[side][6].bg_color]
        Cube[side][7]=code[Cube_buttons[side][3].bg_color]
        Centre[side]=code[Cube_buttons[side][4].bg_color]

def ConvertDataToCube():
    code={'w':White, 'b':Blue, 'g':Green, 'o':Orange, 'r':Red, 'y':Yellow}

    for side in range(6):
        Cube_buttons[side][0].bg_color=code[Cube[side][0]]
        Cube_buttons[side][1].bg_color=code[Cube[side][1]]
        Cube_buttons[side][2].bg_color=code[Cube[side][2]]
        Cube_buttons[side][3].bg_color=code[Cube[side][7]]
        Cube_buttons[side][5].bg_color=code[Cube[side][3]]
        Cube_buttons[side][6].bg_color=code[Cube[side][6]]
        Cube_buttons[side][7].bg_color=code[Cube[side][5]]
        Cube_buttons[side][8].bg_color=code[Cube[side][4]]
        Cube_buttons[side][4].bg_color=code[Centre[side]]

    
def FillSolve(move, n):
    global moves
    if moves==-1:
        moves+=2
        solve.append(move)
        solve_degree.append(n)
    elif solve[moves]==move:
        if (solve_degree[moves]-n)%2==0 and (solve_degree[moves]!=n or n==2):moves-=1
        else:
            n=2 if solve_degree[moves]==n else (n+solve_degree[moves])%4
            solve_degree[moves]=n
    else:
        moves+=1
        if moves<len(solve):
            solve[moves], solve_degree[moves]=move, n
        else:
            solve.append(move)
            solve_degree.append(n)
    
def RotateSide(side, n):
    N=n*2
    Cube[side]=Cube[side][-N:]+Cube[side][:-N]

def u(n):
    RotateSide(5, n)
    for i in range(n):
        temp=[Cube[2][0], Cube[2][1], Cube[2][2]]
        Cube[2][0], Cube[2][1], Cube[2][2]=Cube[1][0], Cube[1][1], Cube[1][2]
        Cube[1][0], Cube[1][1], Cube[1][2]=Cube[4][0], Cube[4][1], Cube[4][2]
        Cube[4][0], Cube[4][1], Cube[4][2]=Cube[3][0], Cube[3][1], Cube[3][2]
        Cube[3][0], Cube[3][1], Cube[3][2]=temp[0], temp[1], temp[2]
    FillSolve('U', n)

def d(n):
    RotateSide(0, n)
    for i in range(n):
        temp=[Cube[1][6], Cube[1][5], Cube[1][4]]
        Cube[1][6], Cube[1][5], Cube[1][4]=Cube[2][6], Cube[2][5], Cube[2][4]
        Cube[2][6], Cube[2][5], Cube[2][4]=Cube[3][6], Cube[3][5], Cube[3][4]
        Cube[3][6], Cube[3][5], Cube[3][4]=Cube[4][6], Cube[4][5], Cube[4][4]
        Cube[4][6], Cube[4][5], Cube[4][4]=temp[0], temp[1], temp[2]
    FillSolve('D', n)

def r(n):
    RotateSide(4, n)
    for i in range(n):
        temp=[Cube[1][4], Cube[1][3], Cube[1][2]]
        Cube[1][4], Cube[1][3], Cube[1][2]=Cube[0][4], Cube[0][3], Cube[0][2]
        Cube[0][4], Cube[0][3], Cube[0][2]=Cube[3][0], Cube[3][7], Cube[3][6]
        Cube[3][0], Cube[3][7], Cube[3][6]=Cube[5][4], Cube[5][3], Cube[5][2]
        Cube[5][4], Cube[5][3], Cube[5][2]=temp[0], temp[1], temp[2]
    FillSolve(move_r[facing], n)

def l(n):
    RotateSide(2, n)
    for i in range(n):
        temp=[Cube[1][0], Cube[1][7], Cube[1][6]]
        Cube[1][0], Cube[1][7], Cube[1][6]=Cube[5][0], Cube[5][7], Cube[5][6]
        Cube[5][0], Cube[5][7], Cube[5][6]=Cube[3][4], Cube[3][3], Cube[3][2]
        Cube[3][4], Cube[3][3], Cube[3][2]=Cube[0][0], Cube[0][7], Cube[0][6]
        Cube[0][0], Cube[0][7], Cube[0][6]=temp[0], temp[1], temp[2]
    FillSolve(move_l[facing], n)

def f(n):
    RotateSide(1, n)
    for i in range(n):
        temp=[Cube[2][4], Cube[2][3], Cube[2][2]]
        Cube[2][4], Cube[2][3], Cube[2][2]=Cube[0][2], Cube[0][1], Cube[0][0]
        Cube[0][2], Cube[0][1], Cube[0][0]=Cube[4][0], Cube[4][7], Cube[4][6]
        Cube[4][0], Cube[4][7], Cube[4][6]=Cube[5][6], Cube[5][5], Cube[5][4]
        Cube[5][6], Cube[5][5], Cube[5][4]=temp[0], temp[1], temp[2]
    FillSolve(move_f[facing], n)

def b(n):
    RotateSide(3, n)
    for i in range(n):
        temp=[Cube[2][0], Cube[2][7], Cube[2][6]]
        Cube[2][0], Cube[2][7], Cube[2][6]=Cube[5][2], Cube[5][1], Cube[5][0]
        Cube[5][2], Cube[5][1], Cube[5][0]=Cube[4][4], Cube[4][3], Cube[4][2]
        Cube[4][4], Cube[4][3], Cube[4][2]=Cube[0][6], Cube[0][5], Cube[0][4]
        Cube[0][6], Cube[0][5], Cube[0][4]=temp[0], temp[1], temp[2]
    FillSolve(move_b[facing], n)

def Perform():
    def cross():
        #Sending Up
        while len(set([Cube[5][1], Cube[5][3], Cube[5][5], Cube[5][7], Centre[0]]))!=1:
            for side in range(6):
                for piece in [1, 3, 5, 7]:
                    if Cube[side][piece]==Centre[0]:
                        if piece==1 and (side not in[0, 5]):
                            if side==1: f(3); l(3)
                            elif side==3: b(1); l(1)
                            elif side==2: l(1); f(1)
                            elif side==4: r(3); f(3)
                        if piece==5 and (side not in [0, 5]):
                            if side==1: f(1); l(3)
                            elif side==3: b(3); l(1)
                            elif side==2: l(3); f(1)
                            elif side==4: r(1); f(3)
                        if (side==0 and piece==1) or (side==4 and piece==7) or (side==2 and piece==3):
                            while Cube[5][5]==Centre[0]: u(1)
                            if side==0: f(2)
                            elif side==4: f(3)
                            elif side ==2: f(1)
                        if (side==0 and piece==3) or (side==1 and piece==3) or (side==3 and piece==7):
                            while Cube[5][3]==Centre[0]: u(1)
                            if side==0: r(2)
                            elif side==1: r(1)
                            elif side==3: r(3)
                        if (side==0 and piece==5) or (side==4 and piece==3) or (side==2 and piece==7):
                            while Cube[5][1]==Centre[0]: u(1)
                            if side==0: b(2)
                            elif side==4: b(1)
                            elif side==2: b(3)
                        if (side==1 and piece==7) or (side==3 and piece==3) or (side==1 and piece==7):
                            while Cube[5][7]==Centre[0]: u(1)
                            if side==0: l(2)
                            elif side==3: l(1)
                            elif side==1: l(3)

        #Bringing Down                            
        while len(set([Cube[0][1], Cube[0][3], Cube[0][5], Cube[0][7], Centre[0]]))!=1:
            done=False
            if Cube[1][1]==Centre[1] and Cube[5][5]==Centre[0]:f(2); done=True
            if Cube[2][1]==Centre[2] and Cube[5][7]==Centre[0]: l(2); done=True
            if Cube[3][1]==Centre[3] and Cube[5][1]==Centre[0]: b(2); done=True
            if Cube[4][1]==Centre[4] and Cube[5][3]==Centre[0]: r(2); done=True            
            if not done: u(1)

    def f2l():
        global facing
        def edge_position():
            end=False
            for edge in range(8):
                if edge==0: u(1); r(3)
                elif edge==1: r(3)
                elif edge==2: u(3); r(3)
                elif edge==3: u(2); r(3)
                elif edge==4: b(2); r(2)
                elif edge==5: r(2)
                elif edge==7: f(2)

                if (Cube[1][3]==Centre[1] and Cube[4][7]==Centre[4]) or (Cube[1][3]==Centre[4] and Cube[4][7]==Centre[1]):
                    end=True

                if edge==0: r(1); u(3)
                elif edge==1: r(1)
                elif edge==2: r(1); u(1)
                elif edge==3: r(1); u(2)
                elif edge==4: r(2); b(2)
                elif edge==5: r(2)
                elif edge==7: f(2)

                if end: break
            return edge

        def corner_position():
            end=False
            for corner in range(8):
                if corner==0: u(2); r(3)
                elif corner==1: r(2)
                elif corner==2: r(3)
                elif corner==3: u(3); r(3)
                elif corner==4: d(2)
                elif corner==5: d(3)
                elif corner==7: d(1)

                if (Cube[0][2]==Centre[0] and Cube[1][4]==Centre[1]) or (Cube[0][2]==Centre[4] and Cube[1][4]==Centre[0]) or (Cube[0][2]==Centre[1] and Cube[1][4]==Centre[4]):
                    end=True

                if corner==0: r(1); u(2)
                elif corner==1: r(2)
                elif corner==2: r(1)
                elif corner==3: r(1); u(1)
                elif corner==4: d(2)
                elif corner==5: d(1)
                elif corner==7: d(3)

                if end: break
            return corner
        for turn in range(4):
            if Cube[0][2]!=Centre[0] or Cube[1][4]!=Centre[1] or Cube[1][3]!=Centre[1] or Cube[4][7]!=Centre[4]:
                count=0
                corner=corner_position()
                if corner in range(4, 8):
                    while corner!=6:
                        count+=1
                        d(1); corner=corner_position()
                    f(3); u(3); f(1)
                    while count!=0:
                        count-=1
                        d(3)
                else:
                    while corner!=1:
                        u(3)
                        corner=corner_position()
                edge=edge_position()
                done=False
                if edge==0 and Cube[5][1]==Cube[5][2] and Cube[3][0]==Cube[3][1]:
                    u(2); r(1); u(3); r(3)
                elif edge==1 and Cube[5][2]==Cube[5][3] and Cube[4][1]==Cube[4][2]:
                    f(3); u(1); f(1)
                
                if not done:
                    if edge==0: r(1); u(3); r(3)
                    elif edge==1: u(1); r(1); u(2); r(3)
                    elif edge==4: l(1); u(1); l(3)
                    elif edge==5: u(1); r(3); u(3); r(1)
                    elif edge==6: f(3); u(3); f(1)
                    elif edge==7: f(1); u(3); f(3)

                    while corner!=2:
                        u(1)
                        corner=corner_position()

                    edge=edge_position()
                    if edge==0: u(1); f(3); u(3); f(1); u(3)
                    
                    if Cube[1][2]==Centre[0]:
                        if Cube[5][7]==Centre[4]: f(3); u(3); f(1)
                        else: u(3); r(1); u(2); r(3); u(2); r(1); u(3); r(3)
                    elif Cube[1][2]==Centre[4]:
                        if Cube[5][7]==Centre[4]: u(3); f(3); u(2); f(1); u(3); f(3); u(1); f(1)
                        else: u(2); r(1); u(1); r(3); u(1); r(1); u(3); r(3)
                    elif Cube[1][2]==Centre[1]:
                        if Cube[5][7]==Centre[4]: u(1); f(3); u(3); f(1); u(2); f(3); u(1); f(1)
                        else: u(1); f(3); u(1); f(1); u(3); r(1); u(1); r(3)

            temp=Cube[4]
            Cube[4], Cube[3], Cube[2], Cube[1]=Cube[3], Cube[2], Cube[1], temp
            RotateSide(5, 1)#clockwise
            RotateSide(0, 3)#anticlockwise
            temp=Centre[4]
            Centre[4], Centre[3], Centre[2], Centre[1]=Centre[3], Centre[2], Centre[1], temp
            facing-=1
            if facing==0: facing=4
                
    def upcross():
        if len(set([Cube[5][3], Cube[5][1], Cube[5][7], Centre[5]]))==4:
            f(1); u(1); r(1); u(3); r(3); f(3); u(1); f(1); r(1); u(1); r(3); u(3); f(3)
        elif Cube[5][1]==Cube[5][5]:
            u(1); f(1); r(1); u(1); r(3); u(3); f(3)
        elif Cube[5][3]==Cube[5][7]:
            f(1); r(1); u(1); r(3); u(3); f(3);
        elif Cube[5][3]==Cube[5][5]:
            u(2); f(1); u(1); r(1); u(3); r(3); f(3)
        elif Cube[5][1]==Cube[5][7]:
            f(1); u(1); r(1); u(3); r(3); f(3)
        elif Cube[5][1]==Cube[5][3]:
            u(3); f(1); u(1); r(1); u(3); r(3); f(3)
        elif Cube[5][5]==Cube[5][7]:
            u(1); f(1); u(1); r(1); u(3); r(3); f(3)

    def oll():
        corners_to_orient=4-[Cube[5][0], Cube[5][2], Cube[5][4], Cube[5][6]].count(Centre[5])

        if corners_to_orient==3:
            while Cube[5][6]!=Centre[5]: u(1)
            if Cube[2][0]==Centre[5]:
                u(3); l(3); u(3); l(1); u(3); l(3); u(2); l(1)
            elif Cube[1][2]==Centre[5]:
                r(1); u(1); r(3); u(1); r(1); u(2); r(3)

        if corners_to_orient==4:
            while Cube[1][0]!=Centre[5] or Cube[1][2]!=Centre[5]: u(1)
            if len(set([Cube[3][0], Cube[3][2], Centre[5]]))==1:
                r(1); u(2); r(3); u(3); r(1); u(1); r(3); u(3); r(1); u(3); r(3)
            else:
                u(1); r(1); u(2); r(2); u(3); r(2); u(3); r(2); u(2); r(1)

        if corners_to_orient==2:
            if (Cube[5][0]==Centre[5] and Cube[5][4]==Centre[5]) or (Cube[5][2]==Centre[5] and Cube[5][6]==Centre[5]):
                while Cube[1][0]!=Centre[5]: u(1)
                r(3); f(1); r(1); b(3); r(3); f(3); r(1); b(1)
            else:
                while Cube[5][4]==Centre[5] or Cube[5][6]==Centre[5]: u(1)
                if Cube[2][2]==Centre[5]:
                    r(1); b(1); r(3); f(1); r(1); b(3); r(3); f(3)
                if Cube[1][0]==Centre[5]:
                    r(2); d(1); r(3); u(2); r(1); d(3); r(3); u(2); r(3)

    def corner_pll():
        count=0
        while Cube[3][0]!=Cube[3][2]:
            u(1); count+=1
            if count==4:break
        if count==4: r(3); f(1); r(3); b(2); r(1); f(3); r(3); b(2); r(2); u(1)
        r(3); f(1); r(3); b(2); r(1); f(3); r(3); b(2); r(2);
        
    def edge_pll():
        count=0
        done=False
        while Cube[3][0]!=Cube[3][1]:
            u(1); count+=1
            if count==4: break
        if count==4:
            if Cube[1][1]==Centre[3] and Cube[3][1]==Centre[1]:
                done=True
                r(2); l(2); d(3); r(2); l(2); u(2); r(2); l(2); d(3); r(2); l(2)
            else:
                r(1); u(3); r(1); u(1); r(1); u(1); r(1); u(3); r(3); u(3); r(2)
                while Cube[3][0]!=Cube[3][1]: u(1)
            
        elif Cube[1][1]==Cube[4][0] and not done:
            r(1); u(3); r(1); u(1); r(1); u(1); r(1); u(3); r(3); u(3); r(2)
        elif Cube[1][1]==Cube[2][0] and not done:
            r(2); u(1); r(1); u(1); r(3); u(3); r(3); u(3); r(3); u(1); r(3)
            
                
    if len(set([Cube[0][1], Cube[0][3], Cube[0][5], Cube[0][7], Centre[0]]))!=1:
        cross()

    f2l()
    
    if len(set([Cube[5][1], Cube[5][3], Cube[5][7], Cube[5][5], Centre[5]]))!=1:
        upcross()


    oll()

    if Cube[1][0]!=Cube[1][2] or Cube[3][0]!=Cube[3][2]:
        corner_pll()

    if Cube[1][0]!=Cube[1][1] or Cube[3][0]!=Cube[3][1]:
        edge_pll()
        
    while Cube[1][0]!=Centre[1]: u(1)
    
def Try():
    r(1); u(1); r(3); u(3)
    FillSolve('X', 0)
    
def Start():
    coloring=True
    SetCube_buttons()
    current_color='white'
    solving=False
    running=False
    while coloring:
        screen.fill(Black)
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                coloring=False
        for color in color_buttons:
            if color_buttons[color].hit():
                if e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
                        current_color=color
                color_buttons[color].change(bg_color=Dark(color_dict[color], 100))
            else:color_buttons[color].restore()
            color_buttons[color].create(screen)
        for side in range(6):
            for piece in range(9):
                if Cube_buttons[side][piece].hit():
                    if e.type==pygame.MOUSEBUTTONDOWN:
                        if e.button==1:
                            Cube_buttons[side][piece].change(bg_color=color_dict[current_color])
                        elif e.button==3:
                            for p in range(9):
                                if piece==4:
                                    Cube_buttons[side][p].change(bg_color=color_dict[current_color])
                                elif Cube_buttons[side][p].bg_color==Grey:
                                    Cube_buttons[side][p].change(bg_color=color_dict[current_color])             
                    elif e.type==pygame.KEYDOWN:
                        color=None
                        if e.key==pygame.K_o:color='orange'
                        if e.key==pygame.K_r:color='red'
                        if e.key==pygame.K_b:color='blue'
                        if e.key==pygame.K_g:color='green'
                        if e.key==pygame.K_w:color='white'
                        if e.key==pygame.K_y:color='yellow'
                        if color:Cube_buttons[side][piece].change(bg_color=color_dict[color])
        if solve_button.hit():
            if e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
                coloring=False
                solving=True
                ConvertCubeToData()
            solve_button.change(bg_color=Dark(Magenta, 100), text_color=Dark(White, 100))
        else:solve_button.restore()
        DisplayCube_buttons()
        solve_button.create(screen)
        pygame.display.update()

    if solving and not coloring:
        #Try()
        Perform()
        ConvertDataToCube()
        running=True
        expand=False
        solve_color={'r':Red, 'b':Blue, 'g':Green, 'o':Orange, 'y':Yellow, 'w':White}
        solve_code={'X':Grey, 'R':solve_color[Centre[4]], 'F':solve_color[Centre[1]], 'L':solve_color[Centre[2]], 'B':solve_color[Centre[3]], 'U':solve_color[Centre[5]], 'D':solve_color[Centre[0]]}

    while running:
        screen.fill(Black)
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                running=False
        #SetCube_buttons(X=235, Y=10)
        #DisplayCube_buttons()
        X, Y=30, 100
        for pos in range(1, 1+moves):
            screen.blit(solve_font.render(solve[pos]+str(solve_degree[pos]), 1, solve_code[solve[pos]]), (X, Y))
            X+=35
            if X>screenWidth-100:
                Y+=50
                X=30
        expand_button.create(screen)
        if expand_button.hit() and e.type==pygame.MOUSEBUTTONDOWN and e.button==1: expand=True
        if expand:
            screen.blit(solve_font.render('R : Rotate Right Side Clockwise', 1, solve_color[Centre[4]]), (30, 350))
            screen.blit(solve_font.render('L : Rotate Left Side Clockwise', 1, solve_color[Centre[2]]), (30, 400))
            screen.blit(solve_font.render('F : Rotate Front Side Clockwise', 1, solve_color[Centre[1]]), (30, 450))
            screen.blit(solve_font.render('B : Rotate Back Side Clockwise', 1, solve_color[Centre[3]]), (30, 500))
            screen.blit(solve_font.render('U : Rotate Up Side Clockwise', 1, solve_color[Centre[5]]), (30, 550))
            screen.blit(solve_font.render('D : Rotate Down Side Clockwise', 1, solve_color[Centre[0]]), (30, 600))
            screen.blit(solve_font.render('1: once, 2: twice, 3: thrice/anticlokwise once', 1, Grey), (30, 650))
        screen.blit(solve_font.render(f'MOVES: {moves}', 1, Gold), (50, 50))
        pygame.display.update()
            
pygame.init()
screenWidth=1000
screenHeight=700
screen=pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_icon(pygame.image.load('Assets/Z.ico'))
pygame.display.set_caption('Cube Solver')

color_buttons={'red':RoundButtons(Red, 235, 35, 25, 0), 
'orange':RoundButtons(Orange, 295, 35, 25, 0), 
'blue':RoundButtons(Blue, 355, 35, 25, 0), 
'green':RoundButtons(Green, 415, 35, 25, 0), 
'white':RoundButtons(White, 475, 35, 25, 0), 
'yellow':RoundButtons(Yellow, 535, 35, 25, 0)}
solve_font=pygame.font.SysFont('Comic Sans MS', 20)
solve_button=OvalButtons(Magenta, 600, 10, 100, 30, border=2, text='  SOLVE !', textX=600, textY=10, text_color=White, font=solve_font)

Cube_buttons=[[SqButtons(Grey, 1, 1, 60, 0) for sides in range(9)]for pieces in range(6)]
solve=['X']
solve_degree=[0]
moves=-1
Cube=[ [None for _ in range(8)] for _ in range(6)]
Centre=[None for _ in range(6)]

facing=1
move_r={1:'R', 2:'F', 3:'L', 4:'B'}
move_l={1:'L', 2:'B', 3:'R', 4:'F'}
move_f={1:'F', 2:'L', 3:'B', 4:'R'}
move_b={1:'B', 2:'R', 3:'F', 4:'L'}

expand_button=SqButtons(Grey, 500, 10, 50)
        
Start()
pygame.quit()
