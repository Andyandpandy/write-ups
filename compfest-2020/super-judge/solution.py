from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('andyadmin', 'admin@myproject.com', 'password')

if __name__ == "__main__":
    main()

