from django.shortcuts import render, get_object_or_404, redirect
from .models import Capteur
from .forms import RechercheCapteurForm, CapteurForm


# Afficher la liste et rechercher des capteurs
def capteur_liste(request):

    # Récupérer tous les capteurs par ordre alphabétique
    capteurs = Capteur.objects.all().order_by("nom")

    # Vérifier si une recherche a été effectuée
    if request.GET:
        formulaire = RechercheCapteurForm(request.GET)

        if formulaire.is_valid():

            # Récupérer les données validées
            nom = formulaire.cleaned_data["q"]
            actifs = formulaire.cleaned_data["actifs_seulement"]

            # Rechercher un capteur par son nom
            if nom:
                capteurs = capteurs.filter(nom__icontains=nom)

            # Afficher uniquement les capteurs actifs
            if actifs:
                capteurs = capteurs.filter(actif=True)

        else:
            # Aucune donnée affichée si le formulaire est invalide
            capteurs = Capteur.objects.none()

    else:
        formulaire = RechercheCapteurForm()

    return render(request, "capteurs/capteur_liste.html", {
        "capteurs": capteurs,
        "formulaire": formulaire
    })


# Afficher les informations d'un capteur
def capteur_detail(request, pk):

    capteur = get_object_or_404(Capteur, pk=pk)

    return render(request, "capteurs/capteur_detail.html", {
        "capteur": capteur
    })

# Ajouter un nouveau capteur
def capteur_ajouter(request):

    if request.method == "POST":
        formulaire = CapteurForm(request.POST)

        if formulaire.is_valid():
            capteur = formulaire.save()

            return redirect(
                "capteurs:detail",
                pk=capteur.pk
            )

    else:
        formulaire = CapteurForm()

    return render(request, "capteurs/capteur_form.html", {
        "formulaire": formulaire,
        "titre": "Ajouter un capteur"
    })

# Modifier un capteur existant
def capteur_modifier(request, pk):

    # Récupérer le capteur ou afficher une erreur 404
    capteur = get_object_or_404(Capteur, pk=pk)

    if request.method == "POST":

        # Remplir le formulaire avec les nouvelles données
        formulaire = CapteurForm(request.POST, instance=capteur)

        if formulaire.is_valid():

            # Enregistrer les modifications
            formulaire.save()

            # Retourner vers la fiche du capteur
            return redirect("capteurs:detail", pk=capteur.pk)

    else:

        # Afficher les informations actuelles du capteur
        formulaire = CapteurForm(instance=capteur)

    return render(request, "capteurs/capteur_form.html", {
        "formulaire": formulaire,
        "titre": "Modifier le capteur"
    })

# Supprimer un capteur
def capteur_supprimer(request, pk):

    # Récupérer le capteur ou afficher une erreur 404
    capteur = get_object_or_404(Capteur, pk=pk)

    # Supprimer uniquement après confirmation
    if request.method == "POST":

        capteur.delete()

        # Retourner vers la liste des capteurs
        return redirect("capteurs:liste")

    # Afficher la page de confirmation
    return render(request, "capteurs/capteur_confsuppression.html", {
        "capteur": capteur
    })

from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Capteur
from .serializers import CapteurSerializer


class CapteurViewSet(ReadOnlyModelViewSet):

    serializer_class = CapteurSerializer

    def get_queryset(self):

        queryset = Capteur.objects.all()

        # Filtrer selon l'état actif ou inactif
        actif = self.request.query_params.get('actif')

        if actif is not None:
            if actif.lower() == 'true':
                queryset = queryset.filter(actif=True)
            elif actif.lower() == 'false':
                queryset = queryset.filter(actif=False)

        # Filtrer selon le type de capteur
        type_capteur = self.request.query_params.get('type_capteur')

        if type_capteur:
            queryset = queryset.filter(type_capteur=type_capteur)

        # Rechercher un capteur par son nom
        q = self.request.query_params.get('q')

        if q:
            queryset = queryset.filter(nom__icontains=q)

        return queryset