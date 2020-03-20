# Asennusohje

Sovelluksen asentaessa tarvitaan Git ja Python3. Varmistathan, että ne ovat koneellasi asennettuina ennen sovelluksen lataamista.

1. Kloonaa projekti tai lataa se ZIP-pakattuna GitHub:sta

    `$ git clone <projekti_git>`

2. Luo Pythonin virtuaaliympäristö sovelluksen juurikansiossa ja aktioi se

    `$ python3 -m venv venv`
    `$ source venv/bin/activate`

3. Asenna sovelluksen tarvittavat riippuvuudet

    `$ pip install -r requirements.txt`

4. Nyt sovellus on valmis käyttämään. Käynnistä sovellus komennolla

    `$ python3 run.py`

5. Jos kaikki menee oikein, sovellus on käynnissä osoitteessa http://127.0.0.1:5000

6. Sovelluksen päättymiseksi painaa `ctrl + c`

    