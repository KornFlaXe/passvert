# PassVert
Décodeur de Pass(e) Sanitaire Européen programmé en Python.

Le programme décode le certificat avec une image du QR Code et affiche les informations contenues dedans.\
Le décodage se fait en plusieurs étapes :
- Décodage en Base45
- Décompression Zlib
- Décodage COSE
- Décodage du message encodé en CBOR
- Affichage du json avec indentation

## Images

Quelques images du script en fonctionnement avec la possibilité de choisir un dump complet ou directement un dump du json.

<table>
    <tr>
    <td><img src="https://raw.githubusercontent.com/KornFlaXe/passvert/master/img/smalldump.png" width="500" />
    <td><img src="https://raw.githubusercontent.com/KornFlaXe/passvert/master/img/fulldump.png" width="500" />
</table>

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
