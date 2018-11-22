import os

def menu():

print:("
mmmmmmm                                       mm  m    m               #     
   #     mmm    m mm  mmmmm  m   m  m   m    m"#  #    #  mmm    mmm   #   m 
   #    #"  #   #"  " # # #  #   #   #m#    #" #  #mmmm# "   #  #"  "  # m"  
   #    #""""   #     # # #  #   #   m#m   #mmm#m #    # m"""#  #      #"#   
   #    "#mm"   #     # # #  "mm"#  m" "m      #  #    # "mm"#  "#mm"  #  "m 

    00. Turn your Android into Hacking Machine

    01.Metasploit
    02.Aircrack
    03.Nmap
    04.Hydra
    05.Wireshark
    06.Kickthemout
    07.HackingScripts

    99.Exit
")

install = True
	menu()
    your = input("#: ")
    if your == "00":
        print("This will install:Metasploit, Aircrack, Nmap, Hydra, Wireshark, HackingScripts")
        task = input(" Do you want to continue? (y/n): ")
        if task == y
            print:("This process can take several minutes")
            os.system("pkg update && upgrade")
            #git install 
            os.system("pkg install -y git")
            #python install
            os.system("pkg install -y python")
            os.system("pkg install -y python2")
            #pip3 install
            os.system("apt-get install pip3")
            #wget install
            os.system("pkg install -y wget")
            #nmap install
            os.system("pkg install -y nmap")
            #hydra install
            os.system("pkg install -y hydra")
            #aircrack install
            os.system("pkg install -y aircrack-ng")
            os.system("apt update -y")
            os.system("pkg update && upgrade")
            #metasploit install
            os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
            os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
            os.system("cd /data/data/com.termux/files/home && bundle install")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update && upgrade")
            #wireshark install
            os.system("wget https://raw.githubusercontent.com/Hax4us/Hax4us.github.io/master/sources-aarch64.list.txt")
            os.system("mv sources-aarch64.list.txt sources.list")
            os.system("mv sources.list $PREFIX/etc/apt")
            os.system("wget https://xeffyr.github.io/termux-x-repository/pubkey.gpg")
            os.system("apt install gnupg gnupg2 && apt-key add pubkey.gpg -y")
            os.system("apt install wireshark")
            os.system("apt update -y")
            #kickthemout --Wifi
            os.system("sudo apt-get update && sudo apt-get upgrade")
            os.system("git clone https://github.com/k4m4/kickthemout.git")
            os.system("sudo -H pip3 install -r requirements.txt")


        else:
            remenu = input("[?] Back to Menu? (y/n): ")
            if remenu == "y":
                menu()
            else:
                break

    if your == "01":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        
        print:("Metasploit was installed")
        remenu = input("[?] Back to Menu? (y/n): ")
        if remenu == "y":
            menu()
        else:
            break

    elif your == "02":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update")
        os.system("pkg install -y aircrack-ng")
        print:("Aircrack was installed")
        remenu = input("[?] Back to Menu? (y/n): ")
        if remenu == "y":
            menu()
        else:
            break

    
    elif your == "03":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg install -y nmap")
        print:("Nmap was installed")
        remenu = input("[?] Back to Menu? (y/n): ")
        if remenu == "y":
            menu()
        else:
            break

    
    elif your == "04":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg install -y hydra")
        print:("Hydra was installed")
        remenu = input("[?] Back to Menu? (y/n): ")
        if remenu == "y":
            menu()
        else:
            break

    elif your == "05":
        os.system("pkg update && upgrade")
        os.system("wget https://raw.githubusercontent.com/Hax4us/Hax4us.github.io/master/sources-aarch64.list.txt")
        os.system("mv sources-aarch64.list.txt sources.list")
        os.system("mv sources.list $PREFIX/etc/apt")
        os.system("wget https://xeffyr.github.io/termux-x-repository/pubkey.gpg")
        os.system("apt install gnupg gnupg2 && apt-key add pubkey.gpg -y")
        os.system("apt install wireshark")
        os.system("apt update -y")
        print:("Wireshark was installed")
        remenu = input("[?] Back to Menu? (y/n): ")
        if remenu == "y":
            menu()
        else:
            break

    elif your == "06":
        os.system("sudo apt-get update && sudo apt-get upgrade")
        os.system("git clone https://github.com/k4m4/kickthemout.git")
        os.system("sudo -H pip3 install -r requirements.txt")
        print:("Kickthemout was installed")
        remenu = input("[?] Back to Menu? (y/n): ")
        if remenu == "y":
            menu()
        else:
            break

    elif your == "99":
        print("Bye, Bye")
        break




    


            
            
            