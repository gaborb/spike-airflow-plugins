from airflow.plugins_manager import AirflowPlugin

from airflow.contrib.hooks.bigquery_hook import BigQueryHook
from airflow.utils.decorators import apply_defaults
# from airflow.models import BaseOperator
from airflow.sensors.base_sensor_operator import BaseSensorOperator
from googleapiclient.errors import HttpError


# pylint: disable=abstract-method
class MyHook(BigQueryHook):
    def is_job_done(self, project_id, job_id):
        service = self.get_service()
        try:
            response = service.jobs().get(projectId=project_id, jobId=job_id).execute()
            state = response["status"]["state"]
            self.log.info("Status state of job is: %s", state)
            return state == "DONE"
        except HttpError as error:
            if error.resp["status"] == "404":
                return False
            raise


# class MyOperator(BaseOperator):
#     pass


class MySensorOperator(BaseSensorOperator):
    template_fields = ("project_id", "job_id")
    ui_color = "#f0eee4"

    @apply_defaults
    def __init__(self,
                 job_id,
                 project_id=None,
                 bigquery_conn_id="bigquery_default",
                 delegate_to=None,
                 **kwargs):
        super(MySensorOperator, self).__init__(**kwargs)
        self.project_id = project_id
        self.job_id = job_id
        self.bigquery_conn_id = bigquery_conn_id
        self.delegate_to = delegate_to

    def poke(self, context):
        self.log.info("Sensor checks status state of job: %s", self.job_id)
        hook = MyHook(bigquery_conn_id=self.bigquery_conn_id, delegate_to=self.delegate_to)
        return hook.is_job_done(self.project_id, self.job_id)


class MyAirflowPlugin(AirflowPlugin):
    name = "my_namespace"
    hooks = [MyHook]
    # operators = [MyOperator]
    sensors = [MySensorOperator]
