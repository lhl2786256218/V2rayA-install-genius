import sys
import os
print ("\033[31m             Welcome!!!        \033[37m")
print ("")
print ("")
print ("\033[32m")
print ("       ******************************")
print ("        ****************************")
print ("                              *****")
print ("                            ****")
print ("                          ****")
print ("                        ****")
print ("                      ****")
print ("                    ****")
print ("                  ****")
print ("                ****")
print ("             ****")
print ("           ****")
print ("         ****")
print ("        *******************************")
print ("       *******************************")
print ("                                *************************************")
print ("                               *************************************")
print ("                              ***                                **")
print ("                             ***                                **")
print ("                            ***                                **")
print ("                           ***                                **")
print ("                          ***                                **")
print ("                         ***                                **")
print ("                        ***                                **")
print ("                       ***                                **")
print ("                      *************************************")
print ("                     *************************************")
print ("                    ***")
print ("                   ***")
print ("                  ***")
print ("                 ***")
print ("                ***")
print ("               ***")
print ("              ***")
print ("             ***")
print ("            ***")
print ("           ***")
print ("          ***")
print ("\033[37m")
print ("\033[32m [+]\033[31m Script Running!!!")
print ("\033[37m")
try:
	print ("\033[32m [*]\033[31m Please wait!!!\033[37m")
	os.system('sudo wget -qO - https://apt.v2raya.org/key/public-key.asc | sudo tee /etc/apt/trusted.gpg.d/v2raya.asc')
	os.system('echo "deb https://apt.v2raya.org/ v2raya main" | sudo tee /etc/apt/sources.list.d/v2raya.list && sudo apt update')
	os.system('sudo apt install v2raya')
	os.system('sudo systemctl start v2raya.service')
	os.system('sudo systemctl enable v2raya.service')
	os.system('apt install iptables')
	os.system('update-alternatives --set iptables /usr/sbin/iptables-nft && update-alternatives --set ip6tables /usr/sbin/ip6tables-nft')
	os.system('update-alternatives --set arptables /usr/sbin/arptables-nft && update-alternatives --set ebtables /usr/sbin/ebtables-nft')
	print ("\033[32m [*]\033[31m Reboot your device please!\033[37m")
	print ("Done!")
except:
	print ("\033[32m [>]\033[31m Error!\033[37m")
