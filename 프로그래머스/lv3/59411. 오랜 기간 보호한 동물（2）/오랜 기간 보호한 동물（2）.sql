select animal_ins.animal_id, animal_ins.name
from animal_ins
join animal_outs
on animal_ins.animal_id = ANIMAL_OUTS.animal_id
order by (ANIMAL_OUTS.DATETIME - animal_ins.DATETIME) desc
limit 2