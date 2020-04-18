#!/usr/bin/env python
import subprocess
import optparse

print('#####################################')
print('##                                 ##')
print('## MAC Address Changer for Linux   ##')
print('## This Was Programmed By: BYY2100 ##')
print('##                                 ##')
print('#####################################')

def mac_change(int_card, newMAC):
    print(f">> Changing The MAC Address for {int_card} to {newMAC}")
   
    subprocess.call(['ifconfig' , int_card, 'down'])
    subprocess.call(['ifconfig' , int_card, 'hw','ether', newMAC])
    subprocess.call(['ifconfig' , int_card, 'up'])

def args():
    prs = optparse.OptionParser()
    prs.add_option("-i","--interface",dest ="int_card", help = "The interface you wanna change its MAC address")
    prs.add_option("-m","--mac",dest ="newMAC", help = "The new MAC address")
    (options, arguments) = prs.parse_args()

    if not options.int_card:
        prs.error(">> Please specify an interface. use --help for more information")
    elif not options.newMAC:
        prs.error(">> Please specify a new MAC address. use --help for more information")
    return options

options = args()
mac_change(options.int_card, options.newMAC)