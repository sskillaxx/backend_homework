from unittest.mock import Mock
from datetime import datetime

from schemas.tasks import CreateTask
from services.tasks import TaskService

def test_create_task_calls_repository_and_returns_result():
    repository = Mock()
    service = TaskService(repository)

    payload = CreateTask(
        name="TaskOne",
        priority="high",
        description="test description",
        deadline=datetime(2026, 3, 24, 12, 0, 0),
    )

    expected_task = Mock()
    repository.create_task.return_value = expected_task

    result = service.create_task(payload)

    repository.create_task.assert_called_once_with(payload)
    assert result == expected_task