-- Create a table with unique field

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
	);
