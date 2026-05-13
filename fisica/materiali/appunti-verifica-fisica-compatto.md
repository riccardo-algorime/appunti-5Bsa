# Formulaio accessibile - verifica fisica

> [!summary] Uso
> Formulaio rapido per esercizi e ripasso finale. Per la teoria discorsiva usa [`teoria-verifica-fisica-orale.md`](./teoria-verifica-fisica-orale.md).

> [!warning] Scope prof
> Questo formulaio serve per la parte di esercizi e formule della relatività ristretta. Fotoelettrico: solo orale teorico, quindi non è incluso qui. Michelson-Morley: scopo e risultato, non matematica. Trasformazioni di Lorentz escluse come teoria.

---

## Costanti

**Velocità della luce**

$$
c=3{,}0\cdot10^8\ \text{m/s}
$$

Serve come velocità limite e in tutte le formule relativistiche.

**Elettronvolt**

$$
1\ \text{eV}=1{,}6\cdot10^{-19}\ \text{J}
$$

**Mega-elettronvolt**

$$
1\ \text{MeV}=10^6\ \text{eV}=1{,}6\cdot10^{-13}\ \text{J}
$$

Serve per convertire energie in esercizi con elettroni, protoni e particelle relativistiche.

**Carica elementare**

$$
e=1{,}6\cdot10^{-19}\ \text{C}
$$

Per l'elettrone la carica è negativa, per il protone è positiva. Negli esercizi con moduli si usa spesso il modulo della carica elementare.

**Massa dell'elettrone**

$$
m_e=9{,}11\cdot10^{-31}\ \text{kg}
$$

oppure:

$$
m_e\approx0{,}511\ \text{MeV}/c^2
$$

**Massa del protone**

$$
m_p=1{,}67\cdot10^{-27}\ \text{kg}
$$

oppure:

$$
m_p\approx938\ \text{MeV}/c^2
$$

---

## Fattore di Lorentz

$$
\beta=\frac{v}{c}
\qquad
\gamma=\frac{1}{\sqrt{1-\beta^2}}
$$

Beta è la velocità in unità di c. Gamma misura quanto sono forti gli effetti relativistici. Deve essere sempre maggiore o uguale a 1.

Forma equivalente:

$$
\gamma=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}}
$$

Approssimazione per velocità non troppo grandi, circa v minore di 0,4c:

$$
\gamma\approx1+\frac{1}{2}\frac{v^2}{c^2}
$$

Inverse:

$$
\beta=\sqrt{1-\frac{1}{\gamma^2}}
\qquad
v=\beta c
$$

> [!error] Se gamma viene minore di 1, la formula è scritta male.

---

## Tempo

$$
\Delta t=\gamma\Delta t_0
$$

Delta t0 = **tempo proprio**, misurato da chi vede i due eventi nello stesso punto.  
Delta t = tempo misurato da chi vede gli eventi in punti diversi.

Poiché gamma è maggiore o uguale a 1, allora Delta t è maggiore o uguale a Delta t0: il tempo non proprio è più lungo.

---

## Lunghezza

$$
L=\frac{L_0}{\gamma}
$$

L0 = **lunghezza propria**, misurata da chi vede l'oggetto fermo.  
L = lunghezza misurata da chi vede l'oggetto in moto.

La contrazione vale solo lungo la direzione del moto.

---

## Composizione delle velocità

Da S a S':

$$
v_x'=\frac{v_x-u}{1-\frac{uv_x}{c^2}}
$$

Con la nomenclatura V = velocità di S' rispetto a S, v = velocità vista da S, v' = velocità vista da S':

$$
v'=\frac{v-V}{1-\frac{vV}{c^2}}
$$

Formula inversa:

$$
v_x=\frac{v_x'+u}{1+\frac{uv_x'}{c^2}}
$$

Nella stessa nomenclatura:

$$
v=\frac{v'+V}{1+\frac{v'V}{c^2}}
$$

Componenti perpendicolari:

$$
v_y'=\frac{v_y}{\gamma\left(1-\frac{uv_x}{c^2}\right)}
\qquad
v_z'=\frac{v_z}{\gamma\left(1-\frac{uv_x}{c^2}\right)}
$$

> [!tip] Prima scegli l'asse e i segni. Il segno negativo è un verso, non un errore.

---

## Quantità di moto e limite c

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

Quando v tende a c, gamma tende all'infinito, quindi servirebbe quantità di moto infinita. Per questo un corpo con massa non raggiunge c.

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

Forza parallela alla velocità:

$$
F=ma\gamma^3
$$

$$
F_\parallel=ma\gamma^3
$$

Forza perpendicolare alla velocità, caso centripeto:

$$
F=ma\gamma
$$

$$
F_\perp=ma\gamma
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

Stessa formula con la notazione K, spesso usata nei testi:

$$
K=mc^2(\gamma-1)
$$

Relazione fondamentale:

$$
E=E_0+K
$$

Se conosci l'energia cinetica:

$$
\gamma=\frac{E_c}{mc^2}+1
\qquad
\beta=\sqrt{1-\frac{1}{\gamma^2}}
\qquad
v=\beta c
$$

> [!tip] E0: energia a riposo. E: energia totale. Ec oppure K: energia cinetica.

Relazione energia-momento:

$$
E^2=(pc)^2+E_0^2
$$

È utile come scorciatoia quando l'esercizio usa unità tipo MeV, MeV/c, MeV/c^2.

---

## Lavoro elettrico

$$
L=\Delta E_c
$$

$$
L=-q\Delta V
$$

In alcune convenzioni, o se il verso è già gestito dal testo, si scrive anche:

$$
L=q\Delta V
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

Se velocità e campo magnetico sono perpendicolari:

$$
F_L=|q|vB
$$

Se q viene usato come modulo della carica:

$$
F_L=qvB
$$

Forza centripeta relativistica:

$$
F_c=\gamma m\frac{v^2}{r}
$$

Raggio:

$$
r=\frac{\gamma mv}{|q|B}=\frac{p}{|q|B}
$$

Versione con q inteso come modulo della carica:

$$
r=\frac{p}{qB}=\frac{\gamma mv}{qB}
$$

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

**Michelson-Morley:** cercava il moto della Terra rispetto all'etere. Risultato nullo: nessuna variazione significativa. Importanza: crisi dell'etere e strada verso c costante.

**Muoni:** evidenza della dilatazione dei tempi.

**Bertozzi:** elettroni accelerati con energia crescente si avvicinano a c, ma non la raggiungono. Conferma c come limite per particelle con massa.

---

## Mini teoria flash

**Postulati RR:** leggi fisiche uguali in tutti i SRI; c uguale in tutti i SRI.

**Tempo proprio:** chi vede i due eventi nello stesso punto.

**Lunghezza propria:** chi vede l'oggetto fermo.

**Limite c:** per v che tende a c, gamma tende all'infinito.

**Massa-energia:** un corpo possiede energia anche da fermo.

$$
E_0=mc^2
$$

**Dualismo:** luce e materia possono mostrare comportamento ondulatorio o corpuscolare.
