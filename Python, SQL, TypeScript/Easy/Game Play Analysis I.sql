select player_id, MIN(event_date) as first_login
from activity
group by 1;