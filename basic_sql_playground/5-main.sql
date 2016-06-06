select distinct last_name from Person P inner join TVSHowPerson TSP on P.id=TSP.person_id inner join TVSHow TS on TS.id= TSP.tvshow_id where TS.name = 'Game of Thrones' order by P.last_name ;

SELECT count(id) from Person where age >30;

select P.id,first_name,last_name,age,color,name from Person P inner join EyesColor E on P.id=E.person_id inner join TVSHowPerson TSP on P.id=TSP.person_id inner join TVSHow TS on TS.id= TSP.tvshow_id;

SELECT SUM(age) from Person;

