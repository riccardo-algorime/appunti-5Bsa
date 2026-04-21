# B2 + B4 — Metabolismo Energetico & DNA e Regolazione Genica
## Appunti di studio dettagliati

---

## Indice

**PARTE 1 — B2: Il Metabolismo Energetico**
1. [Visione d'insieme](#1-visione-dinsieme)
2. [Glicolisi](#2-glicolisi)
3. [Fermentazioni](#3-fermentazioni)
4. [Respirazione cellulare](#4-respirazione-cellulare)
5. [Bilancio energetico completo](#5-bilancio-energetico-completo)
6. [Biochimica del corpo umano](#6-biochimica-del-corpo-umano)
7. [Squilibri metabolici](#7-squilibri-metabolici)

**PARTE 2 — B4: Il DNA e la Regolazione Genica**
1. [Nucleotidi e acidi nucleici](#1-nucleotidi-e-acidi-nucleici)
2. [Struttura del DNA](#2-struttura-del-dna)
3. [Replicazione, trascrizione e traduzione](#3-replicazione-trascrizione-e-traduzione)
4. [Regolazione genica nei procarioti](#4-regolazione-genica-nei-procarioti)
5. [Regolazione genica negli eucarioti](#5-regolazione-genica-negli-eucarioti)
6. [Genetica dei virus](#6-genetica-dei-virus)
7. [Geni mobili e spillover](#7-geni-mobili-e-spillover)

[Domande di ripasso](#domande-di-ripasso)

---

# PARTE 1 — B2: Il Metabolismo Energetico

---

## 1. Visione d'insieme

Il **metabolismo cellulare** è l'insieme di milioni di reazioni chimiche che servono a:
- ricavare energia
- idrolizzare e sintetizzare i polimeri biologici

> **Definizione chiave:** Una *via metabolica* è la sequenza di reazioni coinvolte nello stesso processo metabolico. Molte vie sono comuni a tutti gli organismi; negli eucarioti alcune sono *compartimentate* (es. mitocondri, cloroplasti).

### Anabolismo vs Catabolismo

| | **Anabolismo** | **Catabolismo** |
|---|---|---|
| Direzione | Sintesi di molecole complesse | Degradazione in molecole semplici |
| Energetica | *Endoergonico* (richiede energia) | *Esoergonico* (libera energia) |
| Esempi | Glicogenosintesi, biosintesi proteine | Glicolisi, β-ossidazione |

### Il ruolo dell'ATP

L'**ATP** (*adenosina trifosfato*) è la molecola trasportatrice di energia universale. Agisce come intermediario tra reazioni esoergoniche (che la producono) ed endoergoniche (che la consumano):

$$\text{ATP} \rightleftharpoons \text{ADP} + P_i + \text{energia}$$

### NAD e FAD: trasportatori di elettroni

Le **deidrogenasi** (ossidoreduttasi) catalizzano ossidazioni usando specifici coenzimi:

| Coenzima | Forma ossidata | Forma ridotta | Funzione |
|---|---|---|---|
| NAD | $\text{NAD}^+$ | NADH | Trasporta $H^+$ e $e^-$ nella respirazione |
| NADP | $\text{NADP}^+$ | NADPH | Principalmente nell'anabolismo |
| FAD | FAD | $\text{FADH}_2$ | Trasporta $e^-$ nella catena respiratoria |

> **Attenzione:** NAD e FAD non producono energia direttamente; la cedono alla catena di trasporto degli elettroni.

---

## 2. Glicolisi

La **glicolisi** è la via metabolica universale che ossida parzialmente il glucosio producendo piruvato. Avviene nel *citosol* e comprende **10 tappe** suddivise in due fasi.

### Fase endoergonica (tappe 1–5): investimento di ATP

> Si "investe" ATP per attivare il glucosio. Prodotto finale: 2 molecole di **gliceraldeide 3-fosfato (G3P)**.

| Tappa | Reazione | Enzima | Nota |
|---|---|---|---|
| 1 | Glucosio → Glucosio 6-fosfato | Esochinasi | Consumo 1 ATP |
| 2 | Glucosio 6-fosfato → Fruttosio 6-fosfato | Fosfoesoso isomerasi | |
| 3 | Fruttosio 6-fosfato → Fruttosio 1,6-bisfosfato | Fosfofruttochinasi-1 | Consumo 1 ATP — *tappa di controllo* |
| 4 | Fruttosio 1,6-bisfosfato → G3P + DHAP | Aldolasi | Scissione in 2 C3 |
| 5 | DHAP → G3P | Trioso fosfato isomerasi | Entrambi i prodotti → G3P |

**Bilancio parziale:** −2 ATP, +2 G3P

### Fase esoergonica (tappe 6–10): recupero di energia

> Si ossida la G3P in piruvato, producendo ATP e NADH.

| Tappa | Reazione | Enzima | Prodotto energetico |
|---|---|---|---|
| 6 | G3P → 1,3-bisfosfoglicerato | G3P deidrogenasi | 2 NADH |
| 7 | 1,3-bisfosfoglicerato → 3-fosfoglicerato | Fosfoglicerato chinasi | 2 ATP (substrato) |
| 8 | 3-fosfoglicerato → 2-fosfoglicerato | Fosfoglicerato mutasi | |
| 9 | 2-fosfoglicerato → Fosfoenolpiruvato (PEP) | Enolasi | −2 H₂O |
| 10 | PEP → Piruvato | Piruvato chinasi | 2 ATP (substrato) |

### Bilancio netto della glicolisi

$$\text{Glucosio} + 2\,\text{NAD}^+ + 2\,\text{ADP} + 2\,P_i \rightarrow 2\,\text{Piruvato} + 2\,\text{NADH} + 2\,H^+ + 2\,\text{ATP} + 2\,H_2O$$

**Guadagno netto: 2 ATP + 2 NADH**

> **Nota:** 7 delle 10 tappe sono reversibili; le tappe 1, 3, 10 sono *irreversibili* nelle condizioni intracellulari → la glicolisi è nel complesso irreversibile.

---

## 3. Fermentazioni

In condizioni **anaerobiche**, il piruvato non può entrare nel ciclo di Krebs. La cellula deve rigenerare $\text{NAD}^+$ (necessario per continuare la glicolisi) attraverso la **fermentazione**.

> **Funzione chiave della fermentazione:** Non produce ATP direttamente, ma *rigenera NAD⁺* permettendo alla glicolisi di continuare.

### Fermentazione lattica

**Organismi:** muscolo scheletrico sotto sforzo intenso, *Lactobacillus*

$$\text{Piruvato} + \text{NADH} + H^+ \xrightarrow{\text{Lattato deidrogenasi}} \text{Lattato} + \text{NAD}^+$$

**Equazione netta:**
$$\text{Glucosio} + 2\,\text{ADP} + 2\,P_i \rightarrow 2\,\text{Lattato} + 2\,\text{ATP} + 2\,H_2O$$

**Applicazioni:** produzione di yogurt, formaggi.

### Fermentazione alcolica

**Organismi:** lieviti (*Saccharomyces cerevisiae*, *S. uvarum*)

Si svolge in **due reazioni**:

$$\text{Piruvato} \xrightarrow{\text{Piruvato decarbossilasi}} \text{Acetaldeide} + CO_2$$

$$\text{Acetaldeide} + \text{NADH} + H^+ \xrightarrow{\text{Alcol deidrogenasi}} \text{Etanolo} + \text{NAD}^+$$

**Equazione netta:**
$$\text{Glucosio} + 2\,\text{ADP} + 2\,P_i \rightarrow 2\,\text{Etanolo} + 2\,CO_2 + 2\,\text{ATP} + 2\,H_2O$$

**Applicazioni:** birra (alta fermentazione: *S. cerevisiae* → *ale*; bassa fermentazione: *S. uvarum/carlsbergensis* → *lager*), vino (*S. cerevisiae*, *S. bayanus*), pane.

### Ciclo di Cori

Il **Ciclo di Cori** (Carl e Gerty Theresa Cori) descrive la cooperazione tra muscolo e fegato:

1. **Muscolo:** glucosio → lattato + 2 ATP (fermentazione lattica durante sforzo)
2. **Sangue:** il lattato viene trasportato al fegato
3. **Fegato:** lattato → glucosio (gluconeogenesi, 6 ATP)
4. **Sangue:** il glucosio ritorna ai muscoli

> Il ciclo di Cori consente il recupero del lattato, evitando l'acidosi tissutale prolungata.

---

## 4. Respirazione cellulare

In presenza di $O_2$, il piruvato viene ossidato completamente a $CO_2$ e $H_2O$ nei **mitocondri**.

### Struttura del mitocondrio

Il mitocondrio è delimitato da **due membrane**:

| Membrana | Caratteristiche | Struttura | Contenuto |
|---|---|---|---|
| Esterna | Permeabile a piccole molecole e ioni | Liscia | Delimita lo spazio intermembrana |
| Interna | *Impermeabile* a ioni e piccole molecole | Ripiegata a **creste** | Matrice mitocondriale, ATP sintasi |

**Matrice mitocondriale:** contiene enzimi del ciclo di Krebs, DNA mitocondriale, ribosomi.

### Fase 1: Decarbossilazione ossidativa del piruvato

Il piruvato viene convertito in **acetil-CoA** dal *complesso della piruvato deidrogenasi*:

$$\text{Piruvato} + \text{CoA-SH} + \text{NAD}^+ \xrightarrow{\text{Piruvato deidrogenasi}} \text{Acetil-CoA} + CO_2 + \text{NADH} + H^+$$

**Per molecola di glucosio:** 2 Acetil-CoA + 2 $CO_2$ + 2 NADH

### Fase 2: Ciclo di Krebs

Il ciclo di Krebs è composto da **8 reazioni** che ossidano completamente i 2 atomi di carbonio dell'acetil-CoA. Si svolge nella **matrice mitocondriale**.

| Tappa | Reazione | Enzima | Prodotto |
|---|---|---|---|
| 1 | Acetil-CoA + Ossalacetato → **Citrato** | Citrato sintasi | — |
| 2 | Citrato → *cis*-Aconitato → **Isocitrato** | Aconitasi | — |
| 3 | Isocitrato → **α-Chetoglutarato** | Isocitrato deidrogenasi | NADH, $CO_2$ |
| 4 | α-Chetoglutarato → **Succinil-CoA** | α-Chetoglutarato deidrogenasi | NADH, $CO_2$ |
| 5 | Succinil-CoA → **Succinato** | Succinil-CoA sintetasi | GTP/ATP |
| 6 | Succinato → **Fumarato** | Succinato deidrogenasi | $\text{FADH}_2$ |
| 7 | Fumarato → **Malato** | Fumarasi | — |
| 8 | Malato → **Ossalacetato** | Malato deidrogenasi | NADH |

**Bilancio per giro (1 Acetil-CoA):**
- 3 NADH, 1 $\text{FADH}_2$, 1 GTP/ATP, 2 $CO_2$

**Bilancio per glucosio (2 giri):**
$$\rightarrow \; 6\,\text{NADH} + 2\,\text{FADH}_2 + 2\,\text{GTP} + 4\,CO_2$$

### Fase 3: Fosforilazione ossidativa

La fosforilazione ossidativa comprende due processi interconnessi:

**a) Catena di trasporto degli elettroni** (nella membrana mitocondriale interna):

| Complesso | Nome | Azione | Protoni pompati |
|---|---|---|---|
| **I** | NADH deidrogenasi | Riceve $e^-$ da NADH → riduce ubichinone (Q) | 4 $H^+$ |
| **II** | Succinato deidrogenasi | Riceve $e^-$ da $\text{FADH}_2$ → riduce Q | 0 $H^+$ |
| **III** | Citocromo c reduttasi | Riceve $e^-$ da $QH_2$ → riduce citocromo *c* | 4 $H^+$ |
| **IV** | Citocromo c ossidasi | Riceve $e^-$ da cit. *c* → riduce $O_2$ a $H_2O$ | 4 $H^+$ |

**Reazione finale al Complesso IV:**
$$O_2 + 4e^- + 4H^+ \rightarrow 2\,H_2O$$

**b) Chemiosintesi (ATP sintasi):**

Il pompaggio di $H^+$ crea un **gradiente elettrochimico** (= forza proton-motrice) con due componenti:
- *Gradiente chimico:* differenza di concentrazione protonica tra spazio intermembrana e matrice
- *Gradiente elettrico:* differenza di distribuzione delle cariche

I protoni fluiscono *spontaneamente* attraverso l'**ATP sintasi** ($F_0$–$F_1$) dalla zona ad alta concentrazione (spazio intermembrana) alla zona a bassa concentrazione (matrice), e questa forza aziona la sintesi di ATP:

$$\text{ADP} + P_i \xrightarrow{\text{ATP sintasi}} \text{ATP}$$

> L'ATP sintasi è composta da:
> - **$F_0$:** canale transmembrana per i protoni
> - **$F_1$:** dominio catalitico per la sintesi di ATP (nella matrice)

---

## 5. Bilancio energetico completo

| Tappa | ATP netto | NADH | $\text{FADH}_2$ |
|---|---|---|---|
| Glicolisi | 2 | 2 | 0 |
| Decarbossilazione ossidativa | 0 | 2 | 0 |
| Ciclo di Krebs (×2) | 2 | 6 | 2 |
| **Totale portatori ridotti** | — | **10** | **2** |
| Fosforilazione ossidativa da NADH (×10) | ~25 | — | — |
| Fosforilazione ossidativa da $\text{FADH}_2$ (×2) | ~3 | — | — |
| **TOTALE** | **~32 ATP** | | |

**Equazioni riassuntive:**

*Glicolisi + fermentazione:*
$$C_6H_{12}O_6 \rightarrow 2\,\text{Lattato (o 2 Etanolo} + 2\,CO_2) + 2\,\text{ATP}$$

*Glicolisi + respirazione cellulare:*
$$C_6H_{12}O_6 + 6\,O_2 \rightarrow 6\,CO_2 + 6\,H_2O + 32\,\text{ATP}$$

> **Confronto:** La respirazione cellulare produce **16 volte più ATP** della sola fermentazione.

---

## 6. Biochimica del corpo umano

### Glicemia e omeostasi

La **glicemia** (concentrazione di glucosio nel sangue) è mantenuta costante tra **60–99 mg/dL** grazie a un sistema di regolazione ormonale.

### Metabolismo del glicogeno

**Dopo un pasto ricco di carboidrati:**
- Il glucosio viene metabolizzato per produrre ATP *oppure*
- Viene immagazzinato come **glicogeno** (**glicogenosintesi**) nel fegato e nei muscoli

**Lontano dal pasto:**
- Il glicogeno viene demolito (**glicogenolisi**) per liberare glucosio

### Gluconeogenesi

La **gluconeogenesi** è la sintesi di glucosio a partire da precursori *non glucidici*: piruvato, lattato, etanolo, amminoacidi glucogenetici. Avviene quasi interamente nel **citosol** (tranne la prima tappa mitocondriale).

**Tappe chiave di differenza con la glicolisi:**

| Glicolisi (irreversibile) | Gluconeogenesi (enzima specifico) |
|---|---|
| Glucosio → Glucosio 6-P (Esochinasi) | Glucosio 6-P → Glucosio (Glucosio 6-fosfatasi) |
| Fruttosio 6-P → Fruttosio 1,6-bisP (PFK-1) | Fruttosio 1,6-bisP → Fruttosio 6-P (Fruttosio-1,6-bisfosfatasi) |
| PEP → Piruvato (Piruvato chinasi) | Piruvato → Ossalacetato → PEP (Piruvato carbossilasi + PEP-carbossichinasi) |

### Metabolismo lipidico (cenni)

I **trigliceridi** sono dispersi dai *sali biliari* nell'intestino, degradati da *lipasi* ad acidi grassi + glicerolo, assorbiti dagli enterociti e riassemblati in **chilomicroni** per il trasporto linfatico/ematico.

La **β-ossidazione** degli acidi grassi avviene nella matrice mitocondriale: cicli ripetuti di ossidazione distaccano frammenti bicarboniosi come *acetil-CoA*.

> Tutte le sostanze convertibili in acetil-CoA possono essere trasformate in grasso.

### Metabolismo degli amminoacidi (cenni)

Gli amminoacidi in eccesso vengono catabolizzati. Lo ione ammonio ($NH_4^+$, tossico) viene convertito in **urea** nel fegato attraverso il **ciclo dell'urea** (animali ureotelici: anfibi e mammiferi).

### Organi e tessuti

| Organo/Tessuto | Ruolo metabolico principale |
|---|---|
| **Fegato** | Modifica e distribuisce glucosio, acidi grassi, proteine |
| **Tessuto adiposo** | Immagazzina e mobilizza acidi grassi; produce ormoni metabolici |
| **Muscolo scheletrico** | Produce ATP rapidamente per la contrazione |
| **Cervello** | Usa glucosio ematico come nutriente primario (neuroni) |

### Ormoni e regolazione della glicemia

| Ormone | Prodotto da | Effetto sulla glicemia | Meccanismo principale |
|---|---|---|---|
| **Insulina** | Cellule β del pancreas | ↓ (abbassa) | Favorisce glicogenosintesi, lipogenesi, captazione cellulare di glucosio |
| **Glucagone** | Cellule α del pancreas | ↑ (alza) | Induce glicogenolisi epatica, gluconeogenesi |
| **Adrenalina** | Surrene (midollare) | ↑ (alza) | Risposta "combatti o fuggi": mobilizza glucosio e acidi grassi |
| **Cortisolo** | Surrene (corticale) | ↑ (alza) | Stimola gluconeogenesi, catabolismo proteico |

---

## 7. Squilibri metabolici

### Diabete mellito

| | **Diabete tipo 1** | **Diabete tipo 2** |
|---|---|---|
| Causa | Distruzione autoimmune delle cellule β del pancreas | Produzione insulinica inadeguata o *resistenza all'insulina* |
| Insulina prodotta | **No** | Sì, ma insufficiente o inefficace |
| Terapia | Insulina esogena *obbligatoria* | Farmaci, dieta, stile di vita |
| Predisposizione | Genetica + trigger autoimmune | Genetica + **obesità** e stile di vita |

### Obesità

L'**obesità** risulta dall'assunzione calorica *eccedente* il dispendio energetico. Può essere causata da:
- stile di vita errato (causa più comune)
- patologie endocrine: *ipotiroidismo*, *sindrome di Cushing*

È un fattore di rischio per il **diabete tipo 2** e le malattie cardiovascolari.

> **Diete iperproteiche:** eliminare grassi e carboidrati causa carenze di *vitamine liposolubili* (A, D, E) e *acidi grassi essenziali* (linoleico, linolenico, arachidonico).

---
---

# PARTE 2 — B4: Il DNA e la Regolazione Genica

---

## 1. Nucleotidi e acidi nucleici

### Struttura di un nucleotide

Ogni **nucleotide** è composto da tre parti:

1. **Gruppo fosfato** (uno o più gruppi $-PO_4^{3-}$)
2. **Monosaccaride pentoso**: *ribosio* (RNA) o *2-desossiribosio* (DNA)
3. **Base eterociclica azotata**: uno o due anelli di C e N

![[Pasted image 20260407211826.png]]
### Sintesi di un nucleotide

```
Zucchero + Base azotata  →  [legame N-glicosidico]  →  Nucleoside
Nucleoside + Fosfato     →  [legame estereo C5']   →  Nucleotide
```

### Basi azotate

| Tipo | Basi | Struttura | Presente in |
|---|---|---|---|
| **Purine** (doppio anello) | Adenina (A), Guanina (G) | 2 anelli fusi | DNA e RNA |
| **Pirimidine** (anello singolo) | Citosina (C), Timina (T), Uracile (U) | 1 anello | T solo in DNA; U solo in RNA |
![[Pasted image 20260407212220.png]]
### DNA vs RNA: confronto

| Caratteristica | **DNA** | **RNA** |
|---|---|---|
| Zucchero | *2-Desossiribosio* | *Ribosio* |
| Basi | A, G, C, **T** | A, G, C, **U** |
| Struttura | Doppia elica | Singolo filamento |
| Localizzazione | Nucleo (+ mitocondri, cloroplasti) | Nucleo → citoplasma |
| Funzione | Conserva l'informazione genetica | Trasmette/traduce l'informazione |

### Acidi nucleici: polinucleotidi

I nucleotidi si uniscono tra loro tramite **legami fosfodiestere** (tra il fosfato di un nucleotide e il C-3' del nucletide successivo), formando un **polinucleotide** con:
- Estremità **5'–P**: gruppo fosfato libero
- Estremità **3'–OH**: gruppo ossidrile libero

---

## 2. Struttura del DNA

### La doppia elica di Watson e Crick

La molecola di DNA ha una struttura a **doppia elica** con le seguenti caratteristiche:

1. **Antiparallelismo:** i due filamenti sono orientati in direzioni opposte (5'→3' e 3'→5')
2. **Complementarità:** le basi si appaiano sempre in modo specifico:
   - $A = T$ (2 legami a idrogeno)
   - $G \equiv C$ (3 legami a idrogeno)
3. **Scheletro esterno:** le catene zucchero-fosfato sono rivolte verso l'esterno
4. **Basi interne:** le basi azotate sono rivolte verso l'interno, stabilizzando la struttura

### Dimensioni della doppia elica

| Parametro | Valore |
|---|---|
| Diametro | 2 nm |
| Distanza tra basi | 0,34 nm |
| Passo dell'elica (giro completo) | 3,4 nm |
| Basi per giro | 10 |

> **Regola di Chargaff:** In una molecola di DNA, la quantità di A = T e G = C. Dalla sequenza di un filamento si può dedurre la sequenza del filamento complementare.

![[Pasted image 20260407212236.png]]

---

## 3. Replicazione, trascrizione e traduzione

### Replicazione del DNA

La replicazione è **semi-conservativa**: ciascun filamento originale funge da stampo per il nuovo filamento. Enzimi coinvolti:

| Enzima | Funzione |
|---|---|
| **Elicasi** | *Separa* i due filamenti aprendo la doppia elica |
| **Primasi** | Sintetizza un breve primer a RNA (innesco per la DNA polimerasi) |
| **DNA polimerasi** | *Polimerizza* i nuovi nucleotidi (opera solo 5'→3') |

### Trascrizione: DNA → RNA

Le informazioni dei geni vengono trascritte in **mRNA** dall'enzima **RNA polimerasi**. Si divide in tre stadi:

| Stadio | Evento |
|---|---|
| **Inizio** | L'RNA polimerasi si lega al *promotore* e inizia la sintesi |
| **Allungamento** | Aggiunta sequenziale di nucleotidi al filamento nascente |
| **Terminazione** | Le *sequenze di terminazione* bloccano la sintesi; il trascritto viene rilasciato |

### Traduzione: mRNA → Proteina

Avviene nei **ribosomi** con l'ausilio dei **tRNA**. Ogni **codone** (tripletta di basi dell'mRNA) corrisponde a un amminoacido:

| Stadio | Evento |
|---|---|
| **Inizio** | Il ribosoma si assembla sull'mRNA; il tRNA iniziatore porta *metionina* al codone **AUG** |
| **Allungamento** | I tRNA portano amminoacidi; si formano legami peptidici tra amminoacidi successivi |
| **Terminazione** | Uno dei codoni di stop (**UGA, UAG, UAA**) non è riconosciuto da nessun tRNA; la catena polipeptidica si stacca |

> **Codice genetico ridondante:** ogni amminoacido è codificato da 2 o più codoni; ogni codone specifica un solo amminoacido (**non ambiguo**).

**Il dogma centrale della biologia:**

$$\text{DNA} \xrightarrow{\text{replicazione}} \text{DNA} \xrightarrow{\text{trascrizione}} \text{RNA} \xrightarrow{\text{traduzione}} \text{Proteina}$$

> *Eccezione moderna:* la **trascrittasi inversa** dei retrovirus consente la sintesi di DNA a partire da RNA (senso inverso).

---

## 4. Regolazione genica nei procarioti

### Principi generali

Nei batteri (es. *E. coli*) la regolazione avviene principalmente a livello di **inizio della trascrizione**, tramite:
- regolazione dell'RNA polimerasi
- **proteine regolatorie** (repressori/attivatori) che interagiscono con l'operatore

### Gli operoni

I geni procarioti coinvolti nella stessa via metabolica sono raggruppati in **operoni**: unità trascrizionali coordinate.

**Struttura di un operone:**
```
Promotore — Operatore — Gene 1 — Gene 2 — Gene 3 ...
```

### Operone *lac* (sistema inducibile)

Regola il metabolismo del *lattosio* in *E. coli*.

| Condizione | Stato operone | Meccanismo |
|---|---|---|
| **Assenza di lattosio** | *Spento* (OFF) | Il repressore si lega all'operatore → blocca la trascrizione |
| **Presenza di lattosio** | *Acceso* (ON) | L'*allolattosio* (induttore) si lega al repressore → il repressore si stacca dall'operatore → trascrizione attiva |

> **Induttore = allolattosio** (metabolita del lattosio). Il sistema si accende *solo quando il substrato è disponibile* → risparmio energetico.

### Operone *trp* (sistema reprimibile)

Regola la *biosintesi del triptofano*.

| Condizione | Stato operone | Meccanismo |
|---|---|---|
| **Triptofano assente** | *Acceso* (ON) | Il repressore è inattivo → trascrizione degli enzimi biosintetici |
| **Eccesso di triptofano** | *Spento* (OFF) | Il triptofano (corepressore) si lega al repressore → il complesso blocca l'operatore |

> **Corepressore = triptofano.** Il sistema si spegne quando il prodotto finale è in eccesso → feedback negativo.

| | **Operone lac** | **Operone trp** |
|---|---|---|
| Tipo | Inducibile | Reprimibile |
| Normalmente | Spento (OFF) | Acceso (ON) |
| Molecola chiave | Allolattosio (induttore) | Triptofano (corepressore) |
| Via regolata | Catabolica (demolizione lattosio) | Anabolica (sintesi triptofano) |

---

## 5. Regolazione genica negli eucarioti

La regolazione eucariotica è molto più complessa e avviene a **quattro livelli**:

### Livello 1: Fase pre-trascrizionale

Il DNA è complessato con **istoni** a formare la **cromatina**. Le modificazioni degli istoni determinano il grado di compattazione:

| Cromatina | Compattazione | Trascrizione |
|---|---|---|
| **Eterocromatina** | Alta (condensata) | *Inibita* |
| **Eucromatina** | Bassa (rilassata) | *Attiva* |

**Modificazioni epigenetiche degli istoni:**
- **Metilazione:** aggiunta di $-CH_3$ → generalmente aumenta la compattazione → *silenzia* i geni
- **Acetilazione:** aggiunta di $-COCH_3$ → riduce la compattazione → *attiva* i geni

> Il **codice istonico** è l'insieme delle modificazioni degli istoni che determina, in ogni momento, l'efficienza di trascrizione di una regione di DNA.

### Livello 2: Fase trascrizionale

I promotori eucarioti contengono:
- **TATA box:** sequenza consenso su cui si assembla il *complesso trascrizionale* (fattori generali di trascrizione + RNA polimerasi II)
- **Siti per fattori specifici di trascrizione:** aumentano o diminuiscono l'efficienza di trascrizione
- **Enhancer:** sequenze regolatorie distanti dal promotore che *intensificano* la trascrizione

### Livello 3: Fase post-trascrizionale

Il trascritto primario (**pre-mRNA**) viene processato nel nucleo:
1. **Splicing:** lo **spliceosoma** (complesso di ribonucleoproteine) rimuove gli *introni* e unisce gli *esoni* → mRNA maturo
2. **Capping:** aggiunta di una struttura *cap* all'estremità 5'
3. **Coda poli-A:** aggiunta di una coda poliadenilata all'estremità 3'

Solo dopo questo processing l'mRNA maturo può uscire dal nucleo.

### Livello 4: Fase post-traduzionale

Le proteine neo-sintetizzate possono essere modulate tramite:
- **Modificazioni chimiche post-traduzionali:** aggiunta di gruppi chimici, catene glicidiche o lipidiche
- **Tagli proteolitici:** rimozione di porzioni per attivare la proteina
- **Degradazione via proteasoma:** proteine disfunzionali o in eccesso vengono marcate con **poliubiquitina** e degradate dal **proteasoma** (complesso multienzimatico)

---

## 6. Genetica dei virus

### Struttura generale dei virus

I virus sono **parassiti endocellulari obbligati** — non possono replicarsi autonomamente. Un virione è composto da:

- **Genoma virale:** DNA o RNA (singolo o doppio filamento)
- **Capside:** rivestimento proteico del genoma
- **Pericapside (envelope):** involucro lipidico esterno (presente solo in alcuni virus)

### Ciclo litico vs ciclo lisogeno (batteriofagi)

| | **Ciclo litico** | **Ciclo lisogeno** |
|---|---|---|
| Esito | Lisi e morte della cellula ospite | Latenza (virus dormiente) |
| DNA virale | Rimane nel citoplasma, si replica | Si integra nel DNA batterico → **profago** |
| Produzione virioni | Sì, molti nuovi fagi | No (fino all'induzione) |
| Infettività | Alta e immediata | Latente |

**Sequenza ciclo litico:**
1. Fago si lega alla cellula
2. Iniezione del DNA fagico
3. Trascrizione e traduzione del DNA virale dalla cellula ospite
4. Assemblaggio di nuovi fagi
5. Lisi cellulare → liberazione di virioni

**Sequenza ciclo lisogeno:**
1. Fago si lega alla cellula
2. Iniezione del DNA fagico
3. Integrazione del DNA virale nel cromosoma batterico (= profago)
4. Il profago si replica con il DNA batterico ad ogni divisione cellulare
5. (Raramente) il profago si separa e riprende il ciclo litico

### Virus eucariotici: HPV, SARS-CoV-2, HIV

| Virus | Tipo | Materiale genetico | Note |
|---|---|---|---|
| **HPV** (Papillomavirus) | Virus a DNA | DNA a doppio filamento | Causa papillomi cutanei e mucosali; alcuni ceppi oncogeni (collo utero) |
| **SARS-CoV-2** | Virus a RNA | RNA a singolo filamento (senso +) | Spike proteins sulla superficie; causa COVID-19 |
| **HIV** | *Retrovirus* | RNA → DNA (trascrittasi inversa) | Causa AIDS; si integra nel genoma dell'ospite |

> **Retrovirus:** il loro RNA viene copiato in DNA a doppio filamento dalla **trascrittasi inversa**, poi integrato nel genoma ospite come **provirus**.

---

## 7. Geni mobili e spillover

### Plasmidi batterici

I batteri possiedono, oltre al cromosoma principale, **plasmidi**: molecole circolari di DNA a doppia elica. Si dividono in tre categorie:
1. Operoni metabolici specializzati
2. Geni per la resistenza agli antibiotici
3. Geni per la coniugazione

### Trasferimento genico orizzontale

I batteri scambiano materiale genetico attraverso tre meccanismi:

| Meccanismo | Come funziona |
|---|---|
| **Coniugazione** | Un plasmide in duplicazione passa attraverso il *pilo sessuale* a un batterio ricevente |
| **Trasduzione** | Un batteriofago trasferisce DNA batterico (generalizzata o specializzata) |
| **Trasformazione** | Un batterio acquisisce *DNA libero dall'ambiente* |

> La coniugazione è alla base della diffusione della **resistenza agli antibiotici** tra batteri → problema clinico grave (*superbug*).

### Trasposoni

Un **trasposone** è un *elemento genetico mobile*: si sposta autonomamente all'interno del genoma della stessa cellula. Due classi:

- **Trasposoni a DNA:** contengono la *trasposasi* che taglia e incolla il DNA (es. elementi IS)
- **Retrotrasposoni:** residui di antichi retrovirus; si spostano attraverso un intermedio a RNA

Possono alterare il genoma inattivando geni o modificando sequenze regolatorie → importanti per l'evoluzione genomica.

### Spillover e malattie emergenti

La **virosfera** comprende tutte le specie virali della Terra (~6.800 classificate al 2020, solo ~250 patogene per l'uomo).

- **Specie serbatoio:** ospite naturale in cui il virus vive e si moltiplica
- **Spillover (salto di specie):** passaggio di un virus da un ospite animale agli esseri umani → può causare una *zoonosi*

**Fattori che favoriscono lo spillover:**
1. Contatto diretto tra specie serbatoio e umani (es. deforestazione, mercati di animali vivi)
2. **Tropismo** del virus (capacità di legarsi a recettori sulle cellule umane)
3. Mutazioni nei virus a RNA (alta frequenza) → adattamento a nuovi ospiti
4. Ricombinazione tra due ceppi diversi nella stessa cellula → *virioni ricombinanti*

**Dalla zoonosi alla pandemia:**
- Trasmissione da animale a uomo → *spillover*
- Adattamento → trasmissione interumana
- Diffusione globale → **pandemia**

> L'**impronta antropica** sugli ecosistemi (deforestazione, urbanizzazione, commercio di animali selvatici) *aumenta la frequenza* degli eventi di spillover.

---

## Domande di ripasso

### B2 — Metabolismo Energetico

1. Qual è la differenza tra anabolismo e catabolismo? Fai un esempio per ciascuno.
2. Perché la fase endoergonica della glicolisi viene chiamata "di investimento"?
3. Quale vantaggio offre la fosforilazione a livello del substrato rispetto alla fosforilazione ossidativa?
4. Qual è la funzione metabolica della fermentazione? Perché non produce ATP aggiuntivo?
5. Descrivi il ciclo di Cori: quali organi coinvolge e quale problema metabolico risolve?
6. Elenca le 8 tappe del ciclo di Krebs con i relativi prodotti energetici.
7. Come funziona l'ATP sintasi? Qual è il ruolo del gradiente protonico?
8. Perché i complessi della catena respiratoria pompano protoni nello *spazio intermembrana* e non nella matrice?
9. Quali sono le differenze tra diabete tipo 1 e tipo 2?
10. Che cosa si intende per gluconeogenesi? Da quali precursori può partire?

### B4 — DNA e Regolazione Genica

1. Descrivi la struttura di un nucleotide. Qual è la differenza tra nucleoside e nucleotide?
2. Perché i due filamenti del DNA sono detti "antiparalleli" e "complementari"?
3. Quali enzimi sono coinvolti nella replicazione del DNA e qual è il ruolo di ciascuno?
4. Che differenza c'è tra trascrizione e traduzione? Dove avviene ciascuna?
5. Che cos'è un operone? Perché questa organizzazione è vantaggiosa per i procarioti?
6. Spiega la differenza tra operone *lac* (sistema inducibile) e operone *trp* (sistema reprimibile).
7. Descrivi i quattro livelli di regolazione dell'espressione genica negli eucarioti.
8. Che cos'è il codice istonico? In che modo la metilazione e l'acetilazione influenzano la trascrizione?
9. Qual è la differenza tra ciclo litico e ciclo lisogeno? Cosa è il profago?
10. Che cosa si intende per spillover? Quali fattori aumentano il rischio di pandemia?

---

*Appunti elaborati da B2-raw.md e B4-raw.md — Capitoli B2 e B4 di Scienze Naturali Chimiche e Biologiche*
