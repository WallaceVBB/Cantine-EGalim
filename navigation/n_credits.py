### Navigation de la fenêtre Crédits

from PySide6.QtWidgets import QLabel


CREDITS_TEXT = """
<div style="font-family:'Segoe UI';">

    <p>
        <b>Développement et maintenance</b><br>
        Wallace Victor Bastos Barbosa
    </p>

    <p>
        <b>Soutien au développement</b><br>
        Groupement des Épiceries Sociales de Bourgogne-Franche-Comté
        (GESBFC)<br>
        <span style="color:#666;">
            Soutien au développement d'EpiData dans le cadre professionnel.
        </span>
    </p>

</div>
"""


class CreditsNavigation:
    def __init__(self, load_gui):
        # Fonction permettant de charger un .ui (fournie par Application)
        self.load_gui = load_gui

        # La fenêtre est chargée une seule fois puis réutilisée
        self.fenetre = None

    def ouvrir_credits(self):
        if self.fenetre is None:
            self.fenetre = self.load_gui("Credits.ui")
            self._configurer_credits(self.fenetre)

        self.fenetre.show()
        self.fenetre.raise_()
        self.fenetre.activateWindow()

    def _configurer_credits(self, fenetre):
        label = fenetre.findChild(QLabel, "l_credits")

        if label is None:
            raise RuntimeError("Le label 'l_credits' est introuvable dans Credits.ui")

        label.setText(CREDITS_TEXT)
        label.setWordWrap(True)