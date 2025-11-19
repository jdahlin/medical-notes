
## Polaritet
Förekomsten av polära respektive opolära sidokedjor i ett protein har en avgörande inverkan på proteinets struktur. Förklara innebörden av begreppet polaritet, hur proteinstrukturen påverkas av sidokedjornas polaritet och varför just polaritet har en så avgörande roll för proteinstrukturen.  

Polaritet innebär att en kemisk grupp har en ojämn fördelning av elektroner, vilket ger partiella laddningar och möjlighet till vätebindningar. Polära sidokedjor interagerar gärna med vatten och hamnar därför oftast på proteinets yta, där de stabiliserar strukturen genom vätebindningar och joninteraktioner. Opolära sidokedjor är hydrofoba och packas i proteinets inre, vilket driver den grundläggande veckningen genom den hydrofoba effekten. Polaritet är avgörande eftersom hela proteinets 3D-struktur bestäms av hur sidokedjorna minimerar energin i en vattenmiljö, och små förändringar i polaritet kan dramatiskt ändra konformationen.

### AlphaFold
Sekundärstrukturen hos proteiner är svår att förutsäga från primärsekvensen av aminosyrorna. Redogör för varför det är så och hur programmet Alphafold, vars skapare tilldelats Nobelpriset i kemi 2024, ändå med stor säkerhet kan förutsäga ett proteins tredimensionella struktur.  

Sekundärstruktur är svår att förutsäga från primärsekvensen eftersom varje aminosyras beteende beror på hela den tredimensionella miljön: steriska kollisioner, polaritet, vätebindningar, laddning, lösningsmedel och interaktioner med avlägsna delar av kedjan. Lokala regler räcker därför inte för att bestämma helix eller β-flak. Alphafold lyckas genom att utnyttja enorma mängder evolutionär information från homologer och analyserar bevarande, ko-variation och sannolika avstånd mellan rester. Med dessa mönster beräknar det energimässigt mest sannolika 3D-arrangemanget och förutsäger strukturen med mycket hög precision.
### Proteinanalys
Beskriv tre metoder som kan användas för att rena fram ett protein från lyserade celler och förklara vilken proteinegenskap som används för respektive metod.

**Jonbyteskromatografi** bygger helt på att olika proteiner har olika nettoladdning vid ett givet pH. Kolonnen är packad med ett resin som antingen är negativt laddat (anionbytare) eller positivt laddat (katjonbytare). Proteiner med motsatt laddning binder och hålls kvar, medan andra sköljs bort. Eluering sker genom att höja **saltkoncentrationen**, vilket konkurrerar ut interaktionen, eller genom att ändra **pH** så att proteinets laddning ändras och det släpper från resinet. Fördelen är hög kapacitet och att man kan separera proteiner som skiljer sig bara lite i laddning.

**Gelfiltrering / size-exclusion-kromatografi** separerar proteiner efter **storlek och form**. Kolonnen består av kulor med porer av definierad diameter. **Stora proteiner kan inte gå in i porerna** och passerar därför snabbt genom kolonnen och elueras först. **Mindre proteiner diffunderar in i porerna**, vilket bromsar dem, så de kommer ut senare. Det är en mild metod som inte kräver bindning eller förändring av proteinets struktur, vilket är idealiskt för proteiner som måste renas i aktiv form. Den ger också en bra uppskattning av proteinets storlek i lösning.

**Elektrofores**, framför allt **SDS-PAGE**, utnyttjar både **laddning, storlek och friktion** men gör dem jämförbara genom att denaturera proteinet. SDS binder längs polypeptidkedjan och ger den en **uniform negativ laddning** i proportion till dess längd. Detta gör att vandringshastigheten i gelen styrs nästan uteslutande av molekylens **storlek**. Proteinerna tappar sin 3D-struktur eftersom SDS och värme denaturerar dem. Om man även tillsätter ett **reduktionsmedel** (t.ex. β-ME eller DTT) bryts **disulfidbryggor**, vilket gör att multimerer och subenheter separeras.


### Hemoglobin
En allvarlig komplikation till bl.a. Covid-19 är så kallad Acute Respiratory Distress  Syndrome (ARDS), vilket ger en gravt sviktande lungfunktion orsakad av inflammation och  
vätskeansamling (ödem) i alveolerna. Ödemet leder till att mindre syre når blodet och att mindre koldioxid lämnar blodet. Beskriv hur den minskade mängden syre och den ökade mängden koldioxid påverkar hemoglobinets struktur och funktion.  

Mindre O₂ gör att hemoglobin stabiliseras i **T-state** (tensed), den låga-affinitetsformen → svårare att binda syre. Ökad CO₂ och därmed högre H⁺ (lägre pH) protonerar sidokedjor i Hb och skapar **saltbryggor** som ytterligare stabiliserar T-state (Bohr-effekten). CO₂ binder dessutom **karbamater** till N-terminalerna i Hb och sänker affiniteten ytterligare.
Resultatet är **högerförskjuten dissociationskurva**, lägre O₂-bindning och snabbare O₂-släpp – men vid ARDS räcker inte detta för att kompensera för den låga syrgaskoncentrationen.

### Blodgrupper
En lyckad transfusion av blod från en individ till en annan är beroende av att individerna har kompatibla blodgrupper. Om blodgrupperna inte är kompatibla kan en livshotande reaktion utlösas. Redogör för reaktionen för molekylär nivå.  

Vid inkompatibel blodtransfusion känns mottagarens antikroppar igen donatorns erytrocytantigen (t.ex. A- eller B-antigen) som främmande. Antikropparna binder direkt till antigenen på erytrocyterna och bildar stora immunkomplex. Detta leder till **agglutination** (klumpning) och aktivering av **komplementsystemet**, som skapar porer i cellmembranet och orsakar **intravaskulär hemolys**. Frisatta hemoglobinfragment och komplementaktiverade mediatorer utlöser kraftig inflammation, kärlskada, koagulationsaktivering och kan snabbt leda till chock, njursvikt och cirkulationskollaps.
### Enzymer
Redogör för fördelen med att många enzymer har Km-värden i närheten av de substratkoncentrationer som finns i deras omgivning.  

När ett enzyms Km ligger nära den faktiska substratkoncentrationen fungerar enzymet i det mest känsliga området av Michaelis-Menten-kurvan. Det innebär att små förändringar i substratnivåer direkt ger tydliga förändringar i hastigheten, vilket gör enzymet finreglerbart och responsivt. Enzymet arbetar varken mättat eller ineffektivt, utan i ett dynamiskt intervall där cellen snabbt kan anpassa metabolismen efter behov. Detta gör att enzymaktivitet kan styras av tillgången på substrat utan att kräva stora mängder enzym eller komplex reglering.
### Kofaktorer
Kofaktorer bundna till proteiner är viktiga för att möjliggöra vissa kemiska reaktioner och därmed utöka repertoaren av reaktioner de kan utföra. Redogör för vad en kofaktor är och hur  kofaktorerna ... kan hjälpa enzymer att uppnå effektivitet i de reaktioner de katalyserar.  

Kofaktorer är små icke-proteinkomponenter som ett enzym behöver för att katalysera reaktioner som aminosyror själva inte klarar av. De kan vara **metalljoner** (t.ex. Zn²⁺, Mg²⁺, Fe²⁺) eller **organiska molekyler** som ofta kallas **coenzymer** (t.ex. NAD⁺, FAD, CoA, TPP, biotin). Kofaktorer kan bära elektroner, protoner eller kemiska grupper, stabilisera övergångstillstånd eller skapa reaktiva intermediärer. Genom att tillföra nya kemiska egenskaper – redoxförmåga, gruppöverföring, syra–bas-katalys eller strukturell stabilisering – ökar de både reaktionshastighet och specificitet och gör att enzymet kan utföra reaktioner som annars vore omöjliga.
### Metanol
Förklara hur förtäring av metanol kan ge svåra förgiftningsskador samt hur etanol kan  förhindra förgiftningen.

Metanol i sig är relativt ofarligt, men i levern omvandlar **alkoholdehydrogenas (ADH)** det till **formaldehyd** och vidare till **myrsyra**, vilket orsakar **metabol acidos**, synnervsskada och kan leda till blindhet och död. Etanol fungerar som behandling eftersom ADH har **mycket högre affinitet för etanol än metanol**. När etanol ges konkurrerar det ut metanol på enzymet, vilket stoppar bildningen av de toxiska metaboliterna. Metanol utsöndras då oförändrat och myrsyran kan metaboliseras eller buffras.
