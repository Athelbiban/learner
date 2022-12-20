CREATE TABLE regions (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    active BOOLEAN NOT NULL DEFAULT TRUE 
)   ENGINE InnoDB;

CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    regions_id INTEGER NOT NULL,
    active BOOLEAN NOT NULL DEFAULT TRUE, 
    FOREIGN KEY (regions_id) REFERENCES regions(id)
)   ENGINE InnoDB;

