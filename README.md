<h1> Learning dbt (Data Build Tool) </h1>

![alt text](images/dbt.png)

#### Introduction

This repository contains the code required for learning dbt (data build tool) and setting up your own dbt project for hands-on practice.

I have followed [this Udemy course](https://www.udemy.com/course/complete-dbt-data-build-tool-bootcamp-zero-to-hero-learn-dbt/?couponCode=NVDIN35) for my learning.

Please note that this course uses Snowflake as the data platform for the dbt transformations whereas I have used PostgreSQL for my learning.

But if you want to use Snowflake or data platform, please use [this link](https://docs.getdbt.com/docs/trusted-adapters) to check if they are supported or not.


#### Setting up the environment

**Prerequisites:**
- Have Docker installed in your system, since I have used Docker to host my PostgreSQL database
- Have the latest Python version installed in your system 
- Have Visual Studio Code installed (*you can also use PyCharm for this*)

**Setting up PostgreSQL on Docker:**
- Pull the latest PostgreSQL image using the command, `docker pull postgres`
- Create a volume for the docker container, `docker volume create postgres_data`
- Create the container using the command:
    `docker run --name my_postgres_container -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres`

Once you have created the container, you can start or stop the container using `docker start <container_name>` or `docker stop <conatiner_name>`.

Once the container is up and running, you can connect to the database using the below details:
- Hostname: `localhost`
- Port: `5432`
- Database: `postgres`
- Username: `postgres`
- Password: `the password the you set during the container creation`



