from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


# Create your models here.

# custome user manager
class MyUserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,verbose_name='Email',unique=True)
    name = models.CharField(max_length=255)
    tc = models.BooleanField()
    profile_pic = models.ImageField(upload_to="media", default="profile_pic.jpg")
    back_pic = models.ImageField(upload_to="media", default="back_profile.webp")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','tc']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # simplest possible answer: Yes always
        return self.is_admin
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'? "
        #simplest possible answer:Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a number of staff?"
        # simplest possible answer: All admins are staff
        return self.is_admin

class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    contact =models.CharField(max_length=12)
    dob = models.DateField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.fname
    
class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    board = models.CharField(max_length=200)
    pass_year = models.IntegerField()
    total_marks = models.IntegerField()
    percent = models.CharField(max_length=20)

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comp_name = models.CharField(max_length=200)
    job_role = models.CharField(max_length=200)
    experience = models.IntegerField()
    do_join = models.DateField()
    do_resign = models.DateField()

class SkillsFields(models.Model):
    p=models.CharField(max_length=20)

    def __str__(self):
        return self.p

class Skills(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills_field = models.ManyToManyField(SkillsFields)
    def Skill(self):
        return ", ".join([str(p) for p in self.skills_field.all()])

# class UpdateProfile(User):
#     update_profile = User.profile_pic
#     update_profile_back = User.back_pic
#     pf=models.ImageField(update_profile)
#     pfb=models.ImageField(update_profile_back)
