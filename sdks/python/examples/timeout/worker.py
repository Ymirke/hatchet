import time
from datetime import timedelta

from pydantic import BaseModel

from hatchet_sdk import Context, EmptyModel, Hatchet, TaskDefaults

hatchet = Hatchet(debug=True)


class TaskOutput(BaseModel):
    status: str


# ❓ ScheduleTimeout
timeout_wf = hatchet.workflow(
    name="TimeoutWorkflow",
    task_defaults=TaskDefaults(execution_timeout=timedelta(minutes=2)),
)
# ‼️


# ❓ ExecutionTimeout
# 👀 Specify an execution timeout on a task
@timeout_wf.task(
    execution_timeout=timedelta(seconds=4), schedule_timeout=timedelta(minutes=10)
)
def timeout_task(input: EmptyModel, ctx: Context) -> TaskOutput:
    time.sleep(5)
    return TaskOutput(status="success")


# ‼️


class OutputModel(BaseModel):
    refresh_task: TaskOutput


refresh_timeout_wf = hatchet.workflow(
    name="RefreshTimeoutWorkflow", output_validator=OutputModel
)


# ❓ RefreshTimeout
@refresh_timeout_wf.task(execution_timeout=timedelta(seconds=4))
def refresh_task(input: EmptyModel, ctx: Context) -> TaskOutput:

    ctx.refresh_timeout(timedelta(seconds=10))
    time.sleep(5)

    return TaskOutput(status="success")


# ‼️


def main() -> None:
    worker = hatchet.worker(
        "timeout-worker", slots=4, workflows=[timeout_wf, refresh_timeout_wf]
    )

    worker.start()


if __name__ == "__main__":
    main()
