from .base import UserBaseTests


class LoginTests(UserBaseTests):
    def test_render_the_correct_template(self):
        response = self.client.get('/user/login/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_with_valid_credential(self):
        response = self.client.post('/user/login/', {
            'login': self.alice.username,
            'password': 's3cr3t',            
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/user/confirm-email/')

    def test_with_invalid_credential(self):
        response = self.client.post('/user/login/', {
            'login': 'aaa',
            'password': 'bbb',
        })

        self.assertEqual(
            response.context['form'].non_field_errors()[0], 
            'The username and/or password you specified are not correct.',
        )
