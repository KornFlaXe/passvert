# Decovid
Décodeur de Pass Sanitaire Européen programmé en Python.

![script](https://user-images.githubusercontent.com/88982293/129491150-381fe7e2-1843-4194-aee3-9ff81d339c79.png)
Exemple de décodage sur un qr code factice

Le programme décode le QR Code du Pass Sanitaire (avec une image du QR Code) et affiche les informations contenues dedans.\
Le décodage se fait en plusieurs étapes :
- Décodage en Base45
- Décompression Zlib
- Décodage COSE
- Décodage du message encodé en CBOR
- Affichage du json avec indentation

## Installation

Créer un dossier contenant le script et une image d'un QR Code (de préférence au format png).\
Installer les paquets nécessaires à l'execution du script :

```python
pip install base45 cbor2 cose pillow pizbar tableprint
```

## Execution

Ouvrir un terminal et executer la commande suivante :

```python
passvert.py "image_qrcode.png"
```
