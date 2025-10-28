from load_csv import load
import matplotlib.pyplot as plt


def convert_population(pop):
    """Convertit les valeurs avec suffixes (K, M, B) en nombres réels."""
    if isinstance(pop, str):
        pop = pop.strip()
        if pop.endswith("M"):
            return float(pop[:-1]) * 1e6
        elif pop.endswith("K"):
            return float(pop[:-1]) * 1e3
        elif pop.endswith("B"):
            return float(pop[:-1]) * 1e9
    try:
        return float(pop)
    except ValueError:
        return 0.0  # valeur par défaut si la conversion échoue

def main():
    """
    Affiche la comparaison de population entre la France et le Belgium de 1800 à 2050.

    Cette fonction :
      - charge le fichier CSV 'population_total.csv' via load()
      - filtre les pays France et Belgium
      - convertit les valeurs textuelles (M, K, B) en valeurs numériques
      - affiche un graphique clair et mis en forme
    """

    df = load("population_total.csv")
    df_filtered = df[df["country"].isin(["France", "Belgium"])]
    df_years = df_filtered.loc[:, "1800":"2050"]

    # Années
    years = df_years.columns.astype(int).tolist()

    # Extraction des valeurs pour chaque pays
    france_values = df_filtered[df_filtered["country"] == "France"].loc[:, "1800":"2050"].values[0]
    belgium_values = df_filtered[df_filtered["country"] == "Belgium"].loc[:, "1800":"2050"].values[0]

    # Conversion des unités
    france_values = [convert_population(v) for v in france_values]
    belgium_values = [convert_population(v) for v in belgium_values]

    # --- Graphique ---
    plt.figure(figsize=(10, 6))
    plt.plot(years, france_values, label="France", color="green", linewidth=2)
    plt.plot(years, belgium_values, label="Belgium", color="blue", linestyle="--", linewidth=2)

    plt.title("Comparaison de la population entre la France et le Belgium")
    plt.xlabel("Année")
    plt.ylabel("Population")
    plt.yticks([20e6, 40e6, 60e6, 80e6], ["20M", "40M", "60M", "80M"])
    plt.xticks(range(1800, 2051, 40))
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
