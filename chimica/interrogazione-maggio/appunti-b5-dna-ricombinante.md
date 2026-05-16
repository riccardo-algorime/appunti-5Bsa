# Capitolo B5 - Le tecnologie del DNA ricombinante

> Fonte: trascrizione-B5-Scienze.txt

## Quadro generale del capitolo

Il capitolo riguarda le **tecnologie del DNA ricombinante**, cioe l'insieme delle tecniche che permettono di modificare, copiare, analizzare e usare il DNA in laboratorio. I temi principali sono:

- il **DNA ricombinante**, con clonaggio genico, enzimi di restrizione, DNA ligasi, vettori plasmidici e virali, PCR, elettroforesi e librerie di DNA;
- le **proteine ricombinanti**, prodotte a partire da geni clonati in vettori di espressione;
- il **sequenziamento del DNA**, dal metodo di Sanger ai metodi NGS e di terza generazione;
- la **clonazione** e l'**editing genomico**, con trasferimento nucleare, animali transgenici, topi knock out e CRISPR/Cas9;
- le **scienze omiche**, cioe genomica, trascrittomica, proteomica, metabolomica, interattomica e analisi multi-omiche.

> **Immagine da guardare nel PDF, pag. 2:** la mappa concettuale riassume tutto il capitolo e aiuta a collegare le tecniche: prima si manipola il DNA, poi lo si usa per clonare geni, produrre proteine, sequenziare genomi, modificare organismi e studiare sistemi biologici complessi.

## DNA ricombinante e ingegneria genetica

L'inizio dell'era del **DNA ricombinante** viene fatto risalire al **1973**, quando i genetisti americani **Stanley Cohen** e **Herbert Boyer** trasferirono per la prima volta in un batterio di *Escherichia coli* una molecola di DNA contenente geni per la resistenza a **due antibiotici**, ciascuno proveniente da un ceppo batterico diverso. Il batterio ottenuto era in grado di resistere a entrambi gli antibiotici e quindi mostrava un **fenotipo ibrido**.

Un **DNA ricombinante** e una molecola di DNA che contiene informazione genetica proveniente da **due o piu organismi differenti**. Questa definizione e centrale: non si tratta semplicemente di DNA copiato, ma di DNA costruito combinando frammenti genetici di origine diversa.

L'**ingegneria genetica**, detta anche **tecnologia del DNA ricombinante**, e l'insieme delle tecniche usate per ottenere e manipolare DNA ricombinante. Il principio e che, modificando in laboratorio il **genotipo** di un organismo, si puo alterare il suo **fenotipo** in modo mirato. Questo e diverso da cio che avviene spontaneamente in natura, dove le modificazioni genetiche sono casuali. L'evoluzione dell'ingegneria genetica ha permesso la nascita delle **biotecnologie moderne**.

Nella maggior parte delle applicazioni biotecnologiche, una delle prime operazioni e il **clonaggio genico**, cioe la produzione di numerose copie di un **gene di interesse** usando le tecniche del DNA ricombinante. Per clonare un gene serve una vera e propria "cassetta degli attrezzi":

- il **gene** da clonare;
- gli **enzimi** capaci di tagliare e cucire il DNA;
- un **vettore di clonaggio**, come plasmidi batterici, fagi o virus.

> **Immagine da guardare nel PDF, pag. 3:** le fotografie di Herbert Boyer e Stanley Cohen sono importanti per ricordare il contesto storico: nel 1973 il loro esperimento con *E. coli* resistente a due antibiotici segna la nascita pratica del DNA ricombinante.

## Enzimi di restrizione, DNA ligasi e vettori di clonaggio

Per creare una molecola di DNA ricombinante servono due tipi principali di enzimi: enzimi per il **taglio** e enzimi per la **cucitura** del DNA.

Gli **enzimi di restrizione** sono **endonucleasi** che rompono in modo preciso il **legame fosfodiestere** tra due nucleotidi adiacenti. Tagliano il DNA solo in corrispondenza di sequenze specifiche, chiamate **siti di restrizione**. Il DNA tagliato puo essere sia quello della cellula da cui si estrae il gene di interesse, sia quello del vettore di clonaggio in cui il gene dovra essere inserito.

Esempi importanti:

| Enzima | Origine | Tipo di taglio |
|---|---|---|
| **EcoRI** | scoperto in *Escherichia coli* | taglia formando **estremita coesive** |
| **SmaI** | scoperto in *Serratia marcescens* | genera **estremita piatte** |

La **DNA ligasi** svolge il lavoro opposto: catalizza la **formazione del legame fosfodiestere** tra nucleotidi adiacenti. In pratica, dopo che un frammento di DNA e stato tagliato e inserito in un vettore, la DNA ligasi permette di "cucire" stabilmente le molecole.

Il **vettore di clonaggio** e una molecola di DNA ricombinante capace di entrare in una cellula e replicarsi, generando molte copie di se stessa. I vettori piu usati sono i **plasmidi**, piccole molecole circolari di DNA presenti nei batteri.

Un esempio e il **vettore plasmidico pBSK+**, che contiene come **marcatore di selezione** il gene *ampR*. Questo gene conferisce resistenza all'antibiotico **ampicillina**: se i batteri crescono in presenza di ampicillina, si possono selezionare quelli che hanno acquisito il plasmide.

> **Immagine da guardare nel PDF, pag. 4:** lo schema del batterio con cromosoma batterico e plasmidi chiarisce perche i plasmidi sono utili come vettori: sono molecole di DNA separate, piccole, replicabili e manipolabili.

### Elettroforesi su gel di agarosio

L'**elettroforesi su gel di agarosio** permette di separare frammenti di DNA in base alle loro dimensioni. Le molecole di DNA sono cariche negativamente a causa dei gruppi fosfato nello scheletro del DNA. Quando vengono sottoposte a un campo elettrico, migrano verso il **polo positivo**.

Il gel di agarosio funziona come un **setaccio**:

- i frammenti piu corti passano piu facilmente attraverso il gel e quindi migrano piu velocemente;
- i frammenti piu lunghi incontrano piu resistenza e migrano piu lentamente.

Questa tecnica permette di visualizzare bande di DNA e confrontare la lunghezza dei frammenti. Nella trascrizione e indicato anche un riferimento al laboratorio di elettroforesi su gel: `https://youtu.be/uKwSxPgqS3U`.

> **Immagine da guardare nel PDF, pag. 4:** la camera di elettroforesi con pozzetti, catodo, anodo e bande su gel e fondamentale per capire il verso di migrazione: il DNA, essendo negativo, va verso l'anodo positivo; i frammenti piccoli corrono piu avanti.

## Vettori virali, fagi e retrovirus

Oltre ai plasmidi batterici, come vettori si possono usare anche **genomi virali modificati**. I primi vettori virali furono costruiti a partire dal **batteriofago lambda** (`lambda`), inserendo nel suo genoma il gene da clonare.

Il vantaggio dei vettori virali rispetto ai plasmidi e che possono contenere **frammenti di DNA piu lunghi**. Per l'uomo sono stati utilizzati anche vettori derivati da:

- **adenovirus**, virus a DNA;
- **retrovirus**, virus a RNA.

I **retrovirus** sono particolarmente importanti perche possono integrarsi nel genoma della cellula ospite sotto forma di **provirus**. Per questo sono utili quando si vuole ottenere l'espressione stabile e duratura di una proteina, come in alcuni protocolli di **terapia genica** per curare malattie ereditarie.

Un retrovirus usa l'enzima **trascrittasi inversa** per convertire il proprio genoma da RNA a DNA durante il ciclo di replicazione virale. Questo passaggio RNA -> DNA e essenziale anche per capire il principio della RT-PCR, trattata piu avanti.

> **Immagine da guardare nel PDF, pag. 5:** gli schemi di adenovirus e retrovirus mostrano la differenza tra virus a DNA e virus a RNA. Nel retrovirus sono segnalati proteasi, envelope, nucleocapside, trascrittasi inversa, integrasi, capside, matrice e i due filamenti di RNA.

Video del libro di testo indicati nella trascrizione:

- "Come si fa il clonaggio molecolare?"
- "Come si coltivano i batteri in laboratorio."

## Librerie di DNA e PCR

Una **libreria di DNA** e una collezione di cloni, ciascuno contenente un diverso **inserto di DNA**. Per costruirla:

1. si taglia il DNA di partenza con un enzima di restrizione;
2. si inseriscono i frammenti ottenuti in vettori di clonaggio;
3. ogni plasmide incorpora un solo frammento di DNA;
4. si ottiene una popolazione di plasmidi che contiene tutti i frammenti del genoma di partenza;
5. si trasformano cellule batteriche usando l'intera collezione di plasmidi;
6. ogni cellula trasformata contiene un singolo vettore con il relativo frammento di DNA;
7. ogni cellula genera un clone cellulare che conserva quel singolo frammento.

La **PCR** (*Polymerase Chain Reaction*, reazione a catena della polimerasi) e un sistema automatizzato per isolare e amplificare DNA in provetta, cioe **in vitro**. Lo strumento usato e il **termociclatore**, che permette di variare automaticamente la temperatura.

La PCR si basa sulla capacita della **DNA polimerasi** di sintetizzare un nuovo filamento di DNA a partire da un filamento stampo. La tecnica fu ideata nel **1983** da **Kary Mullis**, che ottenne per questo il premio Nobel per la Chimica nel **1993**.

I reagenti necessari sono:

- il **DNA stampo** da amplificare;
- l'enzima **Taq polimerasi**, una DNA polimerasi termoresistente derivata da *Thermus aquaticus*, organismo associato alle alte temperature del parco nazionale di Yellowstone;
- una coppia di **primer**, cioe inneschi necessari alla Taq polimerasi;
- i quattro **nucleotidi trifosfato**.

> **Immagine da guardare nel PDF, pag. 6:** la fotografia del termociclatore e di Kary Mullis aiuta a collegare la tecnica sia allo strumento pratico sia al suo inventore.

### Le fasi della PCR

La PCR e formata da un ciclo di tre passaggi:

1. **Denaturazione**: la miscela viene riscaldata a circa **95 °C** e i due filamenti del DNA stampo si separano.
2. **Appaiamento** o **annealing**: la temperatura viene abbassata a **50-65 °C** e i primer si appaiano alle sequenze complementari sui filamenti stampo.
3. **Allungamento**: la temperatura viene portata a **68-72 °C** e la **Taq polimerasi** sintetizza il filamento complementare.

Il ciclo viene ripetuto molte volte, di solito circa **30 cicli**. Poiche a ogni ciclo il numero di molecole raddoppia, partendo da una singola copia si arriva a:

$$
2^{30} > 1\,000\,000\,000
$$

cioe piu di **un miliardo di copie**.

Video indicati nella trascrizione:

- PCR: `https://youtu.be/QPOMrRUOMaY`
- Amplificazione DNA PCR: `https://youtu.be/CQ0LCCi7AVY`

> **Immagine da guardare nel PDF, pag. 7:** il diagramma della PCR e molto importante per ripetere oralmente: mostra denaturazione, annealing, allungamento e il raddoppio progressivo `1 -> 2 -> 4 -> 8 -> 16...`.

### Ripasso Active Learning: DNA ricombinante e PCR

Domande da saper spiegare:

- Quali enzimi sono utili per manipolare sequenze di DNA?
- Quali elementi non devono mancare in un vettore di clonaggio?
- Che cos'e la PCR?

Scelte corrette dalla sezione "Scegli le parole":

- Un gene che codifica per la resistenza a un **antibiotico** puo essere usato come **marcatore di selezione** in un plasmide.
- **EcoRI** **taglia** frammenti di DNA.

Attivita proposta:

- Il premio Nobel per la medicina del **1978** fu conferito a **W. Arber**, **D. Nathans** e **H. Smith** per le ricerche sugli enzimi di restrizione. La consegna chiede di illustrare in una presentazione i principali risultati dei loro studi.
- Nella trascrizione compare anche il richiamo: **"DATI IN AGENDA Dna, quanto mi costi?"**.

## Proteine ricombinanti, mRNA e RT-PCR

Le **proteine ricombinanti** sono proteine ottenute dall'espressione di un gene clonato all'interno di un **vettore**.

Quando la sequenza codificante per la proteina di interesse proviene da un organismo eucariotico, e preferibile partire dall'**mRNA** invece che dal DNA genomico. Il motivo e che gli mRNA maturi contengono solo le parti effettivamente codificanti: sono stati privati degli **introni** e conservano gli **esoni**.

Per isolare i trascritti si separano gli mRNA dalle altre componenti cellulari usando sistemi che selezionano molecole con **coda di poli-A**, una caratteristica dei trascritti maturi. In questo modo si ottiene una collezione di tutti gli mRNA della cellula, tra cui anche quello della proteina di interesse.

Il problema successivo e recuperare il trascritto desiderato tra migliaia di altri. Si usa la **RT-PCR** (*Reverse Transcriptase Chain Reaction*), tecnica sfruttata per studiare l'espressione genica. La RT-PCR amplifica una sequenza codificante di interesse partendo da un insieme di mRNA isolati da un campione biologico.

La RT-PCR e una variante della PCR e consiste nella sintesi di una molecola di DNA a partire da uno stampo di RNA. La molecola prodotta tramite retrotrascrizione e chiamata **cDNA**, cioe **DNA complementare**. Nella trascrizione viene indicato come DNA complementare a singolo filamento; poi il prodotto puo essere amplificato con PCR fino a ottenere molte copie della sequenza codificante per la proteina di interesse.

Schema logico:

```text
mRNA maturo con coda poli-A
-> trascrittasi inversa + oligo-dT
-> primo filamento di cDNA
-> PCR
-> molte copie della sequenza codificante
```

Il prodotto della retrotrascrizione dell'RNA puo essere:

- amplificato con una PCR classica;
- quantificato con **real-time PCR**, detta anche **PCR quantitativa** o **qPCR**.

Bisogna distinguere bene:

| Tecnica | Significato | Funzione principale |
|---|---|---|
| **RT-PCR** | Reverse Transcriptase PCR | converte RNA in cDNA e poi amplifica |
| **qPCR / real-time PCR** | quantitative PCR | amplifica e quantifica DNA simultaneamente |

La qPCR e simile alla PCR ma non va confusa con la RT-PCR.

> **Immagine da guardare nel PDF, pag. 9:** lo schema della RT-PCR e utile per memorizzare la successione: cellule -> mRNA isolato -> trascrittasi inversa + oligo-dT -> primo filamento di cDNA -> PCR -> DNA a doppio filamento amplificato.

## Vettori di espressione e produzione di proteine ricombinanti

Dopo avere ottenuto la sequenza codificante, si usano enzimi di restrizione e DNA ligasi per inserirla in un **vettore di espressione**. Un vettore di espressione e un plasmide che, una volta trasferito in cellule batteriche o eucariotiche, permette di sintetizzare la proteina codificata dal gene.

Nel caso illustrato per *E. coli*, il plasmide contiene segnali necessari all'espressione:

- **P**, promotore;
- **R**, sito di legame al ribosoma;
- **T**, terminatore;
- un **sito unico di restrizione**, in cui inserire il gene esogeno.

Il gene esogeno viene inserito nel plasmide, poi il vettore entra in *E. coli* tramite trasformazione. Dentro la cellula, il DNA viene trascritto in mRNA e poi tradotto in **proteina ricombinante**. I batteri ricombinanti possono quindi essere selezionati e coltivati in **colture batteriche** dentro **bioreattori**.

> **Immagine da guardare nel PDF, pag. 10:** lo schema del vettore di espressione mostra in modo completo il percorso gene -> plasmide -> trasformazione di *E. coli* -> mRNA -> proteina ricombinante.

### Ripasso Active Learning: proteine ricombinanti

Domande da saper spiegare:

- Che cosa distingue la PCR convenzionale dalla RT-PCR?
- Per sintetizzare una proteina ricombinante, perche e preferibile clonare la sequenza del suo mRNA anziche quella del DNA?

Scelte corrette dalla sezione "Scegli le parole":

- Un filamento di RNA puo essere convertito in uno di **cDNA** dall'enzima **trascrittasi inversa**.
- Il primo farmaco ricombinante e stato **l'insulina**.

Attivita proposta:

- Prima dell'insulina ricombinante, i pazienti diabetici erano trattati con insulina di origine animale. La consegna chiede di documentarsi sulle difficolta di reperimento di insulina non umana e sui rischi legati al suo uso.

## Sequenziamento del DNA e metodo di Sanger

Il **sequenziamento del DNA** permette di stabilire il preciso ordine dei nucleotidi che formano una molecola di acido desossiribonucleico.

Il **metodo Sanger**, pronunciato "sangher", e detto anche **metodo dei terminatori di catena**. Anche se oggi esistono metodi piu innovativi, come quelli di seconda e terza generazione, il metodo di Sanger resta un punto di riferimento per la biologia molecolare.

Il metodo si basa su una reazione simile alla PCR, ma con differenze fondamentali:

- viene usato **un solo primer**;
- vengono aggiunti **dideossinucleotidi modificati** (**ddNTP**);
- i ddNTP agiscono da **terminatori di catena** perche sono privi del gruppo **3'-OH**, necessario per formare il legame fosfodiestere con il nucleotide successivo;
- i nucleotidi modificati sono marcati con **marcatori fluorescenti**, indispensabili per leggere il risultato.

Video indicato nella trascrizione:

- Sequenziamento del DNA: `https://youtu.be/ACeeNNxdtvM`

### Frederick Sanger

**Frederick Sanger** (1918-2013) e stato un chimico britannico. E l'unico britannico ad avere vinto due volte il premio Nobel per la Chimica:

- nel **1958**, per il lavoro sulla struttura delle proteine, in particolare dell'insulina;
- nel **1980**, per il contributo alla determinazione delle sequenze degli acidi nucleici.

Sanger lavoro al sequenziamento dell'insulina per dieci anni, dal **1944** al **1954**, determinando la sequenza dei **51 amminoacidi** delle due catene dell'insulina con un metodo da lui ideato. Il suo lavoro fu importantissimo perche permise poi di sequenziare anche proteine piu complesse, come:

- ribonucleasi pancreatica;
- enzima tripsina;
- emoglobina;
- mioglobina.

> **Immagine da guardare nel PDF, pag. 12:** le fotografie di Sanger aiutano a ricordare il collegamento tra sequenziamento delle proteine, insulina e sviluppo delle tecniche di sequenziamento degli acidi nucleici.

### Sequenziamento con terminazione di catena

Lo schema del metodo Sanger comprende sei passaggi:

1. Si isola il frammento di DNA da sequenziare, per esempio dal genoma di un batterio.
2. I frammenti vengono uniti ai reagenti necessari per sintetizzare i filamenti complementari e suddivisi in quattro provette. Ogni provetta contiene uno dei quattro ddNTP: **ddATP**, **ddCTP**, **ddTTP**, **ddGTP**.
3. In ogni provetta si genera una miscela di frammenti di lunghezza diversa, ma tutti terminanti con lo stesso nucleotide marcato.
4. I prodotti delle quattro reazioni vengono caricati nei pozzetti di un gel per l'analisi elettroforetica.
5. Leggendo dal frammento piu piccolo in basso verso quello piu grande in alto, si ricostruisce l'ordine con cui i nucleotidi sono stati incorporati.
6. La sequenza ottenuta e complementare a quella che si voleva sequenziare.

Nello schema e riportato un esempio:

- filamento stampo: `3' AACAGCCTTCAAGT 5'`;
- primer: `5' TTGT 3'`;
- risultato indicato come DNA sequenziato: `ACTTGAAGGCTGTT`.

> **Immagine da guardare nel PDF, pag. 13:** l'infografica dei sei passaggi e essenziale per capire che i ddNTP interrompono casualmente la sintesi in punti diversi, generando frammenti di lunghezze diverse che possono essere ordinati tramite elettroforesi.

## NGS, pirosequenziamento e tecniche di terza generazione

I metodi **NGS** (*Next Generation Sequencing*, sequenziamento di nuova generazione) si basano sul **sequenziamento massivo in parallelo** di molte molecole di DNA. Questo approccio permette di sequenziare anche interi genomi, riducendo tempi di analisi e costi.

Un esempio di tecnica NGS e il **pirosequenziamento**, un metodo enzimatico completamente automatizzato che permette il sequenziamento della catena complementare. Il pirosequenziamento sfrutta l'enzima **luciferasi**, quindi consente di leggere direttamente le sequenze senza ricorrere all'elettroforesi.

La tecnica prevede:

1. aggiunta ciclica dei quattro nucleotidi nel nuovo filamento;
2. emissione di un segnale **chemioluminescente** quando un nucleotide viene incorporato;
3. degradazione dei nucleotidi non incorporati;
4. ricostruzione della sequenza del DNA stampo.

Il pirosequenziamento fu usato nel **2007** per determinare la sequenza del genoma di **James Watson**.

Le tecniche di **terza generazione** sono considerate ancora piu promettenti. Un esempio e il **sequenziamento a nanopori**, che usa membrane e deduce la sequenza di un frammento di DNA osservando come cambia il **potenziale elettrico di membrana** quando i singoli nucleotidi attraversano un **nanoporo**.

Nel sequenziamento a nanopori, il filamento di DNA attraversa il nanoporo un nucleotide alla volta. Il potenziale di membrana si modifica in modo diverso a seconda del nucleotide che passa in quel momento, e da questa variazione si ricava la sequenza.

> **Immagine da guardare nel PDF, pag. 14:** la fotografia di James Watson serve come riferimento storico al sequenziamento del suo genoma nel 2007; sono importanti anche le figure citate del libro, fig. 26 e fig. 27 di pag. B177, per pirosequenziamento e nanopori.

### Ripasso Active Learning: sequenziamento

Domande da saper spiegare:

- Quali sono i reagenti necessari per il sequenziamento di Sanger?
- Quali sono i vantaggi del *Next Generation Sequencing*?
- Come funziona il pirosequenziamento?

Scelte corrette dalla sezione "Scegli le parole":

- I **ddNTP** sono **nucleotidi** privi del gruppo **3'-OH**.
- Il **pirosequenziamento** usa la **luciferasi**, che emette un segnale luminoso.

Attivita proposta:

- I sequenziatori a nanopori sono cosi piccoli da poter essere portati nello spazio. La consegna chiede di verificare se siano gia stati eseguiti sequenziamenti in orbita e quali possano essere le applicazioni future.

## Clonazione animale e trasferimento nucleare

La **clonazione** e la creazione di copie geneticamente identiche di un intero organismo. Una tecnica fondamentale e il **trasferimento nucleare**, usato per la clonazione della pecora **Dolly**. Questa tecnica ha segnato una svolta storica, ma viene descritta come poco efficiente e molto complessa.

La pecora Dolly era un clone della pecora **Finn Dorset**, con madre surrogata pecora **Scottish Blackface**. Nacque il **5 luglio 1996** presso il **Roslin Institute** dell'Universita di Edimburgo, grazie agli studi del team di **Ian Wilmut**.

Il trasferimento nucleare procede cosi:

1. si asporta il **nucleo** da una **cellula somatica** di un individuo;
2. si elimina il nucleo di un **oocita non fecondato** di un secondo individuo;
3. si inserisce il nucleo della cellula somatica nell'oocita enucleato, formando uno **pseudo-zigote**;
4. lo pseudo-zigote viene stimolato a dividersi in provetta e a generare un **embrione**;
5. l'embrione viene impiantato nell'utero di una **madre surrogata**;
6. si sviluppa un animale con lo stesso patrimonio genetico della cellula somatica iniziale.

Nel caso di Dolly, la resa fu molto bassa:

```text
434 oociti -> 29 embrioni -> 1 pecora
```

Questo dato dimostra concretamente perche il trasferimento nucleare viene definito poco efficiente.

Video indicato:

- Clonazione pecora Dolly: `https://youtu.be/XZqv49MLHNs`

> **Immagine da guardare nel PDF, pag. 16:** le foto di Ian Wilmut, Dolly e la madre surrogata aiutano a ricordare le tre identita biologiche coinvolte: donatrice del nucleo, donatrice dell'oocita e madre surrogata.

> **Immagine da guardare nel PDF, pag. 17:** lo schema del trasferimento nucleare e fondamentale per ripetere la tecnica: cellula mammaria Finn Dorset, oocita Scottish Blackface, scarica elettrica per fusione, 7 giorni di crescita in vitro, impianto nella madre surrogata e nascita di Dolly.

## Animali geneticamente modificati: transgenici e knock out

Gli **animali geneticamente modificati** sono strumenti importanti per la ricerca biomedica.

I **topi transgenici** sono topi geneticamente modificati in cui e stato inserito un gene normalmente assente nel genoma del topo. Sono fondamentali per costruire sistemi modello utili allo studio di malattie, soprattutto malattie genetiche umane. Gli esempi citati sono:

- **fibrosi cistica**;
- **malattia di Alzheimer**.

I topi transgenici servono anche per:

- analizzare risposte farmacologiche;
- disporre di sistemi efficaci per produrre proteine importanti dal punto di vista farmacologico e terapeutico;
- riprodurre il fenotipo di una malattia umana;
- comprendere meccanismi patogenetici;
- testare nuovi farmaci.

La tecnica per ottenere topi transgenici prevede:

1. prelievo di uno **zigote** da una femmina di topo donatrice;
2. inserimento del **transgene** nello zigote tramite **microiniezione** con un microago di vetro;
3. breve coltivazione dello zigote con transgene **in vitro**, per permettere alcune mitosi;
4. impianto nell'utero di una femmina di topo, che agisce da madre surrogata.

I **topi knock out** sono invece topi geneticamente modificati in cui e stato **inattivato uno specifico gene**. La tecnica descritta prevede l'inserimento nel gene di un **marcatore** che lo inattiva. Il gene inattivato viene integrato nel cromosoma del topo all'interno di una **cellula staminale**. Questa cellula viene poi trapiantata in una **blastocisti**, che formera successivamente un embrione.

| Tipo di topo | Modifica | Scopo principale |
|---|---|---|
| **Transgenico** | inserimento di un gene nuovo, normalmente assente | studiare effetti di un gene introdotto o creare modelli di malattia |
| **Knock out** | inattivazione di un gene specifico | capire che cosa succede quando quel gene non funziona |

> **Immagine da guardare nel PDF, pag. 18:** lo schema della microiniezione nello zigote spiega la generazione di topi transgenici; lo schema del vettore con marcatore e cellula staminale embrionale spiega invece il knock out.

## Manipolazione del genoma ed editing genomico

Molte tecniche di manipolazione del genoma si basano sul trasferimento di geni tra specie diverse, cioe di **transgeni**, tramite vettori virali. Il problema e che non sempre si puo prevedere dove il gene inserito andra a collocarsi. Questo puo causare **mutagenesi inserzionale**.

Un esempio: se il gene inserito interrompe una sequenza regolatrice, come un **promotore**, il gene regolato da quella sequenza puo non essere piu trascritto.

L'**editing genomico** permette di aggirare questi rischi perche consente di modificare in modo mirato specifiche sequenze geniche senza intaccare l'integrita del resto del genoma.

La svolta e arrivata nel **1993** con la scoperta delle sequenze **CRISPR**, acronimo di *Clustered Regularly Interspaced Short Palindromic Repeats*, tradotto nella trascrizione come **brevi sequenze ripetute e palindrome**.

Il sistema **CRISPR/Cas9** si basa sull'abbinamento tra:

- uno specifico **RNA guida**;
- l'**endonucleasi Cas9**.

L'RNA guida riconosce la sequenza bersaglio nel DNA genomico, mentre Cas9 taglia il DNA a doppio filamento in corrispondenza di quella sequenza. Dopo il taglio, puo avvenire l'editing, cioe la modifica della sequenza genica.

La tecnica CRISPR/Cas9 e stata inventata dalla chimica statunitense **Jennifer Doudna** e dalla biochimica, genetista e microbiologa francese **Emmanuelle Charpentier**. Nella trascrizione viene indicato che CRISPR/Cas9 e usata, per esempio, per generare topi knock out.

Dopo il taglio di Cas9, nello schema sono indicati due meccanismi di riparazione:

- **NHEJ** (*Non-Homologous End Joining*), che puo portare a **InDel**, cioe inserzioni o delezioni;
- **HR** (*Homologous Recombination*), che permette di inserire una nuova sequenza.

Video indicato:

- CRISPR/Cas9: `https://youtu.be/8jmNRLmHWPo`

> **Immagine da guardare nel PDF, pag. 19:** lo schema molecolare di CRISPR/Cas9 e essenziale: mostra Cas9, RNA guida, sequenza genomica corrispondente e i due esiti di riparazione NHEJ e HR. La foto di Doudna e Charpentier serve per collegare la tecnica alle scienziate che l'hanno sviluppata.

### Ripasso Active Learning: clonazione ed editing

Domande da saper spiegare:

- Come funziona la procedura di trasferimento nucleare?
- Che cos'e l'editing genomico?
- Che cos'e un topo knock out?
- Che cosa sono le sequenze CRISPR e dove sono state scoperte?

Scelte corrette dalla sezione "Scegli le parole":

- I topi **transgenici** sono topi in cui e stato inserito un nuovo gene mediante la tecnica di **microiniezione**.
- L'enzima **Cas9** e **un'endonucleasi** che taglia **il DNA**.

Attivita proposta:

- Nel **2007** **Mario R. Capecchi**, **Martin J. Evans** e **Oliver Smithies** hanno ricevuto il premio Nobel per la medicina per gli studi sui topi knock out. La consegna chiede di descrivere i principali risultati delle loro ricerche.

## Scienze omiche e salute: l'era della genomica

Le **scienze omiche** si basano su tecnologie ad alta resa, cioe capaci di analizzare grandi quantita di dati biologici, per studiare diversi sottoinsiemi di biomolecole cellulari.

Tra le piu sviluppate ci sono:

| Scienza omica | Oggetto di studio |
|---|---|
| **Genomica** | l'insieme dei geni presenti nel genoma di un organismo |
| **Trascrittomica** | tutte le molecole di RNA trascritte in una cellula |
| **Proteomica** | le proteine cellulari |
| **Metabolomica** | i metaboliti di una cellula e le loro interazioni metaboliche |

Queste discipline forniscono la base della **biologia dei sistemi**, che studia l'evoluzione e i cambiamenti dinamici degli organismi intesi come sistemi complessi.

### Genomica strutturale, comparativa e funzionale

La **genomica strutturale** mira a identificare la sequenza di un intero genoma e a descrivere l'organizzazione strutturale dei suoi geni. Grazie a questa disciplina e stato possibile sequenziare il genoma umano con il **Progetto Genoma Umano** e costruire mappe che descrivono la posizione dei geni nei singoli cromosomi.

La **genomica comparativa** identifica somiglianze tra genomi di organismi diversi. Questo permette di stimare il grado di **correlazione evolutiva** tra specie. La genomica comparativa si puo applicare anche ai virus ed e utile per capire dove e quando ha avuto origine un nuovo virus o per seguirne l'evoluzione nel corso di un'epidemia.

La **genomica funzionale** cerca di comprendere la funzione svolta da tutti i geni presenti nel genoma di un organismo.

### Trascrittomica, proteomica, metabolomica e interattomica

La **trascrittomica** studia il **trascrittoma**, cioe la collezione completa di tutte le molecole di RNA trascritte dal genoma in un dato momento, in un certo tipo di cellula o tessuto. Confrontare i **profili trascrizionali** puo aiutare a comprendere le differenze tra un tessuto sano e un tessuto affetto da patologia.

La **proteomica** descrive il corredo proteico completo di cellule e tessuti.

La **metabolomica** studia il **metaboloma**, cioe l'insieme completo dei metaboliti presenti in una cellula o tessuto.

I dati metabolomici possono essere integrati nelle **analisi multi-omiche**. Il progresso di queste analisi e collegato all'**interattomica**, che descrive la totalita delle interazioni molecolari di una cellula o di un tessuto.

### Ripasso Active Learning: scienze omiche

Domande da saper spiegare:

- Qual e il principio alla base del sequenziamento shotgun?
- In quale modo la genetica comparativa permette di risalire alle correlazioni evolutive tra specie?
- Che cosa si intende per scienze omiche?

Scelte corrette dalla sezione "Scegli le parole":

- Il genoma umano e stato sequenziato con il sequenziamento **shotgun**.
- La **trascrittomica** illustra tutti i geni espressi.

Attivita proposta:

- Nel **2020** si e celebrato il ventesimo anniversario della prima bozza del genoma umano. La consegna chiede di ricostruire le tappe principali del **Progetto Genoma Umano**, chi ha contribuito allo studio e i risultati ottenuti.
- La trascrizione termina con il richiamo: **"DIMMI LA TUA! Nobel a CRISPR"**.
