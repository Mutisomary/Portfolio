import unittest
from flask import current_app
from flaskblog import db, app
from flaskblog.models import User, Post


class TestModels(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_creation(self):
        with app.app_context():
            user = User(username='test_user', email='test@example.com', password='test123')
            db.session.add(user)
            db.session.commit()

            self.assertEqual(User.query.count(), 1)
            self.assertEqual(user.username, 'test_user')
            self.assertEqual(user.email, 'test@example.com')

    def test_post_creation(self):
        with app.app_context():
            user = User(username='test_user', email='test@example.com', password='test123')
            post = Post(title='Test Post', content='This is a test post', author=user)
            db.session.add(user)
            db.session.add(post)
            db.session.commit()

            self.assertEqual(Post.query.count(), 1)
            self.assertEqual(post.title, 'Test Post')
            self.assertEqual(post.content, 'This is a test post')
            self.assertEqual(post.author, user)


if __name__ == '__main__':
    unittest.main()