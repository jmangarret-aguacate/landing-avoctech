from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)

# --- Configuración de Internacionalización (i18n) ---
LANGUAGES = {
    'es': 'Español',
    'en': 'English'
}
app.config['LANGUAGES'] = LANGUAGES
app.config['BABEL_DEFAULT_LOCALE'] = 'es'

# Define la función para seleccionar el idioma PRIMERO
def get_locale():
    # Intenta obtener el idioma de la URL, si no, usa el default
    if g.get('locale') and g.locale in LANGUAGES:
        return g.locale
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

# Pasa la función directamente al inicializar Babel
babel = Babel(app, locale_selector=get_locale)

# Diccionario de traducciones
texts = {
    'es': {
        'nav_inicio': 'Inicio',
        'nav_servicios': 'Servicios',
        'nav_contacto': 'Contacto',
        'hero_titulo': 'Soluciones Tecnológicas para Impulsar tu Negocio',
        'hero_subtitulo': 'Innovación, eficiencia y seguridad para la era digital.',
        'hero_boton': 'Contáctanos',
        'servicios_titulo': 'Nuestros Servicios',
        'servicios_subtitulo': 'Soluciones a la medida de tus necesidades.',
        's1_titulo': 'Soporte TI Integral',
        's1_desc': 'Administración de sistemas, ciberseguridad proactiva y soporte técnico especializado para mantener tu operación sin interrupciones.',
        's2_titulo': 'Infraestructura Cloud con AWS',
        's2_desc': 'Diseñamos, desplegamos y gestionamos soluciones escalables y costo-eficientes en la nube de Amazon Web Services.',
        's3_titulo': 'Desarrollo de API Rest a Medida',
        's3_desc': 'Creamos APIs robustas, seguras y bien documentadas para conectar tus aplicaciones y optimizar procesos.',
        'contacto_titulo': 'Contacto',
        'contacto_subtitulo': '¿Listo para empezar? Envíanos un mensaje.',
        'form_nombre': 'Nombre completo',
        'form_empresa': 'Nombre de la Empresa',
        'form_email': 'Correo electrónico',
        'form_telefono': 'Número de teléfono (Opcional)',
        'form_mensaje': 'Mensaje',
        'form_boton': 'Enviar Mensaje',
        'footer_derechos': 'Todos los derechos reservados.',
        'form_success': '¡Mensaje recibido, gracias por contactarnos!'
    },
    'en': {
        'nav_inicio': 'Home',
        'nav_servicios': 'Services',
        'nav_contacto': 'Contact',
        'hero_titulo': 'Technological Solutions to Boost Your Business',
        'hero_subtitulo': 'Innovation, efficiency, and security for the digital age.',
        'hero_boton': 'Contact Us',
        'servicios_titulo': 'Our Services',
        'servicios_subtitulo': 'Solutions tailored to your needs.',
        's1_titulo': 'Comprehensive IT Support',
        's1_desc': 'Systems administration, proactive cybersecurity, and specialized technical support to keep your operation running smoothly.',
        's2_titulo': 'Cloud Infrastructure with AWS',
        's2_desc': 'We design, deploy, and manage scalable and cost-effective solutions on the Amazon Web Services cloud.',
        's3_titulo': 'Custom Rest API Development',
        's3_desc': 'We create robust, secure, and well-documented APIs to connect your applications and optimize processes.',
        'contacto_titulo': 'Contact',
        'contacto_subtitulo': 'Ready to get started? Send us a message.',
        'form_nombre': 'Full name',
        'form_empresa': 'Company Name',
        'form_email': 'Email address',
        'form_telefono': 'Phone number (Optional)',
        'form_mensaje': 'Message',
        'form_boton': 'Send Message',
        'footer_derechos': 'All rights reserved.',
        'form_success': 'Message received, thank you for contacting us!'
    }
}

@app.context_processor
def inject_conf_var():
    # Inyecta variables en todos los templates
    return dict(LANGUAGES=app.config['LANGUAGES'])

@app.route('/')
@app.route('/<lang>')
def index(lang='es'):
    if lang not in LANGUAGES:
        lang = 'es'
    g.locale = lang
    return render_template('index.html', texts=texts[lang], current_lang=lang)

@app.route('/contact', methods=['POST'])
def contact():
    lang = g.get('locale', 'es')
    if request.method == 'POST':
        name = request.form.get('name')
        company = request.form.get('company')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        print("--- Nuevo mensaje de contacto ---")
        print(f"Nombre: {name}")
        print(f"Empresa: {company}")
        print(f"Email: {email}")
        print(f"Teléfono: {phone}")
        print(f"Mensaje: {message}")
        
        return texts[lang]['form_success']

if __name__ == '__main__':
    app.run(debug=True)