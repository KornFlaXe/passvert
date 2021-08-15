# Decovid
Décodeur de Pass Sanitaire Européen programmé en Python.

Le programme décode le QR Code du Pass Sanitaire (avec une image du QR Code) et affiche les informations contenues dedans.\
Le décodage se fait en plusieurs étapes :
- Décodage en Base45
- Décompression Zlib
- Décodage COSE
- Décodage du message encodé en CBOR
- Affichage du json avec indentation

## Démonstration

```bash
✧ Données en BASE45 du Qr Code :

HC1:NCFOXN%TS3DH3ZSUZK+.V0ETD%65NL-AH-R6IOO6+IUKRG*I.I5BROCWAAT4V22F/8X*G3M9JUPY0BX/KR96R/S09T./0LWTKD33236J3TA3M*4VV2 73-E3GG396B-43O058YIB73A*G3W19UEBY5:PI0EGSP4*2DN43U*0CEBQ/GXQFY73CIBC:G 7376BXBJBAJ UNFMJCRN0H3PQN*E33H3OA70M3FMJIJN523.K5QZ4A+2XEN QT QTHC31M3+E32R44$28A9H0D3ZCL4JMYAZ+S-A5$XKX6T2YC 35H/ITX8GL2-LH/CJTK96L6SR9MU9RFGJA6Q3QR$P2OIC0JVLA8J3ET3:H3A+2+33U SAAUOT3TPTO4UBZIC0JKQTL*QDKBO.AI9BVYTOCFOPS4IJCOT0$89NT2V457U8+9W2KQ-7LF9-DF07U$B97JJ1D7WKP/HLIJLRKF1MFHJP7NVDEBU1J*Z222E.GJF67Z JA6B.38O4BH*HB0EGLE2%V -3O+J3.PI2G:M1SSP2Y3D38-G9C+Q3OT/.J1CDLKOYUV5C3W1A:75S4LB:6REPKM3ZYO4+QDNDLT2*ESLIH

✧ Données en ZLIB du Qr Code :

b'x\xda\xbb\xd4\xe2\xbb\x88\xc5\xe3\xa6\xa4y\xfc\xc1\xe7\xdb61\xaa-\x88d4^\xc2"\x95p\xd95\x95M*\xe1\xc2\xa2T\xc6$\xc7\x10KF\xe6\x85\x8cK\x12\xcb\x1aW%\xa5\xe41&\xe5&\xe6\xfa\x07\xb9\xeb\x1a\x1a\x18\x18\x18\x1b\x18\x19\x9a&\x95\x15d\x19\x1a\x1aZ\x1a\x9bX\x1a\x18\x98\'\xa5\x94d\x19\x01\x85u\r\x8ct\r-\x92\x92\xf3\x81\x06$%gV\x18\x86\x06\xf9Y\x85\x869{Z\x19\x18Z9\x86X\x19\x1aX\x18\x98[\x98\x18\xbbY\x9a8\xba\xba\x1a\xb8\xba\x9a\x1aX\x1a\xbb99\x1b\x99\x9a8\xb9X\x18\x1a+;%\xe5\x16\xe4\xb8\x86\xea\x1b\xea\x1b\x19\xe8\x1b\x9a\x1aY$e\x16WH\xfbf\xe6e\x16\x97\x14U*\xe4\xa7)x\xa4&\xe6\x94d\xe8(8\x96\x02E2\x13\x93\x8aS\x98\x92J\xd23-L\x0cL\x8d\x81N1K\xceK\xcc]\x92\x9c\x96WR\xea\x1b\x1a\x1c\xe2\x1a\xe4\x16\xe4\x18j\xe3\xee\xef\x1a\x1c\xec\xe9\xe7\xee\x1a\x94\x94\x96W\xea\x0b\xd4\x9aZ\x94V\x94X\xaa\xeb~x\xdb\xe1\xf9\x99y\xe9\xa9E\xc9\xe9y%\x19\xee\x8eNA\x9e\xae>\xaeI\xe9y\x19\xee\x89IE\x99\xa99\xa9\xc9e\xa9E\xa9\x86zFz\x86\xc9)\xf9IY\x86\x96\x96\x16 o\x1a\x99E8|\x9c\xc2X\x1b?\xf9W\xcf\x8den\xc9r\x7f\xfb\xe7\x1f\x14\x9dk\xcd&~\xfc\x0b\xf3\xca\xc9\x1d\xb7?\xdcJ*\xd4\xbe\xe9\xa0\x9d\xd8h\xf2\xc1q\xfa\x9f\x19\xdcOg(\xf4\xa6\xed7=\xc8R\x1b\xad\xc3\xf5\xd4\xb6j\xed\x15\x00\xe0\x19\x89\xb8'

✧ Données en COSE du Qr Code :

b'\xd2\x84M\xa2\x04H\xd9\x197_\xc1\xe7\xb6\xb2\x01&\xa0Y\x013\xa4\x04\x1a`\xd3Ee\x06\x1a`\xd0\xa2e\x01bAT9\x01\x03\xa1\x01\xa4av\x81\xaabdn\x01bmamORG-100030215bvpj1119349007bdtj2021-02-18bcobATbcix1URN:UVCI:01:AT:10807843F94AEE0EE5093FBC254BD813#BbmplEU/1/20/1528bisx\x1bMinistry of Health, Austriabsd\x02btgi840539006cnam\xa4cfntuMUSTERFRAU<GOESSINGERbfnuMusterfrau-G\xc3\xb6\xc3\x9fingercgnthGABRIELEbgnhGabrielecvere1.2.1cdobj1998-02-26X@\xf1\x94\x01}_\x93\xfa\x8c\xd8\xa6Fc\x1e\xfd\x8f\x9f\xc1\x15\x9d;\x06\x17\xc7\xf4\x03\xa9\x93\x88\xdb\xf0\xdabq+\xd9@+a\x814\xf0A\x97\xfc\x98\x0b\xe5\x98 \x8df\xbf5\xc1\x04}[,\n\xe5=z\xad\xd4'

✧ Données en CBOR du Qr Code :

<COSE_Sign1: [{'KID': b'\xd9\x197_\xc1\xe7\xb6\xb2', 'Algorithm': 'Es256'}, {}, b'\xa4\x04\x1a`\xd3' ... (307 B), b'\xf1\x94\x01}_' ... (64 B)]>

✧ Données en JSON du Qr Code :

{
   "4": 1624458597,
   "6": 1624285797,
   "1": "AT",
   "-260": {
      "1": {
         "v": [
            {
               "dn": 1,
               "ma": "ORG-100030215",
               "vp": "1119349007",
               "dt": "2021-02-18",
               "co": "AT",
               "ci": "URN:UVCI:01:AT:10807843F94AEE0EE5093FBC254BD813#B",
               "mp": "EU/1/20/1528",
               "is": "Ministry of Health, Austria",
               "sd": 2,
               "tg": "840539006"
            }
         ],
         "nam": {
            "fnt": "MUSTERFRAU<GOESSINGER",
            "fn": "Musterfrau-G\u00f6\u00dfinger",
            "gnt": "GABRIELE",
            "gn": "Gabriele"
         },
         "ver": "1.2.1",
         "dob": "1998-02-26"
      }
   }
}
```

## Installation

Créer un dossier contenant le script et une image d'un QR Code (de préférence au format png).\
Installer les paquets nécessaires à l'execution du script :

```bash
pip install base45 cbor2 cose pillow pizbar tableprint
```

## Execution

Ouvrir un terminal et executer la commande suivante :

```bash
passvert.py "image_qrcode.png"
```
