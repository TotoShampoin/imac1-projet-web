CREATE TABLE IF NOT EXISTS Commande (
    comid       INT             NOT NULL    AUTO_INCREMENT,
    etat        ENUM (
        "commande",
        "preparation",
        "livraison",
        "fini"
    )                           NOT NULL,
    adresse     VARCHAR(4096)   NOT NULL,
    contact     VARCHAR(15)     NOT NULL,

    PRIMARY KEY (comid)
);

CREATE TABLE IF NOT EXISTS Aliment (
    aliid       INT             NOT NULL    AUTO_INCREMENT,
    libelle     VARCHAR(240)    NOT NULL,
    prix        DECIMAL(6,2)    NOT NULL, -- [-9999.99 , 9999.99]
    category    ENUM (
        "burger",
        "boisson",
        "accompagnement",
        "dessert"
    )                           NOT NULL,

    PRIMARY KEY (aliid)
);

CREATE TABLE IF NOT EXISTS Ingredient (
    ingid       INT             NOT NULL    AUTO_INCREMENT,
    libelle     VARCHAR(240)    NOT NULL,
    stock       INT,

    PRIMARY KEY (ingid)
);

CREATE TABLE IF NOT EXISTS CommandeAliment (
    comid       INT             NOT NULL,
    aliid       INT             NOT NULL,

    PRIMARY KEY (comid, aliid),
    FOREIGN KEY (comid)     REFERENCES Commande(comid),
    FOREIGN KEY (aliid)     REFERENCES Aliment(aliid)
);

CREATE TABLE IF NOT EXISTS AlimentIngredient (
    aliid       INT             NOT NULL,
    ingid       INT             NOT NULL,

    PRIMARY KEY (aliid, ingid),
    FOREIGN KEY (aliid)     REFERENCES Aliment(aliid),
    FOREIGN KEY (ingid)     REFERENCES Ingredient(ingid)
);
