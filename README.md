To run tests from the command line

```bash
$ docker-compose run app python setup.py test
```

To print a coverage report from the command line

```bash
$ docker-compose run app bash -c "coverage run --source=spike_airflow_plugins setup.py test; coverage report; coverage erase"
```