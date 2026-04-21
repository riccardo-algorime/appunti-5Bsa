# Capitolo B2 — Il Metabolismo Energetico
> Appunti di studio dettagliati · Scienze Naturali Chimiche e Biologiche

---

## Indice

1. [Visione d'insieme del metabolismo](#1-visione-dinsieme-del-metabolismo)
2. [La glicolisi](#2-la-glicolisi)
3. [Le fermentazioni](#3-le-fermentazioni)
4. [La respirazione cellulare](#4-la-respirazione-cellulare)
5. [Bilancio energetico completo](#5-bilancio-energetico-completo)
6. [Biochimica del corpo umano](#6-biochimica-del-corpo-umano)
7. [Ormoni regolatori del metabolismo](#7-ormoni-regolatori-del-metabolismo)
8. [Squilibri metabolici](#8-squilibri-metabolici)
9. [Domande di ripasso](#9-domande-di-ripasso)

---

## 1. Visione d'insieme del metabolismo

### Che cos'è il metabolismo?

Il **metabolismo** è l'insieme di milioni di reazioni chimiche che avvengono nelle cellule e che svolgono tre funzioni principali:

1. **Ricavare energia** dai nutrienti
2. **Idrolizzare e degradare** i polimeri biologici (catabolismo)
3. **Sintetizzare** molecole complesse (anabolismo)

Una **via metabolica** è la sequenza ordinata di reazioni enzimatiche che partecipano allo stesso processo. Molte vie metaboliche sono condivise da tutti gli organismi viventi; negli eucarioti alcune sono *compartimentate*, cioè avvengono in organuli specifici come **mitocondri** e **cloroplasti**.

### Anabolismo vs Catabolismo

| Caratteristica | **Anabolismo** | **Catabolismo** |
|---|---|---|
| Tipo di reazione | Endoergonica (assorbe energia) | Esoergonica (libera energia) |
| Direzione | Sintesi di molecole complesse | Degradazione a molecole semplici |
| Esempio | Glicogenosintesi, biosintesi proteine | Glicolisi, β-ossidazione |
| Relazione con ATP | Consuma ATP | Produce ATP |

> **Concetto chiave:** anabolismo e catabolismo sono accoppiati: l'energia liberata dalle reazioni cataboliche è catturata sotto forma di ATP e poi utilizzata nelle reazioni anaboliche.

### Il ruolo dell'ATP

L'**ATP** (*adenosina trifosfato*) è la principale *molecola trasportatrice di energia* della cellula. Funziona come una "moneta energetica": incamera temporaneamente l'energia delle reazioni esoergoniche e la cede per le reazioni endoergoniche.

$$\text{ATP} \rightleftharpoons \text{ADP} + P_i + \text{energia}$$

L'ATP non è un deposito di energia a lungo termine; viene continuamente sintetizzato e idrolizzato. Il suo ruolo è *accoppiare* reazioni termodinamicamente sfavorevoli a reazioni favorevoli.

### NAD, NADP e FAD: i carrier di elettroni

Le **deidrogenasi** (classe delle ossidoreduttasi) catalizzano l'ossidazione di centinaia di composti usando coenzimi specifici:

| Coenzima | Forma ossidata | Forma ridotta | Funzione |
|---|---|---|---|
| **NAD** (nicotinamide adenina dinucleotide) | $\text{NAD}^+$ | NADH | Trasporto $H^+$ e $e^-$ nel catabolismo |
| **NADP** | $\text{NADP}^+$ | NADPH | Principalmente nell'anabolismo |
| **FAD** (flavina adenina dinucleotide) | FAD | $\text{FADH}_2$ | Trasporto $e^-$ nella catena respiratoria |

$$\text{NAD}^+ + 2H \rightarrow \text{NADH} + H^+$$

> **Importante:** NAD e FAD non producono ATP direttamente; portano gli elettroni alla catena respiratoria dove l'energia viene estratta con la fosforilazione ossidativa.

### Il glucosio: fonte energetica centrale

Il **glucosio** (esoso, $C_6H_{12}O_6$) è la principale fonte di energia per piante, animali e microrganismi. L'energia contenuta nei suoi legami chimici viene estratta tramite tre processi catabolici:

1. **Glicolisi** (universale, avviene nel citosol)
2. **Respirazione cellulare** (aerobica, avviene nei mitocondri)
3. **Fermentazione** (anaerobica, avviene nel citosol)

---

## 2. La glicolisi

### Panoramica

La **glicolisi** è la via metabolica universale in cui il glucosio viene parzialmente ossidato producendo **2 molecole di piruvato**. Avviene nel **citosol** di tutte le cellule, in assenza o presenza di ossigeno.

**Bilancio complessivo netto:**

$$\text{Glucosio} + 2\,\text{NAD}^+ + 2\,\text{ADP} + 2\,P_i \rightarrow 2\,\text{Piruvato} + 2\,\text{NADH} + 2H^+ + 2\,\text{ATP} + 2\,H_2O$$

### Le due fasi della glicolisi

#### Fase 1 — Fase endoergonica (tappe 1–5)

Scopo: destabilizzare il glucosio e scindere lo scheletro a 6C in due frammenti a 3C. **Costa 2 ATP** (investimento energetico).

| Tappa | Substrato | Prodotto | Enzima | Note |
|---|---|---|---|---|
| **1** | Glucosio | Glucosio-6-fosfato | *Esochinasi* | Consuma 1 ATP; irreversibile |
| **2** | Glucosio-6-fosfato | Fruttosio-6-fosfato | *Fosfoglucosio isomerasi* ($Mg^{2+}$) | Isomerizzazione reversibile |
| **3** | Fruttosio-6-fosfato | Fruttosio-1,6-bisfosfato | *Fosfofruttochinasi-1* ($Mg^{2+}$) | Consuma 1 ATP; **passo regolatorio** irreversibile |
| **4** | Fruttosio-1,6-bisfosfato | G3P + DHAP | *Aldolasi* | Scissione in due triosi |
| **5** | DHAP | Gliceraldeide-3-fosfato (G3P) | *Trioso fosfato isomerasi* | Converte DHAP in G3P |

> Alla fine della fase endoergonica si hanno **2 molecole di G3P** (gliceraldeide-3-fosfato).

#### Fase 2 — Fase esoergonica (tappe 6–10)

Scopo: ossidare G3P a piruvato liberando energia sotto forma di ATP e NADH. **Produce 4 ATP** (guadagno lordo).

| Tappa  | Substrato             | Prodotto                   | Enzima                                | Energia                                                                    |
| ------ | --------------------- | -------------------------- | ------------------------------------- | -------------------------------------------------------------------------- |
| **6**  | G3P (×2)              | 1,3-Bisfosfoglicerato (×2) | *G3P deidrogenasi*                    | Produce 2 NADH                                                             |
| **7**  | 1,3-BPG (×2)          | 3-Fosfoglicerato (×2)      | *Fosfoglicerato chinasi* ($Mg^{2+}$)  | Produce 2 ATP (*1ª fosforilazione a livello del substrato*)                |
| **8**  | 3-Fosfoglicerato (×2) | 2-Fosfoglicerato (×2)      | *Fosfoglicerato mutasi* ($Mg^{2+}$)   | Trasferimento del gruppo fosfato                                           |
| **9**  | 2-Fosfoglicerato (×2) | Fosfoenolpiruvato (×2)     | *Enolasi*                             | Rilascia 2 $H_2O$                                                          |
| **10** | PEP (×2)              | Piruvato (×2)              | *Piruvato chinasi* ($Mg^{2+}$, $K^+$) | Produce 2 ATP (*2ª fosforilazione a livello del substrato*); irreversibile |

### Bilancio della glicolisi

| | ATP | NADH |
|---|---|---|
| **Fase endoergonica** (tappe 1–5) | −2 (consumati) | 0 |
| **Fase esoergonica** (tappe 6–10) | +4 (prodotti) | +2 |
| **Bilancio netto** | **+2 ATP** | **+2 NADH** |

> **Fosforilazione a livello del substrato:** la sintesi di ATP avviene per trasferimento diretto del gruppo fosfato dal substrato all'ADP, senza passare per la catena respiratoria.

### Reversibilità delle tappe

- **7 tappe reversibili** (tappe 2–4, 6–9)
- **3 tappe irreversibili** (tappe 1, 3, 10 — catalizzate da esochinasi, PFK-1 e piruvato chinasi)

Queste tre tappe rendono la glicolisi **irreversibile nel complesso** e sono anche i principali **punti di regolazione**.

---

## 3. Le fermentazioni

### Perché la fermentazione?

Alla fine della glicolisi, i 2 NADH prodotti devono essere riossidati a $\text{NAD}^+$ affinché la glicolisi possa continuare (senza $\text{NAD}^+$ libero la tappa 6 si bloccherebbe). In condizioni aerobiche questo avviene tramite la catena respiratoria. In **condizioni anaerobiche**, la cellula usa la **fermentazione** per rigenerare $\text{NAD}^+$.

> La fermentazione **non produce ATP aggiuntivo**: il suo unico scopo è rigenerare $\text{NAD}^+$ per permettere alla glicolisi di continuare.

### Fermentazione lattica

Il piruvato viene ridotto a **lattato** dall'enzima **lattato deidrogenasi**, che ossida contemporaneamente NADH a $\text{NAD}^+$:

$$\text{Piruvato} + \text{NADH} + H^+ \xrightarrow{\text{lattato deidrogenasi}} \text{Lattato} + \text{NAD}^+$$

**Equazione netta:**

$$C_6H_{12}O_6 + 2\,\text{ADP} + 2\,P_i \rightarrow 2\,\text{Lattato} + 2\,\text{ATP} + 2\,H_2O$$

**Dove avviene:**
- Cellule muscolari durante intensa attività fisica (insufficiente apporto di $O_2$)
- Batteri del genere *Lactobacillus* (es. *Lactobacillus casei*) nell'intestino e nella produzione di yogurt

**Conseguenze fisiologiche:** accumulo di lattato nel sangue → acidificazione dei tessuti → dolore muscolare. Nel periodo di recupero post-esercizio, il lattato è riconvertito in glucosio dal fegato.

#### Il ciclo di Cori

Il **ciclo di Cori** (scoperto dai coniugi Carl e Gerty Theresa Cori) descrive la cooperazione metabolica tra muscolo e fegato:

1. **Muscolo** (durante esercizio intenso): glucosio → lattato + 2 ATP
2. **Fegato** (a riposo): lattato → glucosio (via gluconeogenesi, con consumo di ATP)

Il ciclo garantisce che il lattato non si accumuli in modo permanente e che il glucosio venga resintesizzato.

### Fermentazione alcolica

Il processo avviene in **due tappe** successive:

**Tappa 1:** il piruvato viene decarbossilato ad *acetaldeide* dall'enzima **piruvato decarbossilasi**, con rilascio di $CO_2$:

$$\text{Piruvato} \xrightarrow{\text{piruvato decarbossilasi}} \text{Acetaldeide} + CO_2$$

**Tappa 2:** l'acetaldeide viene ridotta ad *etanolo* dall'enzima **alcol deidrogenasi**, con ossidazione di NADH a $\text{NAD}^+$:

$$\text{Acetaldeide} + \text{NADH} + H^+ \xrightarrow{\text{alcol deidrogenasi}} \text{Etanolo} + \text{NAD}^+$$

**Equazione netta:**

$$C_6H_{12}O_6 + 2\,\text{ADP} + 2\,P_i \rightarrow 2\,\text{Etanolo} + 2\,CO_2 + 2\,\text{ATP} + 2\,H_2O$$

**Organismi coinvolti:**
- *Saccharomyces cerevisiae* (lievito di birra): birre *ale*, vino, pane
- *Saccharomyces bayanus*: fermentazione di mosti ad alto contenuto zuccherino, spumanti
- *Saccharomyces uvarum* e *S. carlsbergensis*: birre *lager* (bassa fermentazione, temperature basse, si depositano sul fondo)

> I lieviti ad **alta fermentazione** (es. *S. cerevisiae*) preferiscono temperature più alte, galleggiano in superficie e producono birre con profilo aromatico complesso (fruttato e speziato).

### Confronto fermentazioni

| Caratteristica | **Fermentazione lattica** | **Fermentazione alcolica** |
|---|---|---|
| Prodotto finale | Lattato | Etanolo + $CO_2$ |
| N° di tappe | 1 | 2 |
| Enzima chiave | Lattato deidrogenasi | Piruvato decarbossilasi + Alcol deidrogenasi |
| $\text{NAD}^+$ rigenerato | Sì | Sì |
| $CO_2$ prodotta | No | Sì |
| Organismi | Cellule muscolari, *Lactobacillus* | Lieviti (*Saccharomyces*) |
| ATP netto | 2 | 2 |

---

## 4. La respirazione cellulare

In presenza di $O_2$, il piruvato non va alla fermentazione ma viene completamente ossidato a $CO_2$ e $H_2O$ tramite la **respirazione cellulare**, che avviene nei **mitocondri**.

### Struttura del mitocondrio

Il mitocondrio è avvolto da **due membrane**:

| Membrana | Caratteristiche | Delimita |
|---|---|---|
| **Esterna** | Liscia, permeabile a piccole molecole e ioni | Spazio intermembrana |
| **Interna** | Estesa, ripiegata in **creste**, *impermeabile* a molecole piccole e ioni | Matrice mitocondriale |

**Componenti della membrana interna:**
- Complessi della catena respiratoria (I, II, III, IV)
- **ATP sintasi** (complesso $F_0F_1$)
- Trasportatori specifici

**Componenti della matrice:**
- Enzimi del ciclo di Krebs
- DNA mitocondriale circolare
- Ribosomi mitocondriali
- Molecole di CoA, NAD, FAD

> La membrana interna impermeabile è **fondamentale**: è il gradiente protonico attraverso di essa che guida la sintesi di ATP.

### Le 3 fasi della respirazione cellulare

#### Fase 1 — Decarbossilazione ossidativa del piruvato

Il piruvato entra nella matrice mitocondriale e viene convertito in **acetil-CoA** dal complesso enzimatico **piruvato deidrogenasi**:

$$\text{Piruvato} + CoA\text{-}SH + \text{NAD}^+ \xrightarrow{\text{piruvato deidrogenasi}} \text{Acetil-CoA} + CO_2 + \text{NADH} + H^+$$

**Per ogni molecola di glucosio** (2 piruvati):
- Produce **2 Acetil-CoA**
- Produce **2 NADH**
- Rilascia **2 $CO_2$**

#### Fase 2 — Il ciclo di Krebs

Il ciclo di Krebs (ciclo dell'acido citrico) è una **via ciclica di 8 reazioni** nella matrice mitocondriale. Ogni ciclo ossida completamente 2 atomi di carbonio dell'acetil-CoA a $CO_2$, rigenerando l'ossalacetato di partenza.

**Punto di ingresso:** condensazione di acetil-CoA con ossalacetato (4C) → citrato (6C).

##### Le 8 tappe del ciclo di Krebs

| Tappa | Substrato | Prodotto | Enzima | Prodotti energetici |
|---|---|---|---|---|
| **1** | Acetil-CoA (2C) + Ossalacetato (4C) | Citrato (6C) | *Citrato sintasi* | — |
| **2** | Citrato | *cis*-Aconitato → Isocitrato | *Aconitasi* | — |
| **3** | Isocitrato (6C) | α-Chetoglutarato (5C) | *Isocitrato deidrogenasi* | NADH + $CO_2$ |
| **4** | α-Chetoglutarato (5C) | Succinil-CoA (4C) | *α-Chetoglutarato deidrogenasi* | NADH + $CO_2$ |
| **5** | Succinil-CoA (4C) | Succinato (4C) | *Succinil-CoA sintetasi* | GTP (≈ ATP) |
| **6** | Succinato (4C) | Fumarato (4C) | *Succinato deidrogenasi* | $\text{FADH}_2$ |
| **7** | Fumarato (4C) | Malato (4C) | *Fumarasi* | — |
| **8** | Malato (4C) | Ossalacetato (4C) | *Malato deidrogenasi* | NADH |

**Bilancio per ogni ciclo (1 Acetil-CoA):**
- 2 $CO_2$
- 3 NADH
- 1 $\text{FADH}_2$
- 1 GTP/ATP

**Bilancio per glucosio (2 giri del ciclo):**
- 4 $CO_2$
- 6 NADH
- 2 $\text{FADH}_2$
- 2 ATP/GTP

> **Nota importante:** il ciclo di Krebs non produce direttamente molto ATP; il suo ruolo principale è **caricare i carrier** NADH e $\text{FADH}_2$ che porteranno gli elettroni alla catena respiratoria.

#### Fase 3 — Fosforilazione ossidativa

La fosforilazione ossidativa è composta da due processi strettamente accoppiati:

**a) Catena di trasporto degli elettroni** (nella membrana mitocondriale interna)
**b) Chemiosintesi** (sintesi di ATP tramite il gradiente protonico)

##### La catena respiratoria: i 4 complessi

| Complesso | Nome | Substrato | Pompa $H^+$? | Accettore |
|---|---|---|---|---|
| **I** | NADH deidrogenasi | NADH | Sì (+4 $H^+$) | Ubichinone (Q) |
| **II** | Succinato deidrogenasi | $\text{FADH}_2$ | **No** | Ubichinone (Q) |
| **III** | Citocromo *bc*₁ (ubichinone-cit. c reduttasi) | Ubichinolo ($QH_2$) | Sì (+4 $H^+$) | Citocromo *c* |
| **IV** | Citocromo *c* ossidasi | Citocromo *c* ridotto | Sì (+4 $H^+$) | $O_2$ (accettore finale) |

**Trasportatori mobili:**
- **Ubichinone (coenzima Q):** diffonde nella membrana tra complesso I/II e complesso III
- **Citocromo *c*:** proteina solubile nello spazio intermembrana, tra complesso III e IV

**Reazione del complesso IV:**

$$O_2 + 4e^- + 4H^+ \rightarrow 2\,H_2O$$

> Il $O_2$ è l'**accettore finale degli elettroni**: senza ossigeno la catena si ferma, non c'è gradiente protonico e l'ATP sintasi smette di funzionare.

##### La chemiosintesi e l'ATP sintasi

Il pompaggio di $H^+$ dallo spazio intermembrana crea un **gradiente elettrochimico** (forza proton-motrice) dovuto a:
- **Gradiente chimico:** differenza di concentrazione di $H^+$ ai due lati
- **Gradiente elettrico:** carica positiva in eccesso nello spazio intermembrana

Poiché la membrana interna è **impermeabile** ai protoni, questi non possono diffondere liberamente. L'unica via è passare attraverso l'**ATP sintasi** (complesso $F_0F_1$):

| Subunità | Posizione | Funzione |
|---|---|---|
| $F_0$ | Immersa nella membrana | Canale per il flusso di $H^+$ |
| $F_1$ | Sporgente nella matrice | Siti attivi per la sintesi di ATP da ADP + $P_i$ |

Il flusso di protoni attraverso $F_0$ fa ruotare un rotore che provoca cambiamenti conformazionali in $F_1$, catalizzando:

$$\text{ADP} + P_i + \text{energia (gradiente protonico)} \rightarrow \text{ATP} + H_2O$$

**Stima:** ogni NADH produce ≈ 2.5 ATP; ogni $\text{FADH}_2$ produce ≈ 1.5 ATP (per via del minor numero di protoni pompati, perché il complesso II non pompa $H^+$).

---

## 5. Bilancio energetico completo

### Produzione di ATP per molecola di glucosio

| Fase | ATP diretto | NADH | $\text{FADH}_2$ | ATP da NADH | ATP da $\text{FADH}_2$ | ATP totale |
|---|---|---|---|---|---|---|
| Glicolisi | +2 | +2 | — | +5 | — | **7** |
| Decarbossilazione ossidativa | — | +2 | — | +5 | — | **5** |
| Ciclo di Krebs | +2 | +6 | +2 | +15 | +3 | **20** |
| **Totale** | **4** | **10** | **2** | **25** | **3** | **≈ 32** |

*(Nota: i valori possono variare tra 30 e 32 a seconda del metodo di calcolo e dell'efficienza di trasporto dei NADH citosolici)*

### Fermentazione vs Respirazione

| | **Fermentazione** | **Respirazione cellulare** |
|---|---|---|
| Condizioni | Anaerobiche | Aerobiche |
| ATP netto | **2 ATP** | **≈ 32 ATP** |
| Prodotti di scarto | Lattato *oppure* Etanolo + $CO_2$ | $H_2O + CO_2$ |
| Ossidazione del glucosio | Parziale | Completa |
| Sede | Citosol | Citosol + Mitocondri |
| Necessità di $O_2$ | No | Sì |
| NADH riossidato? | Sì (nella fermentazione) | Sì (catena respiratoria) |

**Equazione della respirazione cellulare completa:**

$$C_6H_{12}O_6 + 6\,O_2 \rightarrow 6\,CO_2 + 6\,H_2O + 32\,\text{ATP}$$

**Equazione della fermentazione:**

$$C_6H_{12}O_6 \rightarrow 2\,\text{lattato (o } 2\,\text{etanolo} + 2\,CO_2) + 2\,\text{ATP}$$

---

## 6. Biochimica del corpo umano

### Il glucosio nel corpo umano

Il glucosio è la **principale fonte di energia** per il corpo umano. Lo assumiamo prevalentemente come carboidrati complessi (amido, glicogeno alimentare). La **glicemia** (concentrazione di glucosio nel sangue) è normalmente mantenuta tra **60 e 99 mg/dL** grazie a un sistema di regolazione ormonale finemente bilanciato.

### Metabolismo del glicogeno

#### Glicogenosintesi (sintesi del glicogeno)

Dopo un pasto ricco di carboidrati, il glucosio in eccesso nel sangue viene immagazzinato come **glicogeno** (polimero del glucosio con ramificazioni α-1,6) principalmente nel:
- **Fegato** (riserva per tutta la cellula → mantenimento della glicemia)
- **Muscolo scheletrico** (riserva locale per la contrazione muscolare)

La glicogenosintesi richiede la **glicogeno sintasi** e l'attivazione del glucosio tramite UDP-glucosio.

#### Glicogenolisi (degradazione del glicogeno)

Lontano dal pasto (o durante esercizio fisico), le riserve di glicogeno vengono mobilizzate attraverso la **glicogenolisi**: il glicogeno viene idrolizzato e le unità di glucosio-1-fosfato vengono rilasciate nel sangue (dal fegato) o usate localmente (nel muscolo).

Il glicogeno epatico copre il fabbisogno energetico solo per **alcune ore di digiuno**.

### Gluconeogenesi

La **gluconeogenesi** è la sintesi di glucosio a partire da **precursori non glucidici** quando le riserve di glicogeno sono esaurite.

**Precursori:**
- **Piruvato** e **lattato** (dal muscolo, via ciclo di Cori)
- **Glicerolo** (dai trigliceridi)
- **Amminoacidi glucogenetici** (da proteine)
- Etanolo (in piccola parte)

**Sede:** quasi interamente nel **citosol epatico** (prima tappa nel mitocondrio).

**Relazione con la glicolisi:** la gluconeogenesi segue sostanzialmente le tappe *inverse* della glicolisi, **tranne** nelle 3 tappe irreversibili (tappe 1, 3 e 10 della glicolisi), dove si usano enzimi diversi:

| Tappa glicolisi irreversibile | Enzima glicolisi | Enzima gluconeogenesi |
|---|---|---|
| Glucosio → G6P (tappa 1) | Esochinasi | Glucosio-6-fosfatasi |
| F6P → F1,6BP (tappa 3) | Fosfofruttochinasi-1 | **Fruttosio-1,6-bisfosfatasi** (enzima chiave) |
| PEP → Piruvato (tappa 10) | Piruvato chinasi | Piruvato carbossilasi + PEP carbossichinasi |

> **Enzima chiave della gluconeogenesi:** la *fruttosio-1,6-bisfosfatasi*.

**Schema della prima tappa (mitocondriale):**
1. Piruvato → Ossalacetato (enzima: *piruvato carbossilasi*, richiede ATP, biotina, $HCO_3^-$)
2. Ossalacetato → Malato (trasportato fuori dal mitocondrio)
3. Malato → Ossalacetato nel citosol (con produzione di NADH citosolico)
4. Ossalacetato → PEP (enzima: *PEP carbossichinasi*, dipendente da GTP)

### β-Ossidazione degli acidi grassi

I **lipidi** svolgono funzioni energetiche, strutturali, di regolazione e trasporto di vitamine liposolubili.

**Percorso dei lipidi alimentari:**
1. I trigliceridi (insolubili in acqua) sono dispersi dai **sali biliari** nell'intestino
2. Degradati a acidi grassi + glicerolo dalle **lipasi**
3. Assorbiti dagli **enterociti** e riassemblati nei **chilomicroni**
4. Trasportati via **sistema linfatico** → **sistema sanguigno** ai tessuti

La **β-ossidazione** (catabolismo degli acidi grassi) avviene nella **matrice mitocondriale** e consiste in cicli ripetuti di ossidazione al carbonio β, con distacco di un **frammento bicarbonioso** sotto forma di **acetil-CoA**.

Ogni ciclo di β-ossidazione produce:
- 1 Acetil-CoA
- 1 NADH
- 1 $\text{FADH}_2$

L'acetil-CoA così prodotto entra nel ciclo di Krebs.

> **Nota:** la biosintesi degli acidi grassi è una via *diversa* da quella ossidativa e avviene nel citoplasma (non nel mitocondrio).

**Destini biosintetici dell'acetil-CoA:**
- Ossidazione nel ciclo di Krebs
- Sintesi di acidi grassi
- Sintesi di colesterolo
- Sintesi di corpi chetonici (in digiuno prolungato)

### Metabolismo degli amminoacidi

Gli amminoacidi provenienti dalla digestione delle proteine sono usati per:
1. Biosintesi di **proteine endogene**
2. Sintesi di **composti azotati non proteici** (porfirine, basi azotate, neurotrasmettitori)
3. Produzione di **energia** (solo quando carboidrati e lipidi non sono disponibili)

**Il problema dell'azoto:** la demolizione degli amminoacidi comporta l'eliminazione del gruppo amminico ($-NH_2$) come **ammonio** ($NH_4^+$), che è tossico. Negli animali ureotelici (anfibi e mammiferi) viene convertito in **urea** nel fegato tramite il **ciclo dell'urea**.

**Amminoacidi glucogenici:** si trasformano in precursori della gluconeogenesi (piruvato, ossalacetato, ecc.)
**Amminoacidi chetogenici:** si trasformano in acetil-CoA o acetoacetil-CoA

### Funzioni metaboliche degli organi

| Organo/Tessuto | Funzione metabolica principale |
|---|---|
| **Fegato** | Modifica e distribuisce glucosio, acidi grassi e proteine; gluconeogenesi, glicogenolisi, ciclo dell'urea, sintesi di corpi chetonici |
| **Muscolo scheletrico** | Produce ATP rapidamente per la contrazione; usa glucosio, glicogeno e acidi grassi |
| **Tessuto adiposo** | Immagazzina e mobilizza acidi grassi come trigliceridi; produce ormoni (leptina) che segnalano lo stato delle riserve energetiche |
| **Cervello** | Utilizza quasi esclusivamente **glucosio ematico**; in digiuno prolungato può adattarsi a usare corpi chetonici |

---

## 7. Ormoni regolatori del metabolismo

La **glicemia** (60–99 mg/dL) è mantenuta costante grazie all'azione coordinata di quattro ormoni principali:

### Insulina

- **Prodotta da:** cellule β del pancreas (isole di Langerhans)
- **Stimolo:** aumento della glicemia (dopo un pasto)
- **Effetti metabolici:**

| Organo | Effetto |
|---|---|
| Fegato | Attiva glicogenosintesi, inibisce gluconeogenesi e glicogenolisi |
| Muscolo | Attiva captazione di glucosio e glicogenosintesi |
| Tessuto adiposo | Attiva sintesi e deposito di trigliceridi; inibisce lipolisi |

> L'insulina **abbassa la glicemia** favorendo la conversione del glucosio in eccesso in glicogeno e trigliceridi.

### Glucagone

- **Prodotto da:** cellule α del pancreas
- **Stimolo:** diminuzione della glicemia (digiuno)
- **Effetti metabolici:**

| Organo | Effetto |
|---|---|
| Fegato | Attiva glicogenolisi e gluconeogenesi (rilascio di glucosio nel sangue) |
| Tessuto adiposo | Attiva lipolisi (rilascio di acidi grassi) |

> Il glucagone **alza la glicemia** inducendo il fegato a rilasciare glucosio.

### Adrenalina (epinefrina)

- **Prodotta da:** midollare del surrene
- **Stimolo:** stress acuto, esercizio fisico intenso ("combatti e fuggi")
- **Effetti:**
  - Dilata le vie respiratorie
  - Aumenta frequenza cardiaca e pressione sanguigna
  - Stimola glicogenolisi nel fegato e nel muscolo
  - Mobilizza acidi grassi dal tessuto adiposo
  - Consuma rapidamente energia

### Cortisolo

- **Prodotto da:** corteccia surrenale
- **Stimolo:** stress cronico, digiuno prolungato
- **Effetti:**
  - Stimola gluconeogenesi epatica
  - Stimola degradazione delle proteine muscolari (per fornire amminoacidi alla gluconeogenesi)
  - Effetti antinfiammatori

### Schema riassuntivo degli ormoni

| Ormone | Ghiandola | Stimolo | Effetto su glicemia | Azioni principali |
|---|---|---|---|---|
| **Insulina** | Pancreas (cellule β) | Glicemia alta | **Abbassa** | Glicogenosintesi, lipogenesi |
| **Glucagone** | Pancreas (cellule α) | Glicemia bassa | **Alza** | Glicogenolisi, gluconeogenesi |
| **Adrenalina** | Midollare surrene | Stress acuto | **Alza** | Glicogenolisi, lipolisi |
| **Cortisolo** | Corteccia surrene | Stress cronico/digiuno | **Alza** | Gluconeogenesi, catabolismo proteico |

---

## 8. Squilibri metabolici

### Diabete mellito

Il **diabete mellito** è la patologia metabolica più diffusa nel mondo occidentale. Si caratterizza per un'iperglicemia cronica (glicemia a digiuno > 126 mg/dL) causata da problemi con la produzione o l'azione dell'insulina.

#### Diabete di tipo 1 (insulino-dipendente)

- **Causa:** distruzione **autoimmune** delle cellule β del pancreas → mancanza totale di insulina
- **Insorgenza:** tipicamente in età giovanile
- **Trattamento:** somministrazione esogena di insulina (obbligatoria)
- **Conseguenze senza trattamento:** chetoacidosi diabetica, danni vascolari e nervosi

#### Diabete di tipo 2 (insulino-resistente)

- **Causa:** produzione di insulina inadeguata *o* **resistenza all'insulina** dei tessuti bersaglio
- **Fattori di rischio:** obesità, sedentarietà, dieta scorretta, predisposizione genetica
- **Insorgenza:** tipicamente in età adulta, ma in aumento nei giovani
- **Trattamento:** cambiamento stile di vita, ipoglicemizzanti orali, eventualmente insulina

| | Diabete Tipo 1 | Diabete Tipo 2 |
|---|---|---|
| Causa | Autoimmune | Resistenza/carenza insulina |
| Insulina endogena | Assente | Presente (insufficiente o non efficace) |
| Terapia insulinica | Sempre necessaria | Non sempre necessaria |
| Età di insorgenza | Giovane (tipico) | Adulta (tipico) |
| Collegamento con obesità | No | Sì |

### Obesità

L'**obesità** è il risultato di un **eccesso calorico** cronico rispetto alle calorie necessarie all'attività corporea.

**Cause principali:**
- Stili di vita errati (alimentazione ipercalorica + sedentarietà)
- In alcuni casi: cause endocrine (ipotiroidismo, sindrome di Cushing)

**Rischi metabolici:**
- Fattore predisponente per il diabete di tipo 2
- Aumentato rischio cardiovascolare

### Diete iperproteiche e squilibri nutrizionali

Le diete iperproteiche povere di carboidrati e lipidi possono causare:
- Sviluppo di **squilibri metabolici**
- **Carenze nutrizionali**: i lipidi sono necessari per assorbire le vitamine liposolubili (A, D, E) e per fornire acidi grassi essenziali (linoleico, linolenico, arachidonico)

> **Acidi grassi essenziali:** linoleico, linolenico e arachidonico — non possono essere sintetizzati dall'organismo e devono essere assunti con la dieta.

### Patologie metaboliche ereditarie

- **Fenilchetonuria:** accumulo di fenilalanina per difetto enzimatico → danni neurologici
- **Ipercolesterolemia familiare:** predisposizione genetica + stile di vita → rischio cardiovascolare elevato
- **Glicogenosi:** malattie genetiche rare da difetto di enzimi del metabolismo del glicogeno

---

## 9. Domande di ripasso

### Comprensione di base

1. Qual è la differenza tra anabolismo e catabolismo? Fai un esempio per ciascuno.
2. Perché l'ATP viene definito "moneta energetica" della cellula?
3. Qual è la funzione del NAD nella glicolisi? E del FAD nella catena respiratoria?
4. Quante fasi ha la glicolisi? Qual è il guadagno netto di ATP?
5. Che cosa si intende per "fosforilazione a livello del substrato"?
6. Perché la fermentazione non produce ATP aggiuntivo rispetto alla glicolisi?
7. Qual è la differenza tra fermentazione lattica e fermentazione alcolica?
8. Descrivi il ciclo di Cori: quali organi sono coinvolti e quali metaboliti vengono scambiati?

### Approfondimento

9. Qual è la struttura del mitocondrio e perché la membrana interna è impermeabile ai protoni?
10. Quali sono le 8 tappe del ciclo di Krebs? Elenca i prodotti energetici di ciascuna.
11. Quali complessi della catena respiratoria pompano protoni e quali no?
12. Come funziona l'ATP sintasi? Descrivi le subunità $F_0$ e $F_1$.
13. Perché il NADH produce più ATP del $\text{FADH}_2$?
14. Come la gluconeogenesi differisce dalla glicolisi nelle 3 tappe irreversibili?
15. Descrivi il percorso dei lipidi alimentari dall'intestino fino alla β-ossidazione.
16. Come vengono smaltiti i gruppi amminici degli amminoacidi?

### Applicazione clinica

17. Quali vie metaboliche vengono attivate dall'insulina e quali dal glucagone?
18. Qual è la causa del diabete di tipo 1? Perché richiede sempre la terapia insulinica?
19. Perché eliminare completamente i grassi dalla dieta è pericoloso?
20. Qual è il ruolo del cortisolo nel metabolismo durante lo stress cronico?
21. Durante un'intensa maratona, come cambia il metabolismo muscolare? Descrivi il ruolo dell'adrenalina.

---

*Fine degli appunti B2 — Il Metabolismo Energetico*
