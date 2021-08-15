# Decovid
Décodeur de Pass Sanitaire Européen programmé en Python.

Le programme décode le QR Code du Pass Sanitaire (avec une image du QR Code) et affiche les informations contenues dedans.
Le décodage se fait en plusieurs étapes :
- Décodage en Base45
- Décompression Zlib
- Décodage COSE
- Décodage du message encodé en CBOR
- Affichage du json avec indentation

## Installation

Créer un dossier contenant le script et une image d'un QR Code (de préférence au format png)
Installer les paquets nécessaires à l'execution du script :

```bash
pip install base45 cbor2 cose pillow pizbar tableprint
```

## Execution

Ouvrir un terminal et executer la commande suivante :

```bash
passvert.py "image_qrcode.png"
```
