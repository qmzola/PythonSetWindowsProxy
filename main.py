import winreg
import configparser

config=configparser.ConfigParser()
config.read('config.ini')


Proxy_Adderss= config['ProxyAdderss']
ProxyRegistryPath=r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'

try:
    ProxyEnable=winreg.OpenKey(winreg.HKEY_CURRENT_USER,ProxyRegistryPath)
    ProxyEnableKey,_=winreg.QueryValueEx(ProxyEnable,'ProxyEnable')
    if ProxyEnableKey == 0:
        winreg.SetValueEx(ProxyEnable,'ProxyEnable',0,winreg.REG_DWORD,1)
        winreg.SetValueEx(ProxyEnable,"ProxyServer", 0, winreg.REG_SZ, Proxy_Adderss)
        print("代理已开启，服务器地址是" + Proxy_Adderss)
        winreg.CloseKey(ProxyEnable)
    elif ProxyEnableKey == 1:
        winreg.SetValueEx(ProxyEnable,'ProxyEnable',0,winreg.REG_DWORD,0)
        winreg.DeleteValue(ProxyEnable,"ProxyServer")
        print("代理已关闭，服务器地址是")
        winreg.CloseKey(ProxyEnable)
except FileNotFoundError:
    print("无法找到指定的注册表项，请检查路径是否正确。")
except PermissionError:
    print("权限不足，无法修改注册表，请以管理员权限运行脚本。")
except Exception as e:
    print(f"发生未知错误：{e}")
finally:
    winreg.CloseKey(ProxyEnable)