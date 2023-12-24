query =  '''
        drop table if exists customer;
        CREATE TABLE customer (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            date_of_birth DATE,
            address VARCHAR(255),
            phone_number VARCHAR(255),
            email VARCHAR(255),
            account_number VARCHAR(255),
            card_number varchar(255),
            account_type VARCHAR(255),
            state varchar(255),
            country varchar(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        create database SparkStreaming;
        '''

