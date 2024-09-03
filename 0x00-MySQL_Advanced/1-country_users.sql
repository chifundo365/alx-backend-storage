-- Create a table with called 'users' with id, email, name country
-- Country is an enum of three countries
CREATE TABLE users(
	id INTEGER NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
	PRIMARY KEY(id)
)
