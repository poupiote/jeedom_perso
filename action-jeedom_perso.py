#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import ConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology.dialogue import *
from hermes_python.ontology.slot import *
import io

import datetime
import pytz
import json

import requests

jeedomIP=None
jeedomAPIKEY=None
jeedomInteraction = ''

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

#jeedomAPIKEY = conf["secret"].get("jeedom_API_KEY")
#jeedomAPIKEY = self.config.get("secret").get("jeedom_API_KEY")
#jeedomIP = conf["secret"].get("jeedom_IP")    
#jeedomIP = self.config.get("secret").get("jeedom_IP")   

def intent_received(hermes, intent_message):

    print()
    print(intent_message.intent.intent_name)
    print ()
    # action code goes here...
    jeedomAPIKEY = conf["secret"].get("jeedom_API_KEY")
    jeedomIP = conf["secret"].get("jeedom_IP")
    if intent_message.intent.intent_name == 'voleurdespace:salonON':
       print(intent_message.intent.intent_name)
       sentence = 'le salon est allumer '
       print(sentence)
       hermes.publish_end_session(intent_message.session_id, sentence)
       jeedomInteraction = 'allume la lumière du salon'
       requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)

    elif intent_message.intent.intent_name == 'voleurdespace:salonOFF':
	print(intent_message.intent.intent_name)
	sentence = 'le salon est aitin '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'éteind la lumière du salon'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
	
    elif intent_message.intent.intent_name == 'voleurdespace:sejourON':
	print(intent_message.intent.intent_name)
	sentence = 'le saijour est allumer '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'allume la lumière du séjour'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
	
    elif intent_message.intent.intent_name == 'voleurdespace:sejourOFF':
	print(intent_message.intent.intent_name)
	sentence = 'le saijour est aitin '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'éteind la lumière du séjour'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
	
    elif intent_message.intent.intent_name == 'voleurdespace:lampadaireON':
	print(intent_message.intent.intent_name)
	sentence = 'le lampadaire est allumer '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'allume le lampadaire du séjour'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
	
    elif intent_message.intent.intent_name == 'voleurdespace:lampadaireOFF':
	print(intent_message.intent.intent_name)
	sentence = 'le lampadaire est aitin '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'éteind le lampadaire du séjour'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
	
    elif intent_message.intent.intent_name == 'voleurdespace:garageON':
	print(intent_message.intent.intent_name)
	sentence = 'le garage est allumer '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'allume la lumière du garage'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
	
    elif intent_message.intent.intent_name == 'voleurdespace:garageOFF':
	print(intent_message.intent.intent_name)
	sentence = 'le garage est aitin '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'éteind la lumière du garage'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
	
    elif intent_message.intent.intent_name == 'voleurdespace:portailOUV':
	print(intent_message.intent.intent_name)
	sentence = 'le portail est ouvert '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'ouvre le portail'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
	
    elif intent_message.intent.intent_name == 'voleurdespace:portailFER':
	print(intent_message.intent.intent_name)
	sentence = 'le portail est fermai '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'tu peux fermer le portail'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
	
    elif intent_message.intent.intent_name == 'voleurdespace:exterON':
	print(intent_message.intent.intent_name)
	sentence = 'les lumiaires extairieur sont allumai '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'allume extèrieur'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
	
    elif intent_message.intent.intent_name == 'voleurdespace:exterOFF':
	print(intent_message.intent.intent_name)
	sentence = 'les lumiaires extairieur sont aitinte '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'éteind extèrieur'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
	
    elif intent_message.intent.intent_name == 'voleurdespace:voletsalonOUV':
	print(intent_message.intent.intent_name)
	sentence = 'le volet roulant du salon est ouvert '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'ouvre salon'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
	
    elif intent_message.intent.intent_name == 'voleurdespace:voletsalonFER':
	print(intent_message.intent.intent_name)
	sentence = 'le volet roulant du salon est fermer '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'ferme salon'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
		
    elif intent_message.intent.intent_name == 'voleurdespace:voletsejourOUV':
	print(intent_message.intent.intent_name)
	sentence = 'le volet roulant du saijour est ouvert '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'ouvre séjour'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
	
    elif intent_message.intent.intent_name == 'voleurdespace:voletsejourFER':
	print(intent_message.intent.intent_name)
	sentence = 'le volet roulant du saijour est fermer '
	print(sentence)
	hermes.publish_end_session(intent_message.session_id, sentence)
	jeedomInteraction = 'ferme séjour'
	requests.get('http://'+jeedomIP+'/core/api/jeeApi.php?apikey='+jeedomAPIKEY+'&type=interact&query='+jeedomInteraction)
		
		
		
with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
