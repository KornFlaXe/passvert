# Decovid
Décodeur de Pass Sanitaire Européen programmé en Python.

Le programme décode le Qr code du Pass Sanitaire (image) et affiche les informations contenues dedans.
Le décodage se fait en plusieurs étapes :
- Décodage en Base45
- Décompression Zlib
- Décodage COSE
- Décodage du message encodé en CBOR
- Affichage du json avec indentation
