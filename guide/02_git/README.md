# Tutorial Git
Questo file contiene un tutorial per configurare il proprio account **GitHub** e imparare i principali comandi di Git.
Prima di procedere consultare la guida software.

### Informazioni generali
Impostare il proprio file manager per visualizzare le estensioni dei file e i file nascosti (quelli che iniziano con punto).
- In **Finder** (MacOS) usare ```shift+command+period``` per mostrare i file nascosti e andare in  ```Preferenze -> Avanzate -> Mostra tutte le estensioni dei nomi documenti```
- In **Esplora Risorse** (Windows) andare in ```Visualizza-> Elementi nascosti``` e ```Visualizza -> Estensioni nome file```

### Creazione account e token
Creare un account **GitHub**. Usare email e username che si preferiscono, non devono per forza essere quelli istituzionali.

Una volta creato l'account, generare un token seguendo la
[guida](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
Per semplicità si può decidere che il token non scada mai (*expiration*).
Come ambito di validità (*scope*) selezionare solo la voce *repo*.
Questo verrà utilizzato come password per accedere al repository da remoto tramite il client git.

Un volta generato, il token non sarà più visibile, quindi è necessario salvarlo in un posto sicuro,
accessibile anche da casa.
Vi consiglio di utilizzare un password manager come [Bitwarden](https://bitwarden.com/).
Temporaneamente è possibile metterlo su Dropbox/Google Drive o su una chiavetta, ma questo non è molto sicuro.

### Configurazione client Git
Aprire un terminale e digitare i seguenti comandi. Modificarli per usare il proprio nome (o nickname)
e la propria email (se possibile usare la stessa con cui si è iscritti a **GitHub**).
```bash
git config --global user.name "Your Name"                  
git config --global user.email "youremail@yourdomain.com"
```

### Creazione repository
Dopo aver creato un account **GitHub**, cliccare sul bottone **New repository** o **New** per creare un nuovo repository.
Mettere il nome che si preferisce e poi selezionare la visibilità **pubblica**.
Questo permetterà a tutti di vedere il contenuto e faciliterà la risposta a eventuali domande da casa.

**IMPORTANTE**: Selezionare l'opzione *"add a README file"*

Creare il repository. Come si vede esso contiene solamente il file *README.md*.
È comune avere questo tipo di file, scritto in [Markdown](https://www.markdownguide.org/basic-syntax/),
per descrivere il contenuto del repository.

### Sui pc del laboratorio (provvisoria)
Prima di usare git eseguire il seguente comando:

```bash
git config --global http.proxy http://prxlaib.polito.it:8080
```
Aprire la **git bash** e spostarsi nel disco *D:* tramite il seguente comando:

```bash
cd d:\
```

### Checkout repository (git clone)
Sulla pagina del repository, cliccare sul bottone verde **Code** e copiare l'url HTTPS (non SSH).
Aprire un terminale in una cartella del proprio PC dove si vuole scaricarlo.

Digitare il seguente comando sostituendo l'url copiato:
```bash
git clone "url-copiato"
```

Verrà creata una directory con il nome del proprio repository.
La cartella è la working directory,
il cui contenuto viene inizializzato con i file aggiornati all'ultima versione (commit) disponibile sul repository.
In questo caso la directory contiene solamente il file *README.md*.

Se rendete visibili le cartelle nascoste all'interno della working directory, vedrete un cartella nominata .git.
Questa è una copia del repository remoto, contenente tutti i file utili per mantenere la "storia".

### Staging (git add)
Modificare a piacimento il file *README.md* all'interno della working directory, per esempio:
```Markdown
# Il mio primo repository
Contiene tutte le soluzioni dei laboratori!
```
Aprire un terminale nella working directory e digitare:
```bash
git status
```
Il comando mostra lo stato del vostro repository.
In questo caso mostra che il file README.md ha subito delle modifiche.
Digitare i seguenti comandi:

```bash
git add README.md
git status
```
Ora le modifiche al file sono presenti nella *staging area* e verranno incluse nel prossimo commit (versione).
È anche possibile creare nuovi file e aggiungerli alla staging area utilizzando lo stesso comando.
Per aggiungere tutte le modifiche (anche rimozioni file) usare:
```bash
git add -A
```
Per togliere una modifica/file dalla staging area usare:
```bash
git restore --staged nome_file
```

### Commit (git commit)
Per creare un nuovo commit, ovvero una versione dei file di progetto, usare il comando:
```bash
git commit -m "aggiornamento README.md"
```
Il messaggio, definito tramite il flag *-m* è una descrizione delle modifiche fatte.
Evitare messaggi troppo generici: in futuro sarà utile per capire cos'è stato fatto.

Visualizzare lo stato del repository:
```bash
git status
```
L'output ora segnala che il repository locale è avanti di un commit rispetto a quello remoto.

### Aggiornamento repository remoto (git push)
Per aggiornare il repository remoto il seguente comando:
```bash
git push
```
Inserire quando richiesto il proprio username e password. Come password usare il token **GitHub** precedentemente creato.
Su Windows potete copiarlo con ```ctrl + v```, su Mac potete usare ```Modifica -> Incolla```. 
Il token non comparirà perché l'input è nascosto.
Su Windows è possibile che compaia una finestra che richiede il token. Se accade inserirlo lì.

Il comando poi sincronizzerà i commit del repository locale sul server remoto (**GitHub**)
Se andate sulla pagina **GitHub** del repository vedrete le nuove modifiche.

### Aggiornamento repository locale (git fetch/push)
Rinominare la working directory e scaricare un'altra copia del repository remoto.
Aprire un terminale dove si vuole mettere la copia (non nella working directory).
```bash
git clone url-copiato
```
Creare un file hello.py contenete un semplice **hello world** e copiarlo nella working directory.
Per comodità è possibile usare un semplice text editor, salvare il file in *.txt* e rinominare l'estensione a *.py*.
Successivamente fare add, commit e push:

```bash
git add hello.py
git commit -m "aggiunto hello-world"
git push
```

Tornare nella working directory del primo repository ed eseguire i comandi:
```bash
git status
git fetch
git status
```
Come si può vedere il comando fetch scarica informazioni sulle modifiche del repository remoto,
non visibili tramite il primo comando status.
In questo caso comunica che il repository locale è indietro di un commit.

Per aggiornare il repository locale con le nuove modifiche usare il comando pull:
```bash
git pull
git status
```
A questo punto il comando status comunica che il repository locale è aggiornato.

### Ignorare file (.gitignore)
Inserire file binari (non di testo) all'interno dei repository è fortemente sconsigliato,
perché Git hon ha un modo efficiente per tracciarne in cambiamenti,
e li copia interamente ogni volta che vengono modificati.
Dovendo mantenere tutte le versioni precedenti, i file obsoleti non vengono eliminati. 
Questo può far crescere velocemente le dimensioni del repository.

Copiare un'immagine all'interno dela working directory.

Eseguire il comando:
```
git status
```
Questo mostra che l'immagine deve essere aggiunta alla staging area.

Creare un file chiamato *.gitignore* (nascosto, senza estensione) nella working directory. 
Questo può contenere un elenco di file/cartelle da escludere dal tracking:

```
nome_file_immagine
```
Ripetere il comando.
```
git status
```
Ora l'aggiunta dell'immagine è esclusa dalle modifiche. Più informazioni sono presenti
[qui](https://git-scm.com/docs/gitignore)

### Pycharm
In PyCharm è possibile cliccare su ```File-> Open``` 
e aprire la working directory di un repository git locale o una sua sotto-cartella.

In basso sarà visibile la scheda git, 
che permette di accedere alle informazioni sul repository. 
Sul lato sinistro, invece, è presente la scheda commit
che permette di eseguire tramite IDE alcune delle operazioni descritte in precedenza.

Volendo usare il terminale, è presente una scheda *Terminal* che lo permette.
È possibile digitare qui tutti i comandi git visti in precedenza.

### Laboratori
Clonare il [repository del corso](https://github.com/ptrchv/APOpublic), e fare pull quando viene aggiornato.
Usare un proprio repository separato dove copiare i laboratori e svolgerli. Il repository del corso non può essere
aggiornato da voi.


### Conflitti
È possibile che ci siano dei conflitti quando si fa il pull e sono già presenti delle modifiche locali.
Questo aspetto non viene trattato perché più avanzato e riguarda il
[branching](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell),
ovvero quando più fili di sviluppo divergono e si reincontrano.

Il modo semplice per risolvere eventuali conflitti è clonare nuovamente il repository remoto
e sostituire o aggiungere i file modificati nella nuova working directory. Poi si può procedere a fare un nuovo commit.



### Riferimenti
Documentazione di Git (https://git-scm.com/docs)

Libro git (https://git-scm.com/book/en/v2)
