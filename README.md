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
- Have Visual Studio Code installed 
- WSL if you using Windows

```
You can use PyCharm as your IDE but since I have worked completely on WSL and since VS Code allows development on WSL while being installled on Windows, it will be easier if you do the same.

But if you want to use PyCharm on Windows, then please check the environment variables. 

If you are using a Macbook, then you can follow the same steps both with VS Code and PyCharm.
```

**Setting up PostgreSQL on Docker:**
- Pull the latest PostgreSQL image using the command: `docker pull postgres`
- Create a volume for the docker container: `docker volume create postgres_data`
- Create the container using the command:
    `docker run --name my_postgres_container -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres`

Once you have created the container, you can start or stop the container using `docker start <container_name>` or `docker stop <container_name>`.

Once the container is up and running, you can connect to the database using the below details:
- Hostname: `localhost`
- Port: `5432`
- Database: `postgres`
- Username: `postgres`
- Password: `the password the you set during the container creation`

```
If you don't want to use Postgres on Docker that is possible too. 

Just install Postgres on your system and use it.
```


**Setting up the dbt environment:**
- Open up your IDE of choice and create a virtual environment in Python 
- Once that is done, run the command, `pip install dbt-postgres==1.9.0`(*if you are using any other data platform, please install the correspoding module*)
- Once this is done, run the command `dbt --help` to verify whether dbt core has been installed or not 
- Create a folder using the command `mkdir ~/.dbt`
- Run the command, `dbt init dbtlearn` to initialize a dbt project; here *dbtlearn* is the name of the project but you can use a different name
- When you learn the above command, you will be asked to enter a few details on how to connect to PostgreSQL. Please enter the details accordingly
- Once you have entered the details, you can see the details using the command, `cat .dbt/profiles.yml`
- If you want to update the details later, you can do so by editing the file `~/.dbt/profiles.yml`; you can use the `vi`, `vim` or `nano` to edit the file

