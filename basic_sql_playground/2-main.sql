/*add a new person: Jon Snow, 26 years old*/
INSERT OR REPLACE INTO Person (first_name,last_name,age) Values('Jon', 'Snow', 26);

/*add a new person: Arya Stark, 12 years old*/
INSERT OR REPLACE INTO Person (first_name,last_name,age) Values('Arya', 'Stark', 12);

/*display all Person with all attributes ordered by last_name */
select * from Person order by last_name ASC;
