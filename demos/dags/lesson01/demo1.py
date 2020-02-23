import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

#
# TODO : Define a function for PythonOpeartor to call
#

dag = DAG(
    'lesson.dem01',
    start_date = datetime.datetime.now())

