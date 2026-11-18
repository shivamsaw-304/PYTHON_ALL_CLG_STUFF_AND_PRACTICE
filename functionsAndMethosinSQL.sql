
-- methods in 
-- date and time functiona
select now() ;-- prints current_date();
select now() as current_datetime;
show databases;
show tables;

use companyDB;

show tables;

create table users(userName varchar(28) , joinDate date );

alter table users ADD column userID int primary key ;

insert into users (userID ,userName, joinDate)  values (1,"shivamSAw" , "2003-03-31");



/* filtering of table 
where ,select distinct,and,or,not,in,not in , betweeen, like ,limit, is null*/


create database organization;

use organization;

  ALTER TABLE employee
MODIFY role VARCHAR(50);
  
  

desc employee;

INSERT INTO employee(empIsd, FirstName, lastName, Grnder, role, dept, manager_id)
VALUES
(101, 'Shivam', 'Patil', 'M', 'Executive', 'Retail', 'M01'),
(102, 'Priya', 'Sharma', 'F', 'Analyst', 'Finance', 'M02'),
(103, 'Amit', 'Verma', 'M', 'Recruiter', 'HR', 'M03'),
(104, 'Sneha', 'Joshi', 'F', 'Executive', 'Retail', 'M04'),
(105, 'Rahul', 'Gupta', 'M', 'Accountant', 'Finance', 'M05'),
(106, 'Neha', 'Singh', 'F', 'HR Executive', 'HR', 'M06'),
(107, 'Karan', 'Mehta', 'M', 'Sales Lead', 'Retail', 'M07'),
(108, 'Pooja', 'Yadav', 'F', 'Financial Analyst', 'Finance', 'M08'),
(109, 'Arjun', 'Patel', 'M', 'HR Manager', 'HR', 'M09'),
(110, 'Riya', 'Kulkarni', 'F', 'Store Manager', 'Retail', 'M10');

select * from employee;

-- distinct key word use  it sort the data from table 
select distinct dept from employee order by dept;
select distinct role from employee order by role;

-- where keyword use and operator

select * from employee where role = "hr" and dept="hr";

select * from employee where role = "accountant" and dept ="finance";


-- or operator in sql 

select * from employee where role="HR" or role="accountant";

-- in operator in sql it takes arguments of colum values

select * from employee where role in("hr","Accountant", "executive"); -- order by lastName order by main aik value jo dete hain num woh use priority deke data show karta hain

--  not key word hume data show nahe karta 
select * from employee where role not in ("hr");

--  to modify column alter is use 
alter table employee add column Experiance int;
alter table employee rename column empIsd to empId;
-- updet is use to update data in the data bases (set )uses to set the value 




update employee set experiance=9 where empID = 102;
update employee set experiance=3 where empID = 103;
update employee set experiance=10 where empID = 101;
update employee set experiance=19 where empID = 104;

-- between it is use in and operator 

select * from employee where experiance between 1 and 10;
select * from employee where experiance =  1 or 3;

select * from employee where firstName like 'P%';

-- limit operation : it limts to show number of rows

select * from employee limit 3;

-- miujhe 5  data show karo lekin name ke besis pe
select * from employee order by firstName limit 10 ;

-- not null and null ye sab values show karna hain 

select * from employee where manager_id is not null;
select * from employee where experiance is null;


-- aggregate function (sum ,min ,max ,count , avg

-- counting all
select count(*) from employee;

-- selective count according to ccondition

desc employee;
alter table employee rename column grnder to gender;

select count(empID) from employee where role='accountant'; 
select count(empID) from employee where gender ='m';

select max(experiance) from employee;
select min(experiance) from employee;
select avg(experiance) from employee;

select * from employee;

-- group by clause -  devide a group of row into sub group depends on column or expression values (group by ) cluse is used with aggregate functions only like(sum,count,max,min,count)



