select "user".*, post.id, post.name as title, post.user_id from "user"
join post
on post.user_id = "user".id;