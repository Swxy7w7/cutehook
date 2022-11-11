import os;from requests import get, post, delete;from time import sleep;from sys import stdout as _stdout;from os import name as _name, system as _system, get_terminal_size as _terminal_size;from ctypes import c_int, c_byte, Structure, byref, windll

####################################### - DO NOT TOUCH - ###########################################################

def colors(color: str) -> str:
    return f"\033[38;2;{color}m"

Windows = _name == 'nt'
Unix = _name == 'posix'
All = __name__ == '__main__'
OSS = os.getenv('COMPUTERNAME')
e = get
o = post
d = delete
x = input
z = print
s = sleep
c = colors('0;255;196')
m = colors('161;42;252')
g = colors('94;255;110')
r = colors('255;0;0')
w = colors('255;255;255')
y = colors('255;255;0')
rl = colors('255;28;59')
ml = colors('255;0;102')
gl = colors('0;255;128')

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

def ichinisan():
    return _system('cls' if Windows else 'clear')

def Uwu(uwu: str):
    if Windows:
        return _system(f"title {uwu}")

def cc(zerotwo: str, drop: int = None, icon: str = " "):
  if drop is None:
    drop = xd(zerotwo=zerotwo)
    return "\n".join((icon * drop) + zerotwo for zerotwo in zerotwo.splitlines())

def xd(zerotwo: str):
    try:
      nya = _terminal_size().columns
    except OSError:
        return 0
    tortuge = zerotwo.splitlines()
    chocolat = max((len(v) for v in tortuge if v.strip()), default = 0)
    return int((nya - chocolat) / 2)

def t():
    s(3)
    exit()

####################################### - DO NOT TOUCH - ###########################################################

def check_hook(hook):
    msg = '"Unknown Webhook"'
    info = e(hook).text
    if msg in info or 'discord.com/api/webhooks' not in hook:
        z(f"{m}[{r}!{m}]{w} Webhook Invalid")
        x(f"{m}[{r}!{m}]{w} Press enter for continue")
        ichinisan()
        CHook()

def main(webhook, delay, amount, message, hookDeleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            payload = o(webhook, json={"content": str(message), "avatar_url": "https://i.imgur.com/lk79Hlc.jpeg"})
            if payload.status_code == 204:
                z(f" {m}[{w}+{m}] Sent")
            if payload.status_code == 429:
                z(f" {r}[{y}*{r}] {rl}RateLimit")
        except:
            z()
        s(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        d(webhook)
        z(f' {m}[{g}+{m}]{g} Webhook deleted')
    z(f' {m}[{g}+{m}]{g} Done!{w}')

def CHook():
    Uwu(f"𝘾𝙪𝙩𝙚𝙃𝙤𝙤𝙠 ^| 𝙈𝙖𝙙𝙚 𝙗𝙮: 𝙘𝙖𝙩𝙩𝙮𝙣𝙜𝙢𝙙 ^| 𝙒𝙚𝙡𝙘𝙤𝙢𝙚: {OSS}")
    Ocultism()
    chookbanner = fr"""
    {ml} ______   __  __   ______  ______  {rl} __  __   ______   ______   __  __    
    {ml}/\  ___\ /\ \/\ \ /\__  _\/\  ___\ {rl}/\ \_\ \ /\  __ \ /\  __ \ /\ \/ /    
    {ml}\ \ \____\ \ \_\ \\/_/\ \/\ \  __\ {rl}\ \  __ \\ \ \/\ \\ \ \/\ \\ \  _"-.  
    {ml} \ \_____\\ \_____\  \ \_\ \ \_____\{rl}\ \_\ \_\\ \_____\\ \_____\\ \_\ \_\ 
    {ml}  \/_____/ \/_____/   \/_/  \/_____/{rl} \/_/\/_/ \/_____/ \/_____/ \/_/\/_/ 
    {w}
    """[1:]                             
    chookbanner = cc(chookbanner)
    z(chookbanner)
    z()
    webhook = x(f" {m}[{r}*{m}]{ml} Enter ur webhook {c}> {w}")
    ichinisan()
    z(chookbanner)
    message = x(f" {m}[{r}*{m}]{ml} Enter a message {c}> {w}")
    ichinisan()
    z(chookbanner)
    delay = x(f" {m}[{r}*{m}]{ml} Enter a delay {c}> {w}")
    ichinisan()
    z(chookbanner)
    amount = x(f" {m}[{r}*{m}]{ml} Enter an amount {c}> {w}")
    ichinisan()
    z(chookbanner)
    hookDeleter = x(f" {m}[{r}*{m}]{ml} Delete webhook after spam? {r}[Y/N] {c}> {w}")
    ichinisan()
    z(chookbanner)
    try:
        delay = float(delay)
    except ValueError:
        t()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        t()
    else:
        main(webhook, delay, amount, message, hookDeleter)
        t()

if All:
    ichinisan()
    CHook()
