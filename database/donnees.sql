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

INSERT INTO Ingredient (libelle, stock) VALUES
('Pain', 10),
('Viande rouge', 10),
('Viande blanche', 10),
('Poulet', 10),
('Poisson', 10),
('Salade', 10),
('Tomate', 10),
('Oignon', 10),
('Fromage', 10),
('Sauce burger', 10),
('Ketchup', 10),
('Moutarde', 10),
('Frites', 10),
('Potatoes', 10),
('Sprite', 10),
('Orangina', 10),
('Coca Cola', 10),
('Cookie', 10),
('Muffin', 10),
('Donut', 10);
