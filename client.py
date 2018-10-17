# NODE # 
# $ERVER$Y$TEM # 
# CLIENT #

'''
# Node-Server top level client interface:
##  Back-end CLI

This is the higest level client interface meaning that there may be more features 
buried deeper in the repository. Each level may have a client module. This is 
not always the case. good luck ~jpd
'''

# ----- IMPORTS ----- #
from lib import menu 
from lib import ipfs
from lib import tpls_server
from lib import setup
from lib.ntwrk import pyscanner3 as ps3
from lib.network import NetworkClient
from node import *


import datetime
import platform
from time import sleep
import os
import shutil

# CLIENT VARIABLES 
__login = False
__run = True
__title_stat = [0]
__mm = 0
__mm_nm = 0
__help =  """
        (command): (description) 
        0: logout
        1: main menu
        2: networking menu 
        3: python shell
        tpls: transport level security server

        have you even read the source code? 
        did you actually read it though?
        seriously though, read the source for documentation.
        the best help is the help you give yourself.
        when all else fails.
        google it bro.

        """

#==============================================================================================#
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class DateTime():
    def dt(self):
        return datetime.datetime.now()
#==============================================================================================#



#==============================================================================================#
def title_bar():
    print("=" * shutil.get_terminal_size().height)

def title():
    ts = ''
    title_bar()
    print('__ORION_NET_____\t\t____', dt1.dt())
    if __title_stat[0] == 0:
        print('\t\t|__LOGIN')
        title_bar()
    
    elif __title_stat[0] == 1:
        print('\t\t|__LOGIN_FAILED__')
        title_bar()
    
    elif __title_stat[0] == 2:
        print('\t\t|__NODE_ADMIN___|')
        print("\t\t\t\t|__", platform.platform())
        print("\t\t\t\t|__", "Python Version ",platform.python_version())
        print("\t\t\t\t|__", platform.machine())
        title_bar()

def clear():
    ops = platform.system()
    if ops == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')

def refresh_screen():
    clear()
    title()
#=========================================================================================#


#===============================EXTERIOR FUNCTION CALLS===================================#
def rfsm():
    path = input('path>')
    p = rfs(path)
    print(p)

def rfs(pathname):
    index = 0
    tsizevar = 0
    print('\n\nINDEX\t\tSIZE\t\tDIRECTORY')
    title_bar()
    for root, dirs, files in os.walk(pathname):
        for file in files:
            try:
                try:
                    pathname = os.path.join(root, file)
                    size = os.path.getsize(pathname)
                    tsizevar += size
                    print(index, '\t\t', size, '\t\t', pathname)
                    index += 1
                except PermissionError:
                    print('Permission Error')
            except (FileNotFoundError, OSError):
                print('file not found error')

    returndata = {'indexed files': index,'totalsize': tsizevar}
    print(returndata)
    input('>')
    return returndata
 
def __setup_menu():
    menu.initialize_menu(setup_md, "SETUP MAIN MENU")

def __user_build():
    ub = setup.UserBuild()
    input('>>')

def __help_menu():
    print(__help)
    input('> ')

def __tpls_server():
    try:
        print('[0] single instance of tpls')
        print('[1] infinite loop of tpls')
        print('[2] oop instance of tpls')
        _id = int(input("tpls type = "))
        NodeServer()._tpls_server(_id)
    except ValueError:
        print("bruh thats not an option")
        input('>')

def __ntwrk_menu():
    refresh_screen()
    menu.initialize_menu(networking_menu_dict, "NETWORKING MAIN MENU")

def __ipfs_write():
    ipfs.IPFS_add_file('cfg.txt')
    input('>')

def __vim_file_input():
    vimfile = str(input("file> "))
    #_vimfile =  str("start vim ") + str(vimfile)
    #return os.system(_vimfile)
    __vim(vimfile)

def _vim_top_level():
    __vim("client.py")
    __vim("node.py")

def __vim(file_obj):
    launch_cmd = str("start vim ") + str(file_obj)
    os.system(launch_cmd)

def __start_file_io():
    io_file = str(input("file> "))
    __start(io_file)

def __start(io_f):
    start_cmd = str("start py -i ") + str(io_f)
    os.system(start_cmd)

def __pyscanner3():
    return ps3.main()
#==============================================================================================#
nc = NetworkClient()

# Main menu dictionary
mm = {
    'Directory Info': rfsm,
    'Setup Menu': __setup_menu,
    'Networking Menu': __ntwrk_menu,
    'Vim-Top-Level': _vim_top_level
}

networking_menu_dict = {
    'TPLS_$ERVER': __tpls_server,
    'IPFS: Writer': __ipfs_write,
    '$C4N L4N': __pyscanner3,
    "$C4N L4N (NC)": nc._network_scan,
    "Py$canner": nc._pyscanner,
    "Py$canner2": nc._pyscanner2,
    "Rever$e_$he11": nc._reverse_shell,
    "NetworkClient._tpls_server": nc._tpls_server
}

setup_md = {
    'User Build': __user_build,
    'Help': __help_menu
}
#==============================================================================================#

#__menu = menu.newMenu(mm, "main menu")
def ts_c_a(ts_id):
    __title_stat.clear()
    __title_stat.append(ts_id)
    
def _client():
    if __login == False:
        ts_c_a(2)

    while __login:
        title()
        usn = input('username: ')
        if usn != admin1.username:
            ts_c_a(1)
            refresh_screen()
                    
        elif usn == admin1.username:
            ts_c_a(0)
            refresh_screen()
            pasw = input('password: ')

            if pasw == admin1.password:
                ts_c_a(2)
                refresh_screen()
                print('You are logging in as ', usn)
                refresh_screen()
                break
    #==============================================================================================#

    #==============================================================================================#
    ######## APP INTERFACE ########
    while __run:
        refresh_screen()
        command = input('>')
        if command == '0':
            refresh_screen()
            print('LOGING OUT OF THE MATRIX')
            clear()
            break
        
        elif command == 'tpls':
            __tpls_server()

        elif command == "vim":
            refresh_screen()
            __vim_file_input()
        
        elif command == "help":
            refresh_screen()
            __help_menu()

        elif command == '1':
            refresh_screen()              
            menu.initialize_menu(mm, 'PYTHOS MAIN MENU')

        elif command == '2':
            refresh_screen()
            __ntwrk_menu()

        elif command == "3":
            refresh_screen()
            __start_file_io()
    #==============================================================================================#


if __name__ == "__main__":
    #define the class instances
    admin1 = Admin('admin', 'password')
    dt1 = DateTime()
    _client()