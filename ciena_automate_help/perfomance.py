from login import login
import netmiko


connection = login()
interface = input('enter port number: ')
val = input('select value or default all: ')
res = connection.send_command(f'port xcvr show port {interface} d')

lists = ['Temp', 'Vol', 'Tx', 'Rx']
newlist = []
try: 
    newlist = []
    if val in lists:
        ls = res.split('\n')
        if val == 'Temp':
            for i in range(4, 8):
                newlist.append(ls[i])
        if val == 'Vol':
            for i in range(7, 11):
                newlist.append(ls[i])
        if val == 'Tx':
            for i in range(16, 20):
                newlist.append(ls[i])
        if val == 'Rx':
            for i in range(22, 26):
                newlist.append(ls[i])
    else:
        newlist = res.split('\n')     
except:
    pass

newtext = '\n'.join(newlist)
with open('port performance.txt', 'w', encoding='utf-8') as infile:
    infile.write(newtext)

print(newtext)