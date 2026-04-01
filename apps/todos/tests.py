from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.todos.models import Todo, TodoPriority, TodoStatus

User = get_user_model()


class TodoModelTest(TestCase):
    def test_create_todo(self):
        user = User.objects.create_user(username="todo_user", password="pass1234")
        todo = Todo.objects.create(user=user, title="Buy milk")

        self.assertEqual(todo.title, "Buy milk")
        self.assertEqual(todo.status, TodoStatus.TODO)
        self.assertEqual(todo.priority, TodoPriority.MEDIUM)
