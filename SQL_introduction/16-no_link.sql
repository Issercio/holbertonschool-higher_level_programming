-- Supprimer "George" de la table
DELETE FROM second_table WHERE name = 'George';

-- Ajouter trois enregistrements pour "Aria"
INSERT INTO second_table (score, name)
VALUES (18, 'Aria');
INSERT INTO second_table (score, name)
VALUES (18, 'Aria');
INSERT INTO second_table (score, name)
VALUES (12, 'Aria');

-- Sélectionner les résultats, afficher le score et le nom, triés par score décroissant
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
