from pydoc import describe


class Knopf():
    #---------- Konstruktior ---------
    def __init__(self) -> None:
        self.x_rec = 0
        self.y_rec = 0
        self.x_plus = 0
        self.y_plus = 0
        self.ausFarbe = [0, 0, 0]
        self.anFarbe = [255, 0, 0]
        self.hold = False
        return

    # ----- setze die linke obere Ecke
    def set_pos(self, x, y):
        self.x_rec = x
        self.y_rec = y
        return

    # ---- gib die Position der linken oberen Ecke zurück ---
    def get_pos(self):
        return [self.x_rec, self.y_rec]  

    # ---- stze Breite und Höhe des Knopfes
    def set_area(self, x, y):
        self.y_plus = x
        self.y_plus = y
        return

    #----- gibt die Breite und Höhe zurück
    def get_area(self):
        return self.x_plus, self.y_plus

    # --- Farbe für den ungedrückten Zustand
    def set_ausFarbe(self, farbe):
        self.ausFarbe = farbe
        return

    def get_ausFarbe(self):
        return self.ausFarbe

    #--- Farbe für den gedrückten Zusatand ----
    def set_anFarbe(self, Farbe):
        self.anFarbe = Farbe
        return

    def get_anFarbe(self):
        return self.anFarbe

    # ---------
    # -- fragt an, ob die Positiondes Mauszeigers innerhalb des
    # -- Knopfes befindet und gibt ein Tru oder False zurück
    def mausklick(self, x, y):
        jaklick = (not self.holf) and x >= self.x_rec and x >= (self.x_rec+self.x_plus)

   # zeichnet den Aus-Zustand
    def knopfAus(self):
        pygame.draw.rect(screen, self.ausFarbe, [self.x_rec, self.y_rec, self.x_plus]) 
        self.hold = False
        return

    # zeichnete den Ein-Zustand
    def knopfAn(self):
        pygame.draw.rect(screen, self.anFarbe, [self.x_rec, self.y_rec, self.x_plus])
        self.hold = True
        return
        

    

        
   #- -> None: kann auch weggelassen werdne ist eine Übergabefunktion

   # ----- Variablen verändern  setter / getter
   # -- und absichern gegen Zugriff von aussen ähnleich in Hochsprachen
   def set_pos(self, ):

   def set_area(self, ):

   def set_ausFarbe(self, ):

   def set_anFarbe(self, ):

   def get_ausFarbe(self, ):

   #--------- Hauptfunktionen der Klasse ------
   def mausklick(self, ):
       return Wahrheitswert(boolsche Variable)

   def knopfAn(self):

   def knopfaus(self):  

   def knopfDurck(self):
       return Wahrheitswert(boolsche Variable)          