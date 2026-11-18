-- nxt of check ------------
show databases;
use companydb;

show tables;

create table employee7 (empId int primary key  ,
firstName  varchar(30) ,
 lastName varchar(29) ,
 age int ,
 salary double );
 
 insert into  employee7 (empId , firstName , lastName , age,salary ) values  
 ( 1,"shivam" ,"saw" , 21 ,200000 ),
 (2,"ajay" ,"patil " ,21 , 20000),
 (3 ,"saurav" ,"kamte" , 21 ,20000);

 
 select * from employee7 ;
 
 -- to check constrain -- is  ---  show create table employee7
 show  create table  employee7;
 show create table employee7;
 -- to add consttrain with checks 
 alter table employee7 add constraint checkEmpSalaryAge check(salary >= 10 and salary >= 0 )  ;
 
 -- index in my sql it works as pointer for reading the data fromm the data base 
 create index  demoIndex on employee7(firstname);
 create index  demoIndex1 on employee7(fisrtName , lastName );
 
 show index from employee7 ;
 