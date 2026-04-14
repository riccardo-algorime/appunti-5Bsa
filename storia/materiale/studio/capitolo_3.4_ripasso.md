# Ripasso Veloce - Cap. 3.4: L'Europa alla vigilia della Grande guerra

---

## Date fondamentali

| Anno | Evento |
|------|--------|
| **1870** | Francia perde **Alsazia e Lorena** nella guerra franco-prussiana |
| **1882** | **Triplice Alleanza** (Germania, Austria-Ungheria, Italia) |
| **1904** | ***Entente Cordiale*** franco-britannica |
| **1907** | **Convenzione anglo-russa** → nasce la **Triplice Intesa** |
| **1908** | Giovani turchi ottengono Costituzione; Austria annette **Bosnia-Erzegovina**; Bulgaria indipendente |
| **1911** | **Seconda crisi marocchina**; guerra italo-turca in Libia |
| **1912** | **Prima guerra balcanica**: Lega balcanica vs Impero ottomano |
| **1913** | **Seconda guerra balcanica**: Serbia raddoppia il territorio; Germania rinuncia alla gara navale |

---

## 1. L'Europa divisa in blocchi

Tra fine '800 e inizio '900 la competizione tra potenze diventa **mondiale**: non più equilibrio europeo, ma **potere planetario** con logica di scontro finale.

Due blocchi si formano in un quindicennio:
- **Triplice Intesa** (Francia, Russia, Gran Bretagna): alleanza franco-russa (anni 1890) + *Entente Cordiale* (1904) + convenzione anglo-russa (1907)
- **Triplice Alleanza** (Germania, Austria-Ungheria, Italia): trattato 1882, ma l'Italia si avvicina alla Francia dal 1898

```mermaid
flowchart TD
    A["Germania rifiuta il trattato<br/>di controassicurazione con la Russia"] --> B["Alleanza franco-russa<br/>(anni 1890)"]
    B -->|"valenza antitedesca"| C["Entente Cordiale<br/>franco-britannica (1904)"]
    B -->|"valenza antibritannica"| C
    C --> D["Convenzione anglo-russa<br/>(1907)"]
    D --> E["TRIPLICE INTESA<br/>Francia + Russia + Gran Bretagna"]
    F["Triplice Alleanza (1882)<br/>Germania + Austria + Italia"] -.->|"contrapposizione"| E
    G["Italia si avvicina<br/>alla Francia (1898)"] -.->|"posizione ambigua"| F
```

**Aree di tensione** nel 1914: Alsazia-Lorena, Trentino-Trieste, Bosnia, Transilvania, Macedonia, Bosforo.

---

## 2. Crisi marocchine e isolamento tedesco

### Prima crisi marocchina (1905)
- Francia invia missione a Fez col consenso di GB, Italia → Germania esclusa
- Guglielmo II va a Tangeri per sfidare Parigi
- **Conferenza di Algeciras**: Germania isolata (solo Vienna la appoggia), sconfitta diplomatica

```mermaid
flowchart LR
    A["Francia invia missione<br/>a Fez (gen. 1905)"] --> B["Germania esclusa<br/>dagli accordi"]
    B --> C["Guglielmo II<br/>va a Tangeri (mar. 1905)"]
    C --> D["Conferenza di<br/>Algeciras"]
    D --> E{"Chi appoggia chi?"}
    E -->|"Pro Francia"| F["GB, Spagna,<br/>Italia, Russia"]
    E -->|"Pro Germania"| G["Solo Austria"]
    F --> H["Germania sconfitta<br/>e isolata"]
    G --> H
    H --> I["Accordo 1909:<br/>Berlino rinuncia al Marocco"]
```

### Seconda crisi marocchina (1911)
- Francia invia truppe a Fez; incrociatore tedesco ad Agadir
- Esito: Marocco diventa **protettorato francese**, Germania riceve territori nel Congo

### Isolamento e questione navale
- Germania teme **accerchiamento**, reagisce con retorica aggressiva
- Francia: **revanscismo** per Alsazia-Lorena; GB: Reich come minaccia navale
- Riarmo navale tedesco fallimentare (19 navi DE vs 44 GB nel 1905) → rinuncia nel 1913

```mermaid
flowchart TD
    A["Isolamento tedesco<br/>dopo le crisi marocchine"] --> B["Timore di accerchiamento"]
    B --> C["Retorica aggressiva<br/>del Kaiser"]
    B --> D["Potenziamento<br/>della flotta"]
    D --> E["Rivalita navale<br/>con la Gran Bretagna"]
    E --> F["Divario incolmabile:<br/>19 navi DE vs 44 GB (1905)"]
    F --> G["Germania rinuncia<br/>alla gara navale (1913)"]
    H["Francia: revanscismo<br/>per Alsazia e Lorena"] --> I["Germanofobia<br/>diffusa in Europa"]
    C --> I
    E --> I
```

---

## 3. Tensioni e guerre nei Balcani

### Nazionalismo serbo
La Serbia aspirava a una **"grande Serbia"** estesa su territori con forte presenza slava. Programma destabilizzante: i serbi erano minoranza in Bosnia, Voivodina, Croazia, Kosovo, Macedonia.

### Giovani turchi e crisi dell'Impero ottomano
- **1896**: nasce il **CUP** (Comitato unione e progresso) → militanti detti "Giovani turchi"
- Duplice natura: formazione occidentale-liberale + sentimento antieuropeo
- **Maggio 1908**: ribellione del CUP, sultano concede la Costituzione
- Le potenze ne approfittano: Bulgaria indipendente (5 ott.), Austria annette Bosnia (6 ott.)
- Ideologia passa da **ottomanismo** (Stato inclusivo) a **nazionalismo turco**

```mermaid
timeline
    title Crisi dell'Impero ottomano e Giovani turchi
    1896 : Fondazione del CUP<br/>in ambienti studenteschi
    1906 : Societa segreta<br/>nasce a Salonicco
    1907 : Societa segreta<br/>confluisce nel CUP
    Maggio 1908 : Ribellione del CUP<br/>Sultano concede la Costituzione
    Ottobre 1908 : Bulgaria indipendente<br/>Austria annette Bosnia-Erzegovina
    Aprile 1909 : Creta si unisce<br/>alla Grecia
    Dopo 1909 : Giovani turchi passano<br/>da ottomanismo a nazionalismo turco
```

### Annessione della Bosnia (1908) - Conseguenze
- Crisi diplomatica risolta solo con la Grande guerra
- 1909: Germania impone a Russia e Serbia di riconoscere l'annessione
- Rottura dell'accordo Austria-Russia del 1897
- **Radicalizzazione nazionalista** in Russia, Italia e Serbia

```mermaid
flowchart TD
    ANN["Annessione Bosnia-Erzegovina (1908)"] --> MOB["Mobilitazioni: Austria, Russia, Serbia, Italia"]
    MOB --> GER["Germania impone riconoscimento (1909)"]
    ANN --> ROTT["Rottura dell'accordo Austria-Russia del 1897"]
    ROTT --> RAD["Radicalizzazione nazionalista"]
    RAD --> RUS["Russia: umiliazione,<br/>circoli espansionisti"]
    RAD --> ITA["Italia: nascita<br/>del movimento nazionalista"]
    RAD --> SRB["Serbia: Austria<br/>come nemico principale"]
```

### Guerre balcaniche
- **Guerra in Libia** (1911-12): conferma che le potenze non proteggono più l'Impero ottomano
- **Prima guerra balcanica** (ott-dic 1912): Lega balcanica (Serbia, Bulgaria, Montenegro, Grecia) sconfigge l'Impero ottomano
- **Seconda guerra balcanica** (giu-ago 1913): Grecia, Serbia, Romania e Imp. ottomano contro Bulgaria → Bulgaria sconfitta
- **Serbia vera vincitrice**: raddoppia superficie e popolazione
- Nasce lo **Stato albanese** (Valona nov. 1912, sancito maggio 1913)

```mermaid
flowchart TD
    subgraph PGB["PRIMA GUERRA BALCANICA (ott-dic 1912)"]
        direction LR
        L["Lega balcanica:<br/>Serbia, Bulgaria,<br/>Montenegro, Grecia"] -->|"contro"| O["Impero ottomano"]
        O --> R1["Disfatta ottomana"]
    end
    subgraph SGB["SECONDA GUERRA BALCANICA (giu-ago 1913)"]
        direction LR
        C["Grecia, Serbia,<br/>Romania, Imp. ottomano"] -->|"contro"| BU["Bulgaria"]
        BU --> R2["Bulgaria sconfitta"]
    end
    PGB --> D["Contesa sulla Macedonia<br/>tra ex alleati"]
    D --> SGB
    SGB --> V["Serbia: vera vincitrice<br/>raddoppia territorio"]
    SGB --> OT["Imp. ottomano recupera<br/>Tracia e Adrianopoli"]
    SGB --> AL["Nasce lo Stato<br/>albanese indipendente"]
```

### Conseguenze
- Violenze sui civili (massacri in Macedonia), ~330.000 musulmani in fuga verso l'Impero ottomano
- Prima convenzione internazionale per **scambio di popolazione** (Adrianopoli, 1913)
- Russia si avvicina a Serbia e Romania; Bulgaria si accosta all'Austria
- Francia rafforza l'alleanza con la Russia, finanzia ferrovie strategiche anti-tedesche
- **Serbia = spina nel fianco dell'Austria**: alleata della Russia, Stato più potente dei Balcani, minaccia l'unità dell'Impero con il progetto di unire gli slavi del sud

---

## 4. Verso l'abisso?

### Corsa agli armamenti e clima bellicoso
- Dal 1913: vera **corsa agli armamenti**
- L'industrializzazione russa impensierisce Austria e Germania → idea di **guerra preventiva** (il fattore tempo è sfavorevole)
- Clima culturale pro-guerra: **darwinismo sociale**, **militarismo**, guerra come **funzione catartica**
- Queste idee diffuse tra giovani borghesi e intellettuali (in Italia: i "vociani" della rivista *La Voce*, 1908)

```mermaid
flowchart LR
    subgraph GUERRA["Spinte BELLICISTE"]
        A["Darwinismo sociale:<br/>prevalere o soccombere"]
        B["Militarismo:<br/>ordine, gerarchia, onore"]
        C["Guerra catartica:<br/>purificazione della societa"]
        D["Giovani borghesi<br/>e circoli intellettuali"]
    end
    subgraph PACE["Spinte PACIFISTE"]
        E["Movimento operaio<br/>e Seconda Internazionale"]
        F["Reti scientifiche<br/>e accademiche transnazionali"]
        G["Pacifismo umanitario,<br/>socialista, cristiano"]
        H["Diritto internazionale:<br/>Ginevra e Aia"]
    end
    GUERRA -->|"tensione"| I["Europa 1914"]
    PACE -->|"tensione"| I
```

### Spinte pacifiste
- Internazionalismo nel movimento operaio (**Seconda Internazionale**) e in ambienti scientifici
- Tre correnti pacifiste: umanitario-borghese, socialista, cristiana
- **Bertha von Suttner** (Nobel pace 1905): disarmo e arbitrato internazionale
- **Diritto internazionale**: conferenze di Ginevra (Croce Rossa, 1864) e dell'Aia (1899, 1907)

### Guerra non inevitabile
- Dal 1871 nessuna guerra diretta tra grandi potenze (40 anni di pace)
- Dal 1815 nessuna guerra generale europea (100 anni)
- Nel giugno 1914 gli storici ritengono che la diplomazia avrebbe potuto evitare il conflitto

---

## Schema riassuntivo dei nessi

```mermaid
flowchart TD
    A["Nuovo orizzonte planetario: competizione per il potere mondiale"] --> B["Formazione di due blocchi contrapposti"]
    B --> C["Triplice Intesa (FR, RU, GB)"]
    B --> D["Triplice Alleanza (DE, AU, IT)"]
    C --> E["Crisi marocchine (1905, 1911)"]
    D --> E
    E --> F["Isolamento della Germania"]
    F --> G["Riarmo navale tedesco + retorica aggressiva"]
    G --> H["Germanofobia in Francia e Gran Bretagna"]
    
    I["Crisi Impero ottomano + nazionalismi balcanici"] --> J["Annessione Bosnia-Erzegovina (1908)"]
    J --> K["Rivalita Austria-Russia nei Balcani"]
    J --> L["Radicalizzazione nazionalismi"]
    I --> M["Guerre balcaniche (1912-1913)"]
    M --> N["Serbia raddoppia territorio e potenza"]
    M --> O["Uscita di scena dell'Impero ottomano"]
    N --> P["Serbia: spina nel fianco dell'Austria"]
    K --> Q["Corsa agli armamenti dal 1913"]
    H --> Q
    P --> Q
    Q --> R["Giugno 1914: quadro denso di tensioni, ma guerra non inevitabile"]
```

---

## Mappa concettuale

```mermaid
mindmap
  root("**Cap. 3.4: L'Europa alla vigilia<br/>della Grande guerra**")
    ("**1. Europa divisa in blocchi**")
      ("Nuovo orizzonte planetario:<br/>competizione mondiale")
      ("Triplice Intesa<br/>Francia + Russia + GB")
        ("Alleanza franco-russa (anni 1890)")
        ("Entente Cordiale (1904)")
        ("Convenzione anglo-russa (1907)")
      ("Triplice Alleanza<br/>Germania + Austria + Italia")
        ("Trattato del 1882")
        ("Italia in posizione ambigua<br/>dal 1898")
    ("**2. Crisi marocchine<br/>e isolamento tedesco**")
      ("Prima crisi marocchina (1905)")
        ("Conferenza di Algeciras:<br/>Germania sconfitta")
      ("Seconda crisi marocchina (1911)")
        ("Marocco diventa<br/>protettorato francese")
      ("Isolamento della Germania")
        ("Timore di accerchiamento")
        ("Riarmo navale fallito")
      ("Germanofobia e revanscismo")
    ("**3. Tensioni e guerre<br/>nei Balcani**")
      ("Nazionalismo serbo:<br/>progetto Grande Serbia")
      ("Crisi dell'Impero ottomano")
        ("Giovani turchi e CUP")
        ("Da ottomanismo a<br/>nazionalismo turco")
      ("Annessione Bosnia (1908)")
        ("Crisi Austria-Russia")
        ("Radicalizzazione nazionalismi")
      ("Guerre balcaniche 1912-1913")
        ("Serbia raddoppia territorio")
        ("Violenze e migrazioni di massa")
        ("Uscita di scena Imp. ottomano")
      ("Serbia: spina nel fianco<br/>dell'Austria")
    ("**4. Verso l'abisso?**")
      ("Corsa agli armamenti dal 1913")
        ("Russia si industrializza")
        ("Germania teme il fattore tempo")
      ("Clima bellicoso")
        ("Darwinismo sociale")
        ("Militarismo e guerra catartica")
      ("Spinte pacifiste")
        ("Seconda Internazionale")
        ("Bertha von Suttner")
        ("Diritto internazionale umanitario")
      ("Giugno 1914:<br/>guerra non inevitabile")
```
