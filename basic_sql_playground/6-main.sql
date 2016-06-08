/*all sums of age by TVShow ordered by the sum (ascending)*/ 
SELECT NAME, 
       Sum(age) sage 
FROM   person P 
       INNER JOIN tvshowperson TSP 
               ON P.id = TSP.person_id 
       INNER JOIN tvshow TS 
               ON TS.id = TSP.tvshow_id 
GROUP  BY TS.NAME 
ORDER  BY sage ASC; 

/*display the youngest Person of each TVShow ordered by the age (ascending)*/
SELECT NAME, 
       first_name, 
       last_name, 
       Min(age) sage 
FROM   person P 
       INNER JOIN tvshowperson TSP 
               ON P.id = TSP.person_id 
       INNER JOIN tvshow TS 
               ON TS.id = TSP.tvshow_id 
GROUP  BY TS.NAME 
ORDER  BY sage ASC; 
