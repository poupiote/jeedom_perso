#!/usr/bin/env python2
from hermes_python.hermes import Hermes
from datetime import datetime
from pytz import timezone
import request

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

    jeedomAPIKEY = conf["secret"].get("jeedomAPIKEY")
    #jeedomAPIKEY = self.config.get("secret").get("jeedomAPIKEY")
    jeedomIP = conf["secret"].get("jeedomIP")    
    #jeedomIP = self.config.get("secret").get("jeedomIP")   

def intent_received(hermes, intent_message):

	print()
	print(intent_message.intent.intent_name)
	print ()

	if intent_message.intent.intent_name == 'voleurdespace:salonON':       
    # action code goes here...
    print '[Received] intent: {}'.format(intentMessage.intent.intent_name)
    jeedomInteraction = 'allume la lumière du salon'
    requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
		
		sentence = 'le salon est allumé '
		print(intent_message.intent.intent_name)

		#now = datetime.now(timezone('Europe/Paris'))

		#sentence += verbalise_hour(now.hour) + " " + verbalise_minute(now.minute)
		print(sentence)

		hermes.publish_end_session(intent_message.session_id, sentence)

	elif intent_message.intent.intent_name == 'voleurdespace:salonOFF':
	      jeedomInteraction = 'éteind la lumière du salon'
              requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
		sentence = 'le salon est éteind '
		print(intent_message.intent.intent_name)
		print(sentence)
		hermes.publish_end_session(intent_message.session_id, sentence)
	
	elif intent_message.intent.intent_name == 'voleurdespace:séjourON':
	      jeedomInteraction = 'allume la lumière du séjour'
              requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
		sentence = 'le séjour est alumé '
		print(intent_message.intent.intent_name)
		print(sentence)
		hermes.publish_end_session(intent_message.session_id, sentence)
		
	elif intent_message.intent.intent_name == 'voleurdespace:séjourON':
	      jeedomInteraction = 'éteind la lumière du séjour'
              requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
		sentence = 'le séjour est alumé '
		print(intent_message.intent.intent_name)
		print(sentence)
		hermes.publish_end_session(intent_message.session_id, sentence)
		
		#hermes.publish_end_session(intent_message.session_id, "De rien!")


		
		
		
		
with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
