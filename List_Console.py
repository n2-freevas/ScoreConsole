import sys
import math
args = sys.argv


"""=== define ==="""
name_length_limit = 6 # the limit for player name
list_length_limit = 12 # the limit for amount of element in list
digit_length_limit = 3 # the limit for a number of digit
player_limit = 3 # members of player defined
player_names = [] # player names array
players = []

"""=== player information defined ==="""
class player_Info(object):

    def __init__(self,player_name,number):
        self.number = number
        self.name = player_name
        self.point_list = []
        for i in range(list_length_limit):
            self.point_list.append('-')
        self.total = 0
        self.list_empty_pointer = 0

            
    def insert_inlist(self,point):
        if self.list_empty_pointer >= list_length_limit:
            return False
        else:
            self.point_list[self.list_empty_pointer] = int(point)
            self.list_empty_pointer += 1
            self.total = self.total + int(point)
            return True

    def show_list(self,playernum):

        # make horizontal frame
        frame = List_Frame_make()
        frame.horizontal_frame_make()
        if(playernum == 0):
            frame.vertical_frame_make()       
        
        # make player number frame
        print('| ',end='')
        for i in range( (int(math.log10(player_limit))+1) - (len(str(self.number))) ):
            print(' ',end='')
        print(str(self.number),end='')

        # make name frame
        print(' | ' + str(self.name),end="")
        for i in range(name_length_limit-len(self.name)):
            print(' ',end="")
        print(' | ',end="")
        
        # make points frame
        for i in range(len(self.point_list)):
            
            if len(str(self.point_list[i])) == 1 : 
                print('  ' + str(self.point_list[i]) + " ",end="")
            elif len(str(self.point_list[i])) == 2:
                print(' ' + str(self.point_list[i]) + ' ',end="")
            elif len(str(self.point_list[i])) == 3:
                print(str(self.point_list[i]) + ' ',end="")
            else:
                print(' - ',end="")
        print('|',end='')

        # make total frame
        print(' ',end='')
        for i in range((digit_length_limit+int(math.log10(list_length_limit)+1)) - len(str(self.total))):
            print(' ',end='')
        print(str(self.total)+" |")

        # if calling a last member, the under discrive vertical frame 
        if playernum == player_limit - 1:
            frame.horizontal_frame_make()

"""===== The function discrive frame of list ====="""
class List_Frame_make(object):

    def vertical_frame_make(self):
        
        # player No frame
        print('| ',end='')
        for i in range(int(math.log10(player_limit))+1):
            print(' ',end='')
        print(' | ',end='')
        # player name frame
        for i in range(name_length_limit):
            print(' ',end='')
        print(' | ',end='')

        # point index frame
        for i in range(list_length_limit):
            for j in range(digit_length_limit - len(str(i+1))):
                print(' ',end='')
            print(str(i+1)+' ',end='')
        print('| ',end='')

        # make total frame
        for i in range(digit_length_limit+int(math.log10(list_length_limit)+1)):
            print(' ',end='')
        print(' |')
        self.horizontal_frame_make()

    def horizontal_frame_make(self):
        print('+-',end='')
        for i in range(int(math.log10(player_limit))+1):
            print('-',end='')
        print('-+-',end='')
        for i in range(name_length_limit):
            print('-',end='')
        print('-+-',end='')
        for i in range(list_length_limit):
            for j in range(digit_length_limit):
                print('-',end='')
            print('-',end='')
        print('+-',end='')
        for i in range(digit_length_limit+int(math.log10(list_length_limit)+1)):
            print('-',end='')
        print('-+-')

"""===== <Command> Show control Command list function"""
def control_command(players,command):
    # 1 to (player_limit) into command

    if (command.isdecimal())and(1<=int(command)<=player_limit):
        access_the_database(players[int(command)-1])
        return 1

    elif (command.isalpha())and(command in player_names):
        index = player_names.index(command)
        access_the_database(players[int(index)])
        return 1

    elif command == "exit":
        print('(System) Byebye.\n')
        return 0

    elif command == 'show':
        for i in range(player_limit):
            players[i].show_list(i)
        return 1

    elif command == 'addmem':
        
        return 1

    elif command == 'delmem':
        delmem(players)
        return 1

    elif command == 'addlis':
        addlis(players)
        return 1

    elif command == 'deldex':
        deldex(players)
        return 1

    elif command == 'ext':
        for i in range(player_limit):
            for j in range(list_length_limit):
                players[i].point_list[j] = j*(i+1)
                players[i].total += j*(i+1)
        return 1

    elif command == 'opt':
        print('   @-----------------')
        print('   @@ ( Comtrol command index )')
        print('   @@ [No.]  : Access database that its number having')
        print('   @@ [Name] : Access database that its name having')
        print('   @@ exit   : End this application')
        print('   @@ show   : showing list all player got points and its total')
        print('   @@ addMem : Open option for adding member and his list')
        print('   @@ delMem : Open option for deleting member and his list')
        print('   @@ addlis : Open option for expanding list length')
        print('   @@ deldex : Open option for delete all point in certain index or exchange certain a point')
        print('   @ -----------------')
        return 1
    
    else:
        print('   @ '+str(command)+' is undefined.')
        print('   @ If you see command list? Try to [opt] command')
        return 1

"""=== <Command> No. or Name ==="""
def access_the_database(player):
    flag = True
    while(flag):
        print('   -- ■ ('+player.name+'): input a point >> ',end='')
        string = input()
        if string.isnumeric():
            point = int(string)
            flag = False
        else:
            print('   -- [!] Please input a kind of only NUMBER')
    point_limit = 0
    for i in range(digit_length_limit):
        point_limit = 9*(10**(i)) + point_limit
    if point_limit < point:
        boo = player.insert_inlist(point_limit)
        print('   -- (OK) '+player.name+' get max point ('+str(point_limit)+').')
    else:
        boo = player.insert_inlist(point)
        if boo:
            print('   -- (OK) '+player.name+' get '+str(point)+' point.')
        else:
            print('   -- [!] '+str(player.name+'\'s list is full'))

def delmem(players):
    print('   (delmem) if you input only (Name or Player No.), delete all point of its player')
    delmem_flag = 1
    while(delmem_flag):
        print('   (dellis) ■ Please enter command (if you exit? : exit)>',end='')
        command = input()

        # if imput Name
        if (command.isalpha)and(command in player_names):
            global player_limit
            playerNo = player_names.index(command)
            del players[playerNo]
            player_limit -= 1
            dellis_flag = control_command(players,'show') - 1
            
        # if imput Player No.
        elif (command.isdecimal())and(1<=int(command)<=player_limit):
            del players[int(command)-1]
            player_limit -= 1
            dellis_flag = control_command(players,'show') - 1
            
        elif command == 'exit':
            dellis_flag = 0

        else:
            print(str(command)+ ' is unknown command.')
            dellis_flag = 1

"""=== <Command> expanding list length option ==="""
def addlis(players):
    print("   (addlis) ■ How many a number you want to add empty in list? >",end='')
    add = int(input())
    global list_length_limit
    list_length_limit += add
    for i in range(player_limit):
        for j in range(add):
            players[i].point_list.append('-')     
    
    print("   (addlis) Complete expanding list.")
    flag = control_command(players,'show')

def deldex(players):
    print('   (deldex) if input (index)(ex.5), delete all players have point in index')
    print('            if (Name, index)(ex. Taro, 5), exchange a certain point that input indicated')
    dellis_flag = 1
    global list_length_limit
    while(dellis_flag):
        print('   (deldex) ■ Please enter command >',end='')
        command = input()
        commands = [command.strip() for command in command.split(',')]
        command0 = commands[0]
        if len(commands) == 2:
            command1 = commands[1]
        
        # if imput only index No.
        if (command0.isnumeric())and(1<=int(command0)<=list_length_limit):

            for i in range(player_limit):
                players[i].total -= int(players[i].point_list[int(command0)-1])
                del players[i].point_list[int(command0)-1]
            list_length_limit -= 1
            print('   (deldex)Now, list size is '+str(list_length_limit))
            dellis_flag = control_command(players,'show')
        
        # if imput
        elif (command0.isalpha())and(command0 in player_names):
            who = player_names.index(command0)
            if (command1.isnumeric())and(1<=int(command1)<=list_length_limit):
                print('   (deldex_exchange) ■'+str(command0)+' have '+str(players[who].point_list[int(command1)-1])+' point. your true point is >',end='')
                new_point = int(input())
                
                old_point = players[who].point_list[int(command1)-1]
                players[who].point_list[int(command1)-1] = new_point
                players[who].total += new_point - old_point
                dellis_flag = control_command(players,'show')

        elif command == 'exit':
            print('   (deldex) Bye.')
            dellis_flag = 0

        else:
            print('   (deldex) '+str(command)+' is unknown command. Try again')
            dellis_flag = 1

"""===== opperator (main flow) ====="""
def opperator():
    global players
    # if same pyaler_limit and number of command lines, its are defined as player names
    if len(args) == player_limit + 1:
        for i in range(player_limit):
            player_names.append(str(args[i+1]))
            players.append(player_Info(player_names[i],i+1))
    else:
        print('(center) I will make list and please input player information')
        print('(center) number of player is '+str(player_limit) +'.')
        for i in range(player_limit):
            print('■ ['+str(i+1)+'/'+str(player_limit)+'] What your name?>',end='')

            name = input()
            player_names.append(name[0:name_length_limit])
            players.append(player_Info(player_names[i],i+1))

    print('(center) welcome to my list',end='')
    for i in range(player_limit):
        print(', ['+str(players[i].name)+']',end='')
    print('')
    flag = control_command(players,'show')

    while flag == 1:
        print('■ select your control >> ',end='')
        command = str(input())
        flag = control_command(players,command)

opperator()
