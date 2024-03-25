<!--
SPDX-FileCopyrightText: 2021-2024 Taavi Väänänen <hi@taavi.wtf>
SPDX-License-Identifier: AGPL-3.0-only
-->

# prometheus-manager

Centralized configuration management and storage for
[prometheus-configurator](https://gerrit.wikimedia.org/r/plugins/gitiles/cloud/metricsinfra/prometheus-configurator).

## how-to

### Setup local development environment

Export the path to the devel config (from the root of this repository):

```
$ export PROMETHEUS_MANAGER_CONFIG_PATH=$PWD/config.example.yaml
```

Start the mariadb instance using
[docker-compose](https://docs.docker.com/compose/):

```
$ docker compose up -d
```

Wait a few seconds, and then we need to create the non-admin user:

```
$ mariadb -h 127.0.0.1 --user=root --password=root -e "grant all privileges on prometheusconfig.* to 'prometheusconfig'@'%' identified by 'prometheusconfig';"
```

Now we can run the migrations to populate the database:

```
$ python3 scripts/pm-migrate
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 639f4dd7f8c4, create projects table
...
```

Run the service:

```
$ flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```

### Create new database migrations

```
$ python3 scripts/pm-interactive
--- prometheus-manager interactive shell ---
>>> from prometheus_manager.database import alembic
>>> alembic.revision("create projects table")
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'projects'
  Generating /home/taavi/src/prometheus-manager/prometheus_manager/migrations/639f4dd7f8c4_create_projects_table.py ...  done
[Script('639f4dd7f8c4', None, branch_labels={'default'})]
>>>
now exiting InteractiveConsole...

$ python3 scripts/pm-migrate
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 639f4dd7f8c4, create projects table

```
