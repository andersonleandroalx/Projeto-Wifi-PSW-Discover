from PyQt5 import QtWidgets, uic
import subprocess

def search_password():
    if wifipswdiscover_sc.radioButton.isChecked():
        option1 = 'manual'
        print(option1)
        wifi_name = wifipswdiscover_sc.inputssid.text()
        if wifi_name:
            try:
                informations = subprocess.check_output(
                    ["netsh", "wlan", "show", "profile", wifi_name, "key", "=", "clear"],
                    encoding='cp860')
                wifipswdiscover_sc.exibicao.setText('Consulta realizada com sucesso!!')
                wifipswdiscover_sc.all.close()
                wifipswdiscover_sc.manual.show()
                wifipswdiscover_sc.textBrowser.setText(informations)
            except:
                wifipswdiscover_sc.exibicao.setText('SSID incorreto ou não existe conexão anterior neste computador')
        else:
            wifipswdiscover_sc.exibicao.setText('SSID não pode ficar em branco!')
    elif wifipswdiscover_sc.radioButton_2.isChecked():
        option1 = 'all'
        print(option1)
        meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

        data = meta_data.decode('utf-8', errors='backslashreplace')

        data = data.split('\n')

        profiles = []

        for i in data:
            if 'All User Profile' in i:
                i = i.split(':')
                i = i[1]
                i = i[1:-1]
                profiles.append(i)

        print('{:<30}| {:<}'.format('Wifi Name', 'Password'))
        print('------------------------------------------------')
        wifipswdiscover_sc.all.show()
        wifipswdiscover_sc.manual.close()
        #wifipswdiscover_sc.status1.setText('{:<30}| {:<}'.format('Wifi Name', 'Password'))
        wifipswdiscover_sc.status2.setText('------------------------------------------------')

        lista1 = []
        for i in profiles:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key', '=', 'clear'])

                results = results.decode('utf-8', errors='backslashreplace')
                results = results.split('\n')

                results = [b.split(':')[1][1:-1] for b in results if 'Key Content' in b]
                try:
                    print(i, results[0])
                    #print('{:<30}| {:<}'.format(i, results[0]))
                    wifipswdiscover_sc.all.show()
                    wifipswdiscover_sc.manual.close()
                    wifipswdiscover_sc.status1.setText('{:<30}| {:<}'.format('Wifi Name', 'Password'))
                    wifipswdiscover_sc.status3.setText('{:<30}| {:<}'.format(i, results[0]))
                    wifipswdiscover_sc.text1.setText('{:<30}| {:<}'.format(i, results[0]))


                except IndexError:
                    print('{:<30}| {:<}'.format(i, ''))
                    wifipswdiscover_sc.all.show()
                    wifipswdiscover_sc.manual.close()
                    wifipswdiscover_sc.status3.setText('{:<30}| {:<}'.format(i, ''))


                wifipswdiscover_sc.status3.setText('{:<30}| {:<}'.format(i, results[0]))
                # wifipswdiscover_sc.table1.setRowCount(len(results))
                # wifipswdiscover_sc.table1.setColumnCount(7)
                #
                # for i in range(0, len(results)):
                #     for j in range(0, 7):
                #         wifipswdiscover_sc.table1.setItem(i, j, QtWidgets.QTableWidgetItem(str(results[i][j])))

            except subprocess.CalledProcessError:
                print('Encoding Error Occured')
                wifipswdiscover_sc.all.show()
                wifipswdiscover_sc.manual.close()
                wifipswdiscover_sc.status3.setText('Encoding Error Occured')

    else:
        wifipswdiscover_sc.exibicao.setText('Escolha uma das opções para continuar1')
        option1 = 'nda'
        print(option1)





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
