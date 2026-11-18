CREATE database companyDB;

USE COMPANYDB;


CREATE TABLE Employees (EmpId int primary key,
EmpName varchar(100) ,
salary  double  ,
JoinDate date
);

create table Departments (deptId  int primary key  ,
deptName varchar(100) );

show tables;
select * from employees;
select * from departments;
alter table  employees add column email varchar(100) ;
alter table departments add column dept_location varchar(100) ;
alter table employees add column phone int not null ;
alter table employees modify empName varchar(100) ;
alter table departments modify  deptId int  primary key;

ALTER TABLE Employees ADD COLUMN deptId INT;
alter table employees add constraint FKofEmployee_department foreign key(deptId) references departments (deptID);

alter table employees rename column empname to employeeName ;
alter table employees add column age int ;
alter table employees add constraint checkAgeSalary check (age > 18 and salary > 0 ) ; 
alter table employees drop phone ;
alter table employees rename to employeeDetails;
select * from employeeDetails ;


alter table employeedetails drop constraint checkAgeSalary ;

alter table employeedetails drop foreign key FKofEmployee_department ;
drop table departments;


drop database companydb;