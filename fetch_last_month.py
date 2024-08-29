import datetime
from pymisp import PyMISP, MISPEvent, MISPAttribute
import urllib3
import pprint


# Désactiver les avertissements SSL non sécurisés (facultatif)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Remplacez ces variables par vos informations MISP
misp_url = ''
misp_key = ''
verifycert = False  # False si vous avez des problèmes avec le certificat SSL

# Initialiser la connexion à MISP
misp = PyMISP(misp_url, misp_key, verifycert)

# Calculer la date il y a un mois
one_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)

# Chercher des événements récents
events = misp.search(date_from=one_month_ago.strftime('%Y-%m-%d'))

# Récupérer les URLs des attributs récents
urls = []

print("Event in the time frame")
# Récupère la value si c'est des URL
for event in events:
    single_event = event['Event']
    print(single_event['id'])
    for attribute in single_event['Attribute']:
        if attribute['type'] == 'domain':
            urls.append(attribute['value'])
    if single_event['id'] == 1:
            print("Example of an event")
            pprint.pprint(sigle_event)



print(40*"-")

# Afficher les URLs au final
for url in urls:
    print(url)

