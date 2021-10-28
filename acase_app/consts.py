import os

target = [
    {
        'name': 'mercer',
        'url': 'https://www.latam.mercer.com/',
        'keywords': ['liderazgo', 'seguridad', 'recursos humanos', 'innovación', 'transformación digital']
    },
    {
        'name': 'gartner',
        'url': 'https://www.gartner.es/es',
        'keywords': ['liderazgo', 'seguridad', 'recursos humanos', 'innovación', 'transformación digital'],
    },
    {
        'name': 'deloitte',
        'url':'https://www2.deloitte.com/co/es/pages/audit/topics/biblioteca-tecnica.html?icid=nav2_biblioteca-tecnica',
        'keywords': ['liderazgo', 'seguridad', 'recursos humanos', 'innovación', 'transformación digital'],
    },
    # {
        # 'name': 'weforum',
        # 'url': 'https://www.weforum.org/',
        # 'keywords': []
    # },
    # {
        # 'name': 'mckinsey',
        # 'url': 'https://www.mckinsey.com/',
        # 'keywords': []
    # },
    # {
        # 'name': 'bcg',
        # 'url': 'https://www.bcg.com/en-co/',
        # 'keywords': []
    # },
    # {
        # 'name': 'manpower',
        # 'url': 'https://manpowergroupcolombia.co/',
        # 'keywords': []
    # },
    # {
        # 'name': 'wired',
        # 'url': 'https://www.wired.com/',
        # 'keywords': []
    # },
    # {
        # 'name': 'hrt',
        # 'url': 'https://www.humanresourcestoday.com/',
        # 'keywords': []
    # },
    # {
        # 'name': 'thehrdirector',
        # 'url': 'https://www.thehrdirector.com/business-news/',
        # 'keywords': []
    # }
]

months_format = ['january', 'february', 'march', 'april', 'may', 'june',
                 'july', 'august', 'september', 'october', 'november', 'december',
                 'jan', 'feb', 'mar', 'apr', 'jun', 'jul', 'aug', 'sep', 'sept',
                 'oct', 'nov', 'dec', 'enero', 'febrero', 'abril', 'marzo', 'mayo',
                 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre',
                 'diciembre']

text_formatting_html_elements = ['b', 'em', 'i', 'small', 'strong', 'small',
                            'sub', 'sup', 'ins', 'mark']

# after parsing the next variable must be iqual to a route/path
# for instance, :/users/home/acase/selenium_drivers
driver_dir = ':' + '/'.join(os.getcwd().split('/')[:-1]) + '/ACASE_Crawler-Scraper/selenium_drivers'
