-- creates a stored procedure AddBonus that adds a new correction for a student
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INTEGER, IN project_name VARCHAR(255), IN score INTEGER)
BEGIN
	DECLARE project_exists BOOLEAN;

	SET project_exists = EXISTS(
		SELECT name from projects
		WHERE name = project_name
	);

	IF NOT project_exists THEN
		INSERT INTO projects(name) VALUES(project_name);
	
	END IF;
	
	INSERT INTO corrections() VALUES(
		user_id,
		(SELECT id FROM projects WHERE name = project_name),
		score
	);

END $$
DELIMITER ;





