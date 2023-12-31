import os
import psycopg2
from faker import Faker
from datetime import datetime
from psycopg2.extras import execute_values


class FakeDataGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_data(self, num_records):
        data = []
        for _ in range(num_records):
            customer_first_name = self.faker.first_name()
            customer_last_name = self.faker.last_name()
            date_of_birth = self.faker.date_of_birth(minimum_age=18, maximum_age=65)
            address = self.faker.address()
            phone_number = self.faker.phone_number()
            email = self.faker.email()
            account_number = self.faker.uuid4()
            card_number = self.faker.credit_card_number()
            account_type = self.faker.random_element(["Savings", "Current", "Salary"])
            state = self.faker.state()
            country = 'USA'
            created_at = datetime.now()
            updated_at = datetime.now()

            data.append((
                customer_first_name, customer_last_name, date_of_birth, address, phone_number,
                email, account_number, card_number, account_type, state, country, created_at, updated_at
            ))

        return data

class LoadDataPostgres:

    def __init__(self, db_params):
        self.connection = psycopg2.connect(**db_params)

    def load_dataset(self, dataset):
        conn = self.connection
        cursor = conn.cursor()
        query = '''
            INSERT INTO customer (
                first_name, last_name, date_of_birth, address, phone_number, email, account_number,
                card_number, account_type, state, country, created_at, updated_at
            ) VALUES %s;
        '''
        execute_values(cursor, query, dataset)
        conn.commit()
        cursor.close()
        conn.close()


if __name__ == '__main__':
    db_params = {
        'dbname': os.environ.get('DB_NAME'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASSWORD'),
        'host': os.environ.get('DB_HOST'),
        'port': os.environ.get('DB_PORT')
    }

    data_generator = FakeDataGenerator()

    # Specify the number of records you want to generate
    num_records = 10

    # Call the generate_data method to generate fake data
    faker_data = data_generator.generate_data(num_records)

    # load data into postgres
    db_class = LoadDataPostgres(db_params)
    db_class.load_dataset(faker_data)

