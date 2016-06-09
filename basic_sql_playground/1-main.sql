/* list all first_name of Person*/ 
SELECT first_name 
FROM   person; 

/*list all first_name, age of Person*/ 
SELECT first_name, 
       age 
FROM   person; 

/* list distinct color of EyesColor */ 
SELECT DISTINCT color 
FROM   eyescolor; 

/*list of first_name, last_name, age of Person ordered by age (younger to older)*/ 
SELECT first_name, 
       last_name, 
       age 
FROM   person 
ORDER  BY age ASC; 
