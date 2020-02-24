import datetime
import logging 

from airflow import DAG
from airflow.operators.python_operator import PytonOperator

def hello_world():
    logging.info("hello world")

#
# TODO: add a monthly schedule_interval argument to following DAG
#

dag = DAG(
    "lesson01.demo2",
    start_date = datetime.datetime.now() - datetime.timedelta(days=30))

task = PythonOperator(
    task_id = "hello_world_task",
    python_callable = hello_world,
    dag=dag)