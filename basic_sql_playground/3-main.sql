/*update the age of Jon Snow to 27*/ 
UPDATE person 
SET    age = 27 
WHERE  first_name = 'Jon' 
       AND last_name = 'Snow'; 

/*update the age of Walter Junior White to 18*/ 
UPDATE person 
SET    age = 18 
WHERE  first_name = 'Walter Junior' 
       AND last_name = 'White'; 

/*delete the person Walter White from Person and EyesColor*/ 
DELETE FROM eyescolor 
WHERE  person_id = (SELECT id 
                    FROM   person 
                    WHERE  first_name = 'Walter' 
                           AND last_name = 'White'); 

DELETE FROM person 
WHERE  first_name = 'Walter' 
       AND last_name = 'White'; 

/*display all Person with all attributes ordered by first_name (A->Z)*/ 
SELECT * 
FROM   person 
ORDER  BY first_name ASC; 
