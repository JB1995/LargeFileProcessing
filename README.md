# LargeFileProcessing

## Set up to run code
To set up locally

1. Clone the repository

2. Create your env.list file

3. Build and run the docker containers

4. Create the demo database

5. Import data

### Clone repository
    https://github.com/JB1995/LargeFileProcessing.git

### Create your env.list file
Create your own env.list file with the required params
    MYSQL_ROOT_PASSWORD={MySQL root password of your choice}
    DB_CONTAINER_NAME=db

### Build and run docker containers
    docker build --tag demo:latest .
    docker-compose run --name demo demo

### Create the `demo` db
Note that there are 2 containers in play here. When you run docker-compose using the command above, it will open up a CLI for the container that runs the python scripts.
For this step, however, you need to open a another CLI for our db container. You can either use the Docker dashboard to do this or via below command line:
    
    docker exec -it {use database container name} /bin/sh;
    
For database container name, use below command to get running containers
    
    docker ps -a

In this case, command looks like as below for db container CLI:

    docker exec -it largefileprocessing_db_1 /bin/sh;

Once you have it open, connect to mysql

    mysql -u root -p

And once connected, create the database:

    CREATE DATABASE IF NOT EXISTS demo;

### Import
You are now ready to import and export data.

Run the below command on container for python

    python main.py

This will populate data into following two tables and generate csv file on dataset folder
    
    demo.Products: 466693 rows. Contains raw data pulled from products.csv
    Schema:
        name varchar(500) 
        sku varchar(500) PK 
        description varchar(500)
    
    demo.ProductsNumber: 212751 rows. Contains aggregated data
    Schema:
        name varchar(500) PK 
        noofproducts int
        
Execution of this script also generates `aggregate.csv` file into dataset folder and contains the aggregated data same as the data that we have on demo.ProductsNumber

## Points achieved
1. Your code should follow concept of OOPS
2. Support for updating existing products in the table based on `sku` as the primary key. (Yes, we know about the
kind of data in the file. You need to find a workaround for it)
3. All product details are to be ingested into a single table
4. An aggregated table on above rows with `name` and `no. of products` as the columns

Hints
1. Ingest the same file at least 2 times before submitting the assignment, without truncating the products table.
(This is to validate how your code works in case of updates)

## Points NOT achieved
1. Support for regular non-blocking parallel ingestion of the given file into a table. Consider thinking about the
scale of what should happen if the file is to be processed in 2 mins.
