#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *

keymap = {
    0x04: ('a', 'A'), 0x05: ('b', 'B'), 0x06: ('c', 'C'),
    0x07: ('d', 'D'), 0x08: ('e', 'E'), 0x09: ('f', 'F'),
    0x0a: ('g', 'G'), 0x0b: ('h', 'H'), 0x0c: ('i', 'I'),
    0x0d: ('j', 'J'), 0x0e: ('k', 'K'), 0x0f: ('l', 'L'),
    0x10: ('m', 'M'), 0x11: ('n', 'N'), 0x12: ('o', 'O'),
    0x13: ('p', 'P'), 0x14: ('q', 'Q'), 0x15: ('r', 'R'),
    0x16: ('s', 'S'), 0x17: ('t', 'T'), 0x18: ('u', 'U'),
    0x19: ('v', 'V'), 0x1a: ('w', 'W'), 0x1b: ('x', 'X'),
    0x1c: ('y', 'Y'), 0x1d: ('z', 'Z'), 0x1e: ('1', '!'),
    0x1f: ('2', '@'), 0x20: ('3', '#'), 0x21: ('4', '$'),
    0x22: ('5', '%'), 0x23: ('6', '^'), 0x24: ('7', '&'),
    0x25: ('8', '*'), 0x26: ('9', '('), 0x27: ('0', ')'),
    0x28: ('\x0a', '\x0a'), 0x29: ('\x1b', '\x1b'), 0x2a: ('\x08', '\x08'),
    0x2b: ('\x09', '\x09'), 0x2c: ('\x20', '\x20'), 0x2d: ('-', '_'),
    0x2e: ('=', '+'), 0x2f: ('[', '{'), 0x30: (']', '}'),
    0x31: ('\\', '|'), 0x32: (';', ':'), 0x33: ("\'", '\"'),
    0x34: ('`', '~'), 0x35: (',', '<'), 0x36: ('.', '>'),
    0x37: ('/', '?'), 0x38: ('/', '?'), 0x39: ('[CapsLock]', '[CapsLock]'),
    0x3A: ('[F1]', '[F1]'), 0x3B: ('[F2]', '[F2]'), 0x3C: ('[F3]', '[F3]'),
    0x3D: ('[F4]', '[F4]'), 0x3E: ('[F5]', '[F5]'), 0x3F: ('[F6]', '[F6]'),
    0x40: ('[F7]', '[F7]'), 0x41: ('[F8]', '[F8]'), 0x42: ('[F9]', '[F9]'), 
    0x43: ('[F10]', '[F10]'), 0x44: ('[F11]', '[F11]'),
    0x45: ('[F12]', '[F12]'), 0x46: ('[PrintScreen]', '[PrintScreen]'),
    0x47: ('[ScollLock]', '[ScollLock]'), 0x48: ('[Pause]', '[Pause]'),
    0x49: ('[Insert]', '[Insert]'), 0x4A: ('[Home]', '[Home]'), 0x4B: ('[PageUp]', '[PageUp]'),
    0x4C: ('[Delete]', '[Delete]'), 0x4D: ('[End]', '[End]'), 0x4E: ('[PageDown]', '[PageDown]'),
    0x4F: ('[RightArrow]', '[RightArrow]'), 0x50: ('[LeftArrow]', '[LeftArrow]'),
    0x51: ('[DownArrow]', '[DownArrow]'), 0x52: ('[UpArrow]', '[UpArrow]'),
    0x53: ('[NumLock]', '[NumLock]')
}

def read_usbdata_from_pcap():
    pcap = rdpcap("data.pcap")
    usb_data = []
    for pkt in pcap:
        buf = pkt['Raw'].load
        usb_data.append(buf[27:])
    return usb_data

def analyze_usb_data(usb_data): 
    flag = ""
    for d in usb_data:
        if d[2] == 0x00 or not 0x00 in d[3:8]:
            # No event
            continue
        if d[0] == 0x02 or d[0] == 0x20:
            # press shift-key
            # binary -> int
            c = keymap[d[2]][1]
            flag += c
        else:
            # not press shift-key
            # binary -> int
            c = keymap[d[2]][0]
            flag += c
    print(flag)

def main():
    data = read_usbdata_from_pcap()
    analyze_usb_data(data)

if __name__ == '__main__':
    main()