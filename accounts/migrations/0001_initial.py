from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def forward_func(apps, schema_editor):
    # 현재 모든 user에 profile 만들기
    # AUTH_USER_MODEL = "auth.User" (인증에 사용할 커스텀 User model: "앱이름.모델명"
    auth_user_model = settings.AUTH_USER_MODEL.split(".")

    # migration에서 user model 가져올 떄: apps.get_model(o) get_user_model(x)
    User = apps.get_model(*auth_user_model)
    Profile = apps.get_model("account", "Profile")

    for user in User.objects.all():
        print(f"create profile for user#{user.pk}")
        Profile.objects.create(user=user)


def backward_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('website_url', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        # 실행될 때 함수 호출
        migrations.RunPython(forward_func, backward_func),
    ]
