/*add the eyes color Jon Snow in EyesColor with color=Brown*/
INSERT OR REPLACE INTO EyesColor (person_id,color)
       select id,'Brown' from PERSON where first_name='Jon' AND last_name='Snow';

/*add the eyes color Arya Stark in EyesColor with color=Green*/
INSERT OR REPLACE INTO EyesColor (person_id,color)
       select id,'Green' from PERSON WHERE first_name='Arya' AND last_name='Stark';

/*creating a new table TVShow*/
CREATE TABLE  IF NOT EXISTS TVShow(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name char(128)
);

/*create a new table TVShowPerson*/
CREATE TABLE  IF NOT EXISTS TVShowPerson (
    tvshow_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    FOREIGN KEY(tvshow_id) REFERENCES TVShow(id),
    FOREIGN KEY(person_id) REFERENCES Person(id)
);

/*add in TVShow: Homeland The big bang theory Game of Thrones Breaking bad*/
INSERT OR REPLACE INTO TVShow (name) values ('Homeland');
INSERT OR REPLACE INTO TVShow (name) values ('The big bang theory');
INSERT OR REPLACE INTO TVShow (name) values ('Game of Thrones');
INSERT OR REPLACE INTO TVShow (name) values ('Breaking bad');

/*add all TVShow link to Person in TVShowPerson:
Walter Junior White => Breaking bad
Jaime Lannister => Game of Thrones
Sheldon Cooper => The big bang theory
Tyrion Lannister => Game of Thrones
Jon Snow => Game of Thrones
Arya Stark => Game of Thrones*/
INSERT  OR REPLACE INTO TVShowPerson (tvshow_id,person_id) values ((select id from TVshow where name='Breaking bad'),(select id from Person where first_name = 'Walter Junior' and last_name='White') );

INSERT  OR REPLACE INTO TVShowPerson (tvshow_id,person_id) values ((select id from TVshow where name='Game of Thrones'),(select id from Person where first_name = 'Jaime' and last_name='Lannister') );

INSERT  OR REPLACE INTO TVShowPerson (tvshow_id,person_id) values ((select id from TVshow where name='The big bang theory'), (select id from Person where first_name = 'Sheldon' and last_name='Cooper'));

INSERT  OR REPLACE INTO TVShowPerson (tvshow_id,person_id) values ((select id from TVshow where name='Game of Thrones'), (select id from Person where first_name = 'Tyrion' and last_name='Lannister'));

INSERT  OR REPLACE INTO TVShowPerson (tvshow_id,person_id) values ((select id from TVshow where name='Game of Thrones'),(select id from Person where first_name = 'Jon' and last_name='Snow'));

INSERT  OR REPLACE INTO TVShowPerson (tvshow_id,person_id) values ((select id from TVshow where name='Game of Thrones'),(select id from Person where first_name = 'Arya' and last_name='Stark'));


/*display all records with all attributes of all tables (Person, EyesColor, TVShow and TVShowPerson)*/
SELECT * FROM Person;
SELECT * FROM EyesColor;
Select * from TVShow;
SELECT * FROM TVShowPerson;




