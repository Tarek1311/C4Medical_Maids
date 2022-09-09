# C4Medical Maids
### Notre projet est une application de vente et location de matériels médical et paramédical.


**L'aplication a pour objectif d'apporter des solition concrète pour la vente et location de matériel/mobilier médical pour :**  
       1. Les particuliers (personnes âgées, dépendantes, handicapés ou encore personnes à la recherche de confort et de bien-être)    
       2. les professionnels de santé exerçant en libéral (hmédecins, infirmières, kinésithérapeutes, …) et les collectivités (hôpitaux, maisons de retraite, EHPAD, …)    
       3. Prestataire de santé à domicile (location d'un lit médicalisé, location de fauteuil roulant, mise en place d'une nutrition entérale à domicile…)                                                                                                                                                    4. fournisseur de matériel médical et services auprès des professionnels de santé (collectivités ou libéraux).
                
**Nos services et activités :**  
 	     1. La location de lits médicalisés  
 	     2. La location ou vente de fauteuils roulants et déambulateurs    
 	     3. La location ou la vente de fauteuils releveurs   
 	     4. Les accessoires chauffants et massants  
 	     5. La vente d’accessoires d'aide à la toilette, etc    

## Récapitulatif du projet  
C4Medical_Maids
├── app
│     ├── __init__.py
│     └── app.py
├── .gitignore
├── .pre-commit-config.yaml
├── README.md
├── requirements.txt
├── README.md 
└── setup.py  

## Prérequis
Afin de pouvoir exécuter l'application sur votre poste, vous devez d'aborder installer les dépendances suivantes :  
  * Dash
 
### Installation
#### Dash [ici](https://dash.plotly.com//)  

  2. Créer un venv python3 et tous les paquets requis et l'application dans votre environnement virtuel.  
  	       A la racine du projet, lancez :  
		   		`* python3 -m venv venv`  
           		`* pip install -r requirements`  
                `* pip install -e .`    
	       *Remarque : venv\Scripts\activate pour Windows*  
  3. Taper `python app/app.py`  
 
### Lancement de notre application en local
  1. Après avoir installé Dash, ouvrir une invite de commande  
  2. Taper `python app/app.py`  
  3. Visiter http://localhost:8888 dans votre navigateur Web  
 
## Run the tests  
1. pytest  
##  Cloner le repository git distant dans le répertoire local  
git clone https://github.com/Tarek1311/C4Medical_Maids.git   