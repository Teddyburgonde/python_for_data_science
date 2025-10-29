from load_csv import load
import matplotlib.pyplot as plt

def main():
	df_pib = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
	df_el = load("life_expectancy_years.csv")

	# Garder seulement les colonnes 'country' et '1900'
	df_pib_1900 = df_pib[["country", "1900"]].copy()
	df_el_1900 = df_el[["country", "1900"]].copy()

	# Renommer les colonnes pour plus de clarté
	df_pib_1900.columns = ["country", "gdp"]
	df_el_1900.columns = ["country", "life_expectancy"]


	# Fusionner les deux DataFrames sur la colonne 'country'
	df_merged = df_pib_1900.merge(df_el_1900, on="country")

	# Supprimer les lignes avec des valeurs manquantes (NaN)
	df_merged = df_merged.dropna()

	# Convertir les colonnes 'gdp' et 'life_expectancy' en float
	df_merged["gdp"] = df_merged["gdp"].astype(float)
	df_merged["life_expectancy"] = df_merged["life_expectancy"].astype(float)

	# --- Graphique ---
	plt.figure(figsize=(10, 6))
	plt.scatter(df_merged["gdp"], df_merged["life_expectancy"],
	            color="blue", alpha=0.7)

	plt.title("Relation entre le PIB et l'espérance de vie en 1900")
	plt.xlabel("PIB par habitant (USD, ajusté)")
	plt.ylabel("Espérance de vie (années)")
	plt.grid(True, linestyle="--", alpha=0.6)
	plt.tight_layout()
	plt.show()