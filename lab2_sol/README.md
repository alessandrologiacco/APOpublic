# Laboratorio 2
Questo laboratorio è un ripasso di ciò che è stato spiegato
il primo anno nel corso di informatica. 
E' presente un unico esercizio, tratto dal tema d'esame di Febbraio 2022.

Dopo aver svolto l'esercizio,
terminare e testare la configurazione di git come spiegato in aula e
illustrato nella guida presente nel repository.
Provare ad utilizzarlo anche sul PC del laboratorio.
Caricare il codice dei primi due laboratori sul proprio repository git.

## Strategia militare
Il conte von Bülow ha pubblicato un nuovo manuale di strategia militare 
in cui dimostra come le guerre si vincano seguendo precisi procedimenti matematici e l’inutilità delle battaglie.
Permettere alla prova le sue teorie ha bisogno di un programma informatico che permetta di calcolare statistiche sui battaglioni.

Il file *schieramento.txt* contiene la rappresentazione di un piano rettangolare.
Gli 0 rappresentano un'area vuota. I numeri da 1 a 9 rappresentano uno schieramento di truppe rettangolare.
Gli 1 rappresentano la prima fila di uno schieramento, i 2 la seconda e così via fino ad un massimo di 9.
Le file hanno tutte la stessa larghezza (lo schieramento ha forma rettangolare), 
ma in quelle dopo la prima possono esserci dei buchi, rappresentati da 0, 
dovuti ai caduti (non ai bordi della fila, e non nella prima)

Vi si richiede di scrivere un programma python che acquisisca lo schieramento e calcoli e visualizzi:

    la larghezza dello schieramento
    il numero di file dello schieramento
    la direzione (Nord, Est, Sud o Ovest) dello schieramento
    la fila dello schieramento con più buchi (se ci fossero buchi)

Si assuma che lo schieramento abbia almeno due file.

### Esempio
***Input:***
```
000000000
000000000
000000000
032100000
000100000
002100000
032100000
000000000
```

***Output***
```
larghezza: 4
numero di file: 3
direzione: Est
fila con più buchi: 3 
