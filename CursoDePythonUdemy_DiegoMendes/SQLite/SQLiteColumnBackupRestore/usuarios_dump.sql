BEGIN TRANSACTION;
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('usuarios',3);
CREATE TABLE usuarios (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,endereco TEXT NOT NULL,cpf VARCHAR(11) NOT NULL,uf VARCHAR(2) NOT NULL, email TEXT);
INSERT INTO "usuarios" VALUES(2,'Allan Keiiti Nakakita','Rua José Ferreira Rocha 10','38119011848','SP',NULL);
INSERT INTO "usuarios" VALUES(3,'Felippe Tigre','Rua Mato','132131313','MG',NULL);
COMMIT;
