
import subprocess
import time


wifi_name = input('Digite o nome da rede wifi: ')
if wifi_name:
   try:
       informations = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi_name, "key", "=", "clear"],
                                              encoding='cp860')
       print(informations)
       print(30*'-')
       print('Consulta realizada com sucesso!!')
   except:
        print('SSID incorreto ou não existe conexão anterior neste computador')
else:
    print('SSID não pode ficar em branco!')
time.sleep(20)



