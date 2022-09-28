use bill;

create table Cake_Shop (SrNo int auto_increment,
						Customer_Name varchar(50),
                        Total int(50),
                        primary key(SrNo));
                        
select * from Cake_Shop;

insert into Cake_Shop values (01,"Anjana",6000);

select * from Cake_Shop;
