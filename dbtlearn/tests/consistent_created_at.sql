select * 
from {{ ref('fct_reviews') }} r
inner join {{ ref('dim_listings_cleansed') }} l
on r.listing_id  = l.listing_id
where l.created_at <= r.review_date