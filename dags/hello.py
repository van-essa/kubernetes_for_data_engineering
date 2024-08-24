from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'vanessandersson.io',
    'start_date': datetime(2024, 8, 24),
    'catchup': False
}

dag = DAG{
    dag_id: 'hello_world',
    default_args = default_args,
    schedule=timedelta(days=1)
}

t1 = BashOperator(
    task_id = 'hello_world',
    bash_command='echo "Hello World"',
    dag = dag
)


t2 = BashOperator(
    task_id = 'hello_va',
    bash_command='echo "Hello Vanessa Andersson"',
    dag = dag
)

t1 >> t2
