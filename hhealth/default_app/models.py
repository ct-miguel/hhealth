from django.db import models

GENDERS = (
	('M', 'Male'),
    ('F', 'Female'),
    ('E', 'Either'),
)

DURATION_TYPES = (
	('L', 'Long'),
    ('S', 'Short'),
)

YES_NO = (
	('Y', 'Yes'),
	('N', 'No'),
)

AVAILABILITY = (
	('A', 'AM'),
	('P', 'PM'),
	('B', 'AM PM'),
)

# Create your models here.
class CaseTable(models.Model):
	id = models.CharField(primary_key=True, max_length=255)
	topic = models.CharField(max_length=255, blank=True, default='')
	name = models.CharField(max_length=255, blank=True, default='')
	cpc = models.CharField(max_length=255, blank=True, default='')
	type = models.CharField(max_length=6, choices=DURATION_TYPES)
	age = models.CharField(max_length=2, blank=True, default='')
	gender = models.CharField(max_length=6, choices=GENDERS)
	rating = models.CharField(max_length=2, blank=True, default='')

	r1 = models.CharField(max_length=255, blank=True, default='')
	r2 = models.CharField(max_length=255, blank=True, default='')
	r3 = models.CharField(max_length=255, blank=True, default='')
	r4 = models.CharField(max_length=255, blank=True, default='')
	r5 = models.CharField(max_length=255, blank=True, default='')
	r6 = models.CharField(max_length=255, blank=True, default='')
	w1 = models.CharField(max_length=255, blank=True, default='')
	w2 = models.CharField(max_length=255, blank=True, default='')
	w3 = models.CharField(max_length=255, blank=True, default='')
	w4 = models.CharField(max_length=255, blank=True, default='')
	w5 = models.CharField(max_length=255, blank=True, default='')
	w6 = models.CharField(max_length=255, blank=True, default='')

	ab_status = models.CharField(max_length=3, choices=YES_NO)
	role_player = models.BooleanField(blank=False, default=False)
	observer = models.BooleanField(blank=False, default=False)
	actor = models.BooleanField(blank=False, default=False)
	duration = models.CharField(max_length=255, blank=True, default='')

#class ScheduleTable(models.Model):
#	case = models.ForeignKey(CaseTable, unique=False)
#	candidate = models.ForeignKey(CandidateTable, unique=False)
#	time_id
#	examiner_1
#	examiner_2

class ExaminerTable(models.Model):
	id = models.CharField(primary_key=True, max_length=255)
	firstname = models.CharField(max_length=255, blank=True, default='')
	lastname = models.CharField(max_length=255, blank=True, default='')
	gender = models.CharField(max_length=6, choices=GENDERS)
	state_province = models.CharField(max_length=20, blank=True, default='')
	birthdate = models.CharField(max_length=20, blank=True, default='')
	availability = models.CharField(max_length=6, choices=AVAILABILITY)
	ab_status = models.CharField(max_length=3, choices=YES_NO)

class VenueTable(models.Model):
	id = models.CharField(primary_key=True, max_length=255)
	city = models.CharField(max_length=255, blank=True, default='')
	venue = models.CharField(max_length=255, blank=True, default='')
	key = models.CharField(max_length=255, blank=True, default='')
	description = models.CharField(max_length=255, blank=True, default='')
	use = models.BooleanField(blank=False, default=False)
	capacity = models.IntegerField(default=0)
	max_capacity = models.IntegerField(default=0)
	start_time = models.CharField(max_length=255, blank=True, default='')

class CandidateTable(models.Model):
	id = models.CharField(primary_key=True, max_length=255)
	firstname = models.CharField(max_length=255, blank=True, default='')
	lastname = models.CharField(max_length=255, blank=True, default='')
	venue = models.ForeignKey(VenueTable, unique=False)
