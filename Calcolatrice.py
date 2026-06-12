class Calcolatrice:
    
    def __init__(self):
        # Inizializzo le liste vuote per memorizzare i calcoli
        self.risultati = []
        self.valori_inseriti = []
        # Imposto il contatore a zero e definisco il limite massimo di 4 operazioni
        self.numero_operazioni = 0
        self.max_operazioni = 4
        
    def addizione(self, lista):
        # Parto da zero e sommo tutti i numeri passati
        risultato = 0
        for n in lista:
            risultato += n
        # Salvo i numeri usati e il risultato finale
        self.valori_inseriti.append(lista)
        self.risultati.append(risultato)
        # Incremento il contatore delle operazioni eseguite
        self.numero_operazioni += 1
        return risultato
    
    def sottrazione(self, lista):
        # Se la lista è vuota, restituisco 0
        if len(lista) == 0:
            return 0
        # Parto dal primo numero e sottraggo tutti gli altri in sequenza
        risultato = lista[0]
        for i in range(1, len(lista)):
            risultato -= lista[i]
        # Registro i valori e il risultato ottenuto
        self.valori_inseriti.append(lista)
        self.risultati.append(risultato)
        self.numero_operazioni += 1
        return risultato
        
    def moltiplicazione(self, lista):
        # Parto da 1 per poter moltiplicare tutti i numeri della lista
        risultato = 1
        for n in lista:
            risultato *= n
        # Salvo i dati e aggiorno il contatore
        self.valori_inseriti.append(lista)
        self.risultati.append(risultato)
        self.numero_operazioni += 1
        return risultato
    
    def divisione(self, lista):
        # Se la lista è vuota, restituisco 0
        if len(lista) == 0:
            return 0
        # Parto dal primo numero e divido per gli altri
        risultato = lista[0]
        for i in range(1, len(lista)):
            # Controllo che non ci siano divisioni per zero
            if lista[i] == 0:
                print("Errore: divisione per zero")
                return None
            risultato /= lista[i]
        # Se il calcolo è riuscito, lo salvo e conto l'operazione
        self.valori_inseriti.append(lista)
        self.risultati.append(risultato)
        self.numero_operazioni += 1
        return risultato
    
    def media(self, lista):
        # Se la lista è vuota, restituisco 0
        if len(lista) == 0:
            return 0
        # Prima sommo tutti i numeri presenti nella lista
        somma = 0
        for n in lista:
            somma += n
        # Poi divido la somma per la quantità totale per trovare la media
        risultato = somma / len(lista)
        # Memorizzo i valori e il risultato della media
        self.valori_inseriti.append(lista)
        self.risultati.append(risultato)
        self.numero_operazioni += 1
        return risultato
        
    def stampa_storico(self):
        # Scorro la memoria e stampo a video tutte le operazioni eseguite
        for i in range(len(self.valori_inseriti)):
            print(str(i + 1) + ". Valori: " + str(self.valori_inseriti[i]) + " -> Risultato: " + str(self.risultati[i]))
        # Mostro quante operazioni ho consumato rispetto al limite massimo
        print("Operazioni fatte: " + str(self.numero_operazioni) + "/" + str(self.max_operazioni))
