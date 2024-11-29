
# gpt工程
运行环境：python 3.10
## 安装运行环境

### [Windows运行环境](https://community.chocolatey.org/)
1、安装chcoc包管理工具，首先win+r输入powershell打开控制台，输入下面的指令执行（或者[点击链接](https://community.chocolatey.org/install.ps1)直接下载）：
``` powershell
set-ExecutionPolicy RemoteSigned; 
cd C:\Users\$env:UserName\Downloads;
curl -o install.ps1 https://community.chocolatey.org/install.ps1;
.\install.ps1

```
执行后再输入单个字母A回车确认

如果卡住了可能是网络断连了，考虑断一下内网断开重连一下，保证网络正常

2、安装python环境
打开powershell输入执行:
```
 choco install python310
```
3、指定阿里源
```
 mkdir %USERPROFILE%\pip && echo [global] > %USERPROFILE%\pip\pip.ini && echo index-url = https://mirrors.aliyun.com/pypi/simple/ >> %USERPROFILE%\pip\pip.ini
```
4、切到工程根目录路径再执行指令，加载依赖库
```
 pip install -r requirements.txt
```

5、切到工程根目录运行demo.py
```
 python main.py
```
### mac运行环境（待补充）