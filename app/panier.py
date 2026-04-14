def calculer_prix_panier(articles):
    """
    Calcule le prix total d'un panier d'articles.
    articles : liste de dict avec 'nom', 'prix', 'quantite'
    Retourne le total arrondi à 2 décimales.
    """
    if not isinstance(articles, list):
        raise TypeError("Les articles doivent être une liste.")

    total = 0
    for article in articles:
        if article["prix"] < 0:
            raise ValueError("Le prix ne peut pas être négatif.")
        if article["quantite"] < 0:
            raise ValueError("La quantité ne peut pas être négative.")

        total += article["prix"] * article["quantite"]

    return round(total, 2)


def verifier_age(age):
    """
    Vérifie si un utilisateur est majeur.
    Retourne True si l'âge est >= 18, False sinon.
    """
    if not isinstance(age, int):
        raise TypeError("L'âge doit être un entier.")
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif.")

    return age >= 18
