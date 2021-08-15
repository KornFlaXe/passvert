# Decovid
Décodeur de Pass Sanitaire Européen programmé en Python.

Le programme décode le QR Code du Pass Sanitaire (avec une image du QR Code) et affiche les informations contenues dedans.
Le décodage se fait en plusieurs étapes :
- Décodage en Base45
- Décompression Zlib
- Décodage COSE
- Décodage du message encodé en CBOR
- Affichage du json avec indentation

## Execution

Mettre l'image du QR code dans le même dossier que le script.
Ouvrir un terminal et executer la commande suivante :

```bash
passvert.py "image_qrcode.png"
```
