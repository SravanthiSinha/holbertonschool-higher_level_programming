SELECT name,SUM(age) sage from Person P inner join TVSHowPerson TSP on P.id=TSP.person_id inner join TVSHow TS on TS.id= TSP.tvshow_id group by TS.name order by sage;


SELECT name,first_name,last_name,min(age) sage from Person P inner join TVSHowPerson TSP on P.id=TSP.person_id inner join TVSHow TS on TS.id= TSP.tvshow_id group by TS.name order by sage;

