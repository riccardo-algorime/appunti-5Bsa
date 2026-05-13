# Fisica - Appunto compatto per la verifica

> [!summary] Uso del file
> Questo è il ripasso compatto ricavato da [`appunti-verifica-fisica.md`](./appunti-verifica-fisica.md). È diviso per macro-argomenti e tiene insieme teoria, formule e uso pratico. La verifica è valida per orale, quindi le formule non vanno imparate isolate: devi saper dire **cosa significano**, **quando si usano** e **quale idea fisica esprimono**.

> [!warning] Programma reale della prof
> Relatività ristretta ed effetto fotoelettrico. Per Michelson-Morley non servono i dettagli matematici, ma servono scopo e risultato. La simultaneità e la sincronizzazione degli orologi sono abbuonate come parte dettagliata. Le trasformazioni di Lorentz non vanno studiate come teoria. Il fotoelettrico è richiesto soprattutto a livello teorico, non come esercizi applicativi.

---

## 1. Crisi della fisica classica e nascita della relatività ristretta

La relatività ristretta nasce perché la meccanica galileiana e l'elettromagnetismo di Maxwell non sono compatibili se vengono mantenuti entrambi nella forma classica. Galileo descrive bene il passaggio tra sistemi inerziali nella vita quotidiana, dove le velocità sono molto piccole rispetto a \(c\). Maxwell invece porta alla velocità della luce come costante legata alle proprietà del vuoto.

La meccanica galileiana assume che tempo, lunghezze e simultaneità siano assoluti. Inoltre, tra sistemi inerziali in moto rettilineo uniforme, l'accelerazione rimane la stessa:

$$
\vec a' = \vec a
$$

Questa formula significa che, secondo Galileo, due osservatori inerziali possono misurare velocità diverse, ma concordano sull'accelerazione. Se la massa è la stessa, concordano anche sulla risultante delle forze:

$$
\vec R' = \vec R
$$

Il problema compare con la luce. In relatività galileiana le velocità si sommano:

$$
\vec v = \vec v' + \vec u
$$

Qui \(\vec v\) è la velocità del corpo nel sistema \(S\), \(\vec v'\) è la velocità nel sistema \(S'\), e \(\vec u\) è la velocità di \(S'\) rispetto a \(S\). Se questa legge valesse anche per la luce, la velocità della luce cambierebbe da osservatore a osservatore:

$$
\vec c = \vec c' + \vec u
$$

Maxwell invece porta a:

$$
c = \frac{1}{\sqrt{\varepsilon_0\mu_0}}
$$

Questa formula dice che la velocità della luce nel vuoto dipende da costanti elettromagnetiche del vuoto, non dal moto dell'osservatore. Qui nasce il conflitto fondamentale: per Galileo \(c\) dovrebbe variare, per Maxwell sembra costante.

> [!important] Da dire all'orale
> La relatività ristretta non nasce perché Galileo "non funziona mai", ma perché Galileo funziona solo come limite per \(v \ll c\). Quando si considerano luce ed elettromagnetismo, la composizione classica delle velocità entra in crisi.

---

## 2. Michelson-Morley

L'esperimento di Michelson e Morley serviva a verificare se la Terra si muovesse rispetto all'etere. L'etere era immaginato come il mezzo privilegiato in cui la luce si propagava con velocità \(c\). Se la Terra si fosse mossa rispetto all'etere, la luce avrebbe dovuto avere tempi di percorrenza diversi in direzioni diverse.

L'apparato usava un interferometro: un fascio di luce veniva diviso in due raggi perpendicolari, riflesso da specchi e poi ricombinato. Se i tempi di percorrenza fossero cambiati ruotando l'apparato, sarebbe cambiata la figura di interferenza.

Il risultato fu nullo: non si osservarono variazioni significative attribuibili al moto della Terra rispetto all'etere. Questo risultato aprì la strada all'idea che non esista un sistema privilegiato e che la velocità della luce sia la stessa in tutti i sistemi inerziali.

> [!warning] Cosa studiare
> Non servono i dettagli matematici dei tempi nei bracci dell'interferometro. Devi sapere **scopo**, **metodo generale**, **risultato nullo** e **importanza per Einstein**.

---

## 3. Postulati di Einstein e sistemi inerziali

Einstein fonda la relatività ristretta su due postulati.

Il primo dice che **le leggi fisiche sono le stesse in tutti i sistemi di riferimento inerziali**. Non vale solo per la meccanica, ma anche per l'elettromagnetismo. Questo elimina l'idea di un sistema privilegiato.

Il secondo dice che **la velocità della luce nel vuoto è la stessa in tutti i sistemi inerziali**, indipendentemente dal moto della sorgente e dell'osservatore.

La relatività ristretta vale per sistemi inerziali, cioè sistemi non accelerati. Quando compaiono accelerazioni importanti, come nel paradosso dei gemelli completo, la situazione non è più simmetrica e il discorso richiede più attenzione.

---

## 4. Fattore di Lorentz

Il fattore fondamentale della relatività ristretta è:

$$
\beta = \frac{v}{c}
$$

\(\beta\) è la velocità espressa come frazione della velocità della luce. Se \(v=0{,}8c\), allora \(\beta=0{,}8\).

$$
\gamma = \frac{1}{\sqrt{1-\beta^2}}
$$

\(\gamma\) è il fattore di Lorentz. Misura quanto diventano importanti gli effetti relativistici. Se \(v\ll c\), \(\gamma \approx 1\), quindi la fisica classica funziona bene. Se \(v\) si avvicina a \(c\), \(\gamma\) cresce molto e tende all'infinito.

Per corpi con massa diversa da zero:

$$
v<c
$$

La velocità della luce è un limite: non si raggiunge con particelle massive.

> [!error] Errore tipico
> \(\gamma\) è **uno fratto la radice**. Se in un esercizio ottieni \(\gamma<1\), quasi certamente hai scritto la formula al contrario.

---

## 5. Dilatazione dei tempi

La relatività ristretta cambia l'idea di tempo: il tempo non è più assoluto. La formula centrale è:

$$
\Delta t = \gamma \Delta t_0
$$

\(\Delta t_0\) è il **tempo proprio**, cioè il tempo misurato dall'osservatore che vede i due eventi accadere nello stesso punto dello spazio. \(\Delta t\) è il tempo misurato da un osservatore che vede quei due eventi in posizioni diverse.

Poiché \(\gamma \geq 1\):

$$
\Delta t \geq \Delta t_0
$$

Il tempo misurato dall'osservatore esterno è più lungo del tempo proprio: questo è il fenomeno della **dilatazione dei tempi**.

> [!important] Come riconoscere il tempo proprio
> Non chiederti "chi si muove?". Chiediti: **chi vede i due eventi nello stesso punto?** Quello misura \(\Delta t_0\).

---

## 6. Contrazione delle lunghezze

Anche la lunghezza non è più assoluta. La formula centrale è:

$$
L = \frac{L_0}{\gamma}
$$

\(L_0\) è la **lunghezza propria**, cioè la lunghezza misurata dall'osservatore che vede l'oggetto fermo. \(L\) è la lunghezza misurata da chi vede l'oggetto in movimento.

Poiché \(\gamma \geq 1\), si ha:

$$
L \leq L_0
$$

Quindi un oggetto in moto viene misurato più corto nella direzione del moto. La contrazione riguarda solo le dimensioni parallele al moto; le dimensioni perpendicolari non si contraggono.

> [!tip] Negli esercizi
> Devi usare il \(\gamma\) relativo alla velocità dell'oggetto rispetto all'osservatore che misura la lunghezza. Non esiste un gamma unico per tutto l'esercizio.

---

## 7. Muoni

I muoni sono particelle instabili prodotte nell'alta atmosfera dai raggi cosmici. Hanno vita media propria circa:

$$
\Delta t_0 = 2{,}2 \cdot 10^{-6}\ \text{s}
$$

Se si usasse la fisica classica, con \(v=0{,}995c\), percorrerebbero solo:

$$
d = v\Delta t_0 \approx 0{,}995c \cdot 2{,}2\cdot 10^{-6} \approx 657\ \text{m}
$$

Questa distanza non basterebbe per arrivare al suolo. Però per l'osservatore terrestre il tempo di vita del muone è dilatato:

$$
\Delta t = \gamma \Delta t_0
$$

Con \(v=0{,}995c\), \(\gamma \approx 10\), quindi:

$$
d \approx 0{,}995c \cdot \Delta t_0 \cdot \gamma \approx 6570\ \text{m}
$$

I muoni sono importanti perché mostrano che la dilatazione dei tempi non è solo un esperimento mentale: ha conseguenze osservabili.

---

## 8. Paradosso dei gemelli

Nel paradosso dei gemelli, un gemello resta sulla Terra e l'altro viaggia su un'astronave a velocità relativistica. Per il gemello che viaggia, il tempo proprio del viaggio può essere molto più piccolo del tempo misurato sulla Terra.

Se il gemello viaggiatore misura:

$$
\Delta t_0 = 10\ \text{anni}
$$

e viaggia a:

$$
v = 0{,}98c
$$

allora \(\gamma \approx 5\), quindi sulla Terra passa circa:

$$
\Delta t = \gamma \Delta t_0 \approx 50\ \text{anni}
$$

Il punto teorico non è solo che uno invecchia meno. Il paradosso nasce perché sembrerebbe che ciascuno possa dire che è l'altro a muoversi. La risoluzione è che i due sistemi non sono equivalenti: l'astronave accelera, decelera e cambia direzione, quindi il gemello viaggiatore non resta sempre nello stesso sistema inerziale.

---

## 9. Composizione relativistica delle velocità

In Galileo le velocità si sommano:

$$
v = v' + u
$$

In relatività ristretta questa formula viene sostituita, lungo la direzione del moto, da:

$$
v_x' = \frac{v_x-u}{1-\frac{uv_x}{c^2}}
$$

Questa formula dà la velocità del corpo in \(S'\), sapendo la sua velocità \(v_x\) in \(S\) e la velocità \(u\) di \(S'\) rispetto a \(S\).

La formula inversa è:

$$
v_x = \frac{v_x'+u}{1+\frac{uv_x'}{c^2}}
$$

Serve quando conosci la velocità nel sistema \(S'\) e vuoi passare a \(S\).

Per le componenti trasversali:

$$
v_y' = \frac{v_y}{\gamma\left(1-\frac{uv_x}{c^2}\right)}
$$

e:

$$
v_z' = \frac{v_z}{\gamma\left(1-\frac{uv_x}{c^2}\right)}
$$

Queste formule sono importanti perché impediscono di ottenere velocità maggiori di \(c\). Se componi \(c\) con qualunque velocità inferiore a \(c\), il risultato resta \(c\), non \(c+u\).

> [!danger] Procedura negli esercizi
> Scegli l'asse, assegna i segni, identifica il sistema di riferimento e non cancellare i segni negativi. Una velocità negativa significa solo che il moto avviene nel verso opposto all'asse scelto.

---

## 10. Quantità di moto relativistica e limite \(c\)

In meccanica classica:

$$
\vec p = m\vec v
$$

In relatività ristretta:

$$
\vec p = \gamma m\vec v
$$

La differenza è decisiva: quando \(v\) si avvicina a \(c\), \(\gamma\) cresce moltissimo, quindi cresce moltissimo anche la quantità di moto. Per aumentare ancora la velocità servirebbe un impulso sempre più grande.

L'impulso è:

$$
\Delta \vec p = \vec F \Delta t
$$

Per portare una particella con massa fino a \(c\), servirebbe \(\Delta p \to \infty\), quindi forza infinita o tempo infinito. Entrambe le possibilità sono fisicamente irrealizzabili. Per questo un corpo con massa diversa da zero non può raggiungere la velocità della luce.

---

## 11. Bertozzi

L'esperimento di Bertozzi del 1964 conferma sperimentalmente che particelle con massa diversa da zero non raggiungono \(c\). Nell'esperimento vengono accelerati elettroni con campi elettrici sempre più intensi. Aumentando l'energia fornita, la velocità cresce, ma si avvicina asintoticamente a \(c\) senza superarla.

L'energia non sparisce: aumenta l'energia relativistica e la quantità di moto, ma non permette di superare la velocità limite.

---

## 12. Dinamica relativistica

Il secondo principio va scritto nella forma generale:

$$
\vec F = \frac{d\vec p}{dt}
$$

In meccanica classica, poiché \(\vec p=m\vec v\), questa formula diventa:

$$
\vec F = m\vec a
$$

In relatività invece:

$$
\vec F = \frac{d}{dt}(\gamma m\vec v)
$$

Non si può semplificare sempre in \(m\vec a\), perché \(\gamma\) dipende da \(v\). A forza finita, mentre \(v\) si avvicina a \(c\), l'accelerazione diminuisce.

Se forza, accelerazione e velocità sono parallele:

$$
F = ma\gamma^3
$$

Questo caso riguarda una forza che prova ad aumentare direttamente il modulo della velocità.

Se l'accelerazione è perpendicolare alla velocità, come nel moto circolare:

$$
F = ma\gamma
$$

Questo caso serve negli esercizi con forza magnetica centripeta.

Il terzo principio classico, azione e reazione simultanee, non è più sicuro nella forma ingenua perché la simultaneità non è assoluta. In relatività conviene usare la conservazione della quantità di moto totale in un sistema isolato:

$$
\vec p_{\text{tot}} = \text{costante}
$$

---

## 13. Energia relativistica

L'energia totale relativistica è:

$$
E = \gamma mc^2
$$

Questa è l'energia totale di una particella con massa \(m\) e velocità \(v\).

Se il corpo è fermo, allora \(v=0\), \(\gamma=1\), e si ottiene l'energia a riposo:

$$
E_0 = mc^2
$$

Questa formula significa che un corpo possiede energia anche solo perché ha massa.

L'energia cinetica relativistica è:

$$
E_c = E - E_0
$$

Sostituendo:

$$
E_c = \gamma mc^2 - mc^2
$$

quindi:

$$
E_c = (\gamma-1)mc^2
$$

Questa è la formula da usare negli esercizi relativistici. Per ricavare la velocità da \(E_c\), prima trovi:

$$
\gamma = \frac{E_c}{mc^2}+1
$$

poi:

$$
\beta = \sqrt{1-\frac{1}{\gamma^2}}
$$

e infine:

$$
v = \beta c
$$

---

## 14. Applicazioni di \(E=mc^2\)

L'equivalenza massa-energia spiega fenomeni reali in cui una piccola variazione di massa corrisponde a molta energia.

Nel **difetto di massa**, la massa di un nucleo formato è minore della somma delle masse dei nucleoni separati. La differenza corrisponde all'energia di legame.

Nel **decadimento radioattivo**, un nucleo instabile si trasforma emettendo energia, collegata alla differenza di massa tra stato iniziale e finale.

Nella **fissione nucleare**, un nucleo pesante colpito da un neutrone si divide in nuclei più leggeri, altri neutroni ed energia. Anche qui la massa non "sparisce": viene convertita in energia secondo \(E=mc^2\).

---

## 15. Conversioni e lavoro elettrico

L'elettronvolt è un'unità di energia:

$$
1\ \text{eV} = 1{,}6\cdot 10^{-19}\ \text{J}
$$

Il megaelettronvolt vale:

$$
1\ \text{MeV} = 10^6\ \text{eV}
$$

quindi:

$$
1\ \text{MeV} = 1{,}6\cdot 10^{-13}\ \text{J}
$$

Per elettroni accelerati da una differenza di potenziale, si usa:

$$
L = \Delta E_c
$$

e per la forza elettrica:

$$
L = -q\Delta V
$$

Negli esercizi spesso basta il valore assoluto:

$$
\Delta E_c = |q|\,|\Delta V|
$$

quindi:

$$
|\Delta V| = \frac{\Delta E_c}{|q|}
$$

---

## 16. Campo magnetico e raggio della traiettoria

Se una particella entra in un campo magnetico con \(\vec v \perp \vec B\), subisce la forza di Lorentz magnetica:

$$
F_L = |q|vB
$$

Questa forza è perpendicolare alla velocità e fa da forza centripeta. In relatività:

$$
F_c = \gamma m\frac{v^2}{r}
$$

Uguagliando:

$$
|q|vB = \gamma m\frac{v^2}{r}
$$

si ricava:

$$
r = \frac{\gamma mv}{|q|B}
$$

Poiché \(p=\gamma mv\), si può anche scrivere:

$$
r = \frac{p}{|q|B}
$$

---

## 17. Effetto fotoelettrico

L'effetto fotoelettrico consiste nell'emissione di elettroni da una lastra metallica colpita da radiazione elettromagnetica. La fisica classica lo interpreta come assorbimento continuo di energia da parte degli elettroni, ma gli esperimenti mostrano due problemi.

Il primo problema riguarda l'intensità. Aumentando l'intensità della radiazione, la corrente può aumentare perché vengono emessi più elettroni, ma il potenziale di arresto non cambia. Quindi l'energia massima degli elettroni non dipende dall'intensità.

Il secondo problema riguarda la frequenza. Gli elettroni escono solo se:

$$
f \geq f_0
$$

Se:

$$
f<f_0
$$

non escono elettroni, anche aspettando molto tempo. Questo contraddice l'idea classica secondo cui l'energia potrebbe accumularsi gradualmente.

Einstein risolve il problema con il modello dei fotoni. La luce è composta da pacchetti di energia:

$$
E = hf
$$

Ogni fotone interagisce con un solo elettrone. L'energia del fotone serve prima a estrarre l'elettrone dal metallo e il resto diventa energia cinetica:

$$
hf = W_0 + E_{c,\max}
$$

Il lavoro di estrazione è:

$$
W_0 = hf_0
$$

quindi:

$$
E_{c,\max} = hf - hf_0
$$

Il potenziale di arresto è collegato all'energia cinetica massima:

$$
E_{c,\max} = |q_e|\Delta V_0
$$

> [!warning] Per la verifica
> La prof ha detto che il fotoelettrico è richiesto a livello teorico, non come esercizi applicativi. Queste formule servono soprattutto per capire il ragionamento: frequenza significa energia del singolo fotone, intensità significa numero di fotoni.

---

## 18. Dualismo onda-corpuscolo

L'effetto fotoelettrico mostra che la luce, che in interferenza e diffrazione si comporta come onda, in certi fenomeni microscopici si comporta come un insieme di corpuscoli: i fotoni.

Il dualismo onda-corpuscolo significa che la radiazione e la materia possono mostrare aspetti ondulatori o corpuscolari a seconda dell'esperimento. Non significa che la luce cambi natura in modo casuale, ma che i modelli classici "solo onda" e "solo particella" non bastano più da soli.

$$
\text{onda} \leftrightarrow \text{corpuscolo}
$$

---

## 19. Domande teoriche da saper dire a voce

1. Perché elettromagnetismo e relatività galileiana entrano in conflitto?
2. Qual era lo scopo dell'esperimento di Michelson-Morley?
3. Perché il risultato nullo di Michelson-Morley è importante?
4. Quali sono i due postulati di Einstein?
5. Che cosa significa sistema di riferimento inerziale?
6. Che cos'è \(\gamma\) e perché cresce vicino a \(c\)?
7. Che cosa sono tempo proprio e lunghezza propria?
8. Perché i muoni arrivano al suolo?
9. Perché il paradosso dei gemelli non è simmetrico?
10. Perché \(c\) è una velocità limite per corpi con massa?
11. Cosa cambia tra quantità di moto classica e relativistica?
12. Che significato fisico ha \(E_0=mc^2\)?
13. Quali fenomeni mostrano l'equivalenza massa-energia?
14. Perché l'effetto fotoelettrico mette in crisi la fisica classica?
15. Come il modello dei fotoni spiega frequenza soglia e intensità?
16. Che cosa significa dualismo onda-corpuscolo?

