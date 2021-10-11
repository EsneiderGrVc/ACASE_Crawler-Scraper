import os

target = {
    'mercer': 'https://www.latam.mercer.com/',
    'gartner': 'https://www.gartner.es/es',
    'deloitte': 'https://www2.deloitte.com/co/es/pages/audit/topics/biblioteca-tecnica.html?icid=nav2_biblioteca-tecnica',
    'weforum': 'https://www.weforum.org/',
    'mckinsey': 'https://www.mckinsey.com/',
    'bcg': 'https://www.bcg.com/en-co/',
    'manpower': 'https://manpowergroupcolombia.co/',
    'wired': 'https://www.wired.com/',
    'hrt': 'https://www.humanresourcestoday.com/',
    'thehrdirector': 'https://www.thehrdirector.com/business-news/'
}

# after parsing the next variable must be iqual to a route/path
# for instance, :/users/home/acase/selenium_drivers
driver_dir = ':' + '/'.join(os.getcwd().split('/')[:-1]) + '/acase/selenium_drivers'
