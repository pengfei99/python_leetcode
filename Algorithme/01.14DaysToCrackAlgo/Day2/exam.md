```sql
select * from
customer
group by identity
order by

With sign_date
    as
    (select c.client_id as id,
    date(c.signature_date)-date(s2.score_date) as signature_date_diff
    )

select c.client_id as id,
       s1.score_value as score_value_funnel,
       coalesce(s2.score_value, -1)  as score_value_signature
from clients c
         left join scores s1 on c.client_id=s1.client_id and date(c.funnel_date)=s1.score_date
    left join scores s2 on c.client_id=s2.client_id and c.signature_date=s2.score_date
order by id
```