import winreg
import os
import socket


ProxyAdders= "192.168.37.25:20000"
DnsServerAdders= '192.168.1.1'
ProxyCommand= 'netsh interface ip set dns name="以太网" static ' + DnsServerAdders + ' primary'

print(ProxyCommand)
'''
ProxyKey=winreg.OpenKey("HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings", "ProxyEnable")
if ProxyKey=0
    winreg.FlushKey(ProxyKey)
'''