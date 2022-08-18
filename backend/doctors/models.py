from django.db import models
from calendar import FRIDAY, SATURDAY, THURSDAY, TUESDAY, WEDNESDAY
from hospitals.models import hospitals
class doctors(models.Model):

    MALE = 'Male'
    FEMALE = 'Female'

    CHOICE_GENDER = (
        (MALE,'Male'),
        (FEMALE,'Female')
    )

    ALLERGY_AND_IMMUNOLOGY = 'Allergy And Immunology'
    ANESTHESIOLOGY = 'Anesthesiology'
    DERMATOLOGY = 'Dermatology'
    DIAGNOSTIC_RADIOLOGY = 'Diagnostic Radiology'
    EMERGENCY_MEDICINE = 'Emergency Medicine'
    FAMILY_MEDICINE = 'Family Medicine'
    INTERNAL_MEDICINE = 'Internal Medicine'

    CHOICE_SPECIALIST = (
        (ALLERGY_AND_IMMUNOLOGY,'Allergy & Immunology'),
        (ANESTHESIOLOGY,'Anesthesiology'),
        (DERMATOLOGY,'Dermatology'),
        (DIAGNOSTIC_RADIOLOGY,'Diagnostic Radiology'),
        (EMERGENCY_MEDICINE,'Emergency Medicine'),
        (FAMILY_MEDICINE,'Family Medicine'),
        (INTERNAL_MEDICINE,'Internal Medicine'),
    )

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=CHOICE_GENDER)
    specialist = models.CharField(max_length=100, choices=CHOICE_SPECIALIST)
    
    def __str__(self):
        return self.firstName

class doctors_hospitals(models.Model):
    SUNDAY = 'Sunday'
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'

    CHOICE_DAY = (
        (SUNDAY,'Sunday'),
        (MONDAY,'Monday'),
        (TUESDAY,'Tuesday'),
        (WEDNESDAY,'Wednesday'),
        (THURSDAY,'Thursday'),
        (FRIDAY,'Friday'),
        (SATURDAY,'Saturday')
    )
    
    # doctor_id = models.ForeignKey('doctors', on_delete=models.CASCADE)
    # hospital_id = models.ForeignKey('hospitals', on_delete=models.CASCADE)
    hospital_id = models.IntegerField()
    doctor_id = models.IntegerField()
    day = models.CharField(max_length=20,choices=CHOICE_DAY)
    startTime = models.TimeField('%H:%M')
    endTime = models.TimeField('%H:%M')