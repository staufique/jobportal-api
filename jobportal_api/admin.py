from django.contrib import admin
from jobportal_api.models import User,Education,PersonalInfo,Experience,Skills,SkillsFields
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ["id","email", "name", "tc","is_admin","profile_pic","back_pic"]
    list_filter = ["is_admin"]
    fieldsets = [
        ('User Credentials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name","tc","profile_pic","back_pic"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name","tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email","id"]
    filter_horizontal = []

admin.site.register(User, UserModelAdmin)

@admin.register(PersonalInfo)
class PersonalAdmin(admin.ModelAdmin):
    list_display=['id','user','fname','lname','gender','contact','dob','address']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display=['user','qualification','institute','board','pass_year','total_marks','percent']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display=['user','comp_name','job_role','experience','do_join','do_resign']


@admin.register(SkillsFields)
class SkillsFieldsAdmin(admin.ModelAdmin):
    list_display=['id','p']

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display=["user","Skill"]