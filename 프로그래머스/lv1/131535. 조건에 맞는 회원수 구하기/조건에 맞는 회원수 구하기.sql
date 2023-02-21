select count(USER_ID)
from USER_INFO
where YEAR(JOINED) = '2021' and age >= 20 and age <= 29