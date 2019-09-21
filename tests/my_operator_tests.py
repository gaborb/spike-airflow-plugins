import unittest
from unittest import mock
from datetime import datetime
from airflow import DAG, configuration
from airflow.models import TaskInstance
from airflow.operators.my_namespace import MyOperator


class MyOperatorTests(unittest.TestCase):

    def setUp(self):
        configuration.load_test_config()

    @mock.patch("airflow.contrib.operators.bigquery_operator.BigQueryHook")
    def test_execute_should_run_a_dummy_query(self, mock_hook):
        dag = DAG(dag_id="test-my-plugin", start_date=datetime.now())
        task = MyOperator(dag=dag, task_id="test-my-operator")
        task_instance = TaskInstance(task=task, execution_date=datetime.now())
        task.execute(task_instance.get_template_context())
        mock_method = mock_hook.return_value.get_conn().cursor().run_query

        self.assertTrue(mock_method.called)
        self.assertEqual(1, mock_method.call_count)
        self.assertEqual("SELECT 1", mock_method.call_args[1]["sql"])


if __name__ == "__main__":
    unittest.main()
