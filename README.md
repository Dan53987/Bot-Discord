# Bot-Discord
## Progetto Discord Bot

Il progetto consiste nella realizzazione di un bot per Discord usando Python e la libreria discord.py. L’obiettivo è stato quello di creare un bot in grado di gestire comandi utili, comandi per la moderazione e anche qualche comando vario.

Il bot è stato suddiviso in più file per tenere separate le funzionalità principali. Ho usato il sistema dei "Cog", cioè delle classi che raggruppano comandi simili. Questo permette di mantenere il codice più pulito e semplice da gestire. I file sono:

-basic.py contiene comandi semplici come ping, saluto e informazioni utente.

-moderation.py contiene comandi di moderazione come kick, ban e unban.

-fun.py contiene comandi di intrattenimento, come ad esempio la 8ball.

Il file principale (bot.py) si occupa di avviare il bot, caricare automaticamente tutti i cog dalla cartella, e leggere il token di autenticazione da un file esterno.
Funzionalità principali

-Comandi base
 .ping: mostra la latenza del bot.
 .hi: saluta l’utente che scrive.
 .userinfo @utente: mostra nickname, status, ruolo più alto e data di ingresso nel server.

-Comandi di moderazione
 .kick @utente [motivo]: espelle un utente, se l’autore ha i permessi.
 .ban @utente [motivo]: banna un utente e gli invia un messaggio privato con il motivo.
 .unban nome_utente: cerca nella lista dei bannati e rimuove il ban se trova una corrispondenza.

-Comandi vari
  8ball: risponde con una frase casuale tra quelle presenti in una lista.

Aspetti tecnici
Il progetto utilizza funzioni asincrone (async def) per lavorare con gli eventi e i comandi in modo corretto su Discord. Ho gestito i permessi per evitare che gli utenti possano bannare o espellere persone con ruoli più alti. I messaggi più complessi vengono inviati come embed, per renderli più chiari e ordinati. Inoltre, ho fatto attenzione a evitare che il bot possa kickare o bannare sé stesso o l’autore del comando.
Conclusione

Il progetto mi ha aiutato a capire meglio come funziona la programmazione asincrona in Python e come interagire con le API di Discord. È stato utile anche per imparare a scrivere codice più organizzato e a gestire errori.
