from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.todos.models import Todo
from apps.sub_todos.models import SubTodo

User = get_user_model()


class SubTodoModelTest(TestCase):
    def test_create_sub_todo(self):
        user = User.objects.create_user(username="subtodo_user", password="pass1234")
        todo = Todo.objects.create(user=user, title="Build API")
        sub_todo = SubTodo.objects.create(todo=todo, title="Write tests")

        self.assertEqual(sub_todo.todo, todo)
        self.assertFalse(sub_todo.is_done)
