# Kata Unittest pour le Machine Learning

Il s'agit d'un petit kata mettant en pratique des tests unitaires destinés au pipeline de Machine Learning avec un focus
sur les dataframes.

## Instructions

Tout d'abord, checkout sur la branche qui donne un squelette vide :

```
git checkout start
```

Ensuite, le but est de créer une fonction __process__ qui prend un DataFrame en entrée et :

1. Supprime les colonnes voulues
2. Remplit les valeurs manquantes : la moyenne pour les numériques et la modalité la plus présente pour les catégories
3. Traite les catégories avec du one-hot encoding

En entrée, on peut considérer le DataFrame suivant :
![dataframe_entree](images/dataframe_entree.png)

En sortie, on peut considérer le DataFrame suivant :
![dataframe_sortie](images/dataframe_sortie.png)

## Prérequis

Installer les packages suivants avec la commande pip :

```
pip install -r requirements.txt
```

Pour être sûr de ne pas avoir de conflits, utilisez `virtualenv`

## Lancer les tests

Pour lancer les tests en utilisant `pytest`

```
python -m pytest
```

Pour lancer les tests en utilisant `unittest`

```
python -m unittest
```

## Solution

Pour voir la solution proposée :

```
git checkout solution
```

Le fichier TIPS.md donne également des conseils.

```
build and run docker image
```

```
docker image build . -t ai_clinique
```

```
docker run -it ai_clinique file.csv
```