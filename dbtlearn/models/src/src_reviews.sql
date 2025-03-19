WITH raw_reviews AS (
    SELECT
        *
    FROM
        airbnb.raw_reviews
)
SELECT
    listing_id,
    date AS review_date,
    reviewer_name,
    comments AS review_text
FROM
    raw_reviews