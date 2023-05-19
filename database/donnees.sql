INSERT INTO Aliment (libelle, prix, category) VALUES
('Burger viande rouge', 7.99, 'burger'),
('Burger viande blanche', 7.99, 'burger'),
('Burger poisson', 7.99, 'burger'),
('Burger végétarien', 7.99, 'burger'),
('Frites', 5.99, 'accompagnement'),
('Potatoes', 5.99, 'accompagnement'),
('Sprite', 3.99, 'boisson'),
('Orangina', 3.99, 'boisson'),
('Coca Cola', 3.99, 'boisson'),
('Cookie', 4.99, 'dessert'),
('Muffin', 4.99, 'dessert'),
('Donut', 4.99, 'dessert');

INSERT INTO Commande (etat, adresse) VALUES
('preparation', '71, rue Émile Rolland, Langlois'),
('preparation', '62, boulevard Roux, Martel');

INSERT INTO CommandeAliment (comid, aliid, quantite) VALUES
(1, 3, 2),
(1, 5, 1),
(1, 9, 1),
(1, 11, 1),
(2, 4, 1),
(2, 6, 1);
