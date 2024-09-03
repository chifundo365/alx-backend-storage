-- Creates a table 'userrs' with id, email and name columns
CREATE TABLE  IF NOT EXISTS users(
	id INTEGER NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY(id)
)
