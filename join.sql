show databases;
use companydb;
show tables;
drop table users;

create table employee(emp_id int primary key  , emp_name varchar(200) );

create table project(project_id int primary key ,pname varchar(20),employee_id int );

alter table project add constraint foreign key (employee_id) references employee(emp_id);

insert into employee (emp_id , emp_name) values (1,'shivam') , (2,'shaw'),(3,'ajay'),(4,'saurav'),(5,'supria');

insert into project (project_id , pname ,employee_id)  values (101,'project a',1),(102,'project b',2),(103,'project c',2);

select * from employee ;
select * from project;

-- join querys (for join )

select * from employee join project on employee.emp_id = project.employee_id;

-- inner join 

select eobj.emp_name ,pobj.pname from project pobj
inner join employee eobj
on eobj.emp_id = pobj.employee_id;

-- left join 

select eobj.emp_id, eobj.emp_name ,pobj.pname from employee eobj left join project pobj on eobj.emp_id  = pobj.employee_id;


select eobj.emp_id, eobj.emp_name ,pobj.pname from  project pobj left join employee eobj on eobj.emp_id  = pobj.employee_id;

-- right join 

select eobj.emp_name , pobj.pname from employee eobj right join project pobj on eobj.emp_id = pobj.employee_id ;

insert into project (project_id , pname) values (4, 'project d');

update project where project_id = 4 replace project_id  = 4 to project_id = 104;

select * from project;


-- full outer join using union  , display all matching and non matching data from both table 

select * from employee
left join project
on employee.emp_id = project.employee_id
union 
select * from employee
right join project 
on employee.emp_id = project.employee_id;


--  display employee name who has not been assign any project 

select employee.emp_name, project.pname from employee
left join project on employee.emp_id = project.employee_id where project.employee_id is null;

--  display employee name who has  been assign any project 
select employee.emp_name, project.pname from employee
left join project on employee.emp_id = project.employee_id where project.employee_id is not null;


