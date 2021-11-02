import sys
import json
import zlib
import cbor2
import base45
import tableprint
from PIL            import Image
from pyzbar         import pyzbar
from cose.messages  import CoseMessage

qr_code = sys.argv[1]
qr_pict = Image.open(qr_code)
qr_cert = pyzbar.decode(qr_pict)[0].data.decode()
qr_ba45 = qr_cert.replace("HC1:", "")
qr_zlib = base45.b45decode(qr_ba45)
qr_cose = zlib.decompress(qr_zlib)
qr_cbor = CoseMessage.decode(qr_cose)
qr_json = cbor2.loads(qr_cbor.payload)
qr_dump = json.dumps(qr_json, indent=3)

print()
tableprint.banner("     Décodeur Certificat COVID Numérique UE ✧ Version 0.2a     ")

cdump = input('\n✧ Voulez-vous un dump complet du certificat ? [Y/n] ')

if cdump.lower() == "Y".lower():
    print('\n✧ Données Certificat :\n')
    print(qr_cert)
    print('\n✧ Données en BASE45 :\n')
    print(qr_ba45)
    print('\n✧ Données en ZLIB :\n')
    print(qr_zlib)
    print('\n✧ Données en COSE :\n')
    print(qr_cose)
    print('\n✧ Données en CBOR :\n')
    print(qr_cbor)
    print('\n✧ Données en JSON :\n')
    print(qr_json)
    print('\n✧ Indentation JSON :\n')
    print(qr_dump)
    print()
else:
    print()
    print(qr_dump)
    print()
