from PyQt5 import QtWidgets, uic
import subprocess


def search_password():
    wifi_name = wifipswdiscover_sc.inputssid.text()
    if wifi_name:
        try:
            informations = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi_name, "key", "=", "clear"], encoding='cp860')
            wifipswdiscover_sc.exibicao.setText('Consulta realizada com sucesso!!')
            wifipswdiscover_sc.textBrowser.setText(informations)
        except:
            wifipswdiscover_sc.exibicao.setText('SSID incorreto ou não existe conexão anterior neste computador')
    else:
        wifipswdiscover_sc.exibicao.setText('SSID não pode ficar em branco!')


def close():
    wifipswdiscover_sc.close()

app = QtWidgets.QApplication([])
# FORMS
wifipswdiscover_sc = uic.loadUi('wifidiscover.ui')

# BTNs
wifipswdiscover_sc.btngo.clicked.connect(search_password)
wifipswdiscover_sc.btnclose.clicked.connect(close)


# OUTPUT APP
wifipswdiscover_sc.show()
app.exec()
