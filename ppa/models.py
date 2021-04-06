from django.db import models


# Create your models here.

class EventDate(models.Model):
    event_start_date = models.CharField(max_length=50)
    event_end_date = models.CharField(max_length=50)
    second_proposed_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.event_start_date)


class EventAttendance(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.ForeignKey(EventDate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_name


class Organisation(models.Model):
    name_of_organisation = models.CharField(max_length=100)
    email_of_organisation = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    event_date = models.ForeignKey(EventDate, on_delete=models.CASCADE)
    # event_attendance = models.ForeignKey(EventAttendance, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_of_organisation


class Individual(models.Model):
    name = models.CharField(max_length=70)
    index = models.FloatField(unique=True, default='01')
    # department = models.CharField(max_length=100, blank=True, null=True)
    # department_position = models.CharField(max_length=100, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True, default='ama@gmail.com')
    # organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    eventDate = models.ForeignKey(EventDate, on_delete=models.CASCADE)
    # event_attendance = models.ForeignKey(EventAttendance, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
