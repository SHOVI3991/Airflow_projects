from airflow.models import DAG

from datetime import datetime

default_args = {
    'start_date':datetime(2022, 4, 17),
}

with DAG('user_processing', schedule_interval='@daily',
        default_args=default_args,
        catchup=False) as dag:
    # Define tasks/operators



