from weakref import ref
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
#sertificado del proyecto 
firebase_sdk=credentials.Certificate('lincebot-163ba-firebase-adminsdk-uiq38-7b11b084d2.json')
#referencia a la base de datos en tiempo real 
firebase_admin.initialize_app(firebase_sdk,{'databaseURL':'https://lincebot-163ba-default-rtdb.firebaseio.com/'})

#enviar datos 
ref=db.reference('/mensajes')
ref.push(
    {
        'id':'1',
        'mensaje':'Hola a todos!'
    }
)
