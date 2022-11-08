import os
import requests
from requests import get, post
from time import sleep 
from sys import stdout as _stdout
from os import name as _name, system as _system
from ctypes import c_int, c_byte, Structure, byref, windll

def _colors(color: str) -> str:
    return f"\033[38;2;{color}m"

Windows = _name == 'nt'
c = _colors('0;255;196')
m = _colors('161;42;252')
g = _colors('94;255;110')
r = _colors('255;0;0')
w = _colors('255;255;255')
y = _colors('255;255;0')
rl = _colors('255;28;59')
ml = _colors('255;0;102')
gl = _colors('0;255;128')

if _name == 'nt':
    class _OcultInfo(Structure):
        _fields_ = [("size", c_int),
                    ("visible", c_byte)]

def Uwu(uwu: str):
    if Windows:
        return _system(f"title {uwu}")

class Ocult:

    def Ocultism():
        if _name == 'nt':
            Ocult._ocultism(False)
        elif _name == 'posix':
            _stdout.write("\033[?25l")
            _stdout.flush()

    def _ocultism(visible: bool):
        ci = _OcultInfo()
        handle = windll.kernel32.GetStdHandle(-11)
        windll.kernel32.GetConsoleCursorInfo(handle, byref(ci))
        ci.visible = visible
        windll.kernel32.SetConsoleCursorInfo(handle, byref(ci))

def _exit():
    sleep(5)
    exit()


def check_hook(hook):
    info = get(hook).text
    if "\"message\": \"Unknown Webhook\"" in info:
        return False
    return True

def main(webhook, name, delay, amount, message, hookDeleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            payload = post(webhook, json={"content": str(message), "name": str(name), "avatar_url": "https://i.imgur.com/lk79Hlc.jpeg"})
            if payload.status_code == 204:
                print(f" {m}[{w}+{m}] Sent")
            if payload.status_code == 429:
                print(f" {r}[{y}*{r}] {rl}RateLimit")
        except:
            print()
        sleep(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        requests.delete(webhook)
        print(f' {m}[{g}+{m}]{g} Webhook deleted')
    print(f' {m}[{g}+{m}]{g} Done!{w}')


def CHook():
    Ocult.Ocultism()
    print(f"""
    {ml}               __          {rl} __                      __         
    {ml}              /\ \__       {rl}/\ \                    /\ \        
    {ml}  ___   __  __\ \ ,_\    __{rl}\ \ \___     ___     ___\ \ \/'\    
    {ml} /'___\/\ \/\ \\\\ \ \/  /'__`{rl}\ \  _ `\  / __`\  / __`\ \ , <    
    {ml}/\ \__/\ \ \_\ \\\\ \ \_/\  __/{rl}\ \ \ \ \/\ \L\ \/\ \L\ \ \ \\\\`\  
    {ml}\ \____\\\\ \____/ \ \__\ \____{rl}\\\\ \_\ \_\ \____/\ \____/\ \_\ \_\\
     {ml}\/____/ \/___/   \/__/\/____/ {rl}\/_/\/_/\/___/  \/___/  \/_/\/_/
                                                          {gl}by cattyn
     """)
    webhook = input(f" {ml}Enter ur webhook {c}> {w}")
    name = input(f" {ml}Enter a webhook name {c}> {w}")
    message = input(f" {ml}Enter a message {c}> {w}")
    delay = input(f" {ml}Enter a delay {c}> {w}")
    amount = input(f" {ml}Enter an amount {c}> {w}")
    hookDeleter = input(f" {ml}Delete webhook after spam? {r}[Y/N] {c}> {w}")
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        _exit()
    else:
        main(webhook, name, delay, amount, message, hookDeleter)
        _exit()


if __name__ == '__main__':
    os.system('cls' if Windows else 'clear')
    Uwu("CuteHook On Top LOL")
    CHook()
