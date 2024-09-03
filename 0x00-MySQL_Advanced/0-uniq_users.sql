-- Creates a table 'userrs' with id, email and name columns
CREATE TABLE  IF NOT EXISTS users(
	id INTEGER NOT NULL AUTO INCREMENT,
	email STRING(255) NOT NULL, UNIQUE,
	name STRING(255)
)
