
from django.test import TestCase
from django.urls import resolve
from django.core.urlresolvers import reverse
from boards.views import TopicListView, new_topic
from boards.models import Board, Topic, Post
from django.contrib.auth.models import User
from boards.forms import NewTopicForm



class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django Board')

    def test_board_topics_view_success_status_code(self):
        url= reverse('board_topics',kwargs = {'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs = {'pk':99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func.view_class, TopicListView)
    def test_link_back_to_boards(self):
        url = reverse('board_topics',kwargs = {'pk' : 1})
        response = self.client.get(url)
        home_url = reverse('home')
        self.assertContains(response, 'href = "{0}"'.format(home_url))
    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse('board_topics',kwargs = {'pk':1})
        new_topic_url = reverse('new_topic',kwargs = {'pk':1})
        response = self.client.get(board_topics_url)
        self.assertContains(response,'href="{0}"'.format(new_topic_url))
