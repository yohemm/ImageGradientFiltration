SAE Python sur la pollution Lumineuse:


Rappel des filtres:
-Gaussian :
Le filtre Gaussian, le but est d'ajouter un flou sur l'image 

-Sobel
Le filtre de Sobel est utilisé pour détecter les contours dans une image. 

-RregressionLineaireFilter :

-PolynomeFilter : 

-Kalman :
Le but de ce filtre et de gérer le mouvement sur l'image et de gérer donc le gradient 

-MoyenneMobile :
Le but de ce filtre est de faire une moyenne de toute l'image et cet moyenne va se décaler pour faire chaque pixel

-ManualGrayFilter :


Rappel des checkers :


Explication des algos: 

Tout d'abord pour nous faciliter la tache nous avons décider de faire un template pour chaque filtre 
nous utilisons le même template pour chaque filtre. Le test des filtres se fait au niveau du main
ou nous choissisons quel filtre nous soihaitons utiliser. 

Nous avons un main ou tous les filtres sont utilisé a la fois !


Lancement du programme principal:
Pour lancer le proggramme il faut faire la commande "python -m archi"