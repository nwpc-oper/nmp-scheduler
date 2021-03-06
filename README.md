# nmp-scheduler

The scheduler component for NWPC Monitor Platform.

**nmp-scheduler** uses celery to collect status for workflow systems, workload systems and HPC disk usage .

**WARN**: Only workflow collectors are maintained currently.

## Install

Install the following python packages from github:

- [nwpc-workflow-model](https://github.com/nwpc-oper/nwpc-workflow-model)

Install **nmp-scheduler** using pip.

Create all config files needed by collectors.
And set config directory's path to `NWPC_MONITOR_TASK_SCHEDULER_CONFIG` environment variable before running any workers.

## Getting Started

Run celery workers. Each worker should have an unique name and listen on some queues.

```bash
python3 nmp_scheduler/run.py worker --name=celery --queues=celery
python3 nmp_scheduler/run.py worker --name=ecflow --queues=nmp_ecflow
```

Run celery beat to enable schedulers.

```bash
python3 nmp_scheduler/run.py beat
```

## Docker

Build docker images using:

```bash
docker build -t nwpc-oper/nmp-scheduler --rm .
```

## Collectors

### Workflow systems

#### ecFlow

- [ecflow-client-cpp](https://github.com/nwpc-oper/ecflow-client-cpp)
- <del>[nwpc-ecflow-collector](https://github.com/nwpc-oper/nwpc-ecflow-collector)</dev>

#### SMS

- [nwpc-sms-collector](https://github.com/nwpc-oper/nwpc-sms-collector)

## License

Copyright 2019-2020, perillaroc at nwpc-oper.

`nmp-scheduler` is licensed under [GPL-3.0](./LICENSE.md).