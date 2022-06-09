create table post (
	id SERIAL primary key,
	name varchar(255),
	content text,
	user_id INT,
	constraint fk_user foreign KEY(user_id) references "user"(id)
);