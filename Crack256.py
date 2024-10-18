######## ATAQUE A HASH SHA256  ##########
import hashlib, argparse, sys, time, os
from colorama import Fore, Style, init
init(autoreset=True)
so=os.name
RED=f"{Fore.RED}{Style.BRIGHT}"
WHITE=f"{Fore.WHITE}{Style.BRIGHT}"
RST=f"{Style.RESET_ALL}"
if so == 'nt':
 os.system('cls')
else:
	os.system('clear')

print(f'''{WHITE}
        ____                _    ____  ____   __
       / ___|_ __ __ _  ___| | _|___ \\| ___| / /_
      | |   | '__/ _` |/ __| |/ / __) |___ \\| '_ \\
      | |___| | | (_| | (__|   < / __/ ___) | (_) |
       \\____|_|  \\__,_|\\___|_|\\_\\_____|____/ \\___/

	''')
parser = argparse.ArgumentParser(description='Ataque a hashes SHA-256 utilizando un diccionario de palabras.')
parser.add_argument('-a', '--rhashes', required=True, type=str, help='RUTA DEL ARCHIVO CON HASHES')
parser.add_argument('-d', '--rdict', required=True, type=str, help='RUTA DEL DICCIONARIO CON LAS POSIBLES PALABRAS')
args = parser.parse_args()
rhashes = args.rhashes
rdict = args.rdict
def generar_hash(texto):
 return hashlib.sha256(texto.encode()).hexdigest()

with open(rhashes, "r") as f:
 hashes=f.read().splitlines()

with open(rdict, "r") as f:
 texto=f.read().splitlines()
E='   '

def mensaje(msg):
 for i in msg:
  sys.stdout.write(i) 
  sys.stdout.flush()
  time.sleep(0.04)
 print('')
cadena1=f"{E}-> INICIANDO ATAQUE A HASHES SHA256 [EN PROCESO]"
cadena2=f"{E}-> [PGX] NINGUN SISTEMA ES SEGURO..."
mensaje(cadena1) ; mensaje(cadena2)
print("")
n=1
for i in texto:
 transformado=generar_hash(i)
 if transformado in hashes:
  print(f"{E}{RED}[{n}] {WHITE}{i} -> {RST}{transformado}")
  n=n+1
