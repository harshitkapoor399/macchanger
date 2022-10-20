import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i" , "--interface", dest="interface", help="Interface to change its MAC address")

parser.add_option("-m" , "--mac", dest="mac", help="To Change MAC address")

parser.parse_args()




mac = input("enter mac address :")
interface = input("enter your interface :")
subprocess.call(" ifconfig " + interface + " down " ,shell=True )
subprocess.call (" ifconfig " + interface + " hw ether " + mac , shell=True)
subprocess.call(" ifconfig " + interface + " up " ,shell=True )
