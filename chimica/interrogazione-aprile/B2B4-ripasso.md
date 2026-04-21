# B2 + B4 — Ripasso Rapido
## Metabolismo Energetico & DNA e Regolazione Genica

---

## Mappa Mentale Globale (B2 + B4)

```mermaid
mindmap
  root((SCIENZE<br/>B2 + B4))
    B2 Metabolismo
      Visione d'insieme
        ATP
        NAD / FAD
        Anabolismo vs Catabolismo
      Glicolisi
        Fase endoergonica −2 ATP
        Fase esoergonica +4 ATP +2 NADH
        Bilancio netto +2 ATP +2 NADH
      Fermentazioni
        Lattica → Lattato
        Alcolica → Etanolo + CO₂
        Ciclo di Cori
      Respirazione cellulare
        Decarbossilazione ossidativa
        Ciclo di Krebs
        Fosforilazione ossidativa
        Chemiosintesi / ATP sintasi
      Bilancio totale +32 ATP
      Biochimica corpo umano
        Glicemia 60-99 mg/dL
        Glicogenosintesi
        Glicogenolisi
        Gluconeogenesi
        Organi: fegato, muscolo, cervello, adiposo
        Insulina / Glucagone / Adrenalina / Cortisolo
      Squilibri
        Diabete tipo 1
        Diabete tipo 2
        Obesità
    B4 DNA e Regolazione
      Struttura acidi nucleici
        Nucleotide: fosfato + zucchero + base
        DNA: doppia elica, antiparallela, complementare
        RNA: singolo filamento, ribosio, uracile
      Flusso informazione
        Replicazione DNA → DNA
        Trascrizione DNA → RNA
        Traduzione RNA → Proteina
        Trascrittasi inversa RNA → DNA
      Regolazione procarioti
        Operoni
        Operone lac inducibile
        Operone trp reprimibile
      Regolazione eucarioti
        Pre-trascrizionale: cromatina, istoni, epigenetica
        Trascrizionale: TATA box, enhancer, fattori di trascrizione
        Post-trascrizionale: splicing, cap, poli-A
        Post-traduzionale: ubiquitina, proteasoma
      Virus
        Struttura: genoma, capside, envelope
        Ciclo litico vs lisogeno
        HPV - DNA
        SARS-CoV-2 - RNA
        HIV - retrovirus
        Spillover e zoonosi
      Geni mobili
        Plasmidi
        Coniugazione / Trasduzione / Trasformazione
        Trasposoni
```

---

## Flowchart 1 — Destini del Glucosio

```mermaid
flowchart TD
    A[🍬 GLUCOSIO] --> B[GLICOLISI\n−2 ATP investiti\n+4 ATP + 2 NADH prodotti\nBilancio: +2 ATP]
    B --> C{O₂\ndisponibile?}
    C -- NO --> D[FERMENTAZIONE\nRigenera NAD⁺]
    D --> E[Fermentazione\nLATTICA\nPiruvato → Lattato\nenzima: Lattato deidrogenasi]
    D --> F[Fermentazione\nALCOLICA\nPiruvato → Acetaldeide + CO₂\n→ Etanolo\nenzimi: Piruvato decarbossilasi +\nAlcol deidrogenasi]
    C -- SÌ --> G[2 PIRUVATO\nentra nei mitocondri]
    G --> H[RESPIRAZIONE CELLULARE\n+30 ATP aggiuntivi]
    E --> I[TOTALE: 2 ATP]
    F --> I
    H --> J[TOTALE: ~32 ATP]
```

---

## Flowchart 2 — Ciclo di Krebs

```mermaid
flowchart TD
    A([Acetil-CoA\nC₂]) --> |+ Ossalacetato C₄\nCitrato sintasi| B([Citrato\nC₆])
    B --> |Aconitasi| C([Isocitrato\nC₆])
    C --> |Isocitrato deidrogenasi\n→ NADH + CO₂| D([α-Chetoglutarato\nC₅])
    D --> |α-Chetoglutarato deidrogenasi\n→ NADH + CO₂| E([Succinil-CoA\nC₄])
    E --> |Succinil-CoA sintetasi\n→ GTP/ATP| F([Succinato\nC₄])
    F --> |Succinato deidrogenasi\n→ FADH₂| G([Fumarato\nC₄])
    G --> |Fumarasi| H([Malato\nC₄])
    H --> |Malato deidrogenasi\n→ NADH| I([Ossalacetato\nC₄])
    I --> |Rigenerato per\nun nuovo giro| A
    style A fill:#f9d71c,stroke:#e6a817
    style I fill:#a8e6cf,stroke:#3ddc84
```

---

## Flowchart 3 — Catena Respiratoria + ATP Sintasi

```mermaid
flowchart LR
    subgraph MATRICE["🧪 MATRICE MITOCONDRIALE"]
        NA[NADH] --> CI
        FA[FADH₂\nda Succinato] --> CII
    end
    subgraph MEMBRANA["🫧 MEMBRANA INTERNA"]
        CI["COMPLESSO I\nNADH deidrogenasi\n4H⁺ →"] --> Q[Ubichinone\nQ/QH₂]
        CII["COMPLESSO II\nSuccinato deidrogenasi\n0H⁺"] --> Q
        Q --> CIII["COMPLESSO III\nCitocromo c reduttasi\n4H⁺ →"]
        CIII --> CC[Citocromo c]
        CC --> CIV["COMPLESSO IV\nCitocromo c ossidasi\n4H⁺ →\nO₂ + 4e⁻ → 2H₂O"]
    end
    subgraph SPAZIO["🔴 SPAZIO INTERMEMBRANA\n[H⁺] alta"]
        direction LR
        HP["H⁺  H⁺  H⁺ →"]
    end
    CI -.->|pompa H⁺| HP
    CIII -.->|pompa H⁺| HP
    CIV -.->|pompa H⁺| HP
    HP -->|H⁺ fluisce per gradiente| AS["⚙️ ATP SINTASI\nF₀ canale + F₁ catalitico\nADP + Pᵢ → ATP"]
```

---

## Flowchart 4 — Regolazione Glicemica

```mermaid
flowchart TD
    A{GLICEMIA} -->|> 99 mg/dL\nIperglicemia| B[Pancreas rilascia\nINSULINA]
    A -->|< 60 mg/dL\nIpoglicemia| C[Pancreas rilascia\nGLUCAGONE]
    B --> D[Fegato: Glicogenosintesi\nMuscolo: Captazione glucosio\nAdiposo: Lipogenesi]
    D --> E[Glicemia ↓ → Normalizzazione]
    C --> F[Fegato: Glicogenolisi\nFegato: Gluconeogenesi\nAdiposo: Lipolisi]
    F --> G[Glicemia ↑ → Normalizzazione]
    H[ADRENALINA\nstress/esercizio] -->|risposta rapida| F
    I[CORTISOLO\nstress cronico] -->|stimola gluconeogenesi| F
    E --> A
    G --> A
    style B fill:#c8f5a0,stroke:#5a9e3c
    style C fill:#f5c0c0,stroke:#c0392b
```

---

## Flowchart 5 — Flusso dell'Informazione Genetica

```mermaid
flowchart LR
    A([🧬 DNA]) -->|Replicazione\nElicasi + Primasi\n+ DNA polimerasi| A
    A -->|Trascrizione\nRNA polimerasi\npromotore → terminatore| B([📋 pre-mRNA])
    B -->|Processing:\nSplicing spliceosoma\nCap 5' + Poli-A 3'| C([📄 mRNA maturo])
    C -->|Esportazione dal nucleo| D([🏭 Ribosoma])
    D -->|Traduzione\ntRNA + ribosoma\nAUG → Stop| E([🔩 Polipeptide])
    E -->|Folding + modificazioni\npost-traduzionali| F([✅ Proteina funzionale])
    A2([🔴 RNA] ) -->|Trascrittasi inversa\nRetrovirus: HIV| A3([DNA])
    style A2 fill:#ff9999
    style A3 fill:#99ccff
```

---

## Flowchart 6 — Operone *lac* (Sistema Inducibile)

```mermaid
flowchart TD
    subgraph OFF["❌ LATTOSIO ASSENTE — Operone SPENTO"]
        R1[Repressore attivo] -->|si lega all'operatore| OP1[Operatore bloccato]
        OP1 -->|RNA polimerasi\nnon può procedere| G1["Geni lac NON trascritti\nbeta-galattosidasi, permeasi..."]
    end
    subgraph ON["✅ LATTOSIO PRESENTE — Operone ACCESO"]
        L[Lattosio → Allolattosio\ninduttore] -->|si lega al repressore| R2[Repressore inattivo\nnon lega l'operatore]
        R2 --> OP2[Operatore libero]
        OP2 -->|RNA polimerasi\npuò procedere| G2["Geni lac TRASCRITTI\nbeta-galattosidasi, permeasi..."]
        G2 --> MET["Metabolismo del lattosio ✓"]
    end
```

---

## Flowchart 7 — Operone *trp* (Sistema Reprimibile)

```mermaid
flowchart TD
    subgraph ON["✅ TRIPTOFANO ASSENTE — Operone ACCESO"]
        R1[Repressore inattivo\nnon lega l'operatore] --> OP1[Operatore libero]
        OP1 -->|RNA polimerasi\nprocede| G1["Geni trp TRASCRITTI\nenzimi biosintesi Trp"]
        G1 --> SIN["Sintesi triptofano ✓"]
    end
    subgraph OFF["❌ TRIPTOFANO IN ECCESSO — Operone SPENTO"]
        TRP[Triptofano\ncorepressore] -->|si lega al repressore| R2[Repressore attivo]
        R2 -->|si lega all'operatore| OP2[Operatore bloccato]
        OP2 -->|RNA polimerasi\nbloccata| G2["Geni trp NON trascritti\nfeedback negativo"]
    end
```

---

## Flowchart 8 — 4 Livelli di Regolazione Eucariotica

```mermaid
flowchart TD
    A["🧬 DNA genomico"] -->|Livello 1\nPRE-TRASCRIZIONALE\nCompattazione cromatina\nModificazioni istoni\neterocromatina vs eucromatina| B["Cromatina accessibile"]
    B -->|Livello 2\nTRASCRIZIONALE\nTATA box + fattori generali\nFattori specifici di trascrizione\nEnhancer| C["📋 Trascritto primario\npre-mRNA"]
    C -->|Livello 3\nPOST-TRASCRIZIONALE\nSplicing introni via spliceosoma\nCap 5' + Coda poli-A\nStabilità mRNA| D["📄 mRNA maturo"]
    D -->|Traduzione| E["🔩 Proteina neosintetizzata"]
    E -->|Livello 4\nPOST-TRADUZIONALE\nModificazioni chimiche\nTagli proteolitici\nUbiquitina + Proteasoma| F["✅ Proteina attiva\no ♻️ degradata"]
    style A fill:#dce8f5
    style F fill:#d5f5dc
```

---

## Flowchart 9 — Ciclo Litico vs Lisogeno

```mermaid
flowchart TD
    A[Fago si lega alla cellula] --> B[Iniezione DNA fagico]
    B --> C{Scelta del ciclo}
    C -->|Condizioni favorevoli| D[🔴 CICLO LITICO]
    C -->|Condizioni sfavorevoli| E[🟢 CICLO LISOGENO]
    D --> D1[DNA fagico rimane nel citoplasma]
    D1 --> D2[La cellula trascrive e traduce il DNA virale]
    D2 --> D3[Assemblaggio di molti nuovi fagi]
    D3 --> D4[💥 Lisi cellulare\nLiberazione virioni]
    D4 --> A
    E --> E1[DNA virale si integra nel cromosoma batterico\n= PROFAGO]
    E1 --> E2[Il profago si replica con\nogni divisione cellulare]
    E2 --> E3{Stress / UV?}
    E3 -->|Induzione| D
    E3 -->|No| E2
    style D fill:#ffcccc,stroke:#cc0000
    style E fill:#ccffcc,stroke:#009900
```

---

## Tabelle Flash

### Bilancio energetico: Fermentazione vs Respirazione

| | **Fermentazione** | **Respirazione cellulare** |
|---|---|---|
| Condizioni | Anaerobiche | Aerobiche |
| ATP prodotto | **2 ATP** | **~32 ATP** |
| Prodotti finali | Lattato o Etanolo + $CO_2$ | $CO_2$ + $H_2O$ |
| Ossidazione glucosio | Incompleta | Completa |
| NAD⁺ rigenerato | Sì (tramite fermentazione) | Sì (tramite catena respiratoria) |

---

### Fermentazione lattica vs alcolica

| | **Fermentazione lattica** | **Fermentazione alcolica** |
|---|---|---|
| Organismo | Muscolo, *Lactobacillus* | Lieviti (*Saccharomyces*) |
| Prodotto finale | **Lattato** | **Etanolo + $CO_2$** |
| N° reazioni | 1 | 2 |
| Enzima(i) | Lattato deidrogenasi | Piruvato decarbossilasi + Alcol deidrogenasi |
| Applicazioni | Yogurt, formaggi | Birra, vino, pane |

---

### Tappe del Ciclo di Krebs con prodotti

| Tappa | Da → A | Prodotti energetici |
|---|---|---|
| 1 | Acetil-CoA + Ossalacetato → Citrato | — |
| 2 | Citrato → Isocitrato | — |
| 3 | Isocitrato → α-Chetoglutarato | NADH + $CO_2$ |
| 4 | α-Chetoglutarato → Succinil-CoA | NADH + $CO_2$ |
| 5 | Succinil-CoA → Succinato | GTP/ATP |
| 6 | Succinato → Fumarato | $\text{FADH}_2$ |
| 7 | Fumarato → Malato | — |
| 8 | Malato → Ossalacetato | NADH |
| **Totale/giro** | | **3 NADH + 1 FADH₂ + 1 GTP** |

---

### Ormoni e effetti metabolici

| Ormone | Prodotto da | Effetto glicemia | Glicogenosintesi | Glicogenolisi | Gluconeogenesi | Lipogenesi |
|---|---|---|---|---|---|---|
| **Insulina** | Cellule β pancreas | ↓ | ↑ | ↓ | ↓ | ↑ |
| **Glucagone** | Cellule α pancreas | ↑ | ↓ | ↑ | ↑ | ↓ |
| **Adrenalina** | Midollare surrene | ↑ | ↓ | ↑ | ↑ | ↓ |
| **Cortisolo** | Corticale surrene | ↑ | ↓ | — | ↑ | — |

---

### DNA vs RNA

| Caratteristica | **DNA** | **RNA** |
|---|---|---|
| Zucchero | 2-Desossiribosio | Ribosio |
| Basi | A, G, C, **T** | A, G, C, **U** |
| Struttura | Doppia elica | Singolo filamento |
| Stabilità | Alta | Bassa |
| Localizzazione | Nucleo, mitocondri | Nucleo → citoplasma |
| Funzione | Archivio informazione genetica | Trasmissione + traduzione |

---

### Operone *lac* vs operone *trp*

| Caratteristica | **Operone *lac*** | **Operone *trp*** |
|---|---|---|
| Via metabolica | Catabolica (demolizione lattosio) | Anabolica (sintesi triptofano) |
| Tipo di sistema | **Inducibile** | **Reprimibile** |
| Stato di default | *Spento* (OFF) | *Acceso* (ON) |
| Molecola chiave | *Allolattosio* (induttore) | *Triptofano* (corepressore) |
| Meccanismo ON | Induttore distacca repressore dall'operatore | Assenza di corepressore → repressore inattivo |
| Meccanismo OFF | Repressore libero blocca operatore | Corepressore attiva repressore → blocca operatore |
| Logica biologica | Si accende quando il substrato è disponibile | Si spegne quando il prodotto è in eccesso |

---

### 4 Livelli di regolazione eucariotica

| Livello | Fase | Meccanismo principale | Attori chiave |
|---|---|---|---|
| **1** | Pre-trascrizionale | Compattazione della cromatina | Istoni, metilazione, acetilazione, codice istonico |
| **2** | Trascrizionale | Controllo dell'RNA polimerasi | TATA box, fattori generali e specifici di trascrizione, enhancer |
| **3** | Post-trascrizionale | Maturazione e stabilità dell'mRNA | Spliceosoma, cap 5', coda poli-A, miRNA |
| **4** | Post-traduzionale | Attività e degradazione delle proteine | Modificazioni chimiche, tagli proteolitici, ubiquitina, proteasoma |

---

## Concetti da non confondere

### Da B2 — Metabolismo Energetico

1. **Anabolismo ≠ Catabolismo**
   - *Anabolismo:* sintesi di molecole complesse, endoergonico, consuma ATP
   - *Catabolismo:* degradazione di molecole, esoergonico, produce ATP

2. **Glicolisi ≠ Gluconeogenesi**
   - *Glicolisi:* glucosio → piruvato (catabolismo, produce 2 ATP)
   - *Gluconeogenesi:* precursori non glucidici → glucosio (anabolismo, consuma ATP); le tappe sono simili ma inverse e usano enzimi diversi nelle 3 reazioni irreversibili

3. **Fermentazione ≠ Respirazione cellulare**
   - *Fermentazione:* rigenera NAD⁺ senza consumare O₂, produce solo 2 ATP totali
   - *Respirazione:* ossidazione completa con O₂, produce ~32 ATP

4. **Glicogenolisi ≠ Gluconeogenesi**
   - *Glicogenolisi:* mobilizzazione del glicogeno già immagazzinato → glucosio
   - *Gluconeogenesi:* sintesi di nuovo glucosio da precursori non glucidici (lattato, piruvato, amminoacidi)

5. **Fosforilazione a livello del substrato ≠ Fosforilazione ossidativa**
   - *A livello del substrato:* il fosfato è ceduto direttamente da un metabolita all'ADP (es. nella glicolisi, tappe 7 e 10)
   - *Ossidativa:* ATP è prodotto dall'ATP sintasi usando il gradiente protonico (mitocondrio)

### Da B4 — DNA e Regolazione Genica

6. **Nucleoside ≠ Nucleotide**
   - *Nucleoside:* base azotata + zucchero (legame N-glicosidico)
   - *Nucleotide:* nucleoside + gruppo fosfato (legame estereo)

7. **Trascrizione ≠ Traduzione**
   - *Trascrizione:* DNA → RNA (nel nucleo, RNA polimerasi)
   - *Traduzione:* mRNA → Proteina (nel citoplasma, ribosomi + tRNA)

8. **Operone *lac* (inducibile) ≠ Operone *trp* (reprimibile)**
   - *lac:* spento di default, si accende in presenza del substrato (lattosio/allolattosio)
   - *trp:* acceso di default, si spegne in presenza del prodotto finale (triptofano)

9. **Eterocromatina ≠ Eucromatina**
   - *Eterocromatina:* condensata, DNA inaccessibile, trascrizione *inibita*
   - *Eucromatina:* rilassata, DNA accessibile, trascrizione *attiva*

10. **Ciclo litico ≠ Ciclo lisogeno**
    - *Litico:* il virus si replica rapidamente, uccide la cellula ospite per lisi
    - *Lisogeno:* il DNA virale si integra (profago) e rimane silente; si trasmette alle cellule figlie

11. **Codone ≠ Anticodone**
    - *Codone:* tripletta di basi sull'mRNA che specifica un amminoacido
    - *Anticodone:* tripletta complementare sul tRNA che riconosce il codone

12. **Introni ≠ Esoni**
    - *Introni:* sequenze non codificanti rimosse dallo spliceosoma
    - *Esoni:* sequenze codificanti unite nell'mRNA maturo

---

## Equazioni chiave in LaTeX

**Glicolisi (bilancio netto):**
$$\text{Glucosio} + 2\,\text{NAD}^+ + 2\,\text{ADP} + 2\,P_i \rightarrow 2\,\text{Piruvato} + 2\,\text{NADH} + 2\,H^+ + 2\,\text{ATP} + 2\,H_2O$$

**Fermentazione lattica:**
$$\text{Glucosio} + 2\,\text{ADP} + 2\,P_i \rightarrow 2\,\text{Lattato} + 2\,\text{ATP} + 2\,H_2O$$

**Fermentazione alcolica:**
$$\text{Glucosio} + 2\,\text{ADP} + 2\,P_i \rightarrow 2\,\text{Etanolo} + 2\,CO_2 + 2\,\text{ATP} + 2\,H_2O$$

**Decarbossilazione ossidativa:**
$$\text{Piruvato} + \text{CoA-SH} + \text{NAD}^+ \xrightarrow{\text{Piruvato deidrogenasi}} \text{Acetil-CoA} + CO_2 + \text{NADH} + H^+$$

**Bilancio ciclo di Krebs (per giro):**
$$\text{Acetil-CoA} + 3\,\text{NAD}^+ + \text{FAD} + \text{ADP} + P_i + 2\,H_2O \rightarrow 2\,CO_2 + 3\,\text{NADH} + \text{FADH}_2 + \text{ATP} + \text{CoA-SH}$$

**Riduzione dell'ossigeno (Complesso IV):**
$$O_2 + 4\,e^- + 4\,H^+ \rightarrow 2\,H_2O$$

**Respirazione cellulare completa:**
$$C_6H_{12}O_6 + 6\,O_2 \rightarrow 6\,CO_2 + 6\,H_2O + 32\,\text{ATP}$$

**Sintesi ATP dall'ATP sintasi:**
$$\text{ADP} + P_i \xrightarrow{\text{ATP sintasi} + \Delta\mu_{H^+}} \text{ATP} + H_2O$$

---

*Ripasso elaborato da B2-raw.md e B4-raw.md — Scienze Naturali Chimiche e Biologiche*
