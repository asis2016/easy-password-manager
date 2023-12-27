from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import PasswordManager


class PasswordManagerTest(TestCase):

    #Setup initial data for the test
    def setUp(self):
        
        self.user = get_user_model().objects.create_user(    # <--Setup `testuser`
            username='testuser',
            email='test@example.com',
            password='password'
        )

        self.pm = PasswordManager.objects.create(    # <--Creates a `PasswordManager` object
            name='gmail',
            username='testuser@gmail.com',
            password='password',
            url='gmail.com'
        )


    def test_password_manager_content(self):
        '''
        Assert if the data saved in PasswordManager matches.
        '''
        self.assertEqual(f'{self.pm.name}', 'gmail')
        self.assertEqual(f'{self.pm.username}', 'testuser@gmail.com')
        self.assertEqual(f'{self.pm.password}', 'password')
        self.assertEqual(f'{self.pm.url}', 'gmail.com')


    def test_password_manager_list_view(self):
        '''
        Assert if the `password_manager_list` is 200 OK.
        '''
        self.client.login(username='testuser', password='password')    # <--To login the user
        response = self.client.get(reverse('password_manager_list'))
        self.assertEqual(response.status_code, 200)


    def test_password_manager_detail_view(self):
        '''
        Assert if the `PasswordManagerDetailView` is 200 OK.
        '''
        self.client.login(username='testuser', password='password')    
        response = self.client.get('/1/')
        self.assertEqual(response.status_code, 200)


    def test_password_manager_delete_view(self):
        '''
        Assert if the `PasswordManagerDeleteView` is 302.
        '''
        self.client.login(username='testuser', password='password')
        response = self.client.post('/1/delete/')
        self.assertEqual(response.status_code, 302)


    def test_password_manager_update_view(self):
        '''
        Assert if the `PasswordManagerUpdateView` is 200 or 302.
        '''
        self.client.login(username='testuser', password='password')
        update_url = reverse('password_manager_update', kwargs={'pk': self.pm.pk})
        response_get = self.client.get(update_url)
        self.assertEqual(response_get.status_code, 200)

        updated_data = {
            'username':'newuser'
        }

        response_post = self.client.post(update_url, data=updated_data)
        self.assertIn(response_post.status_code, [200, 302])
        self.pm.refresh_from_db()