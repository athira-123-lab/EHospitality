from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login


from ehospital_app.models import Patient, Appointment, Prescription


# Create your views here.
def About(request):
    return render(request,'register.html')



def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')




def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('about')
            else:

                user = User.objects.create_user(username=username,password=password)
                user.save()

                messages.success(request, "User created successfully")
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('about')
    return render(request, 'register.html')





def Login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user:
            try:
                if not user.is_staff:
                    auth_login(request, user)
                    error = "yes"
                else:
                    error = "no"
            except Exception as e:
                error = "yes"
        else:
            error = "yes"

    context = {'error': error}
    return render(request, 'login.html', context)


def Home(request):
    return render(request,'home.html')

def Patient_details(request):
    if not request.user.is_staff:
        return redirect('login')
    patient=Patient.objects.all()
    p={'patient':patient}
    return render(request,'patient_details.html',p)




def Add_patient(request):

    if  not request.user.is_staff:
        return redirect('login')

    error = None

    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        age = request.POST.get('age')
        address = request.POST.get('address')
        disease = request.POST.get('disease')

        try:

            Patient.objects.create(
                name=name,
                gender=gender,
                mobile=mobile,
                age=age,
                address=address,
                disease=disease,

            )
            error = "no"
        except Exception as e:
            error = "yes"
            print(f"Error: {e}")


    p = {'error': error}

    return render(request, 'add_patient.html', p)
def Delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient=Patient.objects.get(id=pid)
    patient.delete()
    return redirect('patient_details')

def Schedule(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment=Appointment.objects.all()
    p={'appointment':appointment}
    return render(request,'schedule.html',p)

def Booking(request):

    if not request.user.is_staff:
        return redirect('login')

    error = None

    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')


        try:

            Appointment.objects.create(
                name=name,
                date=date,
                time=time,

            )
            error = "no"
        except Exception as e:
            error = "yes"
            print(f"Error: {e}")


    p = {'error': error}

    return render(request, 'booking.html', p)

def Delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment=Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('schedule')

def View_prescription(request):
    if not  request.user.is_staff:
        return redirect('login')
    prescription=Prescription.objects.all()
    p={'prescription':prescription}
    return render(request,'view_prescription.html',p)

def Delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    prescription=Prescription.objects.get(id=pid)
    prescription.delete()
    return redirect('view_prescription')

def Add_prescription(request):
    if not request.user.is_staff:
        return redirect('login')

    error = None

    if request.method == 'POST':

        medicine = request.POST.get('medicine')
        dosage = request.POST.get('dosage')

        try:

            Prescription.objects.create(
                medicine=medicine,
                dosage=dosage,
            )
            error = "no"
        except Exception as e:
            error = "yes"
            print(f"Error: {e}")

    context = {'error': error}
    return render(request, 'add_prescription.html', context)

