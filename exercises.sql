select memid, surname, firstname, joindate
from cd.members
where joindate > '2012-09-01'

select firstname, surname, joindate as latest from cd.members order by joindate desc limit 1

select distinct surname from cd.members order by surname asc limit 10

select name, 
	case monthlymaintenance > 100 
	when true then 'expensive'
	when false then'cheap'
	end as cost
	from cd.facilities;
  
select b.starttime 
from cd.members as m, cd.bookings as b
where m.memid = b.memid and m.firstname = 'David' and m.surname = 'Farrell'

select b.starttime as start, f.name
from cd.bookings b, cd.facilities f
where b.facid = f.facid and date(b.starttime) = '2012-09-21%' and f.name like 'Tennis%' order by start asc

select distinct m.firstname, m.surname
from cd.members m, cd.members r where m.memid = r.recommendedby
order by m.surname, m.firstname

select r.firstname, r.surname, m.firstname, m.surname
from cd.members r left outer join cd.members m on m.memid = r.recommendedby
order by r.surname, r.firstname

select distinct m.firstname || ' ' || m.surname as member, f.name as facility
from cd.members m, cd.bookings b, cd.facilities f
where m.memid = b.memid and b.facid = f.facid and f.name like 'Tennis%'
order by member, facility

select distinct m.firstname || ' ' || m.surname as member,
( select r.firstname || ' ' || r.surname as recommenders
  from cd.members r
  where m.recommendedby = r.memid
)
from cd.members m
order by member

update cd.facilities
set membercost = 6, guestcost = 30
where facid in (0,1);

update cd.facilities facs
set membercost = (select membercost * 1.1 from cd.facilities where facid = 0), guestcost = (select guestcost * 1.1 from cd.facilities where facid = 0)
where facs.facid = 1; 

