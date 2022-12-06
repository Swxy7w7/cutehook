from requests import get, post, delete
from time import sleep
from sys import stdout as _stdout
from os import getenv, system, name as _name
from ctypes import c_int, c_byte, Structure, byref, windll

def colors(color: str) -> str:
    return f"\033[38;2;{color}m"

Windows = _name == 'nt'
Unix = _name == 'posix'
All = __name__ == '__main__'
OSS = getenv('COMPUTERNAME')
e = get
o = post
d = delete
i = input
p = print
s = sleep
m = colors('161;42;252')
g = colors('94;255;110')
r = colors('255;0;0')
w = colors('255;255;255')
rl = colors('255;28;59')
ml = colors('255;0;102')

class _OcultInfo(Structure):
    _fields_ = [("size", c_int), ("visible", c_byte)]

def Ocultism():
    if Windows:
        ocultism(False)
    elif Unix:
        _stdout.write("\033[?25l")
        _stdout.flush()

def ocultism(visible: bool):
    ci = _OcultInfo()
    handle = windll.kernel32.GetStdHandle(-11)
    windll.kernel32.GetConsoleCursorInfo(handle, byref(ci))
    ci.visible = visible
    windll.kernel32.SetConsoleCursorInfo(handle, byref(ci))

def clear():
    return system('cls' if Windows else 'clear')

def T(uwu: str):
    if Windows:
        return system(f"title {uwu}")

def back():
    s(3)
    exit()

def check_hook(hook):
    msg = '"Unknown Webhook"'
    info = e(hook).text
    if msg in info or 'discord.com/api/webhooks' not in hook:
        p(f"{m}[{r}!{m}]{w} Webhook Invalid")
        i(f"{m}[{r}!{m}]{w} Press enter for continue")
        clear()
        CHook()

def main(webhook, delay, username, amount, message, hookDeleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            payload = o(webhook, json={"username": username, "avatar_url": "https://i.imgur.com/lk79Hlc.jpeg", "content": message})
            if payload.status_code == 204 or payload.status_code == 200: 
                p(f" {m}[{w}+{m}] Sent")
            if payload.status_code == 429:
                p(f" {m}[{r}*{m}] {rl}RateLimit")
        except:
            p()
        s(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        d(webhook)
        p(f' {m}[{g}+{m}]{g} Webhook deleted')
    p(f' {m}[{g}+{m}]{g} Done!{w}')


def CHook():
    T(f"𝘾𝙪𝙩𝙚𝙃𝙤𝙤𝙠 ^| 𝙈𝙖𝙙𝙚 𝙗𝙮: 𝙘𝙖𝙩𝙩𝙮𝙣𝙜𝙢𝙙 ^| 𝙒𝙚𝙡𝙘𝙤𝙢𝙚: {OSS}")
    Ocultism()
    chookbanner = fr"""
    {ml} ______   __  __   ______  ______  {rl} __  __   ______   ______   __  __    
    {ml}/\  ___\ /\ \/\ \ /\__  _\/\  ___\ {rl}/\ \_\ \ /\  __ \ /\  __ \ /\ \/ /    
    {ml}\ \ \____\ \ \_\ \\/_/\ \/\ \  __\ {rl}\ \  __ \\ \ \/\ \\ \ \/\ \\ \  _"-.  
    {ml} \ \_____\\ \_____\  \ \_\ \ \_____\{rl}\ \_\ \_\\ \_____\\ \_____\\ \_\ \_\ 
    {ml}  \/_____/ \/_____/   \/_/  \/_____/{rl} \/_/\/_/ \/_____/ \/_____/ \/_/\/_/ 
    {w}
    """[1:]                             
    p(chookbanner)
    webhook = i(f" {m}[{r}*{m}]{ml} Enter ur Webhook {r}> {w}")
    if not check_hook(webhook):
        message = i(f" {m}[{r}*{m}]{ml} Enter a message {r}> {w}")
    username = i(f" {m}[{r}*{m}]{ml} Enter a name {r}> {w}")
    delay = i(f" {m}[{r}*{m}]{ml} Enter the delay {r}> {w}")
    delay = float(delay)
    amount = i(f" {m}[{r}*{m}]{ml} Enter the amount {r}> {w}")
    hookDeleter = i(f" {m}[{r}*{m}]{ml} Do you want to delete the webhook after spamming? [y/n]: {r}> {w}")
    if not amount.isdigit() and amount != "inf" or (hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        back()
    else:
        main(webhook, delay, username, amount, message, hookDeleter)
        back()

if All:
    clear()
    CHook()
