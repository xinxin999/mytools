import os
import random
import base64
import binascii
import itertools
from random import choice

def special_same_char_update(cmd_line):
    spcial_string = ['"', "'", '^']
    for i in range(len(spcial_string)):
        leng = len(cmd_line)
        str_list = list(cmd_line)
        str_list.insert(random.randint(0, leng), spcial_string[i])
        str_list.insert(random.randint(0, leng), spcial_string[i])
        spcial_string_command = ''.join(str_list)
        if os.system(spcial_string_command) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(spcial_string_command + '\n')

    spcial_string_1 = ['\\', '/', '|', ':', '+', '-', '~', '..', '//', '\\\\', '_','``',';']
    for i in range(len(spcial_string_1)):
        leng = len(cmd_line)
        str_list = list(cmd_line)
        str_list.insert(random.randint(0, leng), spcial_string_1[i])
        spcial_string_1_command = ''.join(str_list)
        if os.system(spcial_string_1_command) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(spcial_string_1_command + '\n')

    abc = cmd_line + ';'
    if os.system(abc) == 0:
        with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
            f.write(abc + '\n')

def special_diff_char_update(cmd_line):
    spcial_string = ['[', "(", '{', '<']
    spcial_string_1 = [']', ')', '}', '>']
    i2 = 0
    for i in range(len(spcial_string)):
        str_list = list(cmd_line)
        leng = len(cmd_line)
        str_list.insert(0, spcial_string[i])
        str_list.insert(leng + 1, spcial_string_1[i2])
        i2 += 1
        spcial_string_command = ''.join(str_list)
        if os.system(spcial_string_command) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(spcial_string_command + '\n')

def env_hunxiao(cmd_line):
    env_path = {
        'a':'%ProgramData:~-1,1%',
        'd':'%ComSpec:~6,1%',
        'e':'%ComSpec:~15,1%',
        'f':'%ProgramFiles:~-5,1%',
        'g':'%ProgramData:~6,1%',
        'i':'%ComSpec:~4,1%',
        'c':'%PUBLIC:~-1,1%',
        'm':'%ComSpec:~16,1%',
        'l':'%TMP:~-6,1%',
        'n':'%ComSpec:~5,1%',
        'o':'%ComSpec:~7,1%',
        'p':'%TMP:~-1,1%',
        'r':'%ProgramData:~4,1%',
        's':'%ComSpec:~9,1%',
        't':'%ComSpec:~14,1%',
        'u':'%TMP:~3,1%',
        'w':'%ComSpec:~8,1%',
        'x':'%ComSpec:~-2,1%',
        'y':'%ComSpec:~12,1%'
                }
    key = list(env_path)
    set_key = set(key)
    set_cmd_line = set(cmd_line)
    same_char = (set_key & set_cmd_line)
    special_char = choice(list(same_char))
    a_number = key.index(special_char)
    value = list(env_path.values())[a_number]
    cmd_line = cmd_line.replace(special_char, value)
    with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
        f.write(cmd_line + '\n')

def env_hunxiao_set(cmd_line):
    n = 4
    set_value = []
    set_value_2 = []
    for i in range(0, len(cmd_line), n):
        a = 'b'
        set_num = a+str(i)
        value = "set "+set_num+"="+cmd_line[i:i+n]+"&&"
        set_value.append(value)
        set_value_2.append(set_num)

    set_value_str = " ".join(set_value)
    set_value_2_str = "%%".join(set_value_2)
    houzui = 'call %'+set_value_2_str+'%'
    result = set_value_str+houzui
    if os.system(result) == 0:
        with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
            f.write(result + '\n')

def daxiaoxie_reverse(cmd_line):
    a = list(cmd_line)
    b_number = choice(a)
    a_number = a.index(b_number)
    B_number = b_number.upper()
    cmd_line = cmd_line.replace(b_number,B_number)
    if os.system(cmd_line) == 0:
        print(cmd_line)
        with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
            f.write(cmd_line + '\n')

def special_char_replace(cmd_line):
    spcial_string = ['--', "-/", '`', '-^','-\\','/-/','\\-\\','.','..','.-','~','./-','/']
    spcial_char_number = cmd_line.find("-")
    if '-' in cmd_line and 'http' not in cmd_line:
        cmd_line_0 = cmd_line
        for sp_char in spcial_string:
            cmd_line = cmd_line.replace(cmd_line[spcial_char_number], sp_char,1)
            if os.system(cmd_line) == 0:
                with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                    f.write(cmd_line + '\n')
            cmd_line = cmd_line_0

    spcial_string_1 = ['//', "/\\/", './', '. /', '. /\\/', '/-/', '\\-\\/', '.', '../', '.. /', '~/', '.~/','-']
    spcial_char_number_1 = cmd_line.find("/")
    if '/' in cmd_line and 'http' not in cmd_line:
        cmd_line_0 = cmd_line
        for sp_char in spcial_string_1:
            cmd_line = cmd_line.replace(cmd_line[spcial_char_number_1], sp_char, 1)
            if os.system(cmd_line) == 0:
                with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                    f.write(cmd_line + '\n')
            cmd_line = cmd_line_0

    if '(' in cmd_line and 'http' not in cmd_line:
        cmd_line = cmd_line.replace('(', ' (', 1)
        if os.system(cmd_line) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if 'net' in cmd_line and 'http' not in cmd_line:
        cmd_line = cmd_line.replace('net', 'net1', 1)
        if os.system(cmd_line) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if 'iwr' in cmd_line and 'powershell' in cmd_line:
        cmd_line = cmd_line.replace('iwr', 'Invoke-webrequests', 1)
        if os.system(cmd_line) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if 'Invoke-Webrequests' in cmd_line and 'powershell' in cmd_line:
        cmd_line = cmd_line.replace('Invoke-webrequests', 'iwr', 1)
        if os.system(cmd_line) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if 'Invoke-Expression' in cmd_line and 'powershell' in cmd_line:
        cmd_line = cmd_line.replace('Invoke-Expression', 'iex', 1)
        if os.system(cmd_line) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if 'IEX' in cmd_line and 'powershell' in cmd_line:
        cmd_line = cmd_line.replace('IEX', 'Invoke-Expression', 1)
        if os.system(cmd_line) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if 'cscript' in cmd_line:
        cmd_line = cmd_line.replace('cscript', 'wscript', 1)
        if os.system(cmd_line) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if 'wscript' in cmd_line:
        cmd_line = cmd_line.replace('wscript', 'cscript', 1)
        if os.system(cmd_line) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if '/add' in cmd_line and 'user' in cmd_line:
        cmd_line = cmd_line.replace('/add', '/ad', 1)
        if os.system(cmd_line) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if '/domain' in cmd_line and 'net' in cmd_line:
        cmd_line = cmd_line.replace('/domain', 'do', 1)
        if os.system(cmd_line) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if 'os list' in cmd_line or 'process get' in cmd_line and 'wmic' in cmd_line:
        cmd_line = cmd_line.replace('os list', 'os get', 1)
        cmd_line = cmd_line.replace('process get', 'process list', 1)
        if os.system(cmd_line) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if 'os get' in cmd_line or 'process list' in cmd_line and 'wmic' in cmd_line:
        cmd_line = cmd_line.replace('os get', 'os list', 1)
        cmd_line = cmd_line.replace('process list', 'process get', 1)
        if os.system(cmd_line) == 0:
            with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

def powershell_execute(cmd_line):
    a = 'powershell.exe "& {'
    b = '}"'
    cmd_line = a+cmd_line+b
    if os.system(cmd_line) == 0:
        with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
            f.write(cmd_line + '\n')

def powershell_base64(cmd_line):
    spcial_char = 'AA=='
    b64_cmd_line = base64.b64decode(spcial_char.encode("utf-8"))
    base64_cmdline = b64_cmd_line.decode('utf-8')
    lcmd_line = list(cmd_line)
    slcmd_line = [str(i)+base64_cmdline for i in lcmd_line]
    sslcmd_line = "".join(slcmd_line)
    a_b64_cmd_line = base64.b64encode(sslcmd_line.encode("utf-8"))
    a_base64_cmdline = a_b64_cmd_line.decode('utf-8')
    qianzui = "powershell.exe /encodedcomma "
    cmd_line = qianzui+a_base64_cmdline
    if os.system(cmd_line) == 0:
        with open('C:/Users/congya/Desktop/command.txt', 'a') as f:
            f.write(cmd_line + '\n')

if __name__ == "__main__":
    cmd_line = "whoami /all"
    special_same_char_update(cmd_line)
    special_diff_char_update(cmd_line)
    special_char_replace(cmd_line)
    env_hunxiao(cmd_line)
    env_hunxiao_set(cmd_line)
    daxiaoxie_reverse(cmd_line)
    powershell_execute(cmd_line)
    powershell_base64(cmd_line)