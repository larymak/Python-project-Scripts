import os
import json
import sys
import ctypes, time, subprocess
import getpass
import webbrowser
from win32com.client import Dispatch

# file in which all configurations will be stored
FILE = 'config.json'

# return value used in case of success for some functions
# it is set to '' so as to append error messages if error happen
SUCCESS = ''

# set of commands used to check user input in the main method
RESET = ['r', 'reset', 'rm', 'remove']
CREATE = ['c', 'create', 'cr']
YES = ['yes', 'y', 'ya', 'ye']

# gets the username of C:\Users\username
USER = getpass.getuser()

isFile = lambda x : os.path.isfile(x)
rm = lambda x : os.remove(x)



class Config:
    '''
    This class represents a configuration object
    such configuration has a list of strings, each string in this list should be the path to the 
    executable file of a program.
    the n_desktops attribute states how many desktops will be used to start such programs
    the name of the configuration is the way this configuration is identified, it should be unique for
    each configuration
    '''
    
    def __init__(self, programs = None, n_desktops = 1, name = 'main'):
        self.programs = programs
        self.n_desktops = n_desktops
        self.name = name

    def __str__(self):
        return str(self.__dict__)



def reset_config(filename):
    if isFile(filename): rm(filename)


def save_configs(configs, filename):
    json_str = json.dumps([c.__dict__ for c in configs])
    with open(filename, 'w') as f: 
        f.write(json_str)


def load_configs(filename):
    if not isFile(filename) : return None
    
    with open(filename, 'r') as f:
        lines = json.load(f)
    
    return [Config(d['programs'], d['n_desktops'], d['name']) for d in lines]


def find_config(configs, name):
    for c in configs: 
        if c.name == name: return c
    return None

def isUrl(program):
    if "http" in program or "www." in program:
        return True
    return False

def isValid(program):
    return isUrl(program) or isFile(program)

def run_config(configs, name):
    config = find_config(configs, name)
    err_code = SUCCESS
    if config :
        virtual_desktop_accessor = ctypes.WinDLL("./VirtualDesktopAccessor.dll")
        for i in range(len(config.programs)):
            program = config.programs[i]
            if (i < config.n_desktops):
                virtual_desktop_accessor.GoToDesktopNumber(i)
                print("Go to screen ", i)
                
            if isUrl(program):
                webbrowser.open(program)
            else:
                subprocess.Popen(program, close_fds=True)

            time.sleep(1)
            print("Run ", program)
    else : 
        err_code = "No config {0} found".format(name)
    return err_code

def create_config(programs, nScreen, name, filename = FILE):
    configs = load_configs(FILE)
    if name.strip() == "":
        name = 'main'
        
    config = Config(programs, nScreen, name)
    if configs : 
        configs.append(config)
        save_configs(configs, filename)
    else :
        save_configs([config], filename)

    create_executable(config)

def create_executable(config):
    print(config)
    filename = config.name + ".bat"
    print(filename)
    f = open(filename, "w")
    f.write("python configurer.py {0}".format(config.name))
    f.close()

    createShortcut(filename, config.name, icon="C:\\Users\\Ugo\\Documents\\Projet\\FastRun\\icone\\beeboop.ico")


def createShortcut(filename, name, icon=''):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(desktop + "\\" + name + ".lnk")
    shortcut.Targetpath = os.path.abspath(os.getcwd()) + "\\" + filename
    shortcut.WorkingDirectory = os.path.abspath(os.getcwd())
    if icon == '':
        pass
    else:
        shortcut.IconLocation = icon
    shortcut.save()


if __name__ == '__main__':
    configs = load_configs(FILE)
    argv = sys.argv
    
    if configs :
        if len(argv) == 1: 
            error = run_config(configs, configs[0].name)
            if error != SUCCESS: print(error)
        
        elif argv[1].lower() in RESET:
            reset_config(FILE)
        
        else :
            error = run_config(configs, argv[1])
            if error != SUCCESS: print(error)
    
    else :
        create_config(argv[1], argv[2], argv[3])
