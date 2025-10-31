from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """
    Affiche la corrélation entre le PIB par
    habitant et l'espérance de vie en 1900.

    Cette fonction :
      - charge les fichiers CSV :
          'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
          et 'life_expectancy_years.csv'
      - extrait les données pour l’année 1900
      - fusionne les deux datasets sur la colonne 'country'
      - affiche un nuage de points représentant la relation
        entre le PIB par habitant et l’espérance de vie.

    Le graphique contient :
      - un titre clair
      - un axe des X en échelle logarithmique
      - une grille et des ticks personnalisés
    """
    df_pib = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_el = load("life_expectancy_years.csv")

    if df_pib is None or df_el is None:
        print("❌ Erreur : un ou plusieurs fichiers n'ont pas pu être chargés.")
        return

    df_pib_1900 = df_pib[["country", "1900"]].copy()
    df_el_1900 = df_el[["country", "1900"]].copy()

    df_pib_1900.columns = ["country", "gdp"]
    df_el_1900.columns = ["country", "life_expectancy"]

    df_merged = pd.merge(df_pib_1900, df_el_1900, on="country")
    df_merged = df_merged.dropna()

    df_merged["gdp"] = df_merged["gdp"].astype(float)
    df_merged["life_expectancy"] = df_merged["life_expectancy"].astype(float)

    plt.figure(figsize=(10, 6))
    # trace un nuage de points
    plt.scatter(df_merged["gdp"], df_merged["life_expectancy"],
                color="blue", alpha=0.7)

    plt.title("Relation entre le PIB et l'espérance de vie en 1900")
    plt.xlabel("PIB par habitant (USD, ajusté)")
    plt.ylabel("Espérance de vie (années)")
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
