class Calcolatrice:
    
    def __init__(self):
        # Inizializzo le liste vuote per tenere a mente i calcoli
        self.risultati = []
        self.valori_inseriti = []
        # Imposto il contatore a zero e ricordo che posso fare al massimo 4 operazioni
        self.numero_operazioni = 0
        self.max_operazioni = 4
        
    def addizione(self, lista):
        # Parto da zero e sommo tutti i numeri che mi hai passato
        risultato = 0
        for n in lista:
            risultato += n
        # Salvo i numeri usati e il risultato finale nella mia memoria
        self.valori_inseriti.append(lista)
        self.risultati.append(risultato)
        # Tengo conto che ho appena fatto un'operazione
        self.numero_operazioni += 1
        return risultato
    
    def sottrazione(self, lista):
        # Se non mi dai numeri, non posso fare nulla
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
        # Salvo tutto nella mia memoria e aggiorno il contatore
        self.valori_inseriti.append(lista)
        self.risultati.append(risultato)
        self.numero_operazioni += 1
        return risultato
    
    def divisione(self, lista):
        if len(lista) == 0:
            return 0
        # Parto dal primo numero e divido per gli altri
        risultato = lista[0]
        for i in range(1, len(lista)):
            # Controllo che nessuno mi chieda di dividere per zero
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
        if len(lista) == 0:
            return 0
        # Prima sommo tutti i numeri che mi hai dato
        somma = 0
        for n in lista:
            somma += n
        # Poi li divido per la quantità totale per trovare la media
        risultato = somma / len(lista)
        # Memorizzo i valori e il risultato della media
        self.valori_inseriti.append(lista)
        self.risultati.append(risultato)
        self.numero_operazioni += 1
        return risultato
        
    def stampa_storico(self):
        # Scorro la mia memoria e ti mostro a video tutte le operazioni che ho fatto
        for i in range(len(self.valori_inseriti)):
            print(str(i + 1) + ". Valori: " + str(self.valori_inseriti[i]) + " -> Risultato: " + str(self.risultati[i]))
        # Ti dico quante operazioni ho consumato rispetto al mio limite
        print("Operazioni fatte: " + str(self.numero_operazioni) + "/" + str(self.max_operazioni))