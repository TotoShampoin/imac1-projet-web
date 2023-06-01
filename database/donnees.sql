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
('Poisson', 10),
('Steak de soja', 10),
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

INSERT INTO AlimentIngredient (aliid, ingid) VALUES
( 1,  1), ( 1,  2), ( 1,  6), ( 1,  7), ( 1,  8), ( 1,  9), ( 1, 10),
( 2,  1), ( 2,  3), ( 2,  6), ( 2,  7), ( 2,  8), ( 2,  9), ( 2, 10),
( 3,  1), ( 3,  4), ( 3,  6), ( 3,  7), ( 3,  8), ( 3,  9), ( 3, 10),
( 4,  1), ( 4,  5), ( 4,  6), ( 4,  7), ( 4,  8), ( 4,  9), ( 4, 10),
( 5, 13), ( 6, 14), ( 7, 15), ( 8, 16), ( 9, 17), (10, 18), (11, 19), (12, 20);
