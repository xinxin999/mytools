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
            with open('/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(spcial_string_command + '\n')

    spcial_string_1 = ['\\', '/', '|', ':', '+', '-', '~', '..', '//', '\\\\', '_','``']
    for i in range(len(spcial_string_1)):
        leng = len(cmd_line)
        str_list = list(cmd_line)
        str_list.insert(random.randint(0, leng), spcial_string_1[i])
        spcial_string_1_command = ''.join(str_list)
        if os.system(spcial_string_1_command) == 0:
            with open('/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(spcial_string_1_command + '\n')

    abc = cmd_line + ';'
    if os.system(abc) == 0:
        with open('/Users/congya/Desktop/command.txt', 'a') as f:
            f.write(abc + '\n')

def special_diff_char_update(cmd_line):
    spcial_string = ['[', "(", '{', '<']
    spcial_string_1 = [']', ')', '}', '>']
    i2 = 0
    for i in range(len(spcial_string)):
        leng = len(cmd_line)
        leng_qian = leng//2 - 1
        leng_hou = leng//2 + 1
        str_list = list(cmd_line)
        str_list.insert(random.randint(0, leng_qian), spcial_string[i])
        str_list.insert(random.randint(leng_hou, leng), spcial_string_1[i2])
        i2 += 1
        spcial_string_command = ''.join(str_list)
        if os.system(spcial_string_command) == 0:
            with open('/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(spcial_string_command + '\n')

def env_hunxiao(cmd_line):
    env_path = {
        'a': '${TMPDIR: 2: 1}',
        'b':'${PATH: 3: 1}',
        'c':'${SSH_AUTH_SOCK: 13: 1}',
        'd':'${TMPDIR: 8: 1}',
        'e':'${TMPDIR: 9: 1}',
        'f': '${TMPDIR: 5: 1}',
        'h':'${LANG: 1: 1}',
        'k':'${PATH: 17: 1}',
        'm':'${TERM_PROGRAM: 9: 1}',
        'l':'${TMPDIR: 7: 1}',
        'n':'${TERM_PROGRAM: 11: 1}',
        'o': '${TMPDIR: 6: 1}',
        'p':'${TERM_PROGRAM: 1: 1}',
        'r':'${TMPDIR: 3: 1}',
        's':'${TMPDIR: 11: 1}',
        'u':'${SSH_AUTH_SOCK: 25: 1}',
        'v':'${TMPDIR: 1: 1}',
        'w':'${PATH: 14: 1}',
        'y':'${PATH: 7: 1}',
        'z': '${LANG: 0: 1}'
                }
    key = list(env_path)
    set_key = set(key)
    set_cmd_line = set(cmd_line)
    same_char = (set_key & set_cmd_line)
    special_char = choice(list(same_char))
    a_number = key.index(special_char)
    value = list(env_path.values())[a_number]
    cmd_line = cmd_line.replace(special_char,value)
    with open('/Users/congya/Desktop/command.txt', 'a') as f:
        f.write(cmd_line + '\n')

def osa_execute(cmd_line):
    qianzui = "osascript -e 'do shell script \""
    houzui = "\"'"
    osa_cmdline = qianzui+cmd_line+houzui
    if os.system(osa_cmdline) == 0:
        with open('/Users/congya/Desktop/command.txt', 'a') as f:
            f.write(osa_cmdline + '\n')

def special_char_replace(cmd_line):
    spcial_string = ['--', "-/", '`', '-^','-\\','/-/','\\-\\','.','..','.-','~','./-','/']
    spcial_char_number = cmd_line.find("-")
    if '-' in cmd_line and 'http' not in cmd_line:
        cmd_line_0 = cmd_line
        for sp_char in spcial_string:
            cmd_line = cmd_line.replace(cmd_line[spcial_char_number], sp_char,1)
            if os.system(cmd_line) == 0:
                with open('/Users/congya/Desktop/command.txt', 'a') as f:
                    f.write(cmd_line + '\n')
            cmd_line = cmd_line_0

    spcial_string_1 = ['//', "/\\/", './', '. /', '. /\\/', '/-/', '\\-\\/', '.', '../', '.. /', '~/', '.~/']
    spcial_char_number_1 = cmd_line.find("/")
    if '/' in cmd_line and 'http' not in cmd_line:
        cmd_line_0 = cmd_line
        for sp_char in spcial_string_1:
            cmd_line = cmd_line.replace(cmd_line[spcial_char_number_1], sp_char, 1)
            if os.system(cmd_line) == 0:
                with open('/Users/congya/Desktop/command.txt', 'a') as f:
                    f.write(cmd_line + '\n')
            cmd_line = cmd_line_0

    if '(' in cmd_line and 'http' not in cmd_line:
        cmd_line = cmd_line.replace('(', ' (', 1)
        if os.system(cmd_line) == 0:
            with open('/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if ' . ' in cmd_line and 'http' not in cmd_line:
        cmd_line = cmd_line.replace('.', 'localhost', 1)
        if os.system(cmd_line) == 0:
            with open('/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if 'write' in cmd_line and 'defalults' in cmd_line:
        cmd_line = cmd_line.replace('write', '-w', 1)
        if os.system(cmd_line) == 0:
            with open('/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if 'unload' in cmd_line:
        cmd_line = cmd_line.replace('unload', 'remove', 1)
        if os.system(cmd_line) == 0:
            with open('/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if '--remove' in cmd_line:
        cmd_line = cmd_line.replace('--remove', '--unblockapp', 1)
        if os.system(cmd_line) == 0:
            with open('/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if 'kill' in cmd_line:
        cmd_line = cmd_line.replace('kill', 'stop', 1)
        if os.system(cmd_line) == 0:
            with open('/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if '-int' in cmd_line and 'defalults' in cmd_line:
        cmd_line = cmd_line.replace('-int', '-string', 1)
        if os.system(cmd_line) == 0:
            with open('/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

    if '--master-disable' in cmd_line and 'spctl' in cmd_line:
        cmd_line = cmd_line.replace('--master-disable', '--master-disabl', 1)
        if os.system(cmd_line) == 0:
            with open('/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd_line + '\n')

def base64_change(cmd_line):
    b64_cmd_line = base64.b64encode(cmd_line.encode("utf-8"))
    base64_cmdline = b64_cmd_line.decode('utf-8')
    qianzui = ['echo ', 'print ', 'printf ',"/bi$'n/echo\\u0000/notexist/path'syh "]
    qianzui_add = [base64_cmdline]
    qianzui_final = ['{}{}'.format(a, b) for b in qianzui_add for a in qianzui]
    zhongjian = [' |base64 -d|', ' |openssl enc -d -a|','|\\base`printf %x 100` -d |']
    houzui = ['zsh', 'bash', 'sh', 'csh', 'ksh', 'tcsh','$(echo /b)in$(echo /ba)sh']
    for finnal_cmdline in itertools.product(qianzui_final, zhongjian, houzui):
        cmd = ''.join(finnal_cmdline)
        if os.system(cmd) == 0:
            with open('/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd + '\n')

def hex_change(cmd_line):
    h_cmdline = cmd_line.encode('utf-8')
    hex_cmdline = binascii.hexlify(h_cmdline).decode('utf-8')
    qianzui = ['echo ', 'print ', 'printf ',"/bi$'n/echo\\u0000/notexist/path'syh "]
    qianzui_add = [hex_cmdline]
    qianzui_final = ['{}{}'.format(a, b) for b in qianzui_add for a in qianzui]
    zhongjian = [' |xxd -ps -r|']
    houzui = ['zsh', 'bash', 'sh', 'csh', 'ksh', 'tcsh','$(echo /b)in$(echo /ba)sh']
    for finnal_cmdline in itertools.product(qianzui_final, zhongjian, houzui):
        cmd = ''.join(finnal_cmdline)
        if os.system(cmd) == 0:
            with open('/Users/congya/Desktop/command.txt', 'a') as f:
                f.write(cmd + '\n')

def daxiaoxie_reverse(cmd_line):
    a = list(cmd_line)
    b_number = choice(a)
    a_number = a.index(b_number)
    B_number = b_number.upper()
    cmd_line = cmd_line.replace(b_number,B_number)
    if os.system(cmd_line) == 0:
        with open('/Users/congya/Desktop/command.txt', 'a') as f:
            f.write(cmd_line + '\n')

if __name__ == "__main__":
    ex_cmd = 'ifconfig'
    special_char_replace(ex_cmd)
    special_same_char_update(ex_cmd)
    special_diff_char_update(ex_cmd)
    osa_execute(ex_cmd)
    env_hunxiao(ex_cmd)
    base64_change(ex_cmd)
    hex_change(ex_cmd)
    daxiaoxie_reverse(ex_cmd)