--  creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INTEGER)
BEGIN
	DECLARE TotalWeightedScore FLOAT;
	DECLARE TotalWeight FLOAT;

	SET TotalWeightedScore = 0;
	SET TotalWeight = 0;


	SELECT SUM(c.score * p.weight)
	INTO TotalWeightedScore
	FROM corrections c
	INNER JOIN projects p
	ON c.project_id = p.id
	INNER JOIN users u
	ON c.user_id = u.id
	WHERE u.id = user_id;

	SELECT SUM(p.weight) INTO TotalWeight
	FROM projects p
	INNER JOIN corrections c
	ON p.id = c.project_id
	INNER JOIN users u
	ON c.user_id = u.id
	WHERE u.id = user_id;


	IF TotalWeight > 0 THEN
		UPDATE users
		SET average_score = TotalWeightedScore / TotalWeight
		WHERE id = user_id;
	END IF;
END $$
DELIMITER ;
