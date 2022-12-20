PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE regions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    active BOOLEAN NOT NULL DEFAULT TRUE 
);
INSERT INTO regions VALUES(1,'Leningradskaya Oblast',1);
CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    regions_id INTEGER NOT NULL,
    active BOOLEAN NOT NULL DEFAULT TRUE, 
    FOREIGN KEY (regions_id) REFERENCES regions(id)
);
INSERT INTO cities VALUES(1,'Saint Petersburg',1,1);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('regions',1);
INSERT INTO sqlite_sequence VALUES('cities',1);
COMMIT;
