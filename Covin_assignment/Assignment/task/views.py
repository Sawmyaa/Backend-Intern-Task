from django.http import HttpResponseRedirect, JsonResponse
from django.views import View
from django.conf import settings
from urllib.parse import urlencode
import json
import requests


class GoogleCalendarInitView(View):
    def get(self, request):
        params = {
            'client_id': settings.GOOGLE_CLIENT_ID,
            'redirect_uri': settings.GOOGLE_REDIRECT_URI,
            'response_type': 'code',
            'scope': 'https://www.googleapis.com/auth/calendar.readonly',
        }
        auth_url = 'https://accounts.google.com/o/oauth2/auth?' + urlencode(params)
        return HttpResponseRedirect(auth_url)


class GoogleCalendarRedirectView(View):
    def get(self, request):
        code = request.GET.get('code')

        if code:
            token_url = 'https://accounts.google.com/o/oauth2/token'
            data = {
                'code': code,
                'client_id': settings.GOOGLE_CLIENT_ID,
                'client_secret': settings.GOOGLE_CLIENT_SECRET,
                'redirect_uri': settings.GOOGLE_REDIRECT_URI,
                'grant_type': 'authorization_code',
            }
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.post(token_url, data=data, headers=headers)
            if response.status_code == 200:
                access_token = response.json().get('access_token')

                # Get events using access_token
                events_url = 'https://www.googleapis.com/calendar/v3/calendars/primary/events'
                headers = {'Authorization': f'Bearer {access_token}'}
                response = requests.get(events_url, headers=headers)
                if response.status_code == 200:
                    events = response.json().get('items', [])
                    return JsonResponse({'events': events})

        return JsonResponse({'error': 'Invalid authorization'})


