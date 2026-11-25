
from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    # TODO afficher le terrain à l'utilisateur après chaque action
    # afficher() et afficher_avec_terrain() dans Reseau.py donc import possible

    # TODO permettre à l'utilisateur de communiquer un chiffre pour faire un choix
    def entier_naturel(message: str):
        saisie = input(message).strip()
        if saisie == "":
            return None
        try:
            return int(saisie)
        except ValueError:
            print("Erreur : veuillez entrer un entier valide.")
            return None

    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        # TODO définir les différents choix possible
        # definir_entree()
        # ajouter_noeud() -> enlever_noeud() ? 
        # ajouter_arc() -> enlever_arc() ?

        # valider_reseau() à chaque étape ? 
        # valider_distribution() à la fin 
        # Que faire si échec de validation ? 
        # Tout recommencer ? 
        # Réponse : PowerGrid.py fait une vérif après StrategieReseauManuelle() et envoie un message d'erreur
        # Donc pas besoin de vérifier noeud et distribution ici
        return -1, {}, []

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        # TODO
        return -1, {}, []

