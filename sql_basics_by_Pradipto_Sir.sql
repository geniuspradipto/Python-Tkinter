show databases;
create database if not exists student;
-- select the databse
use student;


-- table creation
create table if not exists details(name varchar(20), roll int, city varchar(10), favsub varchar(10));
-- pradipto chatterjee 

CREATE TABLE data(name VARCHAR(20), roll int primary key auto_increment, marks float);


-- how many tables are present 
show tables;
SHOW TABLES;


-- info about the table
desc details;
DESC DATA;


-- insert values into table
insert into data values("Pradipto Chatterjee", 100, 99.9);
-- insert into data values("Krishna Kumar", 2, 99.5); 
-- insert into data values("Mohd. Faraz", 3, 99.7);
insert into data(name, marks) values("Mohd. Faraz", 99.7);
insert into data(name, marks) values("Aradhna", 99.9);

-- to fetch or display the values present in the table
select * from data;
SELECT * FROM data;
select * from marksdetails;

-- to delete or drop a table
drop table data;


-- change table name
ALTER TABLE data RENAME to marksdetails;

-- change col name of a table
ALTER TABLE marksdetails RENAME COLUMN roll to rollno;

