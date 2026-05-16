## Extra: forza di Lorentz

Questo ragionamento serve a mostrare perché **elettromagnetismo** e **relatività galileiana** entrano in conflitto.

Prendiamo due cariche positive che si muovono nello stesso verso con la stessa velocità \(v\). Consideriamo due sistemi di riferimento:

- \(SR\): laboratorio, in cui le cariche si muovono;
- \(SR'\): sistema solidale con le cariche, in cui le cariche sono ferme.

In **relatività galileiana** l'accelerazione è assoluta. Cioè, se due sistemi inerziali si muovono uno rispetto all'altro di moto rettilineo uniforme, dovrebbero misurare la stessa accelerazione:

$$
\mathbf{a}_{SR'}=\mathbf{a}_{SR}
$$

Quindi, se la massa è la stessa, anche la risultante delle forze dovrebbe essere la stessa:

$$
\mathbf{R}_{SR'}=m\mathbf{a}_{SR'}=m\mathbf{a}_{SR}=\mathbf{R}_{SR}
$$

Perciò la fisica classica si aspetta:

$$
\mathbf{R}_{SR'}=\mathbf{R}_{SR}
$$

Ma l'elettromagnetismo dice un'altra cosa.

Nel sistema \(SR\), le cariche sono in movimento. Tra loro c'è la forza elettrica, perché sono cariche, ma c'è anche una forza magnetica, perché una carica in moto genera effetti magnetici. La risultante è:

$$
\mathbf{R}_{SR}=\mathbf{F}_E+\mathbf{F}_L
$$

La forza di Lorentz magnetica, nel caso semplice con velocità perpendicolare al campo magnetico, vale:

$$
F_L=qvB
$$

Quindi l'accelerazione vista da \(SR\) è:

$$
\mathbf{a}_{SR}=\frac{\mathbf{F}_E+\mathbf{F}_L}{m}
$$

Nel sistema \(SR'\), invece, le due cariche si vedono reciprocamente ferme. Se sono ferme, la loro velocità relativa è nulla:

$$
v_{SR'}=0
$$

Allora la parte magnetica della forza di Lorentz si annulla:

$$
F_L=qv_{SR'}B=0
$$

Rimane solo la forza elettrica:

$$
\mathbf{R}_{SR'}=\mathbf{F}_E
$$

e quindi:

$$
\mathbf{a}_{SR'}=\frac{\mathbf{F}_E}{m}
$$

Il problema è evidente:

$$
\mathbf{a}_{SR}=\frac{\mathbf{F}_E+\mathbf{F}_L}{m}
\qquad
\mathbf{a}_{SR'}=\frac{\mathbf{F}_E}{m}
$$

Se \(F_L\neq0\), allora:

$$
\mathbf{a}_{SR}\neq\mathbf{a}_{SR'}
$$

Questa conclusione contraddice Galileo, secondo cui l'accelerazione dovrebbe essere la stessa nei due sistemi. Perciò non si può mantenere insieme, senza modifiche, tutta la relatività galileiana e tutto l'elettromagnetismo di Maxwell.

La relatività ristretta risolve il problema cambiando l'idea classica di spazio e tempo: non sono più assoluti, e le grandezze elettriche e magnetiche dipendono dal sistema di riferimento.

---
