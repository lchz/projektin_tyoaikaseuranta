# Asennusohje

## Paikallisesti

Paikallisesti sovelluksen asentaessa tarvitaan Git ja Python3. Varmistathan, että ne ovat koneellanne asennettuina ennen sovelluksen lataamista.

1. Kloonaa projekti tai lataa se ZIP-pakattuna GitHub:sta

    `$ git clone <projekti_git>`
   
2. Mene projektin juureen komennolla

    `$ cd projektin-tyoaikaseuranta`

3. Luo Pythonin virtuaaliympäristö sovelluksen juurikansiossa ja aktivoi se

    `$ python3 -m venv venv`
    `$ source venv/bin/activate`

4. Asenna sovelluksen tarvittavat riippuvuudet

    `$ pip install -r requirements.txt`

5. Nyt sovellus on valmis käyttämään. Käynnistä sovellus komennolla

    `$ python3 run.py`

6. Jos kaikki menee oikein, sovellus on nyt käynnissä osoitteessa http://127.0.0.1:5000

7. Sovelluksen päättymiseksi painaa `ctrl + c`

## Heroku
Sovellus pyörii valmiina [Herokussa]().

Heroku-apin asettaessa tarvitaan:

1. On käytössä Herokun CLI-työkalun ja tunnukset

    `heroku create <haluttu nimi>`

2. Liitetään git-repositioon Heroku

    `git remote add heroku <osoite herokussa>`
    
3. Asetetaan Herokun HEROKU-ympäristömuuttujan arvoksi 1

    `heroku config:set HEROKU=1`

4. Luodaan sovellukselle PostgreSQL-tietokanta Herokuun

    `heroku addons:add heroku-postgresql:hobby-dev`

5. Pushataan Herokuun

    `git push heroku master`
    
