-- 코드를 입력하세요
SELECT FIRST_HALF.flavor
from FIRST_HALF
join ICECREAM_INFO
on FIRST_HALF.flavor = ICECREAM_INFO.flavor
where FIRST_HALF.total_order > 3000
and ICECREAM_INFO.ingredient_type = "fruit_based"
order by FIRST_HALF.total_order desc