from django.http import HttpResponse
from django.shortcuts import render, redirect


def markSheet(request):
    data = {}

    if request.method=="POST":
        try:
            s1 = eval(request.POST.get('subject1'))
            s2 = eval(request.POST.get('subject2'))
            s3 = eval(request.POST.get('subject3'))
            s4 = eval(request.POST.get('subject4'))
            s5 = eval(request.POST.get('subject5'))
            total = s1+s2+s3+s4+s5
            percentage = total*100/500

            if percentage>85:
                division = "Distinction"
            elif percentage>65:
                division = "First Class"
            elif percentage>55:
                division = "Second Class"
            elif percentage>45:
                division = "Third Class"
            elif percentage>35:
                division = "Just Pass"
            else:
                division = "Fail"

            data = {
                'total': total,
                'percentage': percentage,
                'div': division
            }

        except:
            data['error'] = "Invalid input. Please enter valid marks."

    return render(request, 'marksheet.html', data)