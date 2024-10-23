######## ATAQUE A HASH SHA256  ##########
import hashlib, argparse, sys, time, os, shutil
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
width = shutil.get_terminal_size().columns
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

def generar_md5(texto):
 return hashlib.md5(texto.encode()).hexdigest()


with open(rhashes, "r") as f:
 hashes=f.read().splitlines()

with open(rdict, "r") as f:
 texto=f.read().splitlines()
E=' '

def mensaje(msg):
 for i in msg:
  sys.stdout.write(i) 
  sys.stdout.flush()
  time.sleep(0.03)
 print('')
cadena1=f" -> ATAQUE A HASHES SHA-256 Y MD5 [EN PROCESO]"
cadena2=f" -> [PGX] NINGUN SISTEMA ES SEGURO..."
mensaje(cadena1) ; mensaje(cadena2)
print("")
n=1
found=[]
for i in texto:
 convmd5=generar_md5(i)
 convMmd5=generar_md5(i.upper())
 transformado=generar_hash(i)
 transformado2=generar_hash(i.upper())
 tt=i.upper()
 if transformado in hashes:
  print(f"{E}{RED}[{n}] SHA-256: {WHITE}{i} -> {RST}{transformado}")
  found.append(f"SHA-256 : {i} -> {transformado}")
  n=n+1
 if transformado2 in hashes:
  print(f"{E}{RED}[{n}] SHA-256: {WHITE}{tt} -> {RST}{transformado2}")
  found.append(f"SHA-256 : {tt} -> {transformado2}")
  n=n+1
 if convmd5 in hashes:
  print(f"{E}{RED}[{n}] MD5: {WHITE}{i} -> {RST}{convmd5}")
  found.append(f"MD5 : {i} -> {convmd5}")
  n=n+1
 if convMmd5 in hashes:
  print(f"{E}{RED}[{n}] MD5: {WHITE}{tt} -> {RST}{convMmd5}")
  found.append(f"MD5 : {tt} -> {convMmd5}")
  n=n+1

hashsave='hashes_descifrados.txt'

if os.path.exists(hashsave):
 os.remove(hashsave)

cantidad=len(found)
print("")
if cantidad == 0:
 print(f"{E}NO SE ENCONTRARON COINCIDENCIAS")
else:
 mensaje(f"{E}SE ENCONTRARON COINCIDENCIAS")
 mensaje(f"{E}Y SE ALMACENARON EN \"hashes_descifrados\"")

 guardar='\n'.join(found)
 with open(hashsave, 'a') as f:
  f.write(guardar)
  f.close()

print(f"{E}HASTA LA PROXIMA AMIGO...")
