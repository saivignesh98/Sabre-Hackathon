from django.shortcuts import render
import requests 
import speech_recognition as sr

def button(request):
	return render(request, 'WelcomePage.html')

def output(request):
    r=sr.Recognizer()
    text = ""
    with sr.Microphone() as source :
		#audio = r.adjust_for_ambient_noise(source)
        print("Speak now")
        audio=r.listen(source,timeout=3,phrase_time_limit=2)
        print("done")
        try :
            print(audio)
            text=r.recognize_google(audio)
            print("Simon says : {}.".format(text))
        except Exception as e :
        	print("bsdk", e)
    print(text)
    print(len(text))
    if text.strip() == "yes":
        return render(request, 'TellYourName.html')
    return render(request, 'home.html')
	
def saveName(request):
    r=sr.Recognizer()
    text = ""
    with sr.Microphone() as source :
		#audio = r.adjust_for_ambient_noise(source)
        print("Speak now")
        audio=r.listen(source,timeout=3,phrase_time_limit=2)
        print("done")
        try :
            print(audio)
            text=r.recognize_google(audio)
            print("Simon says : {}.".format(text))
        except Exception as e :
        	print("bsdk", e)
    print(text)
    print(len(text))
    file2write=open("name.txt",'w')
    file2write.write(text.strip())
    file2write.close()
    return render(request, 'days.html', {'name': text.strip()})

def normal(request):
    print("hey")
    return render(request, 'NormalDate.html')

def roombook(request):
    print("xxx")
    return render(request, 'NormalRoomBooking.html')
	
def name(request):
    return render(request, 'TellYourName.html')

def days(request):
    r=sr.Recognizer()
    text = ""
    with sr.Microphone() as source :
		#audio = r.adjust_for_ambient_noise(source)
        print("Speak now")
        audio=r.listen(source,timeout=3,phrase_time_limit=2)
        print("done")
        try :
            print(audio)
            text=r.recognize_google(audio)
            print("Simon says : {}.".format(text))
        except Exception as e :
        	print("bsdk", e)
    print(text)
    print(len(text))
    file2write=open("days.txt",'w')
    file2write.write(text.strip())
    file2write.close()
    return render(request, 'rooms.html')

def selectroom(request):
    r=sr.Recognizer()
    text = ""
    with sr.Microphone() as source :
        print("Speak now")
        audio=r.listen(source,timeout=3,phrase_time_limit=2)
        print("done")
        try :
            print(audio)
            text=r.recognize_google(audio)
            print("Simon says : {}.".format(text))
        except Exception as e :
        	print("bsdk", e)
    print(text)
    print(len(text))
    file2write=open("room.txt",'w')
    file2write.write(text.strip())
    file2write.close()
    return render(request, 'demos/basic.html')
	
def payment(request):
    return render(request, 'NormalPayment.html')
	
def confirm(request):
    return render(request, 'NormalConfirmation.html')
	
def identity(request):
    return render(request, 'identity.html')
'''data= requests.get("https://www.google.com")

print(data.text)
data=data.text
return render(request, 'home.html',{'data':data})'''
	


