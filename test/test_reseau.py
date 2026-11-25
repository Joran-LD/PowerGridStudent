
import unittest
import xmlrunner

from Reseau import Reseau
from Terrain import Terrain, Case

class TestReseau(unittest.TestCase):

    def test_definition_entree(self): # implémenttion nouvelle
        r = Reseau()

        r.ajouter_noeud(0, (0, 0))
        r.ajouter_noeud(1, (0, 1))

        r.definir_entree(0)
        self.assertEqual(r.noeud_entree, 0)

        r.definir_entree(5)
        self.assertEqual(r.noeud_entree, -1)
        # TODO
        #self.fail()

    def test_ajout_noeud(self): # implémentation
        r = Reseau()

        r.ajouter_noeud(0, (2, 3))
        self.assertEqual(r.noeuds[0], (2, 3))

        r.ajouter_noeud(-1, (1, 1)) # Refus d'un identifiant négatif
        self.assertNotIn(-1, r.noeuds)

        r.ajouter_noeud(0, (4, 5))  # Refus d'un identifiant déjà utilisé
        self.assertEqual(r.noeuds[0], (2, 3))
        # TODO
        #self.fail()

    def test_ajout_arc(self):
       r = Reseau()

       r.ajouter_noeud(0, (0, 0)) # Création de deux nœuds voisins
       r.ajouter_noeud(1, (0, 1))

       r.ajouter_arc(0, 1)  # Ajout d'un arc valide
       self.assertIn((0, 1), r.arcs)

       r.ajouter_arc(0, 1)  # Vérification de l'absence de doublon
       self.assertEqual(len(r.arcs), 1)

       r.ajouter_arc(0, 5) # Refus d'un arc vers un nœud inexistant
       self.assertEqual(len(r.arcs), 1)
        # TODO
        #self.fail()

    def test_validation_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        self.assertTrue(r.valider_reseau())

    def test_validation_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)

        self.assertFalse(r.valider_reseau())

    def test_distribution_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.VIDE, Case.CLIENT],
        ]

        self.assertTrue(r.valider_distribution(t))

    def test_distribution_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]

        self.assertFalse(r.valider_distribution(t))

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

