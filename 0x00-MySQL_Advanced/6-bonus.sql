-- Create stored procedure AddBonus to add new correction for a student
-- Project name is created if it does not exist

DELIMITER //

CREATE PROCEDURE AddBonus (
	IN users_id INT,
	IN project_name VARCHAR(255),
	IN users_average_score FLOAT
)

BEGIN
        IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0
        THEN
                INSERT INTO projects (name) VALUES (project_name);
        END IF;

	INSERT into corrections (user_id, project_id, score) 
	VALUES (users_id, (select id from projects where name = project_name), score);

END //

DELIMITER ;
