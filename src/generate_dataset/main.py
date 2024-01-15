import os
import psycopg2
import pycountry
import random
from faker import Faker
from datetime import datetime
from psycopg2.extras import execute_values


class FakeDataGenerator:
    def __init__(self):
        self.faker = Faker()

    @staticmethod
    def get_state_for_country(country_code):
        try:
            country = pycountry.countries.get(alpha_2=country_code)
            subdivisions = list(pycountry.subdivisions.get(country_code=country.alpha_2))

            if subdivisions:
                return random.choice(subdivisions).name
            else:
                return None
        except AttributeError:
            return None

    def generate_data(self, records):
        data = []
        for _ in range(records):
            customer_first_name = self.faker.first_name()
            customer_last_name = self.faker.last_name()
            date_of_birth = self.faker.date_of_birth(minimum_age=18, maximum_age=65)
            address = self.faker.address()
            phone_number = self.faker.phone_number()
            email = self.faker.email()
            account_number = self.faker.uuid4()
            card_number = self.faker.credit_card_number()
            account_type = self.faker.random_element(["Savings", "Current", "Salary"])
            country = 'US'
            state = self.get_state_for_country(country)
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
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'mysecretpassword',
        'host': 'localhost',
        'port': 5432
    }

    data_generator = FakeDataGenerator()

    # Specify the number of records you want to generate
    num_records = 1

    # Call the generate_data method to generate fake data
    faker_data = data_generator.generate_data(num_records)

    # load data into postgres
    db_class = LoadDataPostgres(db_params)
    db_class.load_dataset(faker_data)
