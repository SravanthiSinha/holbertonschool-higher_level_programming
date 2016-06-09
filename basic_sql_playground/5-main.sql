/*all distinct last_name of the TVShow = Game of Thrones ordered by last_name ascending*/ 
SELECT DISTINCT last_name 
FROM   person P 
       INNER JOIN tvshowperson TSP 
               ON P.id = TSP.person_id 
       INNER JOIN tvshow TS 
               ON TS.id = TSP.tvshow_id 
WHERE  TS.NAME = 'Game of Thrones' 
ORDER  BY P.last_name ASC; 

/*the number of Person where the age is greater than 30*/ 
SELECT Count(id) 
FROM   person 
WHERE  age > 30; 

SELECT P.id, 
       first_name, 
       last_name, 
       age, 
       color, 
       NAME 
FROM   person P 
       INNER JOIN eyescolor E 
               ON P.id = E.person_id 
       INNER JOIN tvshowperson TSP 
               ON P.id = TSP.person_id 
       INNER JOIN tvshow TS 
               ON TS.id = TSP.tvshow_id; 

/*sum of age of all Person*/ 
SELECT Sum(age) 
FROM   person; 
