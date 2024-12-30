from time import sleep
from termcolor import colored
from os import system
import random
import platform


# basic variables
system_clear = 'clear' if platform.system() == 'Linux' else "cls"
plural_textes = lambda text, number : text + "s" if number > 0 else text


#decorator 
def sleep_decorator(func):
    def inner():
        system(system_clear)
        print(func())
        sleep(1)
        system(system_clear)
        
    return inner


# error functions
@sleep_decorator
def wrong_text():
    return colored("Please answer to question with the optitions that we specify for you !!!", "light_red")


def wrong_choice():
    print(colored('please choose your choice between 1 to 9 !!', 'light_red'))
    sleep(2)
    system(system_clear)
    print(first_line_inforamtion)
    board()

@sleep_decorator
def some_sleep():
    return board()


#bot functions
def bot_move(brd, plyr_elmnt, bot_elmnt, bt_lvl):
    perfume_bot_move_for_win = False
    prevent_player_move_for_win = False
    good_move_for_make_win_for_future = False
    

    if bt_lvl == "H":

        # prevent_player_move_for_win
        for i in winning_modes:
            if (list_elements := [brd[i[0]],  brd[i[1]], brd[i[2]]]).count(plyr_elmnt) == 2 \
                and list_elements.count(bot_elmnt) == 0:
                prevent_player_move_for_win = True
                for j in list_elements:
                    if isinstance(j, int):
                        move_for_bot =  j 
                        break
    
    if bt_lvl in ["M", "H"]:

        # perfume_bot_move_for_win
        if not prevent_player_move_for_win:
            for i in winning_modes:
                if (list_elements := [brd[i[0]],  brd[i[1]], brd[i[2]]]).count(plyr_elmnt) == 0 \
                    and list_elements.count(bot_elmnt) == 2:
                    perfume_bot_move_for_win = True
                    for j in list_elements:
                        if isinstance(j, int):
                            move_for_bot =  j 
                            break
    
    if bt_lvl == "H":
        
        # good_move_for_make_win_for_future
        if not prevent_player_move_for_win and not perfume_bot_move_for_win:
            for i in winning_modes:
                if (list_elements := [brd[i[0]],  brd[i[1]], brd[i[2]]]).count(plyr_elmnt) == 0 \
                    and list_elements.count(bot_elmnt) == 1:
                    good_move_for_make_win_for_future = True
                    for j in list_elements:
                        if isinstance(j, int):
                            move_for_bot =  j 
                            break

    if bt_lvl in ['E', 'H', 'M']:

        if not perfume_bot_move_for_win and not prevent_player_move_for_win and  not good_move_for_make_win_for_future:
            posible_numbers_to_move = [int(i) for i in brd if str(i).isnumeric()]
            move_for_bot = random.choice(posible_numbers_to_move) if 5 not in posible_numbers_to_move else 5

    return move_for_bot

def bot_level_choice():
    global level_que
    while True:
        try:
            level_que = input("Enter bot level : ((H)ard, (E)asy, (M)edium) :")
        except:
            wrong_text()
            continue
        if level_que not in ['H', "E", "M"]:
            wrong_text()
            continue
        break


# other functions
def isnumeric(lst:list):
    for i in lst:
        if isinstance(i, int):
            return True
    return False

def board():
    for j, i in enumerate(list_range):
        char_be_in_string = f"[{i}]\t\t"
        if (j + 1) % 3 == 0:
            char_be_in_string = f"[{i}]\n\n\n"
        print(char_be_in_string if isinstance(i, int) else 
              colored(char_be_in_string, "light_red") if i == "x" else colored(char_be_in_string, "light_blue") , end="")

def can_move(brd, mve):
    if isinstance(brd[mve - 1], int) and 1 <= mve <= 9:
        return True
    return False

def make_move(brd, mve, plyr_chs):
    if can_move(brd, mve):
        brd[mve - 1] = plyr_chs
        return True
    return False


def is_winner(plyr_trn):
    for i in winning_modes:
        if plyr_trn == list_range[i[0]] and plyr_trn == list_range[i[1]] and plyr_trn == list_range[i[2]]:
            return True
    return False

def Do_you_wana_continue(bt_lvl): 
    while True:
        if 'y' in (que := input("Do you want to continue ? (yes, no) :" if not bt_lvl  else "Do you want to continue ? (yes, no)\nif you want to change bot level enter '(c)hange' :")).lower():
            return True
        elif 'n' in que:
            return False
        elif 'c' in que and bt_lvl:
            bot_level_choice()
        else:
            print(colored("please answer to the question with 'yes' or 'no' !", 'light_red'))
    

# basic codes
while True:
    try:
        original_que = int(input('------------------->> Tic Toc Toe Game <<-------------------\n\t\
1)play with together\n\t\
2)play with computer\n\t\
3)exit\n\
your choice : '))
    except:
        print(colored("please answer to question with these numbers (1, 2, 3)", 'light_red'))
        sleep(2)
        system(system_clear)
        continue
    if original_que == 1 or original_que == 2:
        system(system_clear)
        while True:
            # get players name 
            while True:
                if original_que == 1:
                    name1 = input("Enter first player's name :").strip()
                    name2 = input("Enter second player's name : ").strip()
                else:
                    name1 = input("pleas Enter your name :").strip()
                    name2 = 'bot'
                if (not name1) or (not name2):
                    print(colored("please Enter the good name for each player!!!!" if original_que == 1 else "please Enter the good name for yours", "light_red"))
                    continue
                if name1 == name2:
                    print(colored("you can't Enter the same name with together!!" if original_que == 1 else "you can't Enter the same name with bot!!", 'light_red'))
                    continue
                break

            # choose x or o for each player
            if original_que == 1:
                print("\nplease choose each element that you want to play with them !!\n\
for example x: player1(name), or , y: player2(name)\n")
                while True:
                    x_choice = input("x :").strip()
                    o_choice = input("o : ").strip()
                    if not(x_choice in [name1, name2] or o_choice in [name1, name2]) or not name1 or not name2:
                        print(colored("please choose your names that you assign several second ago !!{0} or {1}".format(name1, name2), "light_red"))
                        continue
                    break
            else:
                print("please Enter your element (x or o)", end="")
                while True:
                    choice = input(": ")
                    if choice == 'x' or choice == 'o':
                        x_choice = name1 if choice == 'x' else name2
                        o_choice = name2 if x_choice == name1 else name1
                        pass
                    else:
                        print(colored("please answer to qeuestio with 'x' or 'o' :", 'light_red'))
                        print("please Enter your element (x or o)", end="")
                        continue
                    break

            x = ("x", colored(x_choice, "light_red"), x_choice)
            o = ("o", colored(o_choice, "light_blue"), o_choice)
            if original_que == 2:
                bot_level_choice()

            print("We are getting everything ready for the game !! please wait......")
            sleep(3)
            ono_loop = True


            x_points = 0
            o_points = 0
            # game started!
            while True:
                # original variables
                list_range = list(range(1, 10))
                winning_modes = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))

                print(f"{x[0]} : {x[1]} and {o[0]} = {o[1]}\n")

                i = 0   
                player_choose = x
                system(system_clear)

                another_game = False
                while True:
                    first_line_inforamtion = f"{player_choose[1]}'s turn" if ono_loop else f"{player_choose[1]}'s turn, {x[1]} = {x_points} {plural_textes('point', x_points)} and {o[1]} = {o_points} {plural_textes('point', o_points)}"
                    print(first_line_inforamtion)
                    board()
                    # player move
                    while True:
                        try:
                            if original_que == 2 and player_choose[2] == 'bot':
                                bot_elemnt = x[0] if x[2] == 'bot' else o[0]
                                player_elemnt = o[0] if bot_elemnt == 'x' else x[0]
                                sleep(1)
                                move = bot_move(brd=list_range, plyr_elmnt=player_elemnt, bot_elmnt=bot_elemnt, bt_lvl=level_que)

                            else:
                                move = int(input("Enter your choice : "))
                        except:
                            wrong_choice()
                            continue

                        if make_move(brd=list_range, mve=move, plyr_chs=player_choose[0]):
                            break
                        wrong_choice()
                        

                    # check winning for each player or bot
                    if is_winner(player_choose[0]):
                        ono_loop = False
                        some_sleep()
                        print(f"{player_choose[1]} win!!")
                        if player_choose[0] == "x":
                            x_points += 1
                        else:
                            o_points += 1
                        if not Do_you_wana_continue(level_que if original_que == 2 else False):
                            another_game = True
                        break


                    system(system_clear)
                    if not isnumeric(list_range):
                        ono_loop = False
                        some_sleep()
                        print(colored('Tie!!!', 'light_green'))
                        if not Do_you_wana_continue(level_que if original_que == 2 else False):
                            another_game = True
                        break
                    i += 1
                    player_choose = x if i % 2 == 0 else o
                if another_game:
                    break
            if another_game:
                system(system_clear)
                break
    # elif original_que == 3:
    #     print(colored('have a great day!!', 'light_green'))
    #     break
    else:
        print(colored("Have a good day!!", 'light_green'))
        sleep(2)
        break








print('hello world')