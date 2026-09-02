# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: HomeInventory
import sys, os

def colorize(text, color=None, bold=False, dim=False, underline=False, reverse=False):
    if color is None:
        return text
    codes = []
    if dim: codes.append(2)
    if bold: codes.append(1)
    codes.append(30 + color)
    if underline: codes.append(4)
    if reverse: codes.append(7)
    start = '\033[' + ''.join(str(c) for c in codes)
    return start + text + '\033[0m'

def disable_colors():
    if sys.stdout.isatty():
        sys.stdout.write('\033[0m')
        return True
    return False

def print_colored(text, color=None, bold=False, dim=False, underline=False, reverse=False):
    if disable_colors():
        print(text)
    else:
        print(colorize(text, color, bold, dim, underline, reverse))
