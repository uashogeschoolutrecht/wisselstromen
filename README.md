# Wisselstromen
Project gestart vanuit de DDHU community voor Data Analyse, met als doel om Python kennis in de praktijk te brengen. 
### Projectleden
Carlijn van Heuveln, Gerwin Hendriks, Harald Breshamer en Fraukje Coopmans. 
test3
## Doel van dit project 
We zijn geinspireerd geraakt door het R package `wisselstroom` (https://github.com/ed2c/wisselstroom) ontwikkeld door Fontys waarmee uit het DUO bekostigingsbestand inzichten rondom de studenten wisselstromen gegenereerd kunnen worden. In dit project zouden we graag het aantal in- en uitgaande studenten (wisselstromen) bij de HU bepalen op basis van het DUO bekostigingsbestand, en dit in Python. 

## Project stappen
De volgende stappen hebben wij uitgevoerd:
- Anonimiseren van het HU DUO bekostigingsbestand (geen BSN)
- Draaien van de al bestaande R demo wisselstromen (zie ook [wisselstroom_demo repo](https://github.com/ed2c/wisselstroom_demo)) met het geanonimiseerde HU bekostigingsbestand

## Bekostigingsbestand
Het bestand bevat de volgende recordsoorten:
VLP = Voorlooprecord  
BLB = Bekostigingsloopbaan student  
BRD = Bekostigingsresultaat deelname  
BRR = Bekostigingsresultaat resultaat  
SLR = Sluitrecord

Zie pagina 164 en verder van [Bijlage 8 van de Programma van Eisen Hoger Onderwijs, DUO](https://duo.nl/zakelijk/images/programma-van-eisen-hoger-onderwijs.pdf). Hieronder volgen twee relevante onderdelen van de definites, namelijk sectie 17.5 en 17.6. 

### Sectie 17.5: Formaat
- Een voorlooprecord (**VLP**);
- Setjes van alle records met de bekostiging van de betrokken persoon. De persoon wordt opgenomen indien hij minimaal één bekostigingsresultaat voor een
deelname of resultaat heeft bij de betrokken BRIN.
    - Nul of één **BLB**-record:  
    - Nul, één of meer **BRD**-records; Dit zijn alle bekostigingsresultaten van in het bekostigingsjaar beoordeelde deelnames. Daarnaast worden er
deelnames geselecteerd, die buiten de beoordeling vallen. Deze krijgen de status MV, om zo alle inschrijvingen van de betreffende persoon, die geldig
zijn in de periode 2 oktober van het bekostigingsjaar - 3 tot en met 1 oktober van het bekostigingsjaar - 2 worden, in het bestand op te nemen.
Dit kunnen ook bekostigingsresultaten bij andere instellingen zijn.  
    - Nul, één of meer **BRR**-records; Dit zijn alle bekostigingsresultaten van in het bekostigingsjaar beoordeelde resultaten. Dit kunnen ook
bekostigingsresultaten bij andere instellingen zijn. 
    - Voor een persoon zal er altijd op zijn minst één BRD- of één BRR-recordzijn;  
    - De records die betrekking hebben op dezelfde persoon, hebben alle hetzelfde burgerservice- en/of onderwijsnummer.  
- Een sluitrecord met aantal BLB, BRD en BRR-records (**SLR**);

De velden van een record worden gescheiden door een pipe-teken (|). Het eerste veld
van een record geeft altijd de recordsoort aan.

De BLB-records zijn oplopend gesorteerd op burgerservicenummer. Als er geen
burgerservicenummer is dan oplopend op onderwijsnummer, waarbij records met alleen
een onderwijsnummer achteraan staan.

### 17.6 Datumformaat
Datumvelden zijn in het formaat JJJJMMDD; Het betreft dus een numeriek veld van 8 positite slang. In de onderstaande beschrijving wordt dit in de kolom 'Formaat' aangegeven als 'Datum 8 (jjjjmmdd)'