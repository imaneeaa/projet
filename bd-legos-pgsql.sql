DROP SCHEMA IF EXISTS projet CASCADE;
CREATE SCHEMA IF NOT EXISTS projet;
SET search_path TO legos;

CREATE TABLE usine (
    idU SERIAL PRIMARY KEY,
    ville VARCHAR(50),
    pays VARCHAR(50)
);

CREATE TABLE brique (
    idB SERIAL PRIMARY KEY,
    longueur integer,
    largeur integer,
    hauteur float,
    couleur varchar(20), 
    nomB VARCHAR(50),
    forme VARCHAR(50),
    mots_cles TEXT,
    idU INTEGER,    
);

CREATE TABLE config (
    idC SERIAL PRIMARY KEY
); 

CREATE TABLE joueuse (
    idJ SERIAL PRIMARY KEY,
    prenomJ VARCHAR(50) NOT NULL,
    dateInscription DATE NOT NULL,
    avatar VARCHAR(255)
);

CREATE TABLE partie (
    idP SERIAL PRIMARY KEY,
    idJ INTEGER,
    idC INTEGER,
    dateDeb DATE NOT NULL,
    dateFin DATE
);

CREATE TABLE participer (
    idP INTEGER,
    idJ INTEGER,
    PRIMARY KEY(idJ, idP),
    dateDeb DATE,
    dateFin DATE
);

CREATE TABLE gagner (
    idJ INTEGER,
    idP INTEGER,
    PRIMARY KEY(idJ, idP),
    score INTEGER
);

CREATE TABLE tour (
    numeroT INTEGER,
    idP INTEGER,
    idB INTEGER,
    idJ INTEGER,
    PRIMARY KEY(numeroT, idP)
);

CREATE TABLE utiliser (
    numeroT INTEGER,
    idB INTEGER,
    idP INTEGER,
    PRIMARY KEY(numeroT, idP, idB)
);

CREATE TABLE jouer (
    briqueUtilisee VARCHAR(50),
    acte VARCHAR(50),
    numeroT INTEGER,
    idJ INTEGER,
    idP INTEGER,
    PRIMARY KEY(numeroT, idP, idJ)
);

CREATE TABLE constituer (
    idP INTEGER,
    numeroT INTEGER,
    PRIMARY KEY(idP, numeroT)
);

CREATE TABLE representer (
    idC INTEGER,
    idPARA INTEGER,
    PRIMARY KEY(idC, idPARA)
);

CREATE TABLE posseder (
    idP INTEGER,
    idC INTEGER,
    PRIMARY KEY(idP,idC)
);

CREATE TABLE parametre (
    idPARA SERIAL PRIMARY KEY,
    propriete VARCHAR(50) NOT NULL,
    valeur FLOAT NOT NULL
);

CREATE TABLE cs (
    idCS SERIAL PRIMARY KEY,
    nomCS VARCHAR(50) NOT NULL,
    commentaire TEXT
);

CREATE TABLE remplacee_selon (
    idCS INTEGER,
    idB INTEGER,
    PRIMARY KEY(idCS,idB)
);

CREATE TABLE substituer (
    idB1 INTEGER,
    idB2 INTEGER,
    PRIMARY KEY(idB1,idB2)
);

CREATE TABLE fabriquer (
    dateFab DATE,
    quantite FLOAT,
    idU INTEGER,
    idB INTEGER,
    PRIMARY KEY (idU, idB)
);

CREATE TABLE construction (
    idCONS SERIAL PRIMARY KEY,
    nomC VARCHAR(50),
    theme VARCHAR(50),
    description TEXT,
    anneeSortie INTEGER,
    longueurC INTEGER,
    largeurC INTEGER,
    hauteurC INTEGER
);

CREATE TABLE construction_amateur (
    nomA VARCHAR(50),
    typeLicence VARCHAR(50),
    PRIMARY KEY(idCONS)
) INHERITS (construction) ;
  
CREATE TABLE construction_officielle (
    ageRecommande INTEGER,
    codeRef INTEGER,
    PRIMARY KEY(idCONS)
) INHERITS (construction) ;

CREATE TABLE vendue_dans (
    codeRef INTEGER,
    idCONS INTEGER,
    PRIMARY KEY(codeRef, idCONS) 
);

CREATE TABLE contenir (
    idB INTEGER,
    idCONS INTEGER,
    PRIMARY KEY(idB, idCONS)
);

CREATE TABLE boite (
    codeRef SERIAL PRIMARY KEY,
    nomBOITE VARCHAR(50),
    idCONS INTEGER,
    prix FLOAT
);

CREATE TABLE etape (
    numero INTEGER,
    image TEXT,
    instructions TEXT,
    idCONS INTEGER,
    PRIMARY KEY(numero, idCONS)
);

CREATE TABLE suivre (
    numero INTEGER,
    idCONS INTEGER,
    PRIMARY KEY(numero, idCONS)
);

CREATE TABLE illustrer (
    idCONS INTEGER,
    idP INTEGER,
    PRIMARY KEY(idCONS, idP)
);

CREATE TABLE photo (
    idP SERIAL PRIMARY KEY,
    description TEXT,
    chemin TEXT
);

CREATE TABLE accompagner (
    idB INTEGER,
    idP INTEGER,
    PRIMARY KEY(idB, idP)
);


ALTER TABLE brique ADD FOREIGN KEY (idU) REFERENCES usine (idU); 

ALTER TABLE partie ADD FOREIGN KEY (idC) REFERENCES config (idC);
ALTER TABLE partie ADD FOREIGN KEY (idJ) REFERENCES joueuse (idJ);

ALTER TABLE participer ADD FOREIGN KEY (idJ) REFERENCES joueuse (idJ);
ALTER TABLE participer ADD FOREIGN KEY (idP) REFERENCES partie (idP);

ALTER TABLE gagner ADD FOREIGN KEY (idJ) REFERENCES joueuse (idJ);
ALTER TABLE gagner ADD FOREIGN KEY (idP) REFERENCES partie (idP);

ALTER TABLE tour ADD FOREIGN KEY (idP) REFERENCES partie (idP);
ALTER TABLE tour ADD FOREIGN KEY (idB) REFERENCES brique (idB);
ALTER TABLE tour ADD FOREIGN KEY (idJ) REFERENCES joueuse (idJ);

ALTER TABLE utiliser ADD FOREIGN KEY (numeroT, idP) REFERENCES tour (numeroT, idP);
ALTER TABLE utiliser ADD FOREIGN KEY (idB) REFERENCES brique (idB);

ALTER TABLE jouer ADD FOREIGN KEY (idJ) REFERENCES joueuse (idJ);
ALTER TABLE jouer ADD FOREIGN KEY (numeroT, idP) REFERENCES tour (numeroT, idP);

ALTER TABLE constituer ADD FOREIGN KEY (idP) REFERENCES partie (idP);
ALTER TABLE constituer ADD FOREIGN KEY (numeroT, idP) REFERENCES tour (numeroT, idP);

ALTER TABLE representer ADD FOREIGN KEY (idC) REFERENCES config (idC);
ALTER TABLE representer ADD FOREIGN KEY (idPARA) REFERENCES parametre (idPARA);

ALTER TABLE posseder ADD FOREIGN KEY (idP) REFERENCES partie (idP);
ALTER TABLE posseder ADD FOREIGN KEY (idC) REFERENCES config (idC);

ALTER TABLE remplacee_selon ADD FOREIGN KEY (idCS) REFERENCES cs (idCS);
ALTER TABLE remplacee_selon ADD FOREIGN KEY (idB) REFERENCES brique (idB);

ALTER TABLE substituer ADD FOREIGN KEY (idB1) REFERENCES brique (idB);
ALTER TABLE substituer ADD FOREIGN KEY (idB2) REFERENCES brique (idB);

ALTER TABLE fabriquer ADD FOREIGN KEY (idU) REFERENCES usine (idU);
ALTER TABLE fabriquer ADD FOREIGN KEY (idB) REFERENCES brique (idB);

ALTER TABLE construction_officielle ADD FOREIGN KEY (coderef) REFERENCES boite (codeRef);

ALTER TABLE vendue_dans ADD FOREIGN KEY (codeRef) REFERENCES boite (codeRef);
ALTER TABLE vendue_dans ADD FOREIGN KEY (idCONS) REFERENCES construction_officielle (idCONS);

ALTER TABLE contenir ADD FOREIGN KEY (idB) REFERENCES brique (idB);
ALTER TABLE contenir ADD FOREIGN KEY (idCONS) REFERENCES construction (idCONS);

ALTER TABLE boite ADD FOREIGN KEY (idCONS) REFERENCES construction_officielle (idCONS);

ALTER TABLE etape ADD FOREIGN KEY (idCONS) REFERENCES construction (idCONS);

ALTER TABLE suivre ADD FOREIGN KEY (numero, idCONS) REFERENCES etape (numero, idCONS);
ALTER TABLE suivre ADD FOREIGN KEY (idCONS) REFERENCES construction (idCONS);

ALTER TABLE illustrer ADD FOREIGN KEY (idCONS) REFERENCES construction (idCONS);
ALTER TABLE illustrer ADD FOREIGN KEY (idP) REFERENCES photo (idP);

ALTER TABLE accompagner ADD FOREIGN KEY (idB) REFERENCES brique (idB);
ALTER TABLE accompagner ADD FOREIGN KEY (idP) REFERENCES photo (idP);





