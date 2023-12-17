from abc import ABC, abstractmethod

class Composition:
    def _init_(self, produit, quantite):
        self.__produit = produit
        self.__quantite = quantite
    
    @property
    def produit(self):
        return self.__produit
    

    def produit(self, value):
        self.__produit = value
    
    @property
    def quantite(self):
        return self.__quantite
    

    def quantite(self, valuer):
        self.__quantite = valuer

class Produit(ABC):
    def _init_(self, nom, code):
        self.__nom = nom
        self.__code = code
    
    @property
    def nom(self):
        return self.__nom
    
    @property
    def code(self):
        return self.__code
    
    @abstractmethod
    def getPrixHT(self):
        pass

class ProduitElementaire(Produit):
    def _init_(self, nom, code, prixAchat):
        super()._init_(nom, code)
        self.__prixAchat = prixAchat
    
    def _str_(self):
        return f"Produit élémentaire {self.nom} ({self.code})"
    
    def getPrixHT(self):
        return self.__prixAchat

class ProduitCompose(Produit):
      tauxTVA = 0.18

      def _init_(self, nom, code, fraisFabrication):
        super()._init_(nom, code)
        self._fraisFabrication = fraisFabrication
        self._listeConstituants = []

@property
def fraisFabrication(self):
        return self._fraisFabrication

def ajouterConstituant(self, constituant):
        self._listeConstituants.append(constituant)

def _str_(self):
        return f"Produit Composé: {self.nom}, Code: {self.code}, Frais de Fabrication: {self._fraisFabrication}"

def getPrixHT(self):
        prixHT = self._fraisFabrication
        for constituant in self._listeConstituants:
            prixHT += constituant.produit.getPrixHT() * constituant.quantite
        return prixHT

def equals(self, other):
        if not ().equals(other):
            return False
        return self._fraisFabrication == other._fraisFabrication and self.compareConstituants(other._listeConstituants)

def compareConstituants(self, otherConstituants):
        if len(self._listeConstituants) != len(otherConstituants):
            return False
        for constituant in self._listeConstituants:
            if not any(constituant.equals(c) for c in otherConstituants):
                return False
        return True