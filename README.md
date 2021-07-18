# prometheus-manager

Centralized configuration management and storage for
[prometheus-configurator](https://gerrit.wikimedia.org/r/plugins/gitiles/cloud/metricsinfra/prometheus-configurator).

## how-to

### create database migrations

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
