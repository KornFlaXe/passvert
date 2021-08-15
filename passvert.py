import sys
import json
import zlib
import cbor2
import base45
import tableprint
from PIL            import Image
from pyzbar         import pyzbar
from cose.messages  import CoseMessage

qr_file = sys.argv[1]
qr_pict = Image.open(qr_file)
qr_data = pyzbar.decode(qr_pict)[0].data
qr_ba45 = base45.b45decode(qr_data[4:])
qr_zlib = zlib.decompress(qr_ba45)
qr_cose = CoseMessage.decode(qr_zlib)
qr_cbor = cbor2.loads(qr_cose.payload)
qr_json = json.dumps(qr_cbor, indent=3)
qr_utf8 = qr_data.decode('utf8')

print()
tableprint.banner("     Décodeur Certificat COVID Numérique UE ✧ Version 1.0     ")
print('\n✧ Données en BASE45 du Qr Code :\n')
print(qr_utf8)
print('\n✧ Données en ZLIB du Qr Code :\n')
print(qr_ba45)
print('\n✧ Données en COSE du Qr Code :\n')
print(qr_zlib)
print('\n✧ Données en CBOR du Qr Code :\n')
print(qr_cose)
print('\n✧ Données en JSON du Qr Code :\n')
print(qr_json)
print()
