from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.template import RequestContext
from .models import CaseTable, ExaminerTable, VenueTable, CandidateTable
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def login_user(request):

	html_param = {}
	return render_to_response('login.html', html_param, RequestContext(request))

@csrf_exempt
def dashboard(request):
	print RequestContext(request)
	html_param = {}
	return render_to_response('dashboard.html', html_param, RequestContext(request))

#########################################
# API STUFFS FOR DATABASE
#########################################

def api_case_all(request):
	response_data = {}
	cases = CaseTable.objects.all()

	for case in cases:
		response_data[case.id] = {
			'topic' : case.topic,
			'name' : case.name,
			'cpc' : case.cpc,
			'type' : case.type,
			'age' : case.age,
			'gender' : case.gender,
			'rating' : case.rating,
			'r1' : case.r1,
			'r2' : case.r2,
			'r3' : case.r3,
			'r4' : case.r4,
			'r5' : case.r5,
			'r6' : case.r6,
			'w1' : case.w1,
			'w2' : case.w2,
			'w3' : case.w3,
			'w4' : case.w4,
			'w5' : case.w5,
			'w6' : case.w6,
			'ab_status' : case.ab_status,
			'role_player' : case.role_player,
			'observer' : case.observer,
			'actor' : case.actor,
			'duration' : case.duration,
		}

	return JsonResponse(response_data)

def api_candidate_all(request):
	response_data = {}
	candidates = CandidateTable.objects.all()

	for candidate in candidates:
		response_data[candidate.id] = {
			'firstname' : candidate.firstname,
			'lastname' : candidate.lastname,
			'venue_id' : candidate.venue_id
		}

	return JsonResponse(response_data)

def api_examiner_all(request):
	response_data = {}
	examiners = ExaminerTable.objects.all()

	for examiner in examiners:
		response_data[examiner.id] = {
			'firstname' : examiner.firstname,
			'lastname' : examiner.lastname,
			'gender' : examiner.gender,
			'state_province' : examiner.state_province,
			'birthdate' : examiner.birthdate,
			'availability' : examiner.availability,
			'ab_status' : examiner.ab_status,
		}

	return JsonResponse(response_data)

def api_venue_all(request):
	response_data = {}
	venues = VenueTable.objects.all()

	for venue in venues:
		response_data[venue.id] = {
			'city' : venue.city,
			'venue' : venue.venue,
			'key' : venue.key,
			'description' : venue.description,
			'use' : venue.use,
			'capacity' : venue.capacity,
			'max_capacity' : venue.max_capacity,
			'start_time' : venue.start_time,
		}
	return JsonResponse(response_data)

def api_candidate_update(request):
	response_data = {}
	
	if request.method == 'POST':
		id = request.POST.get('id', '')
		if CandidateTable.objects.filter(id=id).exists():
			candidate = CandidateTable.objects.get(id=id)
			candidate.firstname = request.POST.get('firstname', '')
			candidate.lastname = request.POST.get('lastname', '')
			candidate.venue_id = request.POST.get('venue_id', '')
			candidate.save()
			response_data = {'status' : 'success'}
		else:
			response_data = {'status' : 'fail'}
	else:
		response_data = {'status' : 'invalid'}


	return JsonResponse(response_data)

def api_examiner_update(request):
	response_data = {}

	if request.method == 'POST':
		id = request.POST.get('id', '')
		if ExaminerTable.objects.filter(id=id).exists():
			examiner = ExaminerTable.objects.get(id=id)
			examiner.firstname = request.POST.get('firstname', '')
			examiner.lastname = request.POST.get('lastname', '')
			examiner.gender = request.POST.get('gender', '')
			examiner.state_province = request.POST.get('state_province', '')
			examiner.birthdate = request.POST.get('birthdate', '')
			examiner.availability = request.POST.get('availability', '')
			examiner.ab_status = request.POST.get('ab_status', '')
			examiner.save()
			response_data = {'status' : 'success'}
		else:
			response_data = {'status' : 'fail'}
	else:
		response_data = {'status' : 'invalid'}

	return JsonResponse(response_data)

def api_venue_update(request):
	response_data = {}

	if request.method == 'POST':
		id = request.POST.get('id', '')
		if VenueTable.objects.filter(id=id).exists():
			venue = VenueTable.objects.get(id=id)
			venue.city = request.POST.get('city', '')
			venue.venue = request.POST.get('venue', '')
			venue.key = request.POST.get('key', '')
			venue.description = request.POST.get('description', '')
			venue.capacity = request.POST.get('capacity', '')
			venue.max_capacity = request.POST.get('max_capacity', '')
			venue.start_time = request.POST.get('start_time', '')
			venue.save()
			response_data = {'status' : 'success'}
		else:
			response_data = {'status' : 'fail'}
	else:
		response_data = {'status' : 'invalid'}

	return JsonResponse(response_data)

def api_case_update(request):
	response_data = {}

	if request.method == 'POST':
		id = request.POST.get('id', '')
		if CaseTable.objects.filter(id=id).exists():
			case = CaseTable.objects.get(id=id)
			case.topic = request.POST.get('topic','')
			case.name = request.POST.get('name','')
			case.cpc = request.POST.get('topic','')
			case.type = request.POST.get('type','')
			case.age = request.POST.get('topic','')
			case.gender = request.POST.get('gender','')
			case.rating = request.POST.get('rating','')
			case.r1 = request.POST.get('r1','')
			case.r2 = request.POST.get('r2','')
			case.r3 = request.POST.get('r3','')
			case.r4 = request.POST.get('r4','')
			case.r5 = request.POST.get('r5','')
			case.r6 = request.POST.get('r6','')
			case.w1 = request.POST.get('w1','')
			case.w2 = request.POST.get('w2','')
			case.w3 = request.POST.get('w3','')
			case.w4 = request.POST.get('w4','')
			case.w5 = request.POST.get('w5','')
			case.w6 = request.POST.get('w6','')
			case.ab_status = request.POST.get('ab_status','')
			case.role_player = request.POST.get('role_player','')
			case.observer = request.POST.get('observer','')
			case.actor = request.POST.get('actor','')
			case.duration = request.POST.get('duration','')			
			venue.save()
			response_data = {'status' : 'success'}
		else:
			response_data = {'status' : 'fail'}
	else:
		response_data = {'status' : 'invalid'}

	return JsonResponse(response_data)

def api_venue_delete(request, id):
	response_data = {}

	if VenueTable.objects.filter(id=id).exists():
		venue = VenueTable.objects.get(id=id)
		venue.delete()
		response_data = {'status' : 'success'}
	else:
		response_data = {'status' : 'invalid'}

	return JsonResponse(response_data)

def api_examiner_delete(request, id):
	response_data = {}

	if ExaminerTable.objects.filter(id=id).exists():
		examiner = ExaminerTable.objects.get(id=id)
		examiner.delete()
		response_data = {'status' : 'success'}
	else:
		response_data = {'status' : 'invalid'}

	return JsonResponse(response_data)

def api_case_delete(request, id):
	response_data = {}

	if CaseTable.objects.filter(id=id).exists():
		case = CaseTable.objects.get(id=id)
		case.delete()
		response_data = {'status' : 'success'}
	else:
		response_data = {'status' : 'invalid'}

	return JsonResponse(response_data)

def api_candidate_delete(request, id):
	response_data = {}

	if CandidateTable.objects.filter(id=id).exists():
		candidate = CandidateTable.objects.get(id=id)
		candidate.delete()
		response_data = {'status' : 'success'}
	else:
		response_data = {'status' : 'invalid'}

	return JsonResponse(response_data)