{{
    config(
        materialized = 'view'
    )
}}
WITH src_listings AS (
    SELECT * FROM {{ ref('src_listings')}}
)
SELECT
 listing_id,
 listing_name,
 room_type,
 CASE
    WHEN minimum_nights::INT = 0 THEN 1
    ELSE minimum_nights::INT
 END AS minimum_nights,
 host_id,
 COALESCE(price_str, 0)::DECIMAL(10,2) AS price,
 created_at,
 updated_at
FROM src_listings
