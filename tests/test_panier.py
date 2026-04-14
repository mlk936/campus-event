import pytest
from app.panier import calculer_prix_panier, verifier_age


# === Tests pour calculer_prix_panier ===

def test_panier_simple():
    """Un panier basique doit retourner le bon total."""
    articles = [
        {"nom": "Stylo", "prix": 1.50, "quantite": 3},
        {"nom": "Cahier", "prix": 2.00, "quantite": 2},
    ]
    assert calculer_prix_panier(articles) == 8.50


def test_panier_vide():
    """Un panier vide doit retourner 0."""
    assert calculer_prix_panier([]) == 0


def test_panier_prix_negatif():
    """Un prix négatif doit lever une erreur."""
    articles = [{"nom": "Erreur", "prix": -5.00, "quantite": 1}]
    with pytest.raises(ValueError):
        calculer_prix_panier(articles)


def test_panier_type_invalide():
    """Un argument non-liste doit lever une erreur."""
    with pytest.raises(TypeError):
        calculer_prix_panier("pas une liste")


# === Tests pour verifier_age ===

def test_utilisateur_majeur():
    """Un utilisateur de 18 ans est majeur."""
    assert verifier_age(18) is True


def test_utilisateur_mineur():
    """Un utilisateur de 17 ans est mineur."""
    assert verifier_age(17) is False


def test_age_negatif():
    """Un âge négatif doit lever une erreur."""
    with pytest.raises(ValueError):
        verifier_age(-1)


def test_age_type_invalide():
    """Un âge non-entier doit lever une erreur."""
    with pytest.raises(TypeError):
        verifier_age("dix-huit")
