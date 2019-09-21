from setuptools import setup, find_packages

setup(
    name="spike_airflow_plugins",
    version="0.1.0",
    packages=find_packages(exclude="tests"),
    test_suite="tests",
    entry_points={
        "airflow.plugins": [
            "my_namespace = spike_airflow_plugins.my_plugin:MyAirflowPlugin"
        ],
    },
)
