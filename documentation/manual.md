# Käyttöohjeet

## Kirjautuminen
Projektien listausta lukuun ottamatt kaikki muut toiminnallisuudet vaativat kirjautumista. Painaamalla pääsivun oikeakulmasta nappia `Sign in` käyttäjä voi kirjautua sovellukseen joko projektipäälikkönä tai peruskäyttäjänä vastaavalla käyttäjätunnuksella ja salasanalla. Sovellukseen on määritelty kolme käyttäjätiliä sovelluksen testausta varten. Nämä tilit ovat:

|Rooli  | Käyttäjätunnus | Salasana  |
|:-----:|:--------------:|:---------:|
|BASIC  |    test        | secret    |
|BASIC  |    test2       | secret2   |
|MASTER |    master      | admin     |

Näistä kaksi ensimmäistä ovat perukäyttäjätiliä ja viimeinen projektipäälikkötili.

## Rekisteröityminen
Sovellukseen on tehty erillinen sivu rekisteröinnille, eli uuden käyttäjän luomiselle. Kirjautumattomana kyseiselle sivulle pääsee painaamalla oikeakulmasta nappia `Sign up`. Sieltä käyttäjä voi luoda itselleen peruskäyttäjätilin tai projektipäälikkötilin valitsemalla `basic account` tai `master account`. 

Molempien roolien rekisteröitymiseen tarvitaan käyttäjän nimi, käyttäjätunnus sekä salasana. Näistä käyttäjätunnuksen on oltava uniikki ja jokaisen pituuden on oltava vähintään 3 merkkiä. Kun kaikki tarvittavat tiedot ovat kunnossa, uusi käyttäjä luodaan `Create` napilla.

## Etusivu (My page)
Etusivulle (My page) pääsee kirjautumalla sovellukseen. Peruskäyttäjä voi tarkistaa sivulta projektit, joihin on ilmoittaunut. Projektipäälikkö puolestaan voi tarkistaa kaikki omien kirjaamiensa projektit. Sekä peruskäyttäjä että projektipäälikkö voi päästä projektin omalle sivulleen painaamalla projektin otsikkoa.

Lisäksi projektipäälikön etusivulta voi päästä tarkistamaan kyseiseen projektiin liittyvää dataa `Data` painikkeen kautta.

## Projektin luominen
Tämä on projektipäälikölle rajattu toiminto. Peruskäyttäjällä ei ole oikeutta luomaan uutta projektia. Projekin luomissivulle pääsee painaamalla navigaatiopalkista painiketta `Create a project`.

## Projektien listaus
Navigaatiopalkissa olevan painikkeen `List projects` kautta päästään sivulle, jossa on listattuna kaikki sovellukseen kirjatut projektit. Projektin otsikosta päästään kyseisen projektin sivulle, josta löytyy kaikki projektiin liittyvät tiedot, muun muuassa projektipäälikkö, projektin kuvaukset, `view`-painike jolla pääsee projektiin kirjattujen tehtävien listaukselle.

Projektipääliköllä on näiden lisäksi vielä mahdollisuus päästä data-sivulle `details`-painikkeen kautta. Data-sivulla on listattuna kaikki projektiin liittyvää dataa.

## Tehtävien listaus projektikohtaisesti
Yllä kuvatun `view`-painikkeen painattuaan käyttäjä pääsee kyseisen projektin tehtävien listaukselle. Olemassa olevien tehtävien lisäksi peruskäyttäjä voi luoda uuden tehtävän tai tarkistaa omien kirattujen tehtävänsä. 

Projektipäälikkö puolestaan pystyy tarkistamaan olemassa olevia tehtäviä, muttei pysty luomaan uutta tehtävää.

## Uuden tehtävän kirjaaminen
Tämä toiminto onnistuu täyttämällä tehtävän luomislomakkeen, johon on kirjattava tehtävän nimi, kuvaukset sekä arvioitu aika tunteina.

## Yksittäisen tehtävän tarkastelu
Yksittäisen tehtävän sivulle pääsee painaamalla tehtävien listauksessa olevaa `view`-painiketta. Sivulla on listattunna kaikki tehtävään liittyvät tiedot. Jos tehtävän omistaja on sama kuin kirjautuneena oleva käyttäjä, sivulla näkyvät myös tehtävän poistonappi ja lomake todellisen käytetyn ajan kirjaamiseen, jos tehtävä ei ole vielä valmis. Toisaalta jos tehtävän omistaja ei ole kirjautuneena oleva käyttäjä, käyttäjällä ei ole muokkausoikeuksia.

## My tasks-sivu


## Projektin datan selaus projektipäälikkönä