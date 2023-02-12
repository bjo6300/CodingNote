select 
MEMBER_ID, 
MEMBER_NAME, 
GENDER, 
DATE_FORMAT(DATE_OF_BIRTH, '%Y-03-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
where DATE_OF_BIRTH LIKE '%-03-%' and gender = 'W' and tlno!= ''
order by MEMBER_ID;