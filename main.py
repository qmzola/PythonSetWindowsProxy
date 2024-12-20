import winreg
import configparser
import os

ProxyRegistryPath=r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'

try:
    #判断配置文件是否存在
    if not os.path.exists('config.ini'):
        raise FileNotFoundError("配置文件config.ini不存在")
    #读取配置文件的内容
    config = configparser.ConfigParser()
    config.read('config.ini')
    Proxy_Address = config.get('Proxy', 'Address')
    # 确保代理地址不为空
    if not Proxy_Address:
        raise ValueError("配置文件中代理地址为空")
    #打开注册表键
    ProxyEnable = winreg.OpenKey(winreg.HKEY_CURRENT_USER, ProxyRegistryPath, 0, winreg.KEY_SET_VALUE | winreg.KEY_QUERY_VALUE)
    ProxyEnableKey,_=winreg.QueryValueEx(ProxyEnable,'ProxyEnable')
    #判断是代理是否是关闭状态，如果是关闭状态就设置代理
    if ProxyEnableKey == 0:
        winreg.SetValueEx(ProxyEnable,'ProxyEnable',0,winreg.REG_DWORD,1)
        winreg.SetValueEx(ProxyEnable,"ProxyServer", 0, winreg.REG_SZ, Proxy_Address)
        print("代理已开启，服务器地址是" + Proxy_Address)
        winreg.CloseKey(ProxyEnable)
    #判断代理是否是开启状态，如果开启状态是就关闭代理
    elif ProxyEnableKey == 1:
        winreg.SetValueEx(ProxyEnable,'ProxyEnable',0,winreg.REG_DWORD,0)
        winreg.DeleteValue(ProxyEnable,"ProxyServer")
        print("代理已关闭")
        winreg.CloseKey(ProxyEnable)
#异常处理
except FileNotFoundError:
    print("配置文件 config.ini 不存在，请检查文件路径。")
except PermissionError:
    print("权限不足，无法修改注册表，请以管理员权限运行脚本。")
except Exception as e:
    print(f"发生未知错误：{e}")
finally:
    # 确保关闭注册表键
    if 'ProxyEnable' in locals():
        winreg.CloseKey(ProxyEnable)