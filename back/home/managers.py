from django.contrib.auth.base_user import BaseUserManager



class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, phone, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, phone, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if not extra_fields.get('is_staff'):
            raise ValueError('blabla')
        if not extra_fields.get('is_superuser'):
            raise ValueError('blabla')
        return self.create_user(email, password, phone, **extra_fields)