from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from boards.models import Board,Topic,Post
from boards.views import reply_topic

class ReplyTopicTestCase(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        self.username = 'John'
        self.password = '123'
        self.user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.topic = Topic.objects.create(subject='Hello, world', board=self.board, starter=self.user)
        Post.objects.create(message='Lorem ipsum dolor sit amet', topic=self.topic, created_by=self.user)
        self.url = reverse('reply_topic', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})


class SuccessfulReplyTopicTests(ReplyTopicTestCase):
    # ...

    def test_redirection(self):
        '''
        A valid form submission should redirect the user
        '''
        url = reverse('topic_posts', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})
        topic_posts_url = '{url}?page=1#2'.format(url=url)
        self.assertRedirects(self.response, topic_posts_url)
