import pandas as pd

# Charger les données
df = pd.read_csv("dataset_valiuz_simule.csv")

# Afficher les premières lignes
print(df.head())

# Infos sur le datasetv
print(df.info())

# Valeurs manquantes
print(df.isnull().sum())

# Doublons
print(df.duplicated().sum())

# Voir les périodes
print(df["periode"].value_counts())

# Nouveau champ : chiffre d'affaires par ligne
df["chiffre_affaires"] = df["quantite"] * df["prix_unitaire"]

# Groupe par période
kpi_par_periode = df.groupby("periode").agg(
    total_ca=("chiffre_affaires", "sum"),
    nb_commandes=("id_commande", "count"),
    panier_moyen=("chiffre_affaires", "mean"),
    nb_clients_uniques=("client_id", "nunique")
)

print(kpi_par_periode)

