from django.contrib.auth.base_user import BaseUserManager



class CustomUserManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, password, phone, **extra_fields):

        if not first_name:
            raise ValueError('The first name must be set')

        if not last_name:
            raise ValueError('The last name must be set')

        if not email:
            raise ValueError('The email must be set')

        if not password:
            raise ValueError('The password must be set')

        if not phone:
            raise ValueError('The phone must be set')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        if user:
            return user
        else:
            raise ValueError('User not created')

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        # if not extra_fields.get('field'):
        #     raise ValueError('The field must be set')

        return self.create_user(
            first_name='John',
            last_name='Doe',
            email=email,
            password=password,
            phone='undefined',
            **extra_fields
        )