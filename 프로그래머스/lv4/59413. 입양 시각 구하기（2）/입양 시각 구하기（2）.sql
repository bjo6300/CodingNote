set @a = -1;

select (@a := @a + 1) as "hour",
    (select count(*)
    from ANIMAL_OUTS
    where hour(datetime) = @a) as "count"
from ANIMAL_OUTS
where @a < 23