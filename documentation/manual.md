# Käyttöohjeet

## Kirjautuminen
Projektien listausta lukuun ottamatt kaikki muut toiminnallisuudet vaativat käyttäjän kirjautumista. Painaamalla oikeakulmasta nappia `Sign in` käyttäjä voi kirjautua sovellukseen joko projektipäälikkönä (Master) tai peruskäyttäjänä (Basic) vastaavalla käyttäjätunnuksella ja salasanalla. Sovellukseen on määritelty etukäteen kolme käyttäjätiliä sovelluksen testausta varten. Nämä tilit ovat:

|Rooli  | Käyttäjätunnus | Salasana  |
|:-----:|:--------------:|:---------:|
|BASIC  |    test        | secret    |
|BASIC  |    test2       | secret2   |
|MASTER |    master      | admin     |

Näistä kaksi ensimmäistä ovat perukäyttäjätiliä ja viimeinen projektipäälikkötili.

## Rekisteröityminen
Sovellukseen on tehty erillinen sivu rekisteröinnille, eli uuden käyttäjän luomiselle. Kirjautumattomana kyseiselle sivulle pääsee painaamalla oikeakulmasta nappia `Sign up`. Siellä käyttäjä voi luoda peruskäyttäjätilin `basic account` tai projektipäälikkötilin `master account`. 

Molempien roolien rekisteröitymiseen tarvitaan käyttäjän nimi, käyttäjätunnus sekä salasana. Näistä käyttäjätunnuksen on oltava uniikki ja jokaisen pituuden on oltava vähintään 3 merkkiä. Kun kaikki tarvittavat tiedot ovat kunnossa, uusi käyttäjä luodaan `Create` napilla.

## Etusivu (My page)
Varsinaiselle etusivulle (My page) pääsee kirjautumalla sovellukseen. Peruskäyttäjä voi tarkistaa sivulta projektit, joihin on ilmoittaunut. Projektipäälikkö puolestaan voi tarkistaa kaikki omien kirjaamiensa projektit. Sekä peruskäyttäjä että projektipäälikkö voi päästä projektin omalle sivulleen painaamalla projektin otsikkoa.

Lisäksi projektipäälikön etusivulta voi päästä tarkistamaan kyseiseen projektiin liittyvää dataa `Data` painikkeen kautta.

## Projektin luominen (MASTER)
Tämä on projektipäälikölle rajattu toiminto. Peruskäyttäjällä ei ole oikeutta luomaan uutta projektia. Projekin luomissivulle pääsee painaamalla navigaatiopalkista painiketta `Create a project`.

## Projektien listaus
Navigaatiopalkissa olevan painikkeen `List projects` kautta päästään sivulle, jossa on listattuna kaikki sovellukseen kirjatut projektit. Projektin otsikosta päästään kyseisen projektin sivulle, josta löytyy kaikki projektiin liittyvät tiedot, muun muuassa projektipäälikkö, projektin kuvaukset, `view`-painike, jolla pääsee projektiin kirjattujen tehtävien listaukselle, sekä `details`-painikkeen kautta päästään data-sivulle, jossa on listattuna kaikki projektiin liittyvää dataa.

## Tehtävien listaus projektikohtaisesti
Yllä kuvatun `view`-painikkeen painattuaan käyttäjä pääsee kyseisen projektin tehtävien listaukselle. Olemassa olevien tehtävien lisäksi peruskäyttäjä voi luoda uuden tehtävän tai tarkistaa oman kirjatut tehtävänsä. 

Projektipäälikkö puolestaan pystyy tarkistamaan olemassa olevia tehtäviä, muttei pysty luomaan uutta tehtävää.

## Uuden tehtävän kirjaaminen
Tämä toiminto onnistuu täyttämällä tehtävän luomislomakkeen, johon on kirjattava tehtävän nimi, kuvaukset sekä arvioitu aika tunteina.

## Yksittäisen tehtävän tarkastelu
Yksittäisen tehtävän sivulle pääsee painaamalla tehtävien listauksessa olevaa `view`-painiketta. Sivulla on listattunna kaikki tehtävään liittyvät tiedot. Jos tehtävän omistaja on sama kuin kirjautuneena oleva käyttäjä, sivulla näkyvät myös tehtävän poistonappi sekä lomake todellisen käytetyn ajan kirjaamiseen, jos tehtävä ei ole vielä valmis. Toisaalta jos tehtävän omistaja ei ole kirjautuneena oleva käyttäjä, käyttäjällä ei ole muokkausoikeuksia.

## Tehtävien datan selaus projektikohtaisesti
Tehtävien data löytyy tehtävien listauksen sivun `My tasks`-painikkeen takaa. Sivulla voi löytyä mm. projektin nimi, tehtävien omistaja (Participant), arvioidun ajan summa sekä käytetyn ajan summa kaikista tehtävistä. Lisäksi  tehtävät on listattuna tarkistettavaksi. `Task details`-sarakkeen takaa taas löytyy yksittäisen tehtävän tietoja.

Sivu näkyy sekä projektipäälikölle että tehtävien omistajalle, muttei muille projektin osallisujille.

## Projektin datan selaus projektipäälikkönä
Projektipäälikkönä datan sivulle voi päästä joko My page-sivulta tai projektin sivulta. Projektipäälikölle on listattuna projektiin käytetyn ajan summa sekä arvioidun ajan summa. Niitä voi myös tarkistaa yhden viikon ajan antamalla aloituspäivän kyseiselle kentälle. Projektipääliköllä on myös mahdollisuus tarkastaa jokaisen osallistjan kirjaamien tehtävien määrää. Tehtävien yksityiskohtia tarkastetaan Details-sarakkeessa sijaitsevasta  `view`-painikkeesta. Samalla osallistujan voi poistaa `Remove`-painikkeella.

## Projektin datan selaus peruskäyttäjänä
Peruskäyttäjä voi selata dataa niihin projkteihin liittyen, joihin itse on osallistunut. Kyseiselle sivulle pääsee projektin yksityissivulta, jossa on painike nimeltään `details`. Peruskäyttäjälle näyttää samat datan sisällöt kuin projektipäälikölle paitsi listaa, jossa on jokaisen osallistjan kirjaamien tehtävien määrä. Kyseisin listan selaus on rajattu projektipäälikölle.