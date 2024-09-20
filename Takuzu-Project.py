import sys ,random
from PyQt5.QtWidgets import QApplication, QMessageBox,QPushButton, QMainWindow,QToolBar, QAction, QStatusBar,QHBoxLayout, QLabel,QVBoxLayout,QWidget, QGridLayout
from PyQt5.QtCore import QCoreApplication,Qt,QSize
from PyQt5.QtGui import QIcon, QKeySequence, QFont
       
    
class PushButton(QPushButton) :
    def __init__(self,text):
        super(PushButton,self).__init__(text)
        self.setText(text)
        self.setMinimumSize(QSize(80,80))
        self.setMaximumSize(QSize(82,82))
        
class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Takuzu")
        self.setGeometry(300,100,1000,700)
        
        self.vie = 6
        self.nbr_indice = 6
        self.label_vie = QLabel()
        self.label_vie.setText('Nombre de vie : '+str(self.vie))
        self.label_vie.setFont(QFont('Calibri',12))
        self.label2 = QLabel()
        self.label2.setText("Nombre d'indices restant : "+ str(self.nbr_indice))
        self.label2.setFont(QFont('Calibri',12))
        self.niveau = QLabel()
        
        self.niveau.setText('Niveau : Débutant')

        self.niveau.setFont(QFont('Calibri',12))
        self.button_indice = QPushButton('indice')
        self.button_indice.clicked.connect(self.indice)
        
        self.L_verif = []
        
        taille = 6
        self.n = 6
        self.solution = self.takuzu(taille)
        self.masque = self.grille_masque(taille)
        self.jeu = self.grille_jeu(self.solution,self.masque,taille)
      
        self.jeu_verif =  self.grille_jeu(self.solution,self.masque,taille)
        
        
        self.button_verifier = QPushButton('vérifier')
        self.button_verifier.clicked.connect(self.verifier)
        self.button_indice.setMinimumSize(QSize(300,150))
        self.button_indice.setMaximumSize(QSize(300,150))
        self.button_verifier.setMinimumSize(QSize(300,150))
        self.button_verifier.setMaximumSize(QSize(300,150))
        
        
    
        self.display(6,self.solution,self.masque,self.jeu)
        
        self.create_menu()
        
        
        
#####################################################################################           
        '''
        Partie codage du jeu
        '''
        
        '''Créer solution'''
    def créer_ligne(self,n) :
        L = []
        for i in range(n) :
            L.append(random.randint(0,1))
        return L
        
    def vérif_ligne(self,L,n) :
        nbr0 = 0
        nbr1 = 0
        i = 0
        compteur = 0
        compteur1 = 0
        for k in L :
            if k == 1 :
                compteur1 += 1 
                compteur = 0
                if compteur>=3 or compteur1>=3 :
                    return False
            else :
                compteur += 1
                compteur1 = 0
                if compteur>=3 or compteur1>=3 :
                    return False
        while nbr0 < n-1 and nbr1< n-1 and i<n :
            if L[i] == 0 :
                nbr0 += 1
            else :
                nbr1 +=1
            i+=1
        if nbr0 == n/2 or nbr1 == n/2 :
            return True
        return False
    
    
    def takuzu_ligne(self,n) :
        solution_ligne = []
        while len(solution_ligne) < n :
            L = self.créer_ligne(n)
            if self.vérif_ligne(L,n) :
                égalité_ligne = False
                for ligne in solution_ligne :
                     if ligne == L :
                        égalité_ligne = True
                if not égalité_ligne :
                     solution_ligne.append(L)
        return solution_ligne
    
     
    def vérif_colonne(self,L,j,n) :
        nbr0 = 0
        nbr1 = 0
        i = 0
        compteur = 0
        compteur1 = 0
        for k in range(n) :
            if L[k][j] == 1 :
                compteur1 += 1 
                compteur = 0
                if compteur>=3 or compteur1>=3:
                    return False
            else :
                compteur += 1
                compteur1 = 0
                if compteur>=3 or compteur1>=3 :
                    return False
        while nbr0 < n-1 and nbr1< n-1 and i<n :
            if L[i][j] == 0 :
                nbr0 += 1
            else :
                nbr1 +=1
            i+=1
        if nbr0 == n/2 or nbr1 == n/2 :
            return True
        return False
     
    def takuzu(self,n):
        ok = False
        while not ok :
            ok = True
            solution = self.takuzu_ligne(n)
            for j in range(n) :
                if not self.vérif_colonne(solution,j,n) :
                     ok = False
        return solution
    
    ''' créer masque '''
    def grille_masque(self,n) :
        if n == 4 :
            masque = [[],[],[],[]]
            N = [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
            random.shuffle(N)
            j = 0
            for i in range(len(masque)):
                while len(masque[i]) < 4 :
                    masque[i].append(N[j])
                    j+=1
            return masque
        elif n == 6 :
            masque = [[],[],[],[],[],[]]
            N = [1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,-1,-1,-1,-1]
            random.shuffle(N)
            j = 0
            for i in range(len(masque)):
                while len(masque[i]) < 6 :
                    masque[i].append(N[j])
                    j+=1
            return masque
        
    ''' créer grile de jeu '''
    def grille_jeu(self,solution,masque,n) :
        grille_jeu = []
        for i in range (n) :
            L = []
            for j in range(n) :
                if masque [i][j] == 1 :
                    L.append(solution[i][j])
                else :
                    L.append('')
            grille_jeu.append(L)
        return grille_jeu
    
    
    
    '''Fin de la partie codage du jeu'''

#####################################################################################
        
    def create_menu(self) :
        ####
        self.menuGrille = self.menuBar().addMenu("Grille")
        self.toolbar = QToolBar('')
        self.addToolBar(self.toolbar)
        self.setStatusBar(QStatusBar(self))
        
        self.action_grille4 = QAction(QIcon("board-game.png"), "Grille 4" , self)
        self.action_grille4.triggered.connect(self.onGrillePar4)
        self.action_grille4.setShortcut(QKeySequence("Ctrl+G"))
        
        
        self.action_grille4.setStatusTip("")
        self.toolbar.addAction(self.action_grille4)
        
        
        self.action_grille6 = QAction(QIcon("board-game-go.png"), "Grille 6" , self)
        self.action_grille6.triggered.connect(self.onGrillePar6)
        self.action_grille6.setShortcut(QKeySequence("Ctrl+X"))
        
        self.action_grille6.setStatusTip("")
        self.toolbar.addAction(self.action_grille6)
        
        
        self.menuGrille.addAction(self.action_grille4)
        self.menuGrille.addAction(self.action_grille6)
        ####
        self.menuJouer = self.menuBar().addMenu("Jouer")
        
        self.action_debutant = QAction(QIcon("user-green.png"), "Niveau débutant" , self)
        self.action_debutant.triggered.connect(self.onNivDeb)
        self.action_debutant.setShortcut(QKeySequence("Ctrl+D"))
        
        self.action_debutant.setStatusTip("")
        self.toolbar.addAction(self.action_debutant)
        
        self.action_inter = QAction(QIcon("user-red.png"), "Niveau intermédiaire" , self)
        self.action_inter.triggered.connect(self.onNivInter)
        self.action_inter.setShortcut(QKeySequence("Ctrl+I"))
        
        self.action_inter.setStatusTip("")
        self.toolbar.addAction(self.action_inter)
        
        self.menuJouer.addAction(self.action_debutant)
        self.menuJouer.addAction(self.action_inter)
        ####
        self.menuResolution = self.menuBar().addMenu("Resolution")
        
        self.action_resolution = QAction(QIcon("application-search-result.png"), "Solveur de grille" , self)
        self.action_resolution.triggered.connect(self.onGenerateur)
        self.action_resolution.setShortcut(QKeySequence("Ctrl+S"))
        
        self.action_resolution.setStatusTip("")
        self.toolbar.addAction(self.action_resolution)
        
        self.menuResolution.addAction(self.action_resolution)
        ####
        self.menuApropos = self.menuBar().addMenu("A propos")
        
        self.action_regle = QAction(QIcon("game-monitor.png"), "Règles du jeu" , self)
        self.action_regle.triggered.connect(self.onRegles)
        self.action_regle.setShortcut(QKeySequence("Ctrl+R"))
        
        self.action_regle.setStatusTip("")
        self.toolbar.addAction(self.action_regle)
        
        self.action_qui = QAction(QIcon("animal-monkey.png"), "Qui ?" , self)
        self.action_qui.triggered.connect(self.onEquipe)
        self.action_qui.setShortcut(QKeySequence("Ctrl+E"))
        
        self.action_qui.setStatusTip("")
        self.toolbar.addAction(self.action_qui)
        
        self.menuApropos.addAction(self.action_regle)
        self.menuApropos.addSeparator()
        self.menuApropos.addAction(self.action_qui)
        ####
        self.menuQuitter = self.menuBar().addMenu("Quiter")
        self.action_quitter = QAction(QIcon("bomb.png"), "Quitter" , self)
        self.action_quitter.triggered.connect(self.onQuitter)
        self.action_quitter.setShortcut(QKeySequence("Ctrl+Q"))
        self.menuQuitter.addAction(self.action_quitter) 
        
        self.action_quitter.setStatusTip("")
        self.toolbar.addAction(self.action_quitter)
    
    def display(self, taille, solu , masque, jeu) :
        
        self.layout = QGridLayout()
        self.layout.setSpacing(1)
        
        if taille == 4 :
            L = ["",1,2,3,4]
            lettre = ["","A","B","C","D"]
        elif taille == 6 :
            L = ["",1,2,3,4,5,6]
            lettre = ["","A","B","C","D","E","F"]
            
        for i in range(taille + 1) :
            for j in range(taille + 1) :
                if i == 0 :
                    label1 = QLabel(f'{L[j]}')
                    label1.setAlignment(Qt.AlignCenter)
                    self.layout.addWidget(label1,i,j)
                elif j == 0 and i != 0 :
                    label = QLabel(str(lettre[i]))
                    label.setAlignment(Qt.AlignCenter) #Qt.AlignRight | 
                    self.layout.addWidget(label,i,j)
                elif i!=0 and j!=0 :
                    if masque[i-1][j-1] == 1 :
                        self.button = PushButton(f'{jeu[i-1][j-1]}')
                        self.button.setStyleSheet('border:1px solid blue')
                        self.button.setFont(QFont('Times',18))
                    
                    #self.button = PushButton('i')
                    #self.button.setMinimumSize(QSize(150,100))
                    #self.button.setMaximumSize(QSize(150,100))
                    elif masque[i-1][j-1] == -1 :
                        self.button = PushButton(f'{jeu[i-1][j-1]}')
                        self.button.setStyleSheet('border:1px solid blue')
                        self.button.setFont(QFont('Times',18))
                        self.button.clicked.connect(self.onClick)
                        self.button.setStyleSheet('background : white')
                    self.layout.addWidget(self.button,i,j)
     
        self.hbox_central = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        
        self.vbox_verif = QVBoxLayout()
        self.vbox_verif.setSpacing(0)
        
        
        self.label1 = QLabel("INDICES ET VERIFICATION")
        self.label1.setAlignment(Qt.AlignTop)
        self.label1.setStyleSheet('background-color : rgb(153,255,153) ; color : black')
        self.label1.setFont(QFont("Times",10))
        self.label1.setMargin(4)
        self.vbox_verif.addWidget(self.label1)
        
        
        self.vbox = QVBoxLayout()
        
        self.hbox_central.addLayout(self.layout)
        self.hbox_central.addLayout(self.vbox_verif)
        
        self.vbox.addLayout(self.hbox_central)
        
        self.hbox1.addWidget(self.label_vie)
        self.hbox1.addWidget(self.label2)
        self.hbox1.addWidget(self.niveau)
        self.hbox2.addWidget(self.button_indice)
        self.hbox2.addWidget(self.button_verifier)
        
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        
        self.widget = QWidget()
        self.widget.setLayout(self.vbox)
        self.setCentralWidget(self.widget)
        
    def onGrillePar4(self) :
        popup = QMessageBox(QMessageBox.Warning,'ATTENTION','En changeant de niveau vous allez réinitialiser la partie, êtes vous sûr ?',QMessageBox.Ok | QMessageBox.Cancel)
        popup.show()
        valeur = popup.exec()
        if valeur == QMessageBox.Ok :
            self.n = 4
            self.solution = self.takuzu(self.n)
            self.masque = self.grille_masque(self.n)
            self.jeu = self.grille_jeu(self.solution,self.masque,self.n)
            self.display(4,self.solution,self.masque,self.jeu)
            
            self.onNivDeb()
            self.L_verif = []
        
        
    def onGrillePar6(self) :
        popup = QMessageBox(QMessageBox.Warning,'ATTENTION','En changeant de niveau vous allez réinitialiser la partie, êtes vous sûr ?',QMessageBox.Ok | QMessageBox.Cancel)
        popup.show()
        valeur = popup.exec()
        if valeur == QMessageBox.Ok :
            self.n = 6
            self.solution = self.takuzu(self.n)
            self.masque = self.grille_masque(self.n)
            self.jeu = self.grille_jeu(self.solution,self.masque,self.n)
            self.display(6,self.solution,self.masque,self.jeu)
            self.onNivDeb()
            self.L_verif = []
        
    def onClick(self) :
        pass
        
        valeur_button = self.sender().text()
        if valeur_button=='' :
            self.sender().setText('0')
        elif valeur_button == '0' :
            self.sender().setText('1')
        elif valeur_button == '1' :
            self.sender().setText('')
        
        val = self.sender()
        idx = self.layout.indexOf(val)
        pos = self.layout.getItemPosition(idx)
        self.L_verif.append(pos[:2])
        
        '''Codage vérification'''

    def compteur_pos(self,L,pos) :
        compteur = 0
        for couple in L :
            if pos == couple :
                compteur += 1
        return compteur
               
    def grille_instant(self,Ljeu,L) :
        L0 = [1,4,7,10,13,16,19,22,25]
        L1 = [2,5,8,11,14,17,20,23,26]
        for i in range(1,len(Ljeu)+1) :
            for j in range(1,len(Ljeu)+1) :
                if (i,j) in L :
                    compteur = self.compteur_pos(L,(i,j))
                    if compteur in L0 :
                        Ljeu[i-1][j-1] = 0
                    elif compteur in L1 :
                        Ljeu[i-1][j-1] = 1
        return Ljeu


    def vérif_ligne_pour_vérifier(self,L,n) :
        nbr0 = 0
        nbr1 = 0
        i = 0
        compteur = 0
        compteur1 = 0
        for k in L :
            if k == 1 :
                compteur1 += 1 
                compteur = 0
                if compteur>=3 or compteur1>=3 :
                    return False
            elif k == 0 :
                compteur += 1
                compteur1 = 0
                if compteur>=3 or compteur1>=3 :
                    return False
        while nbr0 < n-1 and nbr1< n-1 and i<n :
            if L[i] == 0 :
                nbr0 += 1
            elif L[i] == 1 :
                nbr1 +=1
            i+=1
        if nbr0 <= n/2 and nbr1 <= n/2 :
            return True
        return False          
    
    def vérif_colonne_pour_vérifier(self,L,j,n) :
        nbr0 = 0
        nbr1 = 0
        i = 0
        compteur = 0
        compteur1 = 0
        for k in range(n) :
            if L[k][j] == 1 :
                compteur1 += 1 
                compteur = 0
                if compteur>3 or compteur1>3:
                    return False
            elif L[k][j] == 0 :
                compteur += 1
                compteur1 = 0
                if compteur>=3 or compteur1>=3 :
                    return False
        while nbr0 < n-1 and nbr1< n-1 and i<n :
            if L[i][j] == 0 :
                nbr0 += 1
            elif L[k][j] == 0 :
                nbr1 +=1
            i+=1
        if nbr0 <= n/2 or nbr1 <= n/2 :
            return True
        return False
    
    def verif_button(self,Ljeu,Lsolution,Lmasque,n) :
        L = []
        dico = ["A","B","C","D","E","F"]
        for i in range(len(Ljeu)) :
            for j in range(len(Ljeu)) :
                if Ljeu[i][j] != '' :
                    if Ljeu[i][j] != Lsolution[i][j]   :
                        if self.vérif_ligne_pour_vérifier(Ljeu[i],n) and self.vérif_colonne_pour_vérifier(Ljeu,j,n) :
                            phrase = "Vous avez rentré " +str(Ljeu[i][j]) + " en " + str(dico[i])+str(j+1) + ", coup valide mais incorrect ! "
                            Ljeu[i][j] = ''
                            L.append(phrase)
                        else :
                            phrase = "Vous avez rentré " +str(Ljeu[i][j]) + " en " + str(dico[i])+str(j+1)  + ", c'est un coup invalide vous perdez 1 vie "
                            Ljeu[i][j] = ''
                            L.append(phrase)
                            self.label_vie.setText('Nombre de vie : '+str((self.vie)-1))
                            self.vie = self.vie-1
                    elif Ljeu[i][j] == Lsolution[i][j] and Lmasque[i][j] == -1    :
                        phrase = "Vous avez rentré " +str(Ljeu[i][j]) + " en " + str(dico[i])+str(j+1)  + ", coup correct ! "
                        L.append(phrase)
                        Lmasque[i][j]=1
        return L,Ljeu,Lsolution,Lmasque
    
    def verifier(self) :
        self.jeu_instant = self.grille_instant(self.jeu,self.L_verif)
        if self.jeu_instant == self.solution :
            popup = QMessageBox(QMessageBox.Information,'PARTIE GAGNEE' ,'Bravo tout est découvert !',QMessageBox.Ok )
            popup.show()
            valeur = popup.exec()
            if valeur == QMessageBox.Ok :
                self.close()
            return None
                
        
        N,self.jeu,self.solution,self.masque = self.verif_button(self.jeu_instant,self.solution,self.masque,self.n)
        
        for phrase in N :
            self.lab = QLabel(str(phrase))
            self.lab.setStyleSheet('background-color : rgb(153,255,153) ; color : black')
            self.vbox_verif.addWidget(self.lab)
        if self.vie <= 0 :
            popup = QMessageBox(QMessageBox.Warning,'PLUS DE VIES' ,"Vous n'avez plus de vies, la partie est finie \n\n Voulez vous rejouer ?",QMessageBox.Ok |QMessageBox.Cancel )
            popup.show()
            valeur = popup.exec()
            if valeur == QMessageBox.Ok :
                self.onGrillePar6()
            else :
                self.close()
            return None
        popup1 = QMessageBox(QMessageBox.Information,'Vérification' ,"Les vérifications sont dans la case 'INDICES ET VERIFICATION' à droite, cliquez 'Ok' quand vous avez fini de les observer, cela supprimera les entrées dans la case 'INDICE ET VERIFICATION' et mettra à jour la grille.",QMessageBox.Ok )
        popup1.show()
        popup1.setGeometry(1300,400,100,100)
        valeur = popup1.exec()
        if valeur == QMessageBox.Ok :
            self.display(self.n,self.solution,self.masque,self.jeu)
            self.L_verif = []
            
    def indice(self) :
        self.nbr_indice = self.nbr_indice - 1
        self.label2.setText ("Nombre d'indices restant : "+str(self.nbr_indice))
        if self.nbr_indice < 0 :
            self.nbr_indice = 0
            self.label2.setText ("Nombre d'indices restant : "+str(self.nbr_indice))
            self.popup1 = QMessageBox(QMessageBox.Warning,'Indice' ,"Vous avez utilisé tous vos indices",QMessageBox.Ok )
            self.popup1.show()
            return None
        for i in range(len(self.masque)) :
            for j in range(len(self.masque)) :
                if self.masque[i][j] == -1 :
                    self.masque[i][j] = 1
                    self.jeu[i][j] = self.solution[i][j]
                    self.display(self.n,self.solution,self.masque,self.jeu)
                    return None
            
    
    def onNivDeb(self) :
        self.vie = 6
        self.nbr_indice = 6
        self.label_vie.setText('Nombre de vie : '+str(self.vie))
        self.label2.setText ("Nombre d'indices restant : "+str(self.nbr_indice))
        self.niveau.setText('Niveau : Débutant')
                            
    def onNivInter(self):
        self.vie = 3
        self.nbr_indice = 3
        self.label_vie.setText('Nombre de vie : '+str(self.vie))
        self.label2.setText ("Nombre d'indices restant : "+str(self.nbr_indice))
        self.niveau.setText('Niveau : Intermédiaire')
            
    def onGenerateur(self):
        if self.n == 4 :
            self.display(self.n,self.solution,[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],self.solution)
        elif self.n == 6 :
            self.display(self.n,self.solution,[[1, 1, 1, 1,1,1], [1, 1, 1, 1,1,1], [1, 1, 1, 1,1,1],[1, 1, 1, 1,1,1],[1, 1, 1, 1,1,1],[1, 1, 1, 1,1,1]],self.solution)
            
    def onRegles(self) :
        self.popup = QMessageBox(QMessageBox.Information,'Les règles du Takuzu','Les règles du Takuzu sont extrêmement simples :\n\n 1. Dans une ligne, il doit y avoir autant de 0 que de 1 \n\n 2. Dans une colonne, il doit y avoir autant de 0 que de 1 \n\n 3. Il ne peut pas y avoir deux lignes identiques dans une grille\n\n 4. Il ne peut pas y avoir deux colonnes identiques dans une grille\n\n 5. Dans une ligne ou une colonne,' +
                                 'il ne peut y avoir plus de deux 0 ou deux 1 à la suite (on ne peut pas avoir trois 0 de suite ou trois 1 de suite)'+
                                 '\n\n 6. Le niveau débutant vous donne 6 vies \n\n 7. Le niveau intermédiaire vous donne 3 vies')
        self.popup.show()
        
    def onEquipe(self) :
        self.popup_qui = QMessageBox(QMessageBox.Information,'Qui sommes-nous ?',"Nous sommes une petite équipe de deux jeunes étudiants à l'ESME Sudria et avons réalisé ce petit jeu pour acquérir de nouvelles compétences et pour vous distraire. \n\nTrès bonne partie les amis ! \n\nAnthony QUENTIN & Guillaume REGNIER (SpéE 2022)")
        self.popup_qui.show()
    
    def onQuitter(self) :
        self.close()
    
app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
window = FenetrePrincipale()
window.show()
app.exec_()



