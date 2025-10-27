from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Affiche l'évolution de l'espérance de vie
    pour un pays donné (ici la France).

    Cette fonction charge le fichier CSV 'life_expectancy_years.csv'
    à l’aide de la fonction `load()`
    définie dans le module `load_csv.py`. Elle sélectionne ensuite
    les données correspondant au pays souhaité,
    extrait les années et les valeurs
    d'espérance de vie, puis trace un graphique
    représentant leur évolution au fil du temps.

    Le graphique contient :
      - un titre : "Évolution de l'espérance de vie en France"
      - l’axe des abscisses (X) représentant les années
      - l’axe des ordonnées (Y) représentant l’espérance de vie en années

    :returns:
        Aucun retour. La fonction affiche simplement le graphique à l’écran.

    :example:
        >>> main()
        (affiche la courbe d’évolution de l’espérance de vie en France)
    """
    df = load("life_expectancy_years.csv")
    france_data = df[df["country"] == "France"]
    print(france_data)
    years = france_data.columns[1:].tolist()
    values = france_data.values[0][1:].tolist()

    plt.plot(years, values)
    plt.title("Évolution de l'espérance de vie en France")
    plt.xlabel("Année")
    plt.ylabel("Espérance de vie (années)")
    plt.show()


if __name__ == "__main__":
    main()
