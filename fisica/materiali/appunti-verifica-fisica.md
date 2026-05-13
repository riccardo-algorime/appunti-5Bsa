# Appunti completi per la verifica di fisica

> [!summary] Come usare questi appunti
> Questo file ricostruisce tutto il percorso fatto a lezione, nell'ordine in cui gli argomenti sono stati introdotti, ma senza separare meccanicamente per data. L'obiettivo è studiare: capire il filo logico, sapere cosa dire nella parte teorica, riconoscere gli esercizi tipici e ricordare le indicazioni date dalla prof per la verifica.
>
> Le fonti principali sono le trascrizioni delle lezioni in [`trascrizione-lezioni/`](./trascrizione-lezioni/) e gli appunti da immagini in [`trascrizione-app-giulia.md`](./trascrizione-app-giulia.md). Quando la prof parla di schede su Classroom o slide, lo segnalo, ma non invento pagine del libro se non vengono nominate.

---

## Il problema iniziale: elettromagnetismo contro relatività galileiana

Il percorso parte da una crisi: la fisica classica funziona benissimo per moltissimi fenomeni, ma entra in difficoltà quando incontra l'elettromagnetismo di Maxwell. Da una parte c’è l'elettromagnetismo, teoria più recente, fondata sui lavori di Maxwell e Hertz, capace di descrivere in modo molto efficace i fenomeni elettrici, magnetici ed elettromagnetici. Dall'altra c’è la relatività galileiana, molto più antica e consolidata, che descrive il passaggio tra sistemi di riferimento inerziali e su cui poggia la meccanica classica.

La relatività galileiana si porta dietro alcune idee fortissime: il tempo è assoluto, le lunghezze sono assolute, la simultaneità è assoluta, e l'accelerazione è la stessa in sistemi inerziali in moto relativo rettilineo uniforme. In simboli:

$$
\vec a' = \vec a
$$

e quindi, se la massa è la stessa:

$$
\vec R' = \vec R
$$

Inoltre, passando da un sistema inerziale a un altro, le velocità si sommano semplicemente. Se un sistema \(S'\) si muove rispetto a \(S\) con velocità \(u\), allora, in forma elementare:

$$
\vec v = \vec v' + \vec u
$$

Questa idea però crea il primo grande problema con la luce. Per Galileo la velocità della luce dovrebbe dipendere dal sistema di riferimento secondo la composizione delle velocità:

$$
\vec c = \vec c' + \vec v
$$

dove \(\vec c\) è la velocità della luce misurata in \(S\), \(\vec c'\) quella misurata in \(S'\), e \(\vec v\) la velocità di \(S'\) rispetto a \(S\). Dalle equazioni di Maxwell, invece, si ricava una velocità della luce nel vuoto:

$$
c = \frac{1}{\sqrt{\varepsilon_0 \mu_0}}
$$

Il punto delicato è che questa velocità sembra essere una costante fissata dalle proprietà del vuoto, non qualcosa che cambia a seconda dell'osservatore. Se però si applica la composizione galileiana, un osservatore in moto rispetto alla sorgente dovrebbe misurare una velocità della luce diversa: \(c+u\), \(c-u\), o comunque un valore dipendente dal moto relativo. Qui nasce il conflitto.

La prof ha introdotto anche un secondo conflitto attraverso l'origine della forza di Lorentz. Prendiamo due cariche positive che si muovono con la stessa velocità. Nel sistema della Terra si vedono sia la forza elettrica sia la forza magnetica:

$$
\vec R = \vec F_E + \vec F_L
$$

e quindi:

$$
\vec a = \frac{\vec F_E + \vec F_L}{m}
$$

Nel sistema solidale con una delle due particelle, invece, le particelle si vedono reciprocamente ferme. Se sono ferme, la parte magnetica della forza di Lorentz si annulla:

$$
F_L = qvB = 0
$$

Perciò in quel sistema resta solo:

$$
\vec R' = \vec F_E
$$

e:

$$
\vec a' = \frac{\vec F_E}{m}
$$

La relatività galileiana vorrebbe \(\vec a'=\vec a\), ma l'elettromagnetismo porta a risultanti diverse. Anche qui si vede che le due teorie non possono essere entrambe mantenute nella forma classica.

> [!important] Punto da saper spiegare in verifica
> Non basta dire "la velocità della luce è un problema". Bisogna spiegare **perché**: la relatività galileiana prevede la somma ordinaria delle velocità, mentre l'elettromagnetismo porta a una velocità della luce fissata e indipendente dal sistema di riferimento. La relatività ristretta nasce per risolvere questa incompatibilità.

Fonte: [`01-04-26/transcription.txt`](./trascrizione-lezioni/01-04-26/transcription.txt), [`trascrizione-app-giulia.md`](./trascrizione-app-giulia.md).

---

## L'esperimento di Michelson e Morley

Per capire quale teoria descriva meglio la realtà, Michelson e Morley cercano di verificare l'esistenza del moto della Terra rispetto all'etere. L'etere era immaginato come il mezzo o sistema privilegiato rispetto al quale la luce avrebbe avuto velocità \(c\). Se la Terra si muove rispetto all'etere con velocità \(\vec u\), allora la velocità della luce misurata sulla Terra dovrebbe combinarsi con \(\vec u\).

L'esperimento usa un interferometro. Una sorgente luminosa manda un fascio verso uno specchio semiriflettente. Una parte del fascio prosegue lungo un braccio, un'altra viene deviata lungo un braccio perpendicolare. Entrambi i raggi vengono riflessi da specchi e poi ricombinati su uno schermo, dove formano una figura di interferenza.

L'idea è questa: se la Terra si muove rispetto all'etere, i due raggi dovrebbero impiegare tempi diversi nei due bracci, perché il moto terrestre si compone diversamente con il percorso parallelo e perpendicolare. Ruotando l'apparato, la differenza di tempo dovrebbe cambiare e quindi dovrebbe cambiare anche la figura di interferenza.

Il risultato però non mostra variazioni significative. La prof sottolinea che Michelson e Morley condussero l'esperimento per anni e in condizioni diverse, quindi non si tratta di una prova fatta superficialmente. La mancata osservazione di un effetto netto apre varie possibilità: forse la Terra è un sistema privilegiato, forse l'esperimento non è adatto, oppure forse la velocità della luce è davvero la stessa in ogni sistema inerziale.

Einstein sceglie l'ultima via e costruisce la relatività ristretta.

> [!warning] Per la verifica
> La prof ha detto che **non serve la matematica dell'esperimento di Michelson-Morley**. Serve invece sapere:
> - perché è stato fatto;
> - cosa cercava di misurare;
> - perché il risultato è importante;
> - come prepara la strada alla relatività ristretta.

Fonte: [`01-04-26/transcription.txt`](./trascrizione-lezioni/01-04-26/transcription.txt), [`trascrizione-app-giulia.md`](./trascrizione-app-giulia.md).

---

## I due postulati della relatività ristretta

Einstein costruisce la relatività ristretta partendo da due postulati. Un postulato non è dimostrato dentro la teoria: viene assunto come base e poi si verificano le conseguenze.

Il primo postulato afferma che **le leggi fisiche sono le stesse in tutti i sistemi di riferimento inerziali**. La differenza rispetto a Galileo è decisiva: non si parla solo delle leggi della dinamica, ma anche dell'elettromagnetismo. In questo modo l'elettromagnetismo viene elevato a teoria valida in ogni sistema inerziale, non da correggere ogni volta che si cambia osservatore.

Il secondo postulato afferma che **la velocità della luce nel vuoto è la stessa in tutti i sistemi di riferimento inerziali**, indipendentemente dal moto della sorgente o dell'osservatore.

Questi due postulati obbligano a cambiare idee che nella fisica galileiana sembravano ovvie: simultaneità, tempo, lunghezza, quantità di moto, energia.

> [!tip] Come scriverli in verifica
> Negli appunti della classe compare l'indicazione "scrivi per intero": conviene quindi non ridurre i postulati a due parole chiave. Scrivi che le leggi fisiche, compreso l'elettromagnetismo, sono le stesse in ogni sistema di riferimento inerziale, e che la velocità della luce è la stessa in ogni sistema inerziale indipendentemente dal moto della sorgente o dell'osservatore.

> [!note] Campo di validità
> La relatività ristretta vale per **sistemi di riferimento inerziali**. Se entrano in gioco sistemi accelerati, il quadro corretto è la relatività generale. Questo è importante anche per il paradosso dei gemelli.

Fonte: [`01-04-26/transcription.txt`](./trascrizione-lezioni/01-04-26/transcription.txt).

---

## Simultaneità: il tempo non è più assoluto

Nella relatività galileiana il tempo è assoluto. Se due eventi sono simultanei in un sistema \(S\), allora sono simultanei anche in un sistema \(S'\) in moto rettilineo uniforme rispetto a \(S\). Questa idea funziona nella vita quotidiana perché le velocità ordinarie sono piccolissime rispetto a \(c\).

Einstein cambia la prospettiva partendo da un fatto semplice: la luce ha velocità finita. Se vedo un fulmine lontano, non sto vedendo l'istante esatto in cui è caduto; sto ricevendo la luce partita prima. Per definire due eventi simultanei bisogna quindi tenere conto della distanza e del tempo di propagazione del segnale luminoso.

Due eventi \(E_1\) ed \(E_2\) possono essere detti simultanei per un osservatore se:

- l'osservatore è in quiete rispetto agli eventi;
- è equidistante da \(E_1\) ed \(E_2\);
- riceve i segnali luminosi nello stesso istante.

L'esperimento mentale del treno rende chiara la rottura con Galileo. Un osservatore \(O\) sulla banchina è equidistante dai punti in cui cadono due fulmini alle estremità del treno e riceve i segnali insieme: per lui i fulmini sono simultanei. L'osservatore \(O'\) sul treno, invece, si muove verso uno dei fronti d'onda e si allontana dall'altro; riceve quindi prima un segnale e poi l'altro. Poiché per lui i punti di caduta sono alle estremità del vagone e quindi equidistanti, conclude che gli eventi non sono simultanei.

La conclusione è radicale:

$$
\text{la simultaneità è relativa al sistema di riferimento.}
$$

> [!important] Indicazione della prof
> Per la verifica bisogna sapere che la simultaneità è relativa. La prof ha però detto che non chiederà un tema lunghissimo del tipo: "spiega con il treno e i due fulmini perché non sono simultanei". Serve il concetto, non quattro pagine di racconto.

Fonte: [`01-04-26/transcription.txt`](./trascrizione-lezioni/01-04-26/transcription.txt), [`09-05-26/transcription.txt`](./trascrizione-lezioni/09-05-26/transcription.txt).

---

## Dilatazione dei tempi e tempo proprio

Dopo la simultaneità, la prof introduce la relatività del tempo con l'orologio a luce. Immaginiamo un treno che si muove con velocità relativistica \(u\) rispetto alla banchina. Sul treno c’è una sorgente luminosa che manda un impulso verso uno specchio sul soffitto; il raggio sale, viene riflesso e torna alla sorgente.

Per l'osservatore \(O'\) sul treno, sorgente e specchio sono fermi. Il raggio percorre semplicemente una distanza \(2d\), quindi:

$$
\Delta t_0 = \frac{2d}{c}
$$

Per l'osservatore \(O\) sulla banchina, invece, il treno si muove mentre la luce sale e scende. Il percorso della luce non è verticale ma obliquo. Usando Pitagora sul tratto di andata:

$$
(c \Delta t_a)^2 = (u \Delta t_a)^2 + d^2
$$

Da cui:

$$
\Delta t_a = \frac{d}{\sqrt{c^2-u^2}}
$$

e quindi, per andata e ritorno:

$$
\Delta t = \frac{2d}{\sqrt{c^2-u^2}}
$$

Raccogliendo \(c^2\) sotto radice:

$$
\Delta t = \frac{2d}{c\sqrt{1-\frac{u^2}{c^2}}}
$$

Poiché \(\frac{2d}{c} = \Delta t_0\), otteniamo:

$$
\Delta t = \frac{\Delta t_0}{\sqrt{1-\frac{u^2}{c^2}}}
$$

Si definisce:

$$
\beta = \frac{u}{c}
$$

e:

$$
\gamma = \frac{1}{\sqrt{1-\beta^2}}
$$

Il risultato finale è:

$$
\Delta t = \gamma \Delta t_0
$$

Il tempo proprio \(\Delta t_0\) è il tempo misurato dall'osservatore che vede i due eventi avvenire nella stessa posizione spaziale. Nel caso dell'orologio a luce, gli eventi sono partenza e ritorno dell'impulso alla sorgente; chi li vede nello stesso punto è l'osservatore sul treno.

Poiché \(\gamma \geq 1\), allora:

$$
\Delta t \geq \Delta t_0
$$

Questo significa che il tempo misurato da un osservatore che non vede gli eventi nello stesso punto è più lungo: **dilatazione dei tempi**.

> [!error] Errore tipico
> Non bisogna decidere chi misura il tempo proprio chiedendosi "chi si muove?". La domanda giusta è: **chi vede i due eventi nella stessa posizione?**

Fonte: [`08-04-26/transcription.txt`](./trascrizione-lezioni/08-04-26/transcription.txt), [`trascrizione-app-giulia.md`](./trascrizione-app-giulia.md).

---

## Il fattore di Lorentz

Il fattore di Lorentz è:

$$
\gamma = \frac{1}{\sqrt{1-\frac{u^2}{c^2}}}
$$

Il dominio fisico per corpi con massa diversa da zero è:

$$
-c < u < c
$$

Se \(u=0\), allora \(\gamma = 1\). Se \(u\) è molto minore di \(c\), \(\gamma\) è vicinissimo a 1 e gli effetti relativistici sono praticamente impercettibili. Se invece \(u\) si avvicina a \(c\), \(\gamma\) cresce molto rapidamente e tende all'infinito.

```mermaid
flowchart LR
    A["velocità ordinarie: u << c"] --> B["gamma circa 1"]
    B --> C["regime galileiano: effetti trascurabili"]
    D["velocità relativistiche: u vicina a c"] --> E["gamma molto maggiore di 1"]
    E --> F["dilatazione tempi, contrazione lunghezze, dinamica relativistica"]
```

> [!warning] Errore da evitare in esercizio
> La prof insiste: \(\gamma\) è **uno fratto la radice**, non solo la radice. Se viene \(\gamma < 1\), c’è quasi sicuramente un errore.

Fonte: [`08-04-26/transcription.txt`](./trascrizione-lezioni/08-04-26/transcription.txt), [`09-04-26/transcription.txt`](./trascrizione-lezioni/09-04-26/transcription.txt).

---

## Paradosso dei gemelli

Il paradosso dei gemelli non consiste semplicemente nel fatto che due gemelli possano ritrovarsi con età diverse. Quello, in relatività, è spiegabile con la dilatazione dei tempi. Il vero paradosso nasce se si prova ad applicare simmetricamente la relatività del moto: se si dice che si muove la navicella, il gemello sulla navicella invecchia meno; ma se si dice che si muove la Terra rispetto alla navicella, sembrerebbe dover invecchiare meno il gemello sulla Terra.

La risoluzione sta nel fatto che il viaggio della navicella non è tutto in un unico sistema inerziale. La navicella accelera, decelera, cambia direzione. Chi è sulla navicella può accorgersi dell'accelerazione attraverso forze apparenti. Quindi la situazione non è simmetrica come sembrerebbe.

Per gli esercizi semplificati si usa spesso la formula della dilatazione dei tempi, ma la prof ricorda che una trattazione esatta del paradosso richiederebbe la relatività generale o comunque sistemi accelerati.

Un esempio numerico utile è questo: un gemello parte su un'astronave a velocità \(u=0{,}98c\) e misura un tempo proprio di viaggio:

$$
\Delta t_0 = 10\ \text{anni}
$$

Per il gemello rimasto sulla Terra passa:

$$
\Delta t = \frac{\Delta t_0}{\sqrt{1-\frac{u^2}{c^2}}}
$$

Con \(u=0{,}98c\), \(\gamma\) è circa 5, quindi:

$$
\Delta t \approx 50\ \text{anni}
$$

Al ritorno, il gemello che ha viaggiato ha vissuto 10 anni, mentre quello rimasto sulla Terra ne ha vissuti circa 50: la differenza è di circa 40 anni. Il punto teorico però resta quello detto sopra: non è solo "uno invecchia meno", ma il fatto che la simmetria apparente viene rotta dalle accelerazioni dell'astronave.

Fonte: [`08-04-26/transcription.txt`](./trascrizione-lezioni/08-04-26/transcription.txt).

---

## Esercizi su dilatazione dei tempi

La struttura tipica degli esercizi è:

1. identificare i due eventi;
2. capire chi misura il tempo proprio;
3. usare:

$$
\Delta t = \gamma \Delta t_0
$$

Un esempio discusso riguarda un viaggio verso Alfa Centauri. La distanza Terra-Alfa Centauri è \(4{,}3\) anni luce e la navicella viaggia a \(0{,}95c\). Il tempo nel sistema terrestre è:

$$
\Delta t_{\text{Terra}} = \frac{4{,}3 \text{ anni luce}}{0{,}95c} \approx 4{,}5 \text{ anni}
$$

Questo non è il tempo proprio, perché la Terra vede partenza e arrivo in due posizioni diverse. Il tempo proprio è quello misurato dall'astronauta, perché nel suo sistema prima la Terra e poi Alfa Centauri passano dalla sua posizione. Quindi:

$$
\Delta t_0 = \frac{\Delta t}{\gamma}
$$

con:

$$
\gamma = \frac{1}{\sqrt{1-0{,}95^2}} \approx 3{,}2
$$

e quindi:

$$
\Delta t_0 \approx \frac{4{,}5}{3{,}2} \approx 1{,}4 \text{ anni}
$$

> [!tip] Consiglio della prof
> Non usare i \(4{,}3\) anni luce come se fossero automaticamente il tempo della navicella. \(4{,}3\) anni è il tempo che impiegherebbe la luce, non un corpo che viaggia a \(0{,}95c\).

Fonte: [`11-04-26/transcription.txt`](./trascrizione-lezioni/11-04-26/transcription.txt).

---

## Contrazione delle lunghezze e lunghezza propria

La relatività galileiana considerava la lunghezza un invariante: un segmento ha la stessa lunghezza in tutti i sistemi inerziali. In relatività ristretta non è più così.

La prof introduce il problema con due pali fissi sulla banchina e un treno che passa. La distanza tra i pali può essere calcolata misurando il tempo che il treno impiega a passare dal primo al secondo palo e moltiplicando per la velocità.

Per l'osservatore \(O\) sulla banchina:

$$
d = u \Delta t
$$

Per l'osservatore \(O'\) sul treno:

$$
d' = u \Delta t_0
$$

Poiché:

$$
\Delta t = \gamma \Delta t_0
$$

si ottiene:

$$
d = \gamma d'
$$

La notazione \(d\), \(d'\) però può confondere, quindi si introduce la **lunghezza propria** \(L_0\), cioè la lunghezza misurata dall'osservatore che vede il segmento fermo. La relazione viene scritta:

$$
L = \frac{L_0}{\gamma}
$$

La lunghezza misurata da chi vede il segmento in movimento è minore della lunghezza propria: **contrazione delle lunghezze**.

> [!important] Dettaglio essenziale
> La contrazione riguarda solo le lunghezze parallele alla direzione del moto. Le dimensioni perpendicolari al moto non si contraggono.

Esempio: se un treno si muove orizzontalmente, la sua lunghezza si contrae per l'osservatore a terra, ma la sua altezza resta uguale. Un quadrato in moto può essere visto come un rettangolo; una circonferenza può apparire come un'ellisse.

Fonte: [`09-04-26/transcription.txt`](./trascrizione-lezioni/09-04-26/transcription.txt), [`11-04-26/transcription.txt`](./trascrizione-lezioni/11-04-26/transcription.txt), [`trascrizione-app-giulia.md`](./trascrizione-app-giulia.md).

---

## I muoni come evidenza della relatività ristretta

I muoni sono particelle instabili prodotte nell'alta atmosfera dall'interazione dei raggi cosmici con l'atmosfera. Hanno un tempo di vita medio, misurato nel sistema in cui sono fermi, circa:

$$
\Delta t_0 = 2{,}2 \cdot 10^{-6}\ \text{s}
$$

Se si facesse un calcolo classico, con velocità circa \(0{,}995c\), la distanza percorsa sarebbe:

$$
d = 0{,}995c \cdot 2{,}2 \cdot 10^{-6} \approx 657\ \text{m}
$$

Questa distanza non basterebbe per spiegare perché osserviamo muoni al suolo, visto che si formano molto più in alto. La spiegazione relativistica è che il tempo di vita misurato dalla Terra non è il tempo proprio: per l'osservatore terrestre nascita e decadimento avvengono in posizioni diverse, quindi il tempo è dilatato.

$$
\Delta t = \gamma \Delta t_0
$$

Con:

$$
\gamma = \frac{1}{\sqrt{1-0{,}995^2}} \approx 10
$$

La distanza percorsa diventa dell'ordine di:

$$
d \approx 0{,}995c \cdot \Delta t_0 \cdot \gamma \approx 6570\ \text{m}
$$

Questo rende comprensibile l'arrivo dei muoni fino al suolo.

> [!note] Per la verifica
> La prof ha citato i muoni tra le schede di Classroom. Sono un esempio importante per collegare teoria e realtà sperimentale: non sono solo un esperimento mentale.

Fonte: [`11-04-26/transcription.txt`](./trascrizione-lezioni/11-04-26/transcription.txt), [`trascrizione-app-giulia.md`](./trascrizione-app-giulia.md).

---

## Trasformazioni di Lorentz

Lorentz introduce queste trasformazioni prima del 1905 per conciliare elettromagnetismo e relatività galileiana. Einstein le ricava poi in modo autonomo dai postulati della relatività ristretta, dando loro un significato fisico.

Si considera un sistema \(S'\) in moto con velocità \(u\) lungo l'asse \(x\) positivo rispetto a \(S\). Le origini coincidono a \(t=t'=0\). Le trasformazioni sono:

$$
\begin{cases}
x' = \gamma(x-ut) \\
y' = y \\
z' = z \\
t' = \gamma\left(t - \frac{\beta}{c}x\right)
\end{cases}
$$

dove:

$$
\beta = \frac{u}{c}
\qquad
\gamma = \frac{1}{\sqrt{1-\beta^2}}
$$

Le trasformazioni galileiane erano:

$$
\begin{cases}
x' = x-ut \\
y' = y \\
z' = z \\
t' = t
\end{cases}
$$

Se \(u \ll c\), allora \(\beta \approx 0\) e \(\gamma \approx 1\). Le trasformazioni di Lorentz si riducono a quelle di Galileo. Questo mostra che la relatività galileiana non è "falsa" in assoluto: è un caso limite valido per velocità molto piccole rispetto alla luce.

> [!warning] Indicazione esplicita sulla verifica
> Alla domanda sulla prova del 20, la prof ha detto che **non metterà la parte teorica sulle trasformazioni di Lorentz** e non vi farà ricavare le leggi di composizione da esse. Però le trasformazioni restano lo sfondo teorico da cui nascono le formule usate.

Fonte: [`15-04-26/transcription.txt`](./trascrizione-lezioni/15-04-26/transcription.txt), [`09-05-26/transcription.txt`](./trascrizione-lezioni/09-05-26/transcription.txt).

---

## Composizione relativistica delle velocità

Dalle trasformazioni di Lorentz si ricava la composizione relativistica delle velocità. Se \(S'\) si muove rispetto a \(S\) con velocità \(u\) lungo \(x\), e un corpo ha velocità \(v_x\) in \(S\), allora la sua velocità in \(S'\) è:

$$
v_x' = \frac{v_x-u}{1-\frac{uv_x}{c^2}}
$$

La formula inversa è:

$$
v_x = \frac{v_x' + u}{1+\frac{uv_x'}{c^2}}
$$

Per le componenti perpendicolari alla direzione del moto la forma è diversa. Se il moto relativo tra i sistemi è lungo \(x\), allora:

$$
v_y' = \frac{v_y}{\gamma\left(1-\frac{uv_x}{c^2}\right)}
$$

e analogamente:

$$
v_z' = \frac{v_z}{\gamma\left(1-\frac{uv_x}{c^2}\right)}
$$

Questo dettaglio serve per capire che la direzione \(x\), cioè quella del moto relativo tra i sistemi, è speciale: lungo \(x\) compare il termine \(v_x-u\), mentre nelle direzioni trasversali compare comunque il denominatore relativistico e anche \(v_x\), perché il tempo stesso cambia tra i due sistemi.

Questa formula risolve il problema della luce. Se in \(S'\) un raggio luminoso ha velocità \(c\), in \(S\) si ottiene:

$$
v_x = \frac{c+u}{1+\frac{uc}{c^2}}
= \frac{c+u}{1+\frac{u}{c}}
= c
$$

Quindi chi si muove con velocità \(c\) in un sistema si muove con velocità \(c\) anche nell'altro.

### Come impostare gli esercizi

La prof insiste moltissimo su una procedura precisa:

1. scegliere un asse \(x\) e disegnarlo;
2. assegnare il segno alle velocità in base al verso scelto;
3. decidere quale sistema è \(S\) e quale è \(S'\);
4. identificare correttamente \(v\), \(v'\) e \(u\);
5. non buttare via i segni.

> [!danger] Errore grave
> Il segno meno davanti a una velocità ha significato fisico. Non si prende il valore assoluto solo perché "viene negativo". Una velocità negativa indica moto nel verso opposto all'asse scelto.

### Esempio: Picard e La Forge

Due astronavi si muovono verso una base. Si sceglie l'asse \(x\) nel verso del moto. Picard ha velocità:

$$
u = +0{,}806c
$$

La Forge ha velocità:

$$
v = +0{,}906c
$$

La velocità di La Forge rispetto a Picard è:

$$
v' = \frac{0{,}906c-0{,}806c}{1-0{,}906\cdot 0{,}806}
$$

$$
v' \approx +0{,}371c
$$

Se invece La Forge viaggia in direzione opposta, allora:

$$
v = -0{,}906c
$$

e:

$$
v' = \frac{-0{,}906c-(+0{,}806c)}{1-(-0{,}906)(0{,}806)}
$$

Il risultato è negativo e con modulo minore di \(c\). Il segno indica il verso rispetto all'asse di Picard.

Fonte: [`15-04-26/transcription.txt`](./trascrizione-lezioni/15-04-26/transcription.txt), [`18-04-26/transcription.txt`](./trascrizione-lezioni/18-04-26/transcription.txt), [`trascrizione-app-giulia.md`](./trascrizione-app-giulia.md).

---

## Lunghezze contratte e composizione delle velocità nello stesso esercizio

Un esercizio più ricco riguarda una sonda lanciata da un'astronave verso un pianeta. L'astronave si muove rispetto al pianeta con velocità \(0{,}445c\). La sonda ha lunghezza propria:

$$
L_0 = 10\ \text{m}
$$

ma l'astronave la misura lunga:

$$
L_A = 7{,}5\ \text{m}
$$

Da:

$$
L_A = \frac{L_0}{\gamma}
$$

si ricava:

$$
\gamma = \frac{L_0}{L_A} = \frac{10}{7{,}5} = 1{,}\overline{3}
$$

Da \(\gamma\) si ricava \(\beta\):

$$
\beta = \sqrt{1-\frac{1}{\gamma^2}}
$$

Questa è la velocità della sonda rispetto all'astronave. Poi, per trovare la lunghezza vista dal pianeta, serve la velocità della sonda rispetto al pianeta, quindi si usa la composizione relativistica:

$$
v = \frac{v' + u}{1+\frac{v'u}{c^2}}
$$

Infine si ricalcola il \(\gamma\) rispetto al pianeta e si usa:

$$
L_{\text{pianeta}} = \frac{L_0}{\gamma_{\text{pianeta}}}
$$

> [!tip] Consiglio della prof
> Quando devi calcolare una lunghezza contratta, il \(\gamma\) deve essere quello relativo al sistema che sta misurando quella lunghezza. Non basta usare "un gamma qualsiasi": dipende dalla velocità dell'oggetto rispetto all'osservatore considerato.

Fonte: [`18-04-26/transcription.txt`](./trascrizione-lezioni/18-04-26/transcription.txt), [`trascrizione-app-giulia.md`](./trascrizione-app-giulia.md).

---

## Dinamica relativistica: quantità di moto

Nella dinamica classica:

$$
\vec p = m\vec v
$$

In relatività ristretta:

$$
\vec p = \gamma m \vec v
$$

Questo modifica profondamente la dinamica. Quando \(v\) si avvicina a \(c\), \(\gamma\) cresce moltissimo; quindi anche la quantità di moto cresce moltissimo. Per aumentare ulteriormente la velocità servirebbe un impulso sempre più grande.

L'impulso è:

$$
\Delta \vec p = \vec F \Delta t
$$

Per portare un corpo con massa diversa da zero fino a \(c\), servirebbe una quantità di moto infinita. Questo richiederebbe una forza infinita o un tempo infinito, entrambe situazioni non fisicamente realizzabili. Per questo \(c\) è una **velocità limite**.

> [!important] Per la verifica
> La prof ha detto che è importante saper descrivere il grafico di \(\gamma\) e della quantità di moto relativistica in funzione della velocità, soprattutto per spiegare perché \(c\) è una velocità limite.

Fonte: [`trascrizione-app-giulia.md`](./trascrizione-app-giulia.md), [`09-05-26/transcription.txt`](./trascrizione-lezioni/09-05-26/transcription.txt).

---

## L'esperimento di Bertozzi

Un'evidenza laboratoriale della velocità della luce come limite è l'esperimento di Bertozzi del 1964, citato dalla prof nelle indicazioni di ripasso. L'idea è accelerare elettroni, cioè particelle con massa diversa da zero, tramite campi elettrici via via più intensi e misurare la velocità finale raggiunta.

Secondo una visione classica ingenua, aumentando sempre l'energia fornita agli elettroni si dovrebbe riuscire ad aumentare indefinitamente la loro velocità. La relatività ristretta prevede invece che, all'aumentare dell'energia, la velocità cresca sempre meno e tenda asintoticamente a \(c\), senza raggiungerla.

Questo è esattamente il senso dell'esperimento: gli elettroni vengono accelerati sempre di più, ma la loro velocità si avvicina a \(c\) senza superarla. L'energia continua ad aumentare, ma non si traduce in un superamento della velocità della luce; si traduce invece nell'aumento della quantità di moto e dell'energia relativistica.

> [!note] Perché può servire in verifica
> La prof ha detto che Bertozzi è l'evidenza laboratoriale del fatto che \(c\) è una velocità limite per corpi con massa diversa da zero. Se chiede "quali prove danno senso alla RR", questo è un esempio più sperimentale rispetto ai soli ragionamenti matematici.

---

## Secondo e terzo principio in relatività

Il primo principio rimane sostanzialmente lo stesso: in assenza di forze risultanti, un corpo mantiene il suo stato di quiete o moto rettilineo uniforme.

Il secondo principio va espresso in termini di quantità di moto:

$$
\vec F = \frac{d\vec p}{dt}
$$

In classica, poiché \(\vec p = m\vec v\), si ottiene:

$$
\vec F = m\vec a
$$

In relatività:

$$
\vec F = \frac{d}{dt}(\gamma m \vec v)
$$

Il risultato non è semplicemente \(m\vec a\), perché \(\gamma\) dipende dalla velocità. A forza finita, mentre \(v\) si avvicina a \(c\), l'accelerazione deve diminuire: il corpo accelera sempre meno.

Negli appunti compare anche una forma più operativa, utile quando si distinguono i casi geometrici della forza. Se forza, accelerazione e velocità sono parallele, cioè si sta cercando di aumentare direttamente il modulo della velocità lungo la direzione del moto, allora:

$$
F = ma\gamma^3
$$

Se invece l'accelerazione è perpendicolare alla velocità, come nel caso di una forza centripeta che curva la traiettoria senza aumentare direttamente il modulo della velocità, allora:

$$
F = ma\gamma
$$

Questa distinzione spiega perché negli esercizi con campo magnetico perpendicolare alla velocità compare la massa "relativistica" attraverso \(\gamma m\) nella forza centripeta.

Il terzo principio crea un problema concettuale: azione e reazione richiederebbero simultaneità. Ma la simultaneità non è assoluta. Per questo, in relatività ristretta, il terzo principio non può essere mantenuto nella stessa forma ingenua della meccanica classica.

In forma più sicura, in relatività si conserva la quantità di moto totale di un sistema isolato. Per questo, invece di appoggiarsi sempre alla frase classica "azione e reazione", conviene ragionare con:

$$
\vec p_{\text{tot}} = \text{costante}
$$

> [!note] Indicazione della prof
> Ha detto che i principi della dinamica sono da sapere, non per forza come domanda diretta isolata, ma per capire cosa cambia nella dinamica relativistica.

Fonte: [`trascrizione-app-giulia.md`](./trascrizione-app-giulia.md), [`09-05-26/transcription.txt`](./trascrizione-lezioni/09-05-26/transcription.txt).

---

## Massa ed energia

Einstein arriva all'equivalenza massa-energia ragionando su impulsi luminosi e quantità di moto. L'idea, semplificata, è questa: in un sistema solidale con una massa \(m\), due impulsi luminosi uguali e contrari arrivano simmetricamente, quindi le quantità di moto si annullano e la massa resta ferma. In un sistema esterno, però, gli impulsi appaiono obliqui; le componenti verticali si annullano, ma quelle orizzontali si sommano. Sembrerebbe allora che la quantità di moto della massa debba cambiare.

Per evitare l'incongruenza, si deve ammettere che l'energia trasportata dalla radiazione contribuisca alla massa/energia del corpo. La relazione generale per l'energia totale relativistica è:

$$
E = \gamma mc^2
$$

Se il corpo è fermo, \(v=0\), quindi \(\gamma=1\), e si ottiene l'energia a riposo:

$$
E_0 = mc^2
$$

L'energia cinetica relativistica è:

$$
E_c = E - E_0
$$

cioè:

$$
E_c = \gamma mc^2 - mc^2 = (\gamma - 1)mc^2
$$

Per velocità non relativistiche, questa formula torna compatibile con la formula classica:

$$
E_c = \frac{1}{2}mv^2
$$

> [!important] Cosa sapere per la verifica
> La prof ha detto che la scheda sull'energia è dettagliata, ma non serve sapere tutti i passaggi matematici. Bisogna però sapere le formule principali e il significato fisico: un corpo possiede energia anche da fermo, in quanto possiede massa.

Fonte: [`29-04-26/transcription.txt`](./trascrizione-lezioni/29-04-26/transcription.txt), [`trascrizione-app-giulia.md`](./trascrizione-app-giulia.md).

---

## Applicazioni di \(E=mc^2\)

La prof ha richiamato le applicazioni dell'equivalenza massa-energia, soprattutto per collegamenti teorici e storici. Ha citato le reazioni nucleari, il decadimento radioattivo e le bombe atomiche di Hiroshima e Nagasaki come esempi in cui una variazione di massa corrisponde a una grande quantità di energia.

Il punto non è conoscere nei dettagli tutte le reazioni, ma sapere che \(E=mc^2\) non è solo una formula famosa: descrive fenomeni reali in cui massa ed energia si trasformano l'una nell'altra.

Gli appunti della classe organizzano questi fenomeni in tre gruppi particolarmente utili da ricordare.

Il primo è il **difetto di massa** con l'**energia di legame**. Quando più nucleoni si aggregano per formare un nucleo, la massa del nucleo formato non è semplicemente uguale alla somma delle masse dei nucleoni separati. Una parte della massa corrisponde all'energia di legame che tiene insieme il nucleo.

Il secondo è il **decadimento spontaneo di nuclei instabili**. Un nucleo instabile può trasformarsi emettendo particelle o radiazione; l'energia emessa è collegata alla variazione di massa tra stato iniziale e stato finale.

Il terzo è la **fissione nucleare**. Un neutrone può colpire un nucleo radioattivo e produrre nuclei più leggeri, altri neutroni ed energia sotto forma di radiazione e energia cinetica dei frammenti. Anche qui il bilancio energetico è spiegato dal fatto che una piccola differenza di massa corrisponde a molta energia, perché viene moltiplicata per \(c^2\).

> [!quote] Indicazione
> Nelle slide/schede di Classroom sull'energia, la prof dice che c'erano esempi di fenomeni fisici che danno credito all'equivalenza massa-energia. Non sono state indicate pagine del libro nelle trascrizioni.

Fonte: [`09-05-26/transcription.txt`](./trascrizione-lezioni/09-05-26/transcription.txt).

---

## Esercizi su energia, quantità di moto e conversioni

Questi esercizi sono tra i più probabili perché la prof li ha ripresi più volte.

### Energia a riposo ed energia totale

Per un elettrone:

$$
m_e = 9{,}1 \cdot 10^{-31}\ \text{kg}
$$

L'energia a riposo è:

$$
E_0 = m_ec^2
$$

Con \(c = 3 \cdot 10^8\ \text{m/s}\):

$$
E_0 = 9{,}1 \cdot 10^{-31}(3 \cdot 10^8)^2
$$

$$
E_0 \approx 8{,}19 \cdot 10^{-14}\ \text{J}
$$

Se l'elettrone si muove a \(0{,}80c\), allora:

$$
\gamma = \frac{1}{\sqrt{1-0{,}80^2}} \approx 1{,}67
$$

e:

$$
E = \gamma mc^2 \approx 1{,}36 \cdot 10^{-13}\ \text{J}
$$

La quantità di moto è:

$$
p = \gamma mv
$$

> [!warning] Unità di misura
> L'elettronvolt e il megaelettronvolt sono unità di energia, non di quantità di moto. La quantità di moto resta in \(\text{kg}\cdot \text{m/s}\), salvo formule avanzate non trattate.

### Conversione elettronvolt

Da sapere:

$$
1\ \text{eV} = 1{,}6 \cdot 10^{-19}\ \text{J}
$$

e:

$$
1\ \text{MeV} = 10^6\ \text{eV}
$$

Quindi:

$$
1\ \text{MeV} = 1{,}6 \cdot 10^{-13}\ \text{J}
$$

### Da energia cinetica a velocità

Se è data l'energia cinetica, ad esempio:

$$
E_c = 1{,}50\ \text{MeV}
$$

si usa:

$$
E_c = (\gamma - 1)mc^2
$$

Da cui:

$$
\gamma = \frac{E_c}{mc^2} + 1
$$

Poi si ricava \(\beta\):

$$
\gamma = \frac{1}{\sqrt{1-\beta^2}}
$$

quindi:

$$
\beta = \sqrt{1-\frac{1}{\gamma^2}}
$$

Infine:

$$
v = \beta c
$$

### Energia totale doppia dell'energia a riposo

Se un protone ha energia totale doppia dell'energia a riposo:

$$
E = 2E_0
$$

allora:

$$
\gamma mc^2 = 2mc^2
$$

quindi:

$$
\gamma = 2
$$

Da \(\gamma\) si ricava \(\beta\) e quindi la velocità. L'energia cinetica è:

$$
E_c = (\gamma -1)mc^2 = mc^2
$$

Fonte: [`29-04-26/transcription.txt`](./trascrizione-lezioni/29-04-26/transcription.txt), [`07-05-26/transcription.txt`](./trascrizione-lezioni/07-05-26/transcription.txt), [`09-05-26/transcription.txt`](./trascrizione-lezioni/09-05-26/transcription.txt).

---

## Differenza di potenziale e lavoro della forza elettrica

Un tipo di esercizio discusso riguarda un elettrone accelerato da una velocità a un'altra, oppure da fermo fino a una certa energia cinetica. La relazione da usare non è la cinematica del moto uniformemente accelerato, perché in regime relativistico l'accelerazione non resta costante anche se la forza è costante.

La base è:

$$
L = \Delta E_c
$$

Per la forza elettrica:

$$
L = -q\Delta V
$$

Spesso negli esercizi si usa il valore assoluto:

$$
\Delta E_c = |q|\,|\Delta V|
$$

Quindi:

$$
|\Delta V| = \frac{\Delta E_c}{|q|}
$$

> [!tip] Come non confondersi
> Se l'energia cinetica è in eV e la carica è quella elementare, il calcolo è costruito apposta per essere semplice. Però la prof consiglia spesso di convertire in Joule per evitare confusione.

Fonte: [`07-05-26/transcription.txt`](./trascrizione-lezioni/07-05-26/transcription.txt), [`09-05-26/transcription.txt`](./trascrizione-lezioni/09-05-26/transcription.txt).

---

## Campo magnetico e raggio della traiettoria

La prof ha detto che all'esame/verifica potrebbe comparire una domanda in cui una particella entra in una regione con campo magnetico perpendicolare alla velocità. Se \(\vec v \perp \vec B\), la traiettoria è circolare.

La forza di Lorentz magnetica vale:

$$
F_L = |q|vB
$$

perché \(\sin 90^\circ = 1\).

Questa forza è centripeta. In regime relativistico si usa:

$$
F_c = \gamma m \frac{v^2}{r}
$$

Uguagliando:

$$
|q|vB = \gamma m \frac{v^2}{r}
$$

Da cui:

$$
r = \frac{\gamma mv}{|q|B}
$$

cioè:

$$
r = \frac{p}{|q|B}
$$

visto che \(p=\gamma mv\).

Fonte: [`09-05-26/transcription.txt`](./trascrizione-lezioni/09-05-26/transcription.txt).

---

## Effetto fotoelettrico: la crisi della fisica classica

Dopo la relatività, la prof introduce la fisica moderna attraverso l'effetto fotoelettrico. L'effetto fotoelettrico consiste nell'emissione di elettroni da parte di una lastra conduttrice colpita da radiazione elettromagnetica.

L'apparato sperimentale è un tubo a vuoto con due piastre. La radiazione entra e colpisce una piastra metallica; se riesce a estrarre elettroni, questi vengono accelerati o frenati da un campo elettrico tra le piastre. Un amperometro misura la corrente, cioè il passaggio degli elettroni nel circuito.

Classicamente, la radiazione è un'onda che trasporta energia. Se l'energia assorbita da un elettrone è sufficiente a vincere il legame col nucleo/metallo, l'elettrone esce. Questa parte non è strana. I problemi nascono dai risultati sperimentali.

### Prima osservazione problematica: intensità e potenziale di arresto

Se si aumenta la differenza di potenziale in modo favorevole, sempre più elettroni vengono raccolti e la corrente aumenta. A un certo punto però si raggiunge una corrente di saturazione: tutti gli elettroni estratti vengono raccolti, quindi aumentare ancora il campo non aumenta la corrente.

Se invece si inverte il campo, gli elettroni vengono frenati. Quelli con poca energia cinetica vengono fermati prima; quelli più energetici riescono ancora ad arrivare all'altra piastra. Esiste un potenziale di arresto \(\Delta V_0\) che ferma anche gli elettroni più energetici, quindi la corrente diventa zero.

La fisica classica prevederebbe: se aumento l'intensità della radiazione, aumento l'energia trasportata dall'onda, quindi gli elettroni dovrebbero uscire con energia cinetica maggiore. Per fermarli servirebbe un potenziale di arresto maggiore.

Ma sperimentalmente:

$$
\text{aumentando l'intensità, } \Delta V_0 \text{ non cambia}
$$

Cambia la corrente di saturazione, perché escono più elettroni, ma non cambia l'energia massima con cui escono.

### Seconda osservazione problematica: frequenza di soglia

Gli elettroni escono solo se la frequenza della radiazione è maggiore o uguale a una frequenza minima:

$$
f \geq f_0
$$

Se:

$$
f < f_0
$$

non escono elettroni, anche illuminando la lastra per un tempo lunghissimo. Questo è inspiegabile classicamente, perché un'onda dovrebbe poter trasferire energia poco alla volta; dopo abbastanza tempo, l'elettrone dovrebbe accumulare energia sufficiente. Ma non succede.

> [!important] I due grafici da sapere
> La prof ha detto che i due grafici dell'effetto fotoelettrico sono fondamentali:
>
> 1. corrente \(I\) in funzione di \(\Delta V\), con corrente di saturazione e potenziale di arresto;
> 2. energia cinetica massima o potenziale di arresto in funzione della frequenza, con frequenza di soglia \(f_0\).

Fonte: [`06-05-26/transcription.txt`](./trascrizione-lezioni/06-05-26/transcription.txt), [`07-05-26/transcription.txt`](./trascrizione-lezioni/07-05-26/transcription.txt), [`trascrizione-app-giulia.md`](./trascrizione-app-giulia.md).

---

## Il modello a fotoni di Einstein

Einstein riprende l'ipotesi di Planck: l'energia, a livello microscopico, non viene scambiata in modo continuo, ma in pacchetti. Per la radiazione questi pacchetti sono i fotoni.

Un fotone:

- ha massa nulla;
- si muove sempre a velocità \(c\);
- trasporta energia;
- trasporta quantità di moto;
- ha energia:

$$
E = hf
$$

dove \(h\) è la costante di Planck.

La quantità di moto del fotone è legata all'energia da:

$$
p = \frac{E}{c}
$$

Ogni elettrone interagisce con un solo fotone. Questa frase è fondamentale per capire perché l'intensità non cambia l'energia cinetica massima.

Se un elettrone assorbe un fotone, l'energia del fotone viene usata in parte per uscire dal metallo e in parte diventa energia cinetica:

$$
hf = W_0 + E_{c,\max}
$$

Il lavoro di estrazione \(W_0\) è l'energia minima necessaria per estrarre gli elettroni più esterni:

$$
W_0 = hf_0
$$

Quindi:

$$
E_{c,\max} = hf - hf_0
$$

Poiché il potenziale di arresto ferma gli elettroni più energetici:

$$
E_{c,\max} = |q_e|\Delta V_0
$$

Da cui:

$$
|q_e|\Delta V_0 = hf - hf_0
$$

Se aumento l'intensità ma tengo fissa la frequenza, mando più fotoni, ma ogni fotone ha la stessa energia \(hf\). Quindi possono uscire più elettroni, ma non con energia cinetica maggiore. Per questo il potenziale di arresto non cambia.

> [!summary] Risoluzione delle anomalie
> - La frequenza decide l'energia del singolo fotone.
> - L'intensità decide quanti fotoni arrivano.
> - Se \(f<f_0\), nessun fotone ha energia sufficiente a estrarre un elettrone.
> - Se \(f\geq f_0\), gli elettroni possono uscire subito.

Fonte: [`07-05-26/transcription.txt`](./trascrizione-lezioni/07-05-26/transcription.txt), [`trascrizione-app-giulia.md`](./trascrizione-app-giulia.md).

---

## Dualismo onda-corpuscolo

L'effetto fotoelettrico obbliga a recuperare una descrizione corpuscolare della radiazione, ma non cancella il modello ondulatorio. La luce continua a comportarsi come onda in fenomeni come interferenza e diffrazione, ma in fenomeni microscopici come l'effetto fotoelettrico si comporta come un insieme di corpuscoli, i fotoni.

La prof ha sottolineato che il dualismo non riguarda solo la luce. Anche ciò che pensiamo come particella può comportarsi come onda. Un fascio di elettroni, se inviato contro un reticolo cristallino o attraverso strutture con distanze confrontabili con la lunghezza d'onda associata agli elettroni, può produrre figure di diffrazione simili a quelle della luce.

Il dualismo onda-corpuscolo è quindi reciproco:

$$
\text{onda} \leftrightarrow \text{corpuscolo}
$$

Non significa che in certi casi la luce "è solo onda" e in altri "è solo particella" in modo assoluto. Significa che a seconda dell'esperimento alcuni aspetti sono dominanti e altri trascurabili.

> [!note] Estensione teorica
> La prof ha accennato che da qui nasce la meccanica quantistica, con energia quantizzata, elettroni come onde stazionarie negli atomi e principio di indeterminazione di Heisenberg. Non ha sviluppato tutto per mancanza di tempo.

Fonte: [`09-05-26/transcription.txt`](./trascrizione-lezioni/09-05-26/transcription.txt).

---

## Cosa ha detto la prof sulla verifica

La verifica viene indicata come **prova del 20**. Le indicazioni esplicite sono queste.

La parte teorica sulle trasformazioni di Lorentz non viene messa come derivazione. La prof ha detto: non perderà tempo a far ricavare le leggi di composizione dalla relatività. Questo però non significa che la composizione delle velocità non serva: serve eccome negli esercizi.

La simultaneità va saputa come concetto: è relativa. Non sembra voler chiedere una spiegazione lunga dell'esperimento del treno e dei fulmini.

Gli argomenti teorici davvero importanti sono:

- postulati della relatività ristretta;
- sistemi inerziali;
- rottura con la relatività galileiana;
- problema della velocità della luce tra elettromagnetismo e Galileo;
- Michelson-Morley senza matematica;
- dilatazione del tempo e tempo proprio;
- contrazione delle lunghezze e lunghezza propria;
- fattore \(\gamma\);
- composizione relativistica delle velocità;
- quantità di moto relativistica;
- \(c\) come velocità limite;
- massa-energia;
- effetto fotoelettrico;
- dualismo onda-corpuscolo.

Ha detto anche che le schede su Classroom su gemelli, muoni ed energia possono aiutare. Sull'energia non serve conoscere ogni passaggio matematico, ma bisogna saper usare e interpretare le formule.

La prof ha insistito sugli esercizi: se non li fate, poi non potete dire che non siete stati allenati. Gli esercizi più coerenti con quello che ha ripassato sono:

- calcolare \(\gamma\) da una velocità;
- calcolare velocità da \(\gamma\);
- usare \(E_c=(\gamma-1)mc^2\);
- usare \(E=\gamma mc^2\);
- usare \(E_0=mc^2\);
- convertire eV/MeV in Joule;
- calcolare \(p=\gamma mv\);
- usare lavoro elettrico e differenza di potenziale;
- usare forza di Lorentz e raggio di moto circolare;
- comporre velocità relativistiche con segni corretti.

Fonte: [`09-05-26/transcription.txt`](./trascrizione-lezioni/09-05-26/transcription.txt).

---

## Formulario ragionato

> [!info] Questo formulario non sostituisce la teoria
> La prof sembra puntare molto sul capire quale formula usare e in quale sistema di riferimento, non sul buttare formule a caso.

### Fattori relativistici

$$
\beta = \frac{v}{c}
$$

$$
\gamma = \frac{1}{\sqrt{1-\beta^2}}
$$

### Tempo

$$
\Delta t = \gamma \Delta t_0
$$

\(\Delta t_0\): tempo proprio, misurato da chi vede i due eventi nello stesso punto.

### Lunghezza

$$
L = \frac{L_0}{\gamma}
$$

\(L_0\): lunghezza propria, misurata da chi vede il segmento fermo.

### Composizione velocità

$$
v' = \frac{v-u}{1-\frac{uv}{c^2}}
$$

$$
v = \frac{v'+u}{1+\frac{uv'}{c^2}}
$$

### Quantità di moto

$$
p = \gamma mv
$$

### Energia

$$
E_0 = mc^2
$$

$$
E = \gamma mc^2
$$

$$
E_c = (\gamma - 1)mc^2
$$

### Lavoro elettrico

$$
\Delta E_c = |q|\Delta V
$$

### Fotoni

$$
E = hf
$$

$$
p = \frac{E}{c}
$$

### Fotoelettrico

$$
W_0 = hf_0
$$

$$
E_{c,\max} = hf - hf_0
$$

$$
E_{c,\max} = |q_e|\Delta V_0
$$

### Campo magnetico

$$
F_L = |q|vB
$$

se \(\vec v \perp \vec B\):

$$
r = \frac{\gamma mv}{|q|B}
$$

---

## Metodo di studio consigliato

Per studiare bene, conviene seguire il filo della crisi e non memorizzare a blocchi isolati. La relatività ristretta nasce per sistemare il conflitto tra Galileo e Maxwell. Da lì cadono simultaneità assoluta, tempo assoluto e lunghezza assoluta. Poi cambiano quantità di moto ed energia, fino a \(E=mc^2\). Infine, con l'effetto fotoelettrico, anche l'idea classica di energia continua entra in crisi e nasce il modello a fotoni.

Un buon modo per ripassare è provare a rispondere a voce a queste domande:

1. Perché Michelson-Morley è importante anche se non "vede" l'etere?
2. Cosa dicono i due postulati di Einstein?
3. Perché due eventi simultanei per un osservatore possono non esserlo per un altro?
4. Chi misura il tempo proprio?
5. Chi misura la lunghezza propria?
6. Perché \(c\) è una velocità limite?
7. Cosa cambia tra \(p=mv\) e \(p=\gamma mv\)?
8. Che differenza c’è tra \(E_0\), \(E\), \(E_c\)?
9. Perché l'intensità non cambia il potenziale di arresto?
10. Perché sotto \(f_0\) non escono elettroni?
11. Cosa significa dualismo onda-corpuscolo?

Se sai rispondere a queste domande con frasi complete e sai fare gli esercizi base con \(\gamma\), energia, quantità di moto e potenziale, sei allineato con quello che la prof ha detto di voler verificare.
