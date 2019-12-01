import email, imaplib
import datetime 
import nest
import pyhdb
import pwd
import sys
from symbol import break_stmt
from twilio.rest import Client
from asn1crypto._ffi import null


detach_dir = "/Users/anirudhya/eclipse-pythonworkspace/emails/"
user = raw_input("Enter your gmail username")
pwd = raw_input("Enter Your gmail password")

print user + " " + pwd
cntr= 0
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user, pwd)

print m.list()

m.select("INBOX")
resp, items = m.search(None,'FROM','"dublingeniuskids@gmail.com"')
items = items[0].split()

print items

for emailid in items[::-1]:

    resp, data = m.fetch(emailid, "(RFC822)")

 #   if ( break_stmt ):
  #      break

    for response_part in data:

      if isinstance(response_part, tuple):
          msg = email.message_from_string(response_part[1])
          varSubject = 'Subject Arnie ' + msg['subject']
          varDate = msg['date']
          vartestDate = varDate[:-15]
          
          
          if len(vartestDate) > 11:
              vartestDate = vartestDate[5:] 
          
          vartestdate2 = datetime.datetime.strptime(vartestDate, '%d %b %Y')
          
          
          if vartestdate2 > datetime.datetime.strptime('01-01-2018', '%d-%m-%Y'):
             print varSubject
             print varDate
             cntr = cntr + 1  
             print 'Message Counter :' + str(cntr)
            
# Your Account SID from twilio.com/console
account_sid = "AC56f4117ebdd7ac08ff32ff0efb2b218e"
# Your Auth Token from twilio.com/console
auth_token  = "0085a4b97445bf84ce3278b65d650424"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19255487541", 
    from_="+19254063299",
    body="You have " + str(cntr) + " new message from Genius Kids" )

print(message.sid)        

# trying to connect to nest

client_id2 = '47f7be69-adb1-411f-8c12-62f43efa6cbf'
client_secret2 = '3wOGWABdWlifJ5X1EKxM9w0St'
access_token_cache_file2 = 'nest.json'

napi = nest.Nest(client_id=client_id2, client_secret=client_secret2, access_token_cache_file=access_token_cache_file2)

print "napi authorization code: " + str(napi.authorization_required)

#napi.authorization_required='"True"'

if napi.authorization_required:
    print('Go to ' + napi.authorize_url + ' to authorize, then enter PIN below')
    if sys.version_info[0] < 3:
        pin = raw_input("PIN: ")
    else:
        pin = input("PIN: ")
    napi.request_token(pin)

for structure in napi.structures:
    print ('Structure %s' % structure.name)
    print ('    Away: %s' % structure.away)
    print ('       num thermostats %s' % structure.num_thermostats)
    print ('        Long Name %s' % structure.country_code)
  

#this gets the device name and device temperature 
for device in structure.thermostats:
        print ('        Device: %s' % device.name_long)
        print ('            Temp: %0.1f' % device.temperature) 
        print (' HVAC State %s' % device.hvac_state)
        print('HAVC mode %s' % device.mode)
        #trying to set the devices on 
        #device.mode = 'heat' 
        #device.target_temperature_f= 75
       
        
        if device.temperature > 72 : 
           message3 = client.messages.create(
               to="+19255487541", 
               from_="+19254063299",
               body="Consider turning on ac"+ device.name +" Your current temperature is"  + str(device.temperature) +" Device Mode :"+ device.mode ) 
           if device.mode !='cool' : 
               device.mode = 'cool' 
               device.target_temperature_f= 65
               message3 = client.messages.create(
                   to="+19255487541", 
                   from_="+19254063299",
                   body="I have turned on AC for " + device.name +" and set Target Temperature to"  + str(device.target_temperature_f) ) 
               
        elif device.temperature < 68:        
        
            message3 = client.messages.create(
               to="+19255487541", 
               from_="+19254063299",
               body="Consider turning on heating on "+ device.name +"  Your current temperature is"  + str(device.temperature) +" Device Mode :"+ device.mode ) 
            if device.mode !='heat': 
               device.mode = 'heat' 
               device.target_temperature_f= 72
               message3 = client.messages.create(
                   to="+19255487541", 
                   from_="+19254063299",
                   body="I have turned on heating for " + device.name +" and set Target Temperature to"  + str(device.target_temperature_f) )        
        
        else :
            message3 = client.messages.create(
                to="+19255487541", 
                from_="+19254063299",
                body="Your "+ device.name+"  temperature is " + str(device.temperature)+" Device Mode :"+ device.mode + ". No action is being taken") 
#this sends the text message to me 

#SAP Cloud platform details 
#password Welcome123Welcome123







