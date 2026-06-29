import re

with open('../STORIA-3.7.md', 'r') as f:
    source = f.read()
    
# Find the exact text of the missing block
start_idx = source.find("**L'organizzazione delle forze politiche**")
end_idx = source.find("**La crescita del malcontento e la rivoluzione del febbraio 1917**")

missing_text = source[start_idx:end_idx]

print("--- Missing concepts ---")
if "1898" in missing_text: print("- Nascita Partito socialdemocratico (1898) e scissione (1903)")
if "bolscevichi" in missing_text: print("- Differenza bolscevichi (Lenin, rivoluzionari) / menscevichi (riformisti)")
if "populista" in missing_text: print("- Partito socialista-rivoluzionario (1901) e populismo")
if "cadetti" in missing_text: print("- Partito dei cadetti (1905) e partiti nazionali")
if "1905" in missing_text: print("- Rivoluzione del 1905 e sconfitta col Giappone")
if "domenica" in missing_text: print("- La 'Domenica di sangue' (gennaio 1905)")
if "Duma" in missing_text: print("- Nascita della Duma e Costituzione (1905-1906)")
if "Trockij" in missing_text: print("- Nascita dei Soviet e prima ascesa di Trockij")
if "Stolypin" in missing_text: print("- Riforme agrarie e assassinio di Stolypin (1906-1911)")
if "Rasputin" in missing_text: print("- Ascesa e influenza di Rasputin a corte")
if "guerra totale" in missing_text: print("- Ingresso nella Grande Guerra (1914) e mobilitazione di 15 milioni di soldati")
