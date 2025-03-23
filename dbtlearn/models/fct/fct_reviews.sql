{{
    config(
        materialized = 'incremental',
        on_schema_change = 'fail'
    )
}}
WITH src_reviews AS (
    SELECT * FROM {{ ref('src_reviews') }}
)
SELECT * FROM src_reviews 
WHERE review_text IS NOT NULL

/* The below macro checks if the model is running in incremental or not*/
{% if is_incremental() %}
/* 
    The below condition checks if the review_date of the source model (src_reviews) is greater than the 
    mximum review_date of this (fct_reviews) model
*/
    AND review_date > (select max(review_date) from {{ this }})
{% endif %}