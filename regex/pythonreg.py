import re
from prettytable import PrettyTable
sentence = '''
show arp:
Address            Age         Hardware Addr          State        Type      Interface
60.123.76.81        -         d4:6f:ab:89:b1:bb       Interface    ARPA      Fa1/0/3
78.45.89.90      00.44.05     d4:6d:80:f1:b0:b2       Dynamic      ARPA      Gi1/0/1
68.66.72.97      00:07:12     d4:c6:50:49:42:84       Interface    ARPA      Gi2/1/4
'''
pattern = re.compile('((?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])).*((?:[a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}).*([a-zA-Z]{2}[1-9]\/[0-9]\/[0-9])')
table=PrettyTable(["ip address","mac address","Interface"])
matches = pattern.finditer(sentence)
for x in matches:
    table.add_row([x.group(1),x.group(2),x.group(3)])
print(table)		