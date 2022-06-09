CREATE TABLE profile(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255),
    password TEXT,
    age INT
);

CREATE TABLE "user"(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255),
    password TEXT,
    age INT
);

DROP TABLE Profile;

INSERT INTO "user" (email, name, age, password)
VALUES ('Bob@fake.com', 'Bob', 89, 'fjklsajflkjewoifnlkd;j');

INSERT INTO "user" (email, name, age, password)
VALUES ('chicken@fake.com', 'tim', 6, 'fwelsajflkjdsaf');

SELECT * FROM "user";
SELECT id, name, email FROM "user";
SELECT * FROM "user" WHERE age > 20;

UPDATE "user" SET age = 30 WHERE name = 'tim';

SELECT * FROM "user" WHERE age = 30;

DELETE FROM "user" WHERE id = 3;

CREATE TABLE post(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    content TEXT,
    user_id INT,
    CONSTRAINT fk_us
        FOREIGN KEY(user_id)
            REFERENCES "user"(id)
);

INSERT INTO post (name, content, user_id)
VALUES ('Bananas', 'tengo hambre', 1);
INSERT INTO post (name, content, user_id)
VALUES ('Why I love Corgis', 'omg I love them so much', 1);

SELECT * FROM post;

SELECT * FROM "user" JOIN post ON post.user_id = "user".id;

SELECT "user".*, post.id, post.name AS title, post.content
FROM "user" JOIN post ON post.user_id = "user".id;
