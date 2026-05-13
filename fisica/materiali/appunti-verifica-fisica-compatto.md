# Formulaio accessibile - verifica fisica

> [!summary] Uso
> Formulaio rapido per esercizi e ripasso finale. Per la teoria discorsiva usa [`teoria-verifica-fisica-orale.md`](./teoria-verifica-fisica-orale.md).

> [!warning] Scope prof
> Fotoelettrico solo teorico. Michelson-Morley: scopo e risultato, non matematica. Trasformazioni di Lorentz escluse come teoria.

---

## Costanti

| Quantità | Formula / valore | Uso |
|---|---:|---|
| Luce | \(c=3{,}0\cdot10^8\ \text{m/s}\) | velocità limite |
| Elettronvolt | \(1\ \text{eV}=1{,}6\cdot10^{-19}\ \text{J}\) | conversioni |
| Mega-eV | \(1\ \text{MeV}=10^6\ \text{eV}=1{,}6\cdot10^{-13}\ \text{J}\) | energie relativistiche |

---

## Fattore di Lorentz

$$
\beta=\frac{v}{c}
\qquad
\gamma=\frac{1}{\sqrt{1-\beta^2}}
$$

\(\beta\) è la velocità in unità di \(c\). \(\gamma\) misura quanto sono forti gli effetti relativistici. Deve essere sempre \(\gamma\geq1\).

Inverse:

$$
\beta=\sqrt{1-\frac{1}{\gamma^2}}
\qquad
v=\beta c
$$

> [!error] Se \(\gamma<1\), formula scritta male.

---

## Tempo

$$
\Delta t=\gamma\Delta t_0
$$

\(\Delta t_0\) = **tempo proprio**, misurato da chi vede i due eventi nello stesso punto.  
\(\Delta t\) = tempo misurato da chi vede gli eventi in punti diversi.

Poiché \(\gamma\geq1\), allora \(\Delta t\geq\Delta t_0\): il tempo non proprio è più lungo.

---

## Lunghezza

$$
L=\frac{L_0}{\gamma}
$$

\(L_0\) = **lunghezza propria**, misurata da chi vede l'oggetto fermo.  
\(L\) = lunghezza misurata da chi vede l'oggetto in moto.

La contrazione vale solo lungo la direzione del moto.

---

## Composizione delle velocità

Da \(S\) a \(S'\):

$$
v_x'=\frac{v_x-u}{1-\frac{uv_x}{c^2}}
$$

Formula inversa:

$$
v_x=\frac{v_x'+u}{1+\frac{uv_x'}{c^2}}
$$

Componenti perpendicolari:

$$
v_y'=\frac{v_y}{\gamma\left(1-\frac{uv_x}{c^2}\right)}
\qquad
v_z'=\frac{v_z}{\gamma\left(1-\frac{uv_x}{c^2}\right)}
$$

> [!tip] Prima scegli l'asse e i segni. Il segno negativo è un verso, non un errore.

---

## Quantità di moto e limite \(c\)

Classica:

$$
\vec p=m\vec v
$$

Relativistica:

$$
\vec p=\gamma m\vec v
$$

Impulso:

$$
\Delta\vec p=\vec F\Delta t
$$

Quando \(v\to c\), \(\gamma\to\infty\), quindi servirebbe quantità di moto infinita. Per questo un corpo con massa non raggiunge \(c\).

---

## Dinamica relativistica

Secondo principio generale:

$$
\vec F=\frac{d\vec p}{dt}
$$

In relatività:

$$
\vec F=\frac{d}{dt}(\gamma m\vec v)
$$

Forza parallela a \(\vec v\):

$$
F=ma\gamma^3
$$

Forza perpendicolare a \(\vec v\), caso centripeto:

$$
F=ma\gamma
$$

Sistema isolato:

$$
\vec p_{\text{tot}}=\text{costante}
$$

---

## Energia relativistica

Energia totale:

$$
E=\gamma mc^2
$$

Energia a riposo:

$$
E_0=mc^2
$$

Energia cinetica:

$$
E_c=E-E_0=(\gamma-1)mc^2
$$

Se conosci \(E_c\):

$$
\gamma=\frac{E_c}{mc^2}+1
\qquad
\beta=\sqrt{1-\frac{1}{\gamma^2}}
\qquad
v=\beta c
$$

> [!tip] \(E_0\): fermo. \(E\): totale. \(E_c\): moto.

---

## Lavoro elettrico

$$
L=\Delta E_c
$$

$$
L=-q\Delta V
$$

In valore assoluto:

$$
\Delta E_c=|q|\,|\Delta V|
\qquad
|\Delta V|=\frac{\Delta E_c}{|q|}
$$

Da usare quando una particella carica viene accelerata da una differenza di potenziale.

---

## Campo magnetico

Se \(\vec v\perp\vec B\):

$$
F_L=|q|vB
$$

Forza centripeta relativistica:

$$
F_c=\gamma m\frac{v^2}{r}
$$

Raggio:

$$
r=\frac{\gamma mv}{|q|B}=\frac{p}{|q|B}
$$

---

## Fotoelettrico e fotoni

Energia del fotone:

$$
E=hf
$$

Quantità di moto del fotone:

$$
p=\frac{E}{c}
$$

Lavoro di estrazione:

$$
W_0=hf_0
$$

Bilancio:

$$
hf=W_0+E_{c,\max}
$$

Quindi:

$$
E_{c,\max}=hf-hf_0
$$

Potenziale di arresto:

$$
E_{c,\max}=|q_e|\Delta V_0
$$

> [!warning] Per teoria
> Frequenza \(f\) = energia del singolo fotone. Intensità = numero di fotoni. Se \(f<f_0\), non escono elettroni.

---

## Muoni

$$
\Delta t_0=2{,}2\cdot10^{-6}\ \text{s}
\qquad
v\approx0{,}995c
$$

Classico:

$$
d=v\Delta t_0\approx657\ \text{m}
$$

Relativistico:

$$
d=v\gamma\Delta t_0\approx6570\ \text{m}
$$

Arrivano al suolo perché per la Terra il loro tempo di vita è dilatato.

---

## Gemelli

$$
\Delta t=\gamma\Delta t_0
$$

Esempio:

$$
v=0{,}98c,\quad \gamma\approx5,\quad \Delta t_0=10\ \text{anni}
$$

$$
\Delta t\approx50\ \text{anni}
$$

Non è simmetrico perché il gemello sull'astronave accelera e cambia sistema di riferimento.

---

## Esperimenti da ricordare

**Michelson-Morley:** cercava il moto della Terra rispetto all'etere. Risultato nullo: nessuna variazione significativa. Importanza: crisi dell'etere e strada verso \(c\) costante.

**Muoni:** evidenza della dilatazione dei tempi.

**Bertozzi:** elettroni accelerati con energia crescente si avvicinano a \(c\), ma non la raggiungono. Conferma \(c\) come limite per particelle con massa.

**Fotoelettrico:** mostra che la luce scambia energia in fotoni; spiega frequenza soglia e ruolo dell'intensità.

---

## Mini teoria flash

**Postulati RR:** leggi fisiche uguali in tutti i SRI; \(c\) uguale in tutti i SRI.

**Tempo proprio:** chi vede i due eventi nello stesso punto.

**Lunghezza propria:** chi vede l'oggetto fermo.

**Limite \(c\):** per \(v\to c\), \(\gamma\to\infty\).

**Massa-energia:** un corpo possiede energia anche da fermo: \(E_0=mc^2\).

**Fotoelettrico:** intensità aumenta quanti elettroni escono; frequenza aumenta l'energia massima.

**Dualismo:** luce e materia possono mostrare comportamento ondulatorio o corpuscolare.

