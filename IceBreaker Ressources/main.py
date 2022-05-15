from Graphics50 import *
#==============================================================================#
#Program purpose: Creation of a playable IceBreaker game using the Graphics50
#module
#==============================================================================#
#NAME: Moses Lemma
#==============================================================================#

#CONSTANTS

#Names of player Icons
FNAME1,FNAME2 = "Player_Popeye.gif", "Dot_Blue.gif"
img1 = Image(Point(0,0),FNAME1)
img2 = Image(Point(100,100),FNAME2)

#Number of rows and coloumns the board contains 
ROWS,COLS = 8,10

#SQUARE BOTTAM AND GAP SIZE(S)
SQ_SZ,BOTTOM,GAP = max( img1.getWidth(),img1.getHeight() ),100,5

#WINDOW DIMENSIONS
WIN_W = (SQ_SZ+GAP) * COLS + GAP
WIN_H = (SQ_SZ+GAP) * ROWS + GAP + BOTTOM

#WINDOW TITLE
win_title = "IceBreaker "+str(WIN_W)+"x"+str(WIN_H)

#Button width and height
BTN_W, BTN_H = 60,30

#Msg = Text(Point(100,100),"CLICK")

#Colors for unbroken (white) and broken (cyan) tiles
SOLID, BROKEN = color_rgb(255,255,255), color_rgb(0,255,255)

#PLAYERS
player = 0
players = [ [ ROWS//2, 0,      img1, "Popeye" ], 
            [ ROWS//2, COLS-1, img2, "Blue"   ] ]

#board: 2-dim list of lists: board[r][c] of 2-valued objects created in setup
board = []                          #set up in board_setup()

#VISUAL 
#==============================================================================#
#CREATES GAME WINDOW 
#win = GraphWin(win_title,WIN_W,WIN_H)


#DISPLAYS TURN
player_info = Text(Point(WIN_W//4,WIN_H-75),(f"{players[player][3]} can MOVE")) 
player_info.setSize(14)

#SHOWS CLICK COORDINATE
click_info = Text(Point(WIN_W//4+50,WIN_H-40),(""))
click_info.setSize(14)
#==============================================================================#

# |FUNCTION THAT CREATES AND RETURNS A RECTANGLE OBJECT AND TEXT OBJECT|
def btn_create(x, y, w, h, txt):
    rect = Rectangle(Point(x,y),Point(x+w,y+h))
    text = Text(Point(x+30,y+15),txt)
    return (rect,  text)


# |FUNCTION THAT SETS THE GAME BOARD BY CREATING THE ROWS AND COLOUMNS OF INDI-|
# |VIDUAL SQUARES                                                              |
def board_setup():
    #Recall: board is an empty list
    global win,board
    #r, c: row and col for any given square
    
    #BOARD CREATION 
    for r in range(ROWS):
        board.append([])                      # for each row of rectangles
        for c in range(COLS):
            xL = GAP + c * (GAP+SQ_SZ)
            yU = GAP + r * (GAP+SQ_SZ)   
            board[r].append(Rectangle(Point(xL,        yU      ),
                                      Point(xL+ SQ_SZ, yU+SQ_SZ)))
            board[r][c].draw(win)
            board[r][c].setFill(SOLID)
            
     
    # |PLAYER STARTING POSITIONS WITH: |
    # |players[0][2] = player popeye   |
    # |players[1][2] = player blue     |
    
    
    players[0][2].move( players[0][1]*(GAP+SQ_SZ)+GAP+SQ_SZ//2,
                        players[0][0]*(GAP+SQ_SZ) + GAP + SQ_SZ // 2)
    
    # |PLAYER POPEYE IMAGE IS DRAWN TO WINDOW|
    players[0][2].draw(win)
    
    players[1][2].move( players[1][1]+(GAP+SQ_SZ)+GAP*7+SQ_SZ*6,
                        players[1][0]+(GAP+SQ_SZ)+GAP+SQ_SZ+10 )
    
    # |PLAYER BLUE IS DRAWN TO WINDOW        |
    players[1][2].draw(win)
    
# |FUNCTION THAT RETURNS "check" AS TRUE IF A CLICK IS WITHIN A RECTANGLE|
def in_rectangle(pt,r):
    check = False
    if r.getP1().x < pt.x < r.getP2().x and \
       r.getP1().y < pt.y < r.getP2().y:
        check = True
    return check


# |FUNCTION THAT DETERMINES IF ANY OF THE PLAYERS CAN MAKE A LEGAL MOVEMENT TO|
# |AN ADJACENT UNBROKEN TILE                                                  |
def can_move():
    #returns True if there is at least one legal tile the player can move to. 
    global player, players
    ADJACENT = ( (-1,-1), (-1, 0), (-1, +1),
                 (0, -1),          ( 0, +1),
                 (+1, -1), (+1, 0),(1, +1) ) 
    rp, cp = players[player][0:2]
    
    for dr, dc in ADJACENT:
        ra, ca = rp + dr, cp + dc
        if 0 <= ra < ROWS and 0 <= ca < COLS     and\
           board[ra][ca].config['fill'] == SOLID and\
           players[0][0:2] != [ra,ca]:
            return True
        elif 0 <= ra < ROWS and 0 <= ca < COLS     and\
           board[ra][ca].config['fill'] == SOLID and\
           players[1][0:2] != [ra,ca]:
            return True        
    return False 
        

# |SPLASH WINDOW THAT LAUNCHES WITH THE TITLE OF THE GAME, PROGRAMMER NAME| 
# |AND A BUTTON LABELED "PLAY GAME" THAT CLOSES THE LAUNCHER WINDOW AND   |
# |LAUNCHES THE GAME"                                                     |
def splash():
    # |splash CREATES THE WINDOW| 
    splash = GraphWin("ICEBREAKER LAUNCHER",WIN_W,WIN_H)
    
    # |CREATES THE TITLE FOR THE SPLASH WINDOW AND SETS TEXT SIZE TO PURPLE|
    # |AND SETS TEXT COLOR TO PURPLE                                       |
    game_title = Text(Point(230,100),"ICE BREAKER!\n (The board game not"
                      "\n introduction activity's)")
    game_title.setSize(18)
    game_title.setOutline("purple")
    game_title.draw(splash)
    
    
    # |CREATES AND RETURNS THE PLAY BUTTON AND THE TEXT "PLAY GAME" TO BE DRAWN|
    # |ONTO THE BUTTON                                                         |
    play,play_info = btn_create(WIN_W-275,WIN_H-250,BTN_W+50,BTN_H+25,"PLAY "
                                "GAME")
    play.setFill("blue")
    play_info.move(24,5)
    play.draw(splash)
    
    play_info.setOutline("red")
    play_info.setSize(10)
    play_info.draw(splash)
    
    
    # |CREATES AND RETURNS THE NAME RECTANGLE AND THE TEXT "Moses Lemma"|
    # |TO BE DRAWN ONTO THE RECTANGLE                                   |    
    name_box,name = btn_create(5,5,BTN_W+50,BTN_H,"Moses Lemma")
    name_box.draw(splash)
    name.move(25,0)
    name.draw(splash)
    
    
    
    while True :
        # |GET'S USER MOUSE CLICK LOCATION STORED AS (x,y)|
        splash_pt = splash.getMouse()
        
        # |IF THE USER CLICKS ON THE "PLAY GAME" BUTTON THEN THE SPLASH WINDOW|
        # |IS CLOSED AND THE GAME WINDOW IS LAUNCHED                          |
        if in_rectangle(splash_pt, play):
            splash.close()
            break
        # |IF THE USER CLICKS ANYWHERE ELSE NOTHING OCCURS|
        else:
            pass
    

# |FUNCTION RESPONSIBLE FOR CREATING A NEW WINDOW AFTER A WINNER IS DECLARED|
# |WHERE THE PLAYER CAN CHOOSE (VIA BUTTONS) WHETHER TO QUIT OR PLAY AGAIN  |

def quit_or_reset():
    # |WIDTH AND HEIGHT FOR THE WINDOW ARE ASSIGNED|
    w, h = 200, 100
    win_2 = GraphWin("QUIT OR RESET?", w, h)
    
    # |QUIT BUTTON IS MADE ALONG WITH THE TEXT "QUIT" TO BE DRAWN OVER IT|
    # |IN THE WINDOW                                                     |
    Quit_Btn, Quit_info = btn_create(10, 10, 70, 30, "QUIT")
    Quit_Btn.setFill("pink")
    Quit_Btn.draw(win_2)
    Quit_info.draw(win_2)
    
    # |RESET BUTTON IS MADE ALONG WITH THE TEXT "RESET" TO BE DRAWN OVER IT|
    # |IN THE WINDOW                                                       |
    Reset_Btn, Reset_info = btn_create(w-10-70, 10, 70, 30, "RESET")
    Reset_Btn.setFill("orange")
    Reset_Btn.draw(win_2)
    Reset_info.draw(win_2)
    
    # |VARIABLE SET AS BLANK BY DEFAULT TO BE RETURNED LATER|
    ret_msg = ""
    
    while True:
        pt = win_2.getMouse()
        
        # |IF THE USER CLICKS WITHIN THE QUIT BUTTON THE "QUIT OR RESET" WINDOW| 
        # |THE ret_msg IS SET TO "quit" AND RETURNED                           |
        if in_rectangle(pt,Quit_Btn):
            win_2.close()
            ret_msg = 'quit'
            break
        # |IF THE USER CLICKS WITHIN THE RESET BUTTON THE "QUIT OR RESET" WINDOW 
        # |IS CLOSED AND THE GAME O
        elif in_rectangle(pt,Reset_Btn):
            win_2.close()
            ret_msg = 'reset'
            break
    return ret_msg



# |RESETS THE GAME-BOARD|

# GOAL OF THE FUNCTION IS TO RESET ALL OBJECTS OF THE GAME 
def board_reset():
    # |UNDRAWS THE PLAYERS FROM THE GAME WINDOW|
    players[0][2].undraw()
    players[1][2].undraw()    
    
    # | 2D LIST USING A FOR LOOP TO RECREATE THE BOARD|
    for r in range(ROWS):
        board.append([])                      # for each row of rectangles
        for c in range(COLS):
            xL = GAP + c * (GAP+SQ_SZ)
            yU = GAP + r * (GAP+SQ_SZ)   
            board[r].append(Rectangle(Point(xL,        yU      ),
                                      Point(xL+ SQ_SZ, yU+SQ_SZ)))
            
            # |RESETS ALL TILES BACK TO THE SOLID (white) COLOR|
            board[r][c].setFill(SOLID)    
    
    # |RESETS THE PLAYER IMAGES TO THE VERY INITIAL POSITION ON THE WINDOW|
    # |(WHERE PLAYER POPEYE BEGINS AT (0,0) AND PLAYER BLUE AT (100,100)  | 
    players[0][2] = Image(Point(0,0),FNAME1)
    players[1][2] = Image(Point(100,100),FNAME2)    
    
    # |DRAWS THE PLAYER IMAGES BACK TO THE WINDOW|
    players[0][2].draw(win)
    players[1][2].draw(win)      
    
   
    # | MOVES THE PLAYER IMAGES (BOTH POPEYE AND BLUE) TO THE STARTING|
    # | POSITIONS ON THE GAME BOARD                                   |                    
    players[0][2].move( 0*(GAP+SQ_SZ)+GAP+SQ_SZ//2,
                        ROWS//2*(GAP+SQ_SZ) + GAP + SQ_SZ // 2)

    
    players[1][2].move( COLS-1+(GAP+SQ_SZ)+GAP*7+SQ_SZ*6,
                        ROWS//2+(GAP+SQ_SZ)+GAP+SQ_SZ+10 ) 

    #|UPDATES PLAYER POSITION WITH RESPECT TO ROW AND COLOUMN BACK TO THE START-
    # ING POSITION 
    players[0][0:2] = 4, 0
    players[1][0:2] = 4, 9


    


    
#==============================================================================#            
#GUI LOOP
def main():
    #GLOBAL VARIABLES
    global splash,win,btn_Quit,player_info,click_info,player,players,SOLID,BROKEN,start_pop_x,start_pop_y,start_blu_x,start_blu_y
    
    win = GraphWin(win_title,WIN_W,WIN_H)
    
    #Quit_BTN DRAWN TO WINDOW 
    Quit_Btn,Quit_info = btn_create(WIN_W-100,WIN_H-100,BTN_W,BTN_H,"QUIT")
    Quit_Btn.draw(win)
    Quit_info.setSize(10)
    Quit_info.draw(win)
    
  
         
    #Game Board DRAWN TO WINDOW 
    Board = board_setup()
    
    #GLOBAL Player_info DRAWN TO WINDOW 
    player_info.draw(win)
    
    #GLOBAL click_info DRAWN TO WINDOW
    click_info.draw(win)
    

    
    #MOVES VARIABLE TO KEEP TRACK OF WHETHER THE PLAYER CAN:
    # 0) MAKE A LEGAL MOVEMENT
    # 1) BREAK A SOLID TILE 
    moves = 0
    
        
    
    while True:
   
       
        # |INFORMS THE PLAYER TO MAKE A LEGAL MOVE|
                
        
        # |MOUSE CLICK OCCURS IF ALL PLAYERS CAN MAKE A LEGAL MOVE TO AN| 
        # |ADJACENT UNBROKEN TILE                                      |
        if can_move():
            
            pt = win.getMouse() 
            
        
        # |TURNS THE X AND Y FROM THE MOUSE CLICK INTO INTEGERS|
        x, y = int(pt.x), int(pt.y)
        
        # |c AND r = COLOUMN AND ROW NUMBER RESPECTIVLEY|
        c,r = (x - GAP) // (GAP+SQ_SZ) , (y - GAP) // (GAP+SQ_SZ)
              
        
        # |CLICK INFORMATION IF A PLAYER TRIES TO MAKE AN INVALID MOVE|
        click_info.setText("Invalid Move")
        
        
        #==============================================================================# 
        # |QUIT BUTTON| IF CLICK ON QUIT BUTTON CHECK: 
        
        # IF THE PLAYER MOUSE CLICK IS WITHIN THE "QUIT" BUTTON THE WHILE TRUE LOOP
        # IS BROKEN ENDING THE GAME
        if in_rectangle(pt,Quit_Btn) and can_move():
            
            click_info.setText("BYE BYE!")
         
            pt = win.getMouse()
            
            if in_rectangle(pt,Quit_Btn) and can_move():
                win.close()
                break
            Quit_info.setText("QUIT")
            

#==============================================================================# 

        #|BOARD INTERACTION|
        
        # IF THE PLAYER CLICKS WITHIN THE BOARD THE FOLLOWING OUTCOMES ARE
        # CHECKED
        if x > (0+GAP) and x <= (WIN_H-GAP) and \
             y > (0+GAP) and y <= WIN_H-(100+GAP) and can_move():
            
            
            # |CLICK ON PLAYER|
            
            # IF THE PLAYER CLICKS ON A PLAYER ICON THE LOCATION OF THE CLICKED
            # PLAYER IS REPORTED RELATIVE TO IT'S (ROW, COLOUMN)
            if [r, c] == players[0][0:2]:
                click_info.setText(f"{players[0][3]} at ({r}, {c})")
                
            elif [r, c] == players[1][0:2]:
                click_info.setText(f"{players[1][3]} at ({r}, {c})")
        
           
#==============================================================================#            
            # |LEGAL/ILLEGAL MOVEMENT|
            
            # IF THE PLAYER CLICKS ON A TILE ON THE BOARD 
            elif in_rectangle(pt, board[r][c]) and can_move():
                
                #DISPLAYS THE LOCATION OF THE TILE CLICKED ON THE BOARD
                click_info.setText(f"({r}, {c}) Too far! ")
                    
                                 

                #====================================================#
                #CALCULATIONS FOR PLAYER MOVEMENT 
                #(dy = y movement, dx = x movement)
                
                dr,dc = r - players[player][0], c - players[player][1]
                dx,dy = dc*(SQ_SZ + GAP), dr*(SQ_SZ+GAP)                
                #====================================================# 

#==============================================================================#
                # |BROKEN TILE CHECKS|
                
                # IF PLAYER CLICKS AN UNBROKEN TILE 
                if board[r][c].config['fill'] == BROKEN and can_move():
                    # |CHECKS FOR BROKEN TILES AROUND THE PLAYER(S)|
                    
                    # |IF THE PLAYER CLICKS ON AN ADJACENT TILE    |
                    if -1 <= dr <= 1 and -1 <= dc <= 1 and moves == 0 \
                       and can_move():
                        click_info.setText(f"({r}, {c}) Can't MOVE, space"
                                           " Already BROKEN!")
                        click_info.setSize(12)
                   
                   # |CHECKS FOR BROKEN TILES WHEN THE    | 
                   # |PLAYER(S) ARE PERMITTED TO BREAK ICE|
                   
                    else:
                        click_info.setText(f"({r}, {c}) Already BROKEN!")                        
                        click_info.setSize(12)
                        
                    


                
#==============================================================================#                  
                # |ENSURES VARIABLE "moves" IS 0 SO THE PLAYER | 
                # |MAKES A LEGAL MOVEMENT                      |
                
                elif  -1 <= dr <= 1 and -1 <= dc <= 1 and moves == 0 \
                      and can_move():
                                            
                    # |MOVES PLAYER|
                    # THE dy dx CALCULATED ABOVE (line 355,356) ^ 
                    # USED TO MOVE THE PLAYER
                    players[player][2].move(dx,dy)  
                                   
                    
                    # |UPDATES PLAYER POSITION ON BOARD|
                    
                    # |CHANGES PLAYER POSITION WITH RESPECT TO ROW AND COLOUMN|
                    # |(stored in players[player][0:2])                       |
                    players[player][0:2] = [r, c]                    
                    
                    
                    # DISPLAYS WHERE THE PLAYER HAS MOVED ON THE BOARD WITH 
                    # RESPECT TO ROW AND COLOUMN
                    click_info.setText(f"{players[player][3]} to ({r}, {c})")
                    
                    #INFORMS THE PLAYER TO BREAK ICE
                    player_info.setText(f"{players[player][3]} can BREAK Ice")                    
                                    
                    if not can_move():
                        moves = 0
                    else:
                        moves = 1
                    
                
                #CHECKS IF VARIABLE "moves" IS 1 
                #(MEANING THE PLAYER HAS MOVED) AND PERMITS ONE TILE TO 
                #BE BROKEN
#==============================================================================#                  
                elif in_rectangle(pt, board[r][c]) and moves == 1 \
                     and can_move():                   
                                    
                    #|BREAKS AND DISPLAYS LOCATION OF THE TILE BROKEN| 
                    #|BY THE PLAYER(S)                               |
                    board[r][c].setFill(BROKEN)
                    click_info.setText(f" Ice BROKEN at ({r}, {c})")
                    
                    #CHANGES THE PLAYER TURN
                    if player == 0:
                        if not can_move():
                            player = 0
                        else:
                            player += 1

                    elif player == 1:
                        if not can_move():
                            player = 1
                        
                        else:
                            player -= 1                    
                    # |INFORMS THE PLAYER TO MAKE A LEGAL MOVE|
                    if can_move():
                        player_info.setText(f"{players[player][3]} can MOVE")
                        moves = 0
                  
            
#==============================================================================#        
        #|END OF GAME CONDITIONS|
        
        # |IF ANY PLAYERS CAN NO LONGER MAKE A LEGAL MOVMENT, THE TURN IS| 
        # |CHANGED TO REPORT WHICH WINNER WON                            |
        elif not can_move():
            if player == 0:
                player = 1
            elif player == 1:
                player = 0
      
            
            click_info.setText("")      
            player_info.undraw()
           
            # |REPORTS WINNER|
            player_info.setText(f"{players[player][3]} WON !\nCLICK" 
            " ANYWHERE TO CONTINUE")
            # |MOVES THE TEXT 50 PIXELS RIGHT|
            player_info.move(50,0)
            player_info.draw(win)
            
            # |MOUSE CLICK TO BE REGISTERED ANYWHERE ON THE WINDOW TO CONTINUE|
            # |TO THE QUIT GAME OR RESET WINDOW                               |
            end_game_click = win.getMouse()
            
            
            # |END GAME FUNCTION IS CALLED TO ASK PLAYER IF THEY WOULD LIKE TO|
            # |QUIT OR RESTART THE GAME                                       |
            end_game_menu = quit_or_reset()
           
           
            # IF THE end_game_menu function returns "quit" (if user clicks on 
            # quit button) the menu window and game are closed
            if end_game_menu == "quit":
                win.close()
                break
            
            # IF THE end_game_menu function returns "reset" (if user clicks on 
            # reset button) the menu window is closed and game is reset       
            elif end_game_menu == "reset":
                player_info.setText("")
                player_info.move(-50,0)
                
                
        
            
                
                #RESET IS DISPLYED ON WINDOW
                click_info.setText("RESET")
                 
                # reset_board FUNCTION RESETS THE BOARD COLORS AND 
                # PLAYER POSITIONS
                reset_board = board_reset()     
                
                
              
                
                

                
                #RESETS TURN TO FIRST PLAYER (POPEYE)
                player = 0
                moves = 0
                player_name = players[player][3]
                
                #INFORMS THE PLAYER TO MAKE A LEGAL MOVE
                player_info.setText(f"{players[player][3]} CAN MOVE")             
                
                
                
                can_move() == True
                

#==============================================================================# 


def icebreaker():
    splash()
    main()
   

icebreaker()
