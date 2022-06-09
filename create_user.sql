create table "user"(
	id SERIAL primary key,
	name varchar(100),
	email VARCHAR(255),
	password text,
	age INT
);