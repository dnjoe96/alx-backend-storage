-- Create a function

DELIMITER //

CREATE FUNCTION SafeDiv ( a INT, b INT )
RETURNS INT

BEGIN

   RETURN a / b;

END; //

DELIMITER ;
