alter table public."Deposits" add column User_ID bigint
alter table public."Deposits" add column First_name character varying
alter table public."Deposits" add column Last_name character varying
alter table public."Deposits" add column Date_of_Birth date
alter table public."Deposits" add column City text
alter table public."Deposits" add column Srteet_Name text
alter table public."Deposits" add column Deposit_Amount integer
alter table public."Deposits" add column Interest integer
alter table public."Deposits" add column Comision integer
alter table public."Deposits" add column Total integer

--INSERT INTO Deposits (DepositID, DepOwnerName, DateOfBirth, City, StreetName, DepositAmount, Interest, Comission, Total)

insert into public.'Deposits' values(1, 'John Doe', '1990-05-15',	'New York',	'Elm Street', '5000', '0.03', '50','4950')
insert into public.'Deposits' values(2, 'Jane Smith', '1985-09-20', 'Los Angeles', 'Sunset Blvd', '3000', '0.02', '30', '2970')
insert into public.'Deposits' values(3, 'Robert Johnson', '1978-03-10', 'Chicago', 'Main St', '8000', '0.04', '80', '7920')	
insert into public.'Deposits' values(4, 'Mary Johnson', '1982-11-05', 'Houston', 'Main St', '7000', '0.035', '70', '6930')
insert into public.'Deposits' values(5, 'Michael Brown', '1995-07-18', 'Miami', 'Ocean Ave', '4000', '0.025', '40', '3960')
insert into public.'Deposits' values(6, 'Emily Lee', '1998-02-28', 'San Francisco', 'Market St', '6000', '0.03', '60', '5940')

select * from Deposits 


--string-ის ნაცვლად text-ი იმიტო გამოვიყენე რომ stringi არმიჩვენა და ისევ სიტყვის ფორმატი რომ დარჩენოდა თან სხვა არვიცოდი