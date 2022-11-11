#Collecting user input for size of tree
# arg lines=integer
import colorama
from colorama import Fore,Back,Style
colorama.init()

lines= int(input('how big do you want to your tree to be?'))

#multipying user number by 2 and subtracting 1 to get an odd number
length= (lines *2 -1)
spaces = int((length -1)/2)
i=1

for i in range(1,lines+1):
    print (Fore.RED + " "*(spaces -i + (5*10 )) + '*'*(2*i-1))
    i=i+1



for i in range(1,lines-1):
    print (Fore.BLUE+ " "*(spaces -i+(2*23)-1 ) + '*'*(2*(i+3)+3))
    i=i+1


for i in range(1,lines-1):
    print (Fore.GREEN +" "*(spaces -i+(2*23)-3) + '*'*(2*(i+5)+3))
    i=i+1



for i in range(1,lines-1):
    print (Fore.WHITE + " "*(spaces +(3*16)) + '***')
   