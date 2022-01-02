import os
import sys
import time
import os.path
from tqdm import tqdm
from os import close, listdir
from datetime import datetime
from os.path import isfile, join

cli_cmd_list = [    ['set prompt',           'f_set_prompt'   ], 
                    ['show files',           'f_show_files'   ],
                    ['show dirs',            'f_show_dirs'    ],
                    ['show date',            'f_show_date'    ]
                ]

def print_message(msg, msg_type,delay):
    current_datetime = str(datetime.now())
    print(f'{current_datetime} [ {msg_type} ] {msg}')
    time.sleep(delay)

def isValidCmd(entered_cmd):   
    for c in cli_cmd_list:
        e_cmd = "".join(entered_cmd.split())
        v_cmd = "".join(str(c[0]).split())
        if e_cmd == v_cmd:
            return True, str(c[1])
    return False, entered_cmd

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

def f_set_prompt():
    global prompt
    print_message('Prompting for new prompt.',"INFO", 1)
    prompt = input('Enter new prompt : ')

def f_show_dirs():
    print_message('Showing only directories',"INFO", 1)
    os.system('dir /ad')

def f_show_files():
    print_message('Showing only files',"INFO", 1)
    os.system('dir /b /a-d')

def f_show_date():
    print_message('Showing current date and time',"INFO", 1)
    os.system('date /T')
    os.system('time /T')

## MAIN
print_message('Starting Pycli v1.0 2022....',"INFO", 2)
os.system('cat learnAtyourDesk_banner.txt')
os.system('echo.')


beInLoop    = True
prompt      = 'PyCLI # >' 

while beInLoop:
    try:
        cli_input = input(prompt+' ')
        if cli_input == 'exit':
            print_message('Exiting....',"INFO", 3)
            sys.exit()

        isValid, func = isValidCmd(cli_input)
        
        if isValid:     
            str_to_class(func)()
        else:
            os.system(cli_input)

    except KeyboardInterrupt:
        print_message("Exiting... ","INFO", 1)
        sys.exit()
