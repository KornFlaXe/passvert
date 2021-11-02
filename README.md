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

Pour procéder à l'installation, le logiciel **git** doit être présent sur votre machine et également **Python** avec son gestionnaire de bibliothèque **pip**.

Pour le commencement, clonez le projet à partir de cet ligne de commande : 
```bash
git clone https://github.com/L1444/passvert
```
Par la suite, rendez vous sur le dossier *passvert* : 
```bash
cd passvert/
```
Et installez, toutes les dépendances grâce à cet ligne de commande.
```bash
pip install -r requirements.txt
```

## L'utilisation

Afin d'utiliser le script, vous devez mettre python au début afin d'éxecuter l'intérpreteur Python *(en guise de programme à démarrer)*, ensuite le nom du script qui sera dans tous les cas **passvert.py** et par la suite le chemin du QRCode.

Le QRCode est à la racine du script donc cet ligne de commande suffit : 
```bash
python passvert.py "nomduqrcode.png"
```
