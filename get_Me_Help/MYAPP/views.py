import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.db.models.expressions import RawSQL
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def view_fuel_provider(request):
    request.session['head']='VIEW AND VERIFY FUEL PROVIDER'
    res=fuel_provider.objects.filter(LOGIN__usertype='pending')
    return render(request,'admin/fuel provider table.html', {'data':res})

def approve_fuel_provider(request,id):
    login.objects.filter(id=id).update(usertype='fuel_provider')
    return HttpResponse("<script>alert('Approved');window.location='/view_fuel_provider'</script>")

def reject_fuel_provider(request,id):
    login.objects.filter(id=id).update(usertype='reject')
    return HttpResponse("<script>alert('Rejected');window.location='/view_fuel_provider'</script>")


def approved__fuel_provider(request):
    request.session['head'] = 'VIEW APPROVED FUEL PROVIDER'
    res=fuel_provider.objects.all()
    return render(request,'admin/approved fuel provider.html', {'data':res})

def view_mechanic(request):
    request.session['head'] = 'VIEW AND VERIFY MECHANIC'
    res=mechanic.objects.filter(LOGIN__usertype='pending')
    return render(request, 'admin/mechanic aprove or reject table.html', {'data':res})

def approve_mechanic(request,id):
    login.objects.filter(id=id).update(usertype='mechanic')
    return HttpResponse("<script>alert('Approved');window.location='/view_mechanic'</script>")

def reject_mechanic(request,id):
    login.objects.filter(id=id).update(usertype='reject')
    return HttpResponse("<script>alert('Rejected');window.location='/view_mechanic'</script>")

def view_approved_mechanic(request):
    request.session['head'] = 'VIEW APPROVED MECHANIC'
    res=mechanic.objects.filter(LOGIN__usertype='mechanic')
    return render(request, 'admin/verified mechanic.html', {'data':res})

def send_reply(request,id):
    request.session['head'] = 'REPLY'
    return render(request, 'admin/Send Reply.html',{'id':id})

def send_reply_post(request,id):
    reply = request.POST['textarea']
    complaint.objects.filter(id=id).update(reply=reply,reply_date=datetime.datetime.now().date())
    return HttpResponse("<script>alert('Success');window.location='/view_complaint'</script>")

def view_complaint(request):
    request.session['head'] = 'COMPLAINT'
    res=complaint.objects.all()
    return render(request, 'admin/view complaint.html', {'data':res})

def view_feedback(request):
    request.session['head'] = 'FEEDBACK'
    res=feedback.objects.all()
    return render(request, 'admin/View Feedback Table.html', {'data':res})

def view_rating(request):
    request.session['head'] = 'RATING'
    res=rating.objects.all()
    return render(request, 'admin/View Rating table.html', {'data':res})

def view_user(request):
    request.session['head'] = 'VIEW USER'
    res=user.objects.all()
    return render(request, 'admin/view user table.html', {'data':res})

def log(request):
    return render(request,'index.html')
def log_post(request):
    Username = request.POST['username']
    Password = request.POST['pass']
    data = login.objects.filter(username=Username,password=Password)
    if data.exists():
        data=data[0]
        request.session['lg'] = 1
        request.session['lid'] = data.id
        if data.usertype == 'admin':

            return HttpResponse("<script>alert('Login Success');window.location='/admin_home'</script>")
        elif data.usertype== 'fuel_provider':
            request.session['lid'] = data.id
            return HttpResponse("<script>alert('Login Success');window.location='/Fuel_Provider_Home'</script>")
        elif data.usertype== 'mechanic':
            request.session['lid'] = data.id

            return HttpResponse("<script>alert('Login Success');window.location='/Mechanic_Home'</script>")


    return HttpResponse("<script>alert('Invalid authentication');window.location='/'</script>")

def admin_home(request):
    return render(request, 'admin/admin_index.html')

def logout(request):
    request.session['lg'] = 0
    return HttpResponse("<script>alert('Logged out');window.location='/'</script>")






####Fuel provider




def Adding_Fuel_Price(request):
    request.session['head'] = 'ADD FUEL PRICE'
    return render(request, "Fuel provider/Fuel_Provider_Add_Fuel_price.html")

def Adding_Fuel_Price_post(request):
    fuel_prices = request.POST['textfield']
    fuel_density = request.POST['textfield2']
    fuel_type = request.POST['CheckboxGroup1']

    obj = fuel_price()
    obj.Fuel_Price = fuel_prices
    obj.Fuel_Density = fuel_density
    obj.Fuel_type = fuel_type
    obj.FUEL_PROVIDER_id = fuel_provider.objects.get(LOGIN=request.session['lid']).id
    obj.save()

    return HttpResponse("<script>alert('Success');window.location='/Adding_Fuel_Price'</script>")




def Fuel_Price_Edit(request,id):
    request.session['head'] = 'FUEL PRICE EDIT'
    data = fuel_price.objects.get(id=id)
    return render(request, "Fuel provider/Fuel_Provider_Fuel_Price_Edit.html",{'data':data})

def Fuel_Price_Edit_post(request,id):
    fuel_prices = request.POST['textfield']
    fuel_density = request.POST['textfield2']
    fuel_type = request.POST['CheckboxGroup1']
    fuel_price.objects.filter(id=id).update(Fuel_Price=fuel_prices,Fuel_Density=fuel_density,Fuel_type=fuel_type)
    return HttpResponse("<script>alert('Success');window.location='/Fuel_Price_View'</script>")


def Fuel_Price_View(request):
    request.session['head'] = 'VIEW FUEL PRICE'
    res=fuel_price.objects.filter(FUEL_PROVIDER__LOGIN=request.session['lid'])
    return render(request, "Fuel provider/Fuel_Provider_Fuel_price_view.html",{"data":res})

def Fuel_Provider_Profile_Manager(request):
    print("MMMMM",request.session['lid'])
    request.session['head'] = 'MANAGE PROFILE'
    Fuel_provider=fuel_provider.objects.get(LOGIN=request.session['lid'])
    return render(request, "Fuel provider/Fuel_provider_Manage_Profile_Table.html",{"data":Fuel_provider})

def Fuel_Provider_Profile_Manager_post(request):

    Name = request.POST['textfield']
    Email = request.POST['textfield2']
    Contact = request.POST['textfield3']
    fuel_provider.objects.filter(LOGIN=request.session['lid']).update(name=Name,email=Email,contact_no=Contact)
    return HttpResponse("<script>alert('uccess');window.location='/Fuel_Provider_Profile_Manager'</script>")


def Fuel_Provider_Payment_Table(request):
    request.session['head'] = 'FUEL PROVIDER PAYMENT TABLE'
    data = fuel_provider_request.objects.filter(FUEL_PRICE__FUEL_PROVIDER__LOGIN=request.session['lid'])
    return render(request, "Fuel provider/Fuel_Provider_Payment_Table.html",{"data":data})

def Fuel_Provider_Rating(request):
    request.session['head'] = 'FUEL PROVIDER RATING'
    data = rating.objects.filter(LOGIN=request.session['lid'])
    return render(request, "Fuel provider/Fuel_Provider_rating_table.html",{"data":data})

def Fuel_Provider_Register_Table(request):
    return render(request, "Fuel provider/registerfp.html")

def Fuel_Provider_Register_Table_post(request):

    name = request.POST['textfield']
    email = request.POST['textfield2']
    contact = request.POST['textfield3']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    password = request.POST['textfield4']
    cpass = request.POST['textfield5']
    if password == cpass:
        obj1 = login()
        obj1.username = name
        obj1.password = password
        obj1.usertype = "pending"
        obj1.save()

        obj = fuel_provider()
        obj.name = name
        obj.email = email
        obj.contact_no = contact
        obj.latitude = latitude
        obj.longitude = longitude
        obj.LOGIN = obj1
        obj.save()

        return HttpResponse("<script>alert('registered');window.location='/'</script>")

def Fuel_Provider_View_User_request(request):
    request.session['head'] = 'FUEL PROVDER USER REQUEST'
    res=fuel_provider_request.objects.filter(status='pending',FUEL_PRICE__FUEL_PROVIDER__LOGIN = request.session['lid'])

    return render(request, "Fuel provider/Fuel_Provider_View_User_Request.html",{"data":res})

def Fuel_Provider_Home(request):
    return render(request, 'Fuel provider/Fuel_Provider_home_index.html')

def Delete_Fuel_Price(request,id):
    fuel_price.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/Fuel_Price_View'</script>")

def approve_user_request(request,id):
    fuel_provider_request.objects.filter(id=id).update(status='approved')
    return HttpResponse("<script>alert('Approved');window.location='/Fuel_Provider_View_User_request'</script>")

def reject_user_request(request,id):
    fuel_provider_request.objects.filter(id=id).update(status='rejected')
    return HttpResponse("<script>alert('Rejected');window.location='/Fuel_Provider_View_User_request'</script>")

def Fuel_Provider_Order_History(request):
    request.session['head'] = 'FUEL PROVIDER ORDER HISTORY'
    res=fuel_provider_request.objects.filter(FUEL_PRICE__FUEL_PROVIDER__LOGIN_id=request.session['lid'],status='completed')
    return render(request,"Fuel provider/Fuel_Provider_Order_History.html",{"data":res})

def Fuel_Provider_trackOrder(request):
    request.session['head'] = 'FUEL PROVIDER TRACK ORDER'
    res=fuel_provider_request.objects.filter(FUEL_PRICE__FUEL_PROVIDER__LOGIN_id=request.session['lid'],status='approved')
    print("jjjjj",res)
    return render(request,"Fuel provider/Fuel_Provider_trackOrder.html",{"data":res})




##Mechanic

def Mechanic_Home(request):
    return render(request,"mechanic/Mechanic_Home_index.html")

def Mechanic_Add_Amount(request):
    request.session['head'] = 'ADD AMOUNT'
    return render(request,"mechanic/Mechanic_Add_Service_Amount.html")

def Mechanic_Add_Amount_Post(request):
    S_Details = request.POST['serv-det']
    Amount = request.POST['Serv-Ammount']

    obj = service_amount()
    obj.Service_Details = S_Details
    obj.amount = Amount
    obj.MECHANIC=mechanic.objects.get(LOGIN_id=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('Amount Added Successfully');window.location='/Mechanic_View_Amount'</script>")

def Mechanic_View_Amount(request):
    request.session['head'] = 'VIEW AMOUNT'
    res=service_amount.objects.filter(MECHANIC__LOGIN_id=request.session['lid'])
    return render(request,"mechanic/Mechanic_view_Serviceamount.html",{'data':res})

def Mechanic_Edit_Amount(request,id):
    request.session['head'] = 'EDIT AMOUNT'
    res=service_amount.objects.get(id=id)
    return render(request,"mechanic/Mechanic_Edit_Service.html",{'data':res})

def Mechanic_Edit_Amount_Post(request,id):
    S_Details = request.POST['serv-det']
    Amount = request.POST['Serv-Ammount']
    service_amount.objects.filter(id=id).update(Service_Details=S_Details,amount=Amount)
    return HttpResponse("<script>alert('Service Amount Edited');window.location='/Mechanic_View_Amount'</script>")

def Mechanic_Delete_Amount(request,id):
    service_amount.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Service Amount Deleted');window.location='/Mechanic_View_Amount'</script>")

def Mechanic_Manage_Profile(request):
    request.session['head'] = 'MANAGE PROFILE'
    data = mechanic.objects.get(LOGIN=request.session['lid'])
    return render(request,"mechanic/Mechanic_Manage_Profle.html", {'data':data})

def Mechanic_Manage_Profile_post(request):
    Name = request.POST['Name']
    Email = request.POST['Email']
    Contact = request.POST['Contact']
    Category = request.POST['Category']
    mechanic.objects.filter(LOGIN=request.session['lid']).update(name=Name,email=Email,contact_no=Contact,category=Category)
    return HttpResponse("<script>alert('Success');window.location='/Mechanic_Manage_Profile'</script>")

def Mechanic_Payment_History(request):
    request.session['head'] = 'PAYMENT HISTORY'
    res = mechanic_request.objects.filter(MECHANIC__LOGIN_id=request.session['lid'],Payment_Status__in=['Offline','online'])
    return render(request,"mechanic/Mechanic_Payment_History_Table.html",{'data':res})

def Mechanic_Register_Table(request):
    return render(request,"mechanic/mec_registerfp.html")

def Mechanic_Register_Table_post(request):
    Name = request.POST['Name']
    Email = request.POST['Email']
    Contact = request.POST['Contact']
    Category = request.POST['Category']
    Certificate = request.FILES['certificate']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    Password = request.POST['Password']

    fs=FileSystemStorage()
    d=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\zaifv\PycharmProjects\get_Me_Help\MYAPP\static\certificates\\"+d+".pdf",Certificate)
    path="/static/certificates/"+d+".pdf"
    CPassword = request.POST['Confirm Password']
    if Password == CPassword:
        obj1 = login()
        obj1.username = Name
        obj1.password = Password
        obj1.usertype = "pending"
        obj1.save()

        obj = mechanic()
        obj.name = Name
        obj.email = Email
        obj.contact_no = Contact
        obj.category = Category
        obj.longitude = longitude
        obj.latitude = latitude
        obj.certificate = path
        obj.LOGIN = obj1
        obj.save()
    return HttpResponse("<script>alert('Success');window.location='/'</script>")

def Mechanic_TrackOrder(request):
    request.session['head'] = 'TRACK ORDER'
    return render(request,"mechanic/Mechanic_Track_Order.html")

def Mechanic_View_order_History(request):
    request.session['head'] = 'VIEW ORDER HISTORY'
    res =mechanic_request.objects.filter(Q(MECHANIC__LOGIN_id=request.session['lid']),~Q(Payment_Status='pending'))
    return render(request,"mechanic/Mechanic_View_Order_History.html",{'data':res})

def Mechanic_View_Service_Details(request):
    request.session['head'] = 'VIEW SERVICE DETAILS'
    return render(request, "mechanic/Mechanic_view_Serviceamount.html")

def Mechanic_View_User_Request(request):
    request.session['head'] = 'VIEW USER REQUEST'
    res =mechanic_request.objects.filter(MECHANIC__LOGIN_id=request.session['lid'],status='pending')
    return render(request,"mechanic/Mechanic_View_User_Request.html",{'data':res})

def Mechanic_Request_Approve(request,id):
    mechanic_request.objects.filter(id=id).update(status='Approved')
    return HttpResponse("<script>alert('Approved');window.location='/Mechanic_View_User_Request'</script>")

def Mechanic_Request_Reject(request,id):
    mechanic_request.objects.filter(id=id).update(status='Rejected')
    return HttpResponse("<script>alert('Rejected');window.location='/Mechanic_View_User_Request'</script>")



def Mechanic_Rating(request):
    request.session['head'] = 'RATING'
    res =rating.objects.filter(LOGIN_id=request.session['lid'])
    return render(request,"mechanic/View Rating table.html",{'data':res})

def Mechanic_View_User_Request_Approved(request):
    request.session['head'] = 'VIEW USER REQUEST'
    res =mechanic_request.objects.filter(MECHANIC__LOGIN_id=request.session['lid'],status='Approved')
    return render(request,"mechanic/Approved mechanics.html",{'data':res})



##User Android


def user_login (request):
    Name=request.POST['Name']
    password=request.POST['password']
    data=login.objects.filter(username=Name , password=password)
    if data.exists():
        data=data[0]
        lid=data.id
        type=data.usertype
        return JsonResponse({'status':'ok',"lid":lid,"type":type})
    else:

        return JsonResponse({'status':None})


# def user_register (request):
#     Name=request.POST['name']
#     Email=request.POST['email']
#     latitude1=request.POST['latitude']
#     longitude1=request.POST['longitude']
#     Phnumber=request.POST['phone']
#     gender=request.POST['gender']
#     place=request.POST['place']
#     landmark=request.POST['landmark']
#     password=request.POST['password']
#     cpassword = request.POST['cpassword']
#     if password == cpassword:
#         obj = login()
#         obj.username = Email
#         obj.password = password
#         obj.usertype = "user"
#         obj.save()
#
#         data = user.objects.filter(LOGIN=obj)
#         if data.exists():
#             lati = data.latitude
#             logi = data.longitude
#             if lati == '' and logi == '':
#                 user.objects.filter(LOGIN=obj).update(latitude=latitude1, longitude=longitude1)
#                 return JsonResponse({'status': 'ok'})
#
#             else:
#                 obj1 = user()
#                 obj1.name = Name
#                 obj1.email = Email
#                 obj1.contact_no = Phnumber
#                 obj1.gender = gender
#                 obj1.longitude = longitude1
#                 obj1.latitude = latitude1
#                 obj1.place = place
#                 obj1.landmark = landmark
#                 obj1.LOGIN = obj
#                 obj1.save()
#                 return JsonResponse({'status': 'ok'})
#
#
#         else:
#             return JsonResponse({'status': 'notok'})


def user_register(request):
    Name = request.POST['name']
    Email = request.POST['email']
    latitude1 = request.POST['latitude']
    longitude1 = request.POST['longitude']
    Phnumber = request.POST['phone']
    gender = request.POST['gender']
    place = request.POST['place']
    landmark = request.POST['landmark']
    password = request.POST['password']
    cpassword = request.POST['cpassword']

    if password == cpassword:
        # Create or update login information
        obj, created = login.objects.get_or_create(
            username=Email,
            defaults={'password': password, 'usertype': 'user'}
        )
        if not created:
            # If user already exists, update the password if required
            obj.password = password
            obj.save()

        # Now check if user data exists in the user table for this login
        data = user.objects.filter(LOGIN=obj)
        if data.exists():
            # If latitude and longitude are empty, update them
            user_instance = data.first()
            if not user_instance.latitude and not user_instance.longitude:
                user_instance.latitude = latitude1
                user_instance.longitude = longitude1
                user_instance.save()
                return JsonResponse({'status': 'ok', 'message': 'latitude and longitude updated'})

            else:
                return JsonResponse({'status': 'ok', 'message': 'user already exists with full information'})

        else:
            # If the user does not exist, create a new user entry
            obj1 = user()
            obj1.name = Name
            obj1.email = Email
            obj1.contact_no = Phnumber
            obj1.gender = gender
            obj1.longitude = longitude1
            obj1.latitude = latitude1
            obj1.place = place
            obj1.landmark = landmark
            obj1.LOGIN = obj
            obj1.save()
            return JsonResponse({'status': 'ok', 'message': 'user registered successfully'})

    else:
        return JsonResponse({'status': 'error', 'message': 'Passwords do not match'})


def user_Manage_profile (request):
    lid=request.POST['lid']
    data=user.objects.get(LOGIN=lid)
    return JsonResponse({'status':'ok','name':data.name,'email':data.email,'phone number':data.contact_no,'gender':data.gender,'place':data.place,'landmark':data.landmark})








def edit_profile(request):
    Name = request.POST['name']
    lid = request.POST['lid']
    Email = request.POST['email']
    Phnumber = request.POST['phone']
    gender = request.POST['gender']
    place = request.POST['place']
    landmark = request.POST['landmark']

    user.objects.filter(LOGIN=lid).update(name=Name,email=Email,contact_no=Phnumber,gender=gender,place=place,landmark=landmark)
    return JsonResponse({'status': 'ok'})


def user_view_nearby_fuel_provider (request):
    latitude = str(request.POST['lati'])
    longitude = str(request.POST['logi'])

    ###### NEAR-BY code

    gcd_formula = "6371 * acos(least(greatest(cos(radians(%s)) * cos(radians('" + latitude + "')) * cos(radians('" + longitude + "') - radians(%s)) + sin(radians(%s)) * sin(radians('" + latitude + "')), -1), 1))"
    print(gcd_formula)
    distance_raw_sql = RawSQL(
        gcd_formula, (latitude, longitude, latitude)
    )

    data=fuel_provider.objects.filter(LOGIN__usertype='fuel_provider')

    a=[]
    for i in data:
        qs = fuel_provider.objects.filter(id=i.id).annotate(
            distance=RawSQL(gcd_formula, (i.latitude, i.longitude, i.latitude))).order_by('distance')

        a.append({"freid":i.id,
                  "name":i.name,
                  "email":i.email,
                  "contact_no":i.contact_no,
                  "latitude":i.latitude,
                  "longitude":i.longitude,
                  "distance": qs[0].distance
                  })

        #### Distance arranging.........................

    def nearby_sort(e):
        return e['distance']

    a.sort(key=nearby_sort)
    return JsonResponse({'status':'ok','users':a})

def user_book_fuel (request):
    freid=request.POST['freid']
    fname=request.POST['fname']
    date=request.POST['date']
    status=request.POST['status']
    ftype=request.POST['ftype']
    return JsonResponse({'status':'ok'})

def user_view_nearby_mechanic (request):
    latitude = str(request.POST['lati'])
    longitude = str(request.POST['logi'])

    ###### NEAR-BY code

    gcd_formula = "6371 * acos(least(greatest(cos(radians(%s)) * cos(radians('" + latitude + "')) * cos(radians('" + longitude + "') - radians(%s)) + sin(radians(%s)) * sin(radians('" + latitude + "')), -1), 1))"
    print(gcd_formula)
    distance_raw_sql = RawSQL(
        gcd_formula, (latitude, longitude, latitude)
    )

    data = mechanic.objects.filter(LOGIN__usertype='mechanic')

    a = []
    for i in data:
        qs = fuel_provider.objects.filter(id=i.id).annotate(
            distance=RawSQL(gcd_formula, (i.latitude, i.longitude, i.latitude))).order_by('distance')

        a.append({"mechid":i.id,
                  "name": i.name,
                  "email": i.email,
                  "contact_no": i.contact_no,
                  "latitude": i.latitude,
                  "longitude": i.longitude,
                  "distance": qs[0].distance })
    def nearby_sort(e):
        return e['distance']

    a.sort(key=nearby_sort)
    return JsonResponse({'status': 'ok', 'users': a})
def user_view_services (request):
    mid=request.POST['mid']
    data = service_amount.objects.filter(MECHANIC=mid)

    a = []
    for i in data:
        a.append({"sid":i.id,
                  "details": i.Service_Details,
                  "amount": i.amount,
                  })

    return JsonResponse({'status': 'ok', 'users': a})


def user_book_mechanic (request):
    mechid=request.POST['mechid']
    mname=request.POST['mname']
    date=request.POST['date']
    status=request.POST['status']



    return JsonResponse({'status':'ok'})

def user_view_fuel_booking_status (request):
    lid=request.POST['lid']
    data = fuel_provider_request.objects.filter(USER__LOGIN=lid)

    a = []
    for i in data:
        a.append({"freid":i.id,
                  'fid':i.FUEL_PRICE.FUEL_PROVIDER.id,
                  "fname":i.FUEL_PRICE.FUEL_PROVIDER.name,
                  "date":i.Payment_Date,
                  "status":i.status,
                  "ftype":i.FUEL_PRICE.Fuel_type,
                  "amount":i.amount,})
        print(a)

    return JsonResponse({'status':'ok','users': a})

def user_view_mechanic_booking_status (request):
    lid = request.POST['lid']
    data = mechanic_request.objects.filter(USER__LOGIN=lid)

    a = []
    for i in data:
        a.append({"mechid":i.id,
                  'mid':i.MECHANIC.id,
                  "mname":i.MECHANIC.name,
                  "date":i.Payment_Date,
                  "status":i.status,"amount":i.amount})
        print(a)

    return JsonResponse({'status': 'ok', 'users': a})


def user_make_payment (request):
    return JsonResponse({'status':'ok'})

def user_payment_history (request):
    data1=fuel_provider_request.objects.all()

    a = []
    for i in data1:
        a.append({"pdate":i.date,
                  "type":i.FUEL_PRICE.Fuel_type,
                  "details":i.FUEL_PRICE.FUEL_PROVIDER.name,
                  "pamount":i.amount,
                  "pstatus":i.Payment_Status })


    return JsonResponse({'status': 'ok', 'users': a})
def user_network_call_with_fuel_provider (request):
    return JsonResponse({'status':'ok'})

def user_network_call_with_worker (request):
    return JsonResponse({'status':'ok'})

def user_send_feedback (request):
    feedback1=request.POST['feedback']
    lid=request.POST['lid']

    obj = feedback()
    obj.date = datetime.datetime.now()
    obj.feedback = feedback1
    obj.USER = user.objects.get(LOGIN=lid)
    obj.save()

    return JsonResponse({'status':'ok'})

def user_send_complaint(request):
    complaint1=request.POST['complaint']
    lid=request.POST['lid']

    obj = complaint()
    obj.reply = "pending"
    obj.reply_date = "pending"
    obj.complaint = complaint1
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.USER = user.objects.get(LOGIN=lid)
    obj.save()

    return JsonResponse({'status':'ok'})

def user_view_reply (request):
    lid=request.POST['lid']
    data = complaint.objects.filter(USER__LOGIN=lid)

    a = []
    for i in data:
        a.append({"cid":i.id,
        "complaint":i.complaint,
        "cdate":i.date,
        "reply":i.reply,
        "rdate":i.reply_date})

    return JsonResponse({'status': 'ok', 'users': a})


def user_rating (request):
    lid = request.POST['lid']
    rt_log = request.POST['rt_log']
    r = request.POST['rating']
    obj = rating()
    obj.Date = datetime.datetime.now().date()
    obj.Rating = r
    obj.USER = user.objects.get(LOGIN=lid)
    obj.LOGIN = fuel_provider.objects.get(id=rt_log).LOGIN
    obj.save()
    return JsonResponse({'status':'ok'})

def mechaic_rating (request):
    lid = request.POST['lid']
    rt_log = request.POST['rt_log']
    r = request.POST['rating']
    obj = rating()
    obj.Date = datetime.datetime.now().date()
    obj.Rating = r
    obj.USER = user.objects.get(LOGIN=lid)
    obj.LOGIN = mechanic.objects.get(id=rt_log).LOGIN
    obj.save()
    return JsonResponse({'status':'ok'})

def book_mechanic (request):

    # latitude=request.POST["latitude"]
    mech=request.POST["mechid"]
    lid=request.POST["lid"]
    amt=request.POST["amt"]
    obj = mechanic_request()
    obj.status = "pending"
    obj.date = datetime.datetime.now().date()
    obj.amount = amt
    obj.Payment_Date = "pending"
    obj.longitude =11
    obj.latitude = 11
    obj.Payment_Status = "pending"
    obj.MECHANIC_id = mech
    obj.USER = user.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({'status': 'ok'})

def book_fuel_provider (request):
    fprice = request.POST["fprice"]
    fp = request.POST["fid"]
    lid = request.POST["lid"]
    obj = fuel_provider_request()
    obj.status = "pending"
    obj.date = datetime.datetime.now().date()
    obj.Payment_Date = "pending"
    obj.Payment_Status = "pending"
    obj.amount = fprice
    obj.FUEL_PRICE_id= fp
    obj.USER = user.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({'status': 'ok'})



def view_fuelprice (request):
    rt_log=request.POST['rt_log']
    data = fuel_price.objects.filter(FUEL_PROVIDER=rt_log)

    a = []
    for i in data:
        a.append({"fid":i.id,
        "fprice":i.Fuel_Price,
        "ftype":i.Fuel_type,
        "fdensity":i.Fuel_Density,

                  })
    return JsonResponse({'status': 'ok',"users":a})

def online_payment (request):
    fid = request.POST["fid"]
    amount = request.POST["amount"]
    fuel_provider_request.objects.filter(id=fid).update(Payment_Date=datetime.datetime.now(),
                                                                 Payment_Status="Online", amount=amount)
    return JsonResponse({'status': 'ok',})

def online_payment_mech (request):
    mechid = request.POST["mechid"]
    amount = request.POST["amount"]
    mechanic_request.objects.filter(id=mechid).update(Payment_Date=datetime.datetime.now(),
                                                                 Payment_Status="Online", amount=amount)
    return JsonResponse({'status': 'ok',})

def offline_payment (request):
    fid = request.POST["fid"]
    amount = request.POST["amount"]
    fuel_provider_request.objects.filter(id=fid).update(Payment_Date=datetime.datetime.now(),Payment_Status = "Offline",amount = amount)

    return JsonResponse({'status': 'ok',})

def offline_payment_mech (request):
    mechid = request.POST["mechid"]
    amount = request.POST["amount"]
    mechanic_request.objects.filter(id=mechid).update(Payment_Date=datetime.datetime.now(),Payment_Status = "Offline",amount = amount)
    return JsonResponse({'status': 'ok',})


#________________________chat fuelprovoder vs user____________________________________



def chatt(request,u):
    # request.session['head']="CHAT"
    request.session['uid'] = u
    print("GGG  ", u)
    return render(request,'Fuel provider/chat.html',{'u':u})


def chatsnd(request):
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    c = request.session['lid']
    b=request.POST['n']
    print(b)
    m=request.POST['m']
    cc = fuel_provider.objects.get(LOGIN=request.session['lid'])
    uu = user.objects.get(id=request.session['uid'])
    print(uu,"customer_id")
    print("cccccc",cc)
    print("uuuuuuuuuu",uu)
    obj=chat()
    obj.Date=d
    obj.Type='fuelprovider'
    obj.LOGIN_id=request.session['lid']
    obj.USER_id=uu.id
    obj.chat=m
    obj.save()
    print(obj)
    v = {}
    if int(obj) > 0:
        v["status"] = "ok"
    else:
        v["status"] = "error"
    r = JsonResponse.encode(v)
    return r
# else:
#     return redirect('/')

def chatrply(request):
    c = request.session['lid']
    cc=fuel_provider.objects.get(LOGIN_id=c)
    print(cc,"ccccccccccccccccccc")
    uu=user.objects.get(id=request.session['uid'])
    print("uuuuuuu",uu)
    res = chat.objects.filter(LOGIN=request.session['lid'],USER=uu)
    print(res)
    v = []
    if len(res) > 0:
        print(len(res))
        for i in res:
            v.append({
                'type':i.Type,
                'chat':i.chat,
                'name':'user',
                # 'id':i.CUSTOMERS.id,
                # 'upic':i.USER.photo,
                'dtime':i.Date,
                'tname':i.USER.name,
            })
        print(v)
        return JsonResponse({"status": "ok", "data": v})
    else:
        return JsonResponse({"status": "error"})



    #########user_chat######


# --------------------chat with mechanic-------------------------------------------------


def chatt_m(request,u):
    # request.session['head']="CHAT"
    request.session['uid'] = u
    print("GGG  ", u)
    return render(request,'mechanic/chat.html',{'u':u})


def chatsnd_m(request):
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    c = request.session['lid']
    b=request.POST['n']
    print(b)
    m=request.POST['m']
    cc = mechanic.objects.get(LOGIN=request.session['lid'])
    uu = user.objects.get(id=request.session['uid'])
    print(uu,"customer_id")
    print("cccccc",cc)
    print("uuuuuuuuuu",uu)
    obj=chat()
    obj.Date=d
    obj.Type='mechanic'
    obj.LOGIN_id=request.session['lid']
    obj.USER_id=uu.id
    obj.chat=m
    obj.save()
    print(obj)
    v = {}
    if int(obj) > 0:
        v["status"] = "ok"
    else:
        v["status"] = "error"
    r = JsonResponse.encode(v)
    return r
# else:
#     return redirect('/')

def chatrply_m(request):
    c = request.session['lid']
    cc=mechanic.objects.get(LOGIN_id=c)
    print(cc,"ccccccccccccccccccc")
    uu=user.objects.get(id=request.session['uid'])
    print("uuuuuuu",uu)
    res = chat.objects.filter(LOGIN=request.session['lid'],USER=uu)
    print(res)
    v = []
    if len(res) > 0:
        print(len(res))
        for i in res:
            v.append({
                'type':i.Type,
                'chat':i.chat,
                'name':'user',
                # 'id':i.CUSTOMERS.id,
                # 'upic':i.USER.photo,
                'dtime':i.Date,
                'tname':i.USER.name,
            })
        print(v)
        return JsonResponse({"status": "ok", "data": v})
    else:
        return JsonResponse({"status": "error"})










# __________________________________________________________________£
###################fuel chat####################

def fuel_add_chat(request):
    lid = request.POST['lid']
    toid = request.POST['fid']
    message = request.POST['message']
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    t=datetime.datetime.now().strftime("%H:%m:%d")
    expid = fuel_provider.objects.get(id=toid).LOGIN.id
    uid = user.objects.get(LOGIN=lid)
    obj=chat()
    obj.Date=d
    obj.Type='user'
    obj.LOGIN_id= expid
    obj.USER=uid
    obj.chat=message
    obj.save()
    return JsonResponse({'status':"Inserted"})



def fuel_view_chat(request):
    lid = request.POST['lid']
    toid = request.POST['fid']
    flid=fuel_provider.objects.get(id=toid).LOGIN
    lastid = request.POST['lastid']
    print(lid,toid,lastid)
    # res=chat.objects.filter(userid=user.objects.get(login=lid))
    res=chat.objects.filter(Q(USER=user.objects.get(LOGIN=lid)),Q(id__gt=lastid),Q(LOGIN=flid))
    print(res)
    ar=[]
    for i in res:
        ar.append({
            "id":i.id,
            "date":i.Date,
            "userid":i.USER.id,
            "sid":i.Type,
            "chat":i.chat,
        })
    print(ar,"arrrrrrrrrrr")
    return JsonResponse({'status':"ok",'data':ar})



def mech_add_chat(request):
    lid = request.POST['lid']
    toid = request.POST['mid']
    message = request.POST['message']
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    t=datetime.datetime.now().strftime("%H:%m:%d")
    expid = mechanic.objects.get(id=toid).LOGIN.id
    uid = user.objects.get(LOGIN=lid)
    obj=chat()
    obj.Date=d
    obj.Type='user'
    obj.LOGIN_id= expid
    obj.USER=uid
    obj.chat=message
    obj.save()
    return JsonResponse({'status':"Inserted"})



def mech_view_chat(request):
    lid = request.POST['lid']
    toid = request.POST['mid']
    mlid=mechanic.objects.get(id=toid).LOGIN
    lastid = request.POST['lastid']
    print(lid,toid,lastid)
    # res=chat.objects.filter(userid=user.objects.get(login=lid))
    res=chat.objects.filter(Q(USER=user.objects.get(LOGIN=lid)),Q(id__gt=lastid),Q(LOGIN=mlid))
    print(res)
    ar=[]
    for i in res:
        ar.append({
            "id":i.id,
            "date":i.Date,
            "userid":i.USER.id,
            "sid":i.Type,
            "chat":i.chat,
        })
    print(ar,"arrrrrrrrrrr")
    return JsonResponse({'status':"ok",'data':ar})


def update_location(request):
    return JsonResponse({'status': 'ok',})
