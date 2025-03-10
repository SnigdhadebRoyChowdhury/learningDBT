/* Creating the database */
CREATE DATABASE dbt;


/* Creating the schema */
CREATE SCHEMA airbnb;

CREATE TABLE IF NOT EXISTS airbnb.raw_listings
                    (id bigint,
                     listing_url text,
                     name text,
                     room_type text,
                     minimum_nights text,
                     host_id bigint,
                     price float,
                     created_at timestamp without time zone,
                     updated_at timestamp without time zone);

CREATE TABLE IF NOT EXISTS raw_hosts
                    (id bigint,
                    name text,
                    is_superhost text,
                    created_at timestamp without time zone,
                    updated_at timestamp without time zone);


CREATE TABLE IF NOT EXISTS raw_reviews
                    (listing_id bigint,
                        date date,
                        reviewer_name text,
                        comments_string text,
                        sentiment text);