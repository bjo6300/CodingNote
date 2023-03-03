select hour(datetime) as "HOUR",
    count(hour(datetime)) as "COUNT"
from ANIMAL_OUTS
where hour(datetime) between 9 and 19
group by HOUR
order by HOUR