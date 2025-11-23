import csv, random
from faker import Faker

# Initialiser Faker en français
fake = Faker("fr_FR")

disciplines = ["Athlétisme - Sprint", "Athlétisme - Marathon", "Football", "Natation"]

with open("sportifs_data_enrichi.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Nom", "Prénom", "Âge", "Sexe", "Discipline", "VMA", "VO2max", "FC_REPOS", "FC_MAX",
                     "PUISSANCE_MAX", "AGILITE", "FORCE_MUSCULAIRE", "ENDURANCE", "VITESSE_100M", "RECUPERATION_1MIN",
                     "NIVEAU_STRESS"])

    for i in range(1, 301):
        discipline = random.choice(disciplines)

        # Génération semi-cohérente selon discipline
        if discipline == "Athlétisme - Sprint":
            vma = round(random.uniform(22, 24), 1);
            vo2 = random.randint(52, 60)
            endurance = round(random.uniform(10.5, 11.5), 1);
            vitesse = round(random.uniform(10.2, 10.8), 1)
        elif discipline == "Athlétisme - Marathon":
            vma = round(random.uniform(17, 19), 1);
            vo2 = random.randint(70, 78)
            endurance = round(random.uniform(14.5, 15.5), 1);
            vitesse = round(random.uniform(13, 14), 1)
        elif discipline == "Football":
            vma = round(random.uniform(19, 21), 1);
            vo2 = random.randint(60, 65)
            endurance = round(random.uniform(12, 13), 1);
            vitesse = round(random.uniform(11.5, 12), 1)
        else:  # Natation
            vma = round(random.uniform(19, 21), 1);
            vo2 = random.randint(68, 74)
            endurance = round(random.uniform(13, 14), 1);
            vitesse = round(random.uniform(12.5, 13), 1)

        # Génération aléatoire de nom et prénom
        prenom = fake.first_name()
        nom = fake.last_name()
        sexe = "M" if prenom[-1] not in ["a", "e"] else "F"  # petit hack pour varier

        writer.writerow([i, nom, prenom, random.randint(18, 30), sexe, discipline,
                         vma, vo2, random.randint(42, 55), random.randint(187, 202),
                         random.randint(480, 750), random.randint(75, 90), random.randint(90, 125),
                         endurance, vitesse, random.randint(28, 37), random.randint(2, 5)])