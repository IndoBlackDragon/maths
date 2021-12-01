' this is indo🇮🇩black dragon '
' welcome to script '

# importing module
from os import system
from time import sleep
from sys import *



# made a animation
def main(teks):
	for x in teks:
		stdout.write(x);stdout.flush()
		from random import uniform
		sleep(round(uniform(0.002,0.1),1))


# installing module if False and continue if True
try:
	from pyfiglet import Figlet
	from fractions import Fraction as Fr
except:
	main("\nmodule not installed")
	print ('installing module..'); sleep(1)
	print ('waiting..');sleep(0.5)
	system("python3 -m pip install Fraction")
	system("python3 -m pip install pyfiglet")
	system("pkg install toilet -y")
	main("\n[[ done! ]] ");system("python kalkulator.py")



# colors
normal = "\x1b[0m"
red,white = '\x1b[31;1m','\033[37;1m'
yellow,blue = '\x1b[33;1m','\x1b[0;34m'
green,black = "\x1b[32;1m",'\x1b[30;1m'
cyan,agung = "\x1b[1;36m","\033[35;1m"
bw,br,bc,bb = "\x1b[47;1m","\x1b[41;1m","\x1b[46;1m","\x1b[40;1m"


# class kalkulator
class dragon(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		# substitusion


# class diff
class IndoBlack(dragon):


	def Ahmad(self): # for jumlah
		return f'{blue}[{yellow}hasil{blue}]{green} >> {self.x} + {self.y} = {Fr(self.x+self.y).limit_denominator()}'

	def Rifal(self): # for kurang
		return f'{blue}[{yellow}hasil{blue}]{green} >> {self.x} - {self.y} = {Fr(self.x-self.y).limit_denominator()}'

	def Dharma(self): # for dif
		return f'{blue}[{yellow}hasil{blue}]{green} >> {self.x} / {self.y} = {Fr(self.x/self.y).limit_denominator()}'

	def Indoblack(self): # for kali
		return f'{blue}[{yellow}hasil{blue}]{green} >> {self.x} × {self.y} = {Fr(self.x*self.y).limit_denominator()}'
	# done


txt = f"{black}\n[[ program finished ]]{yellow}"

def penjumlahan():
	x = Fr(input(f'\n{blue}[{green}enter{blue}]{green} >> '))
	y = Fr(input(f'{blue}[{green}enter{blue}]{green} >> '))
	pro = IndoBlack(x,y)
	print (pro.Ahmad())
def pengurangan():
	x = Fr(input(f'\n{blue}[{green}enter{blue}]{green} >> '))
	y = Fr(input(f'{blue}[{green}enter{blue}]{green} >> '))
	pro = IndoBlack(x,y)
	print (pro.Rifal())
def pembagian():
	x = Fr(input(f'\n{blue}[{green}enter{blue}]{green} >> '))
	y = Fr(input(f'{blue}[{green}enter{blue}]{green} >> '))
	pro = IndoBlack(x,y)
	print (pro.Dharma())
def perkalian():
	x = Fr(input(f'\n{blue}[{green}enter{blue}]{green} >> '))
	y = Fr(input(f'{blue}[{green}enter{blue}]{green} >> '))
	pro = IndoBlack(x,y)
	print (pro.Indoblack())



def replay():
	ln = input(f"{cyan}Try again? [y/n]: ")
	if ln=="n":exit()
	elif ln=="y":menu()
	else: print (f"{red}[!] Error!") ;sleep(1);replay()




# function menu
def menu():
	print ("")
	system("figlet -f pagga kalkulator | lolcat");print (green)
	print ("[•] 1. Penjumlahan")
	print ("[•] 2. pengurangan")
	print ("[•] 3. Pembagian")
	print ("[•] 4. Perkalian")
	print (f"{red}[•] 0. Exit")

	try:
		expectation = int(input(f'\n{white}masukkan pilihan >>{blue} '))
	except (NameError,ValueError,UnboundLocalError): main(f"{red}\n[!] Error!{green}\n");sleep(1);menu()

	try:
		if expectation == 1:
			penjumlahan();print (txt)
			replay()
		elif expectation == 2:
			pengurangan();print (txt)
			replay()
		elif expectation == 3:
			pembagian();print (txt)
			replay()
		elif expectation == 4:
			perkalian();print (txt)
			replay()
		elif expectation == 0:
			main(f"{blue}\n{bw}terima kasih telah gunakan script ini..{normal} \n")
	except (UnboundLocalError,ValueError):
		main(f"\n{red}[!] Error\n")
		menu()
menu()

