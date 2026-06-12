class Utente:
    
    
    lista_utenti = []
    
    def __init__(self, nome, password):
        self.nome = nome
        self.password = password
        self.max_operazioni = 4
        
    
    @classmethod
    def login(cls):
        print("LOGIN")
        
        controllo = True
        while controllo:
            nome = input("Inserisci nome:")
            password = input("Inserisci password:")
        
            for utente in cls.lista_utenti:
                if utente.nome == nome and utente.password == password:
                    print("Utente loggato") 
                    controllo = False
                    return utente
                else:
                    print("nome o password errati")
                
        
    @classmethod
    def registrati(cls):
        print("REGISTRATI")
        controllo = True
        while controllo:
            nuovo_nome = input("Inserisci nome:")
            nuova_password = input("Inserisci password:")

            for utente in cls.lista_utenti:
                if utente.nome == nuovo_nome:
                    print("Nome già usato")
                    controllo = False
                    continue
                    
            nuovo_utente = Utente(nuovo_nome, nuova_password)
            cls.lista_utenti.append(nuovo_utente)
            
            print("Utente", nuovo_utente.nome,"registrato con successo!")
            return nuovo_utente
    
        
        