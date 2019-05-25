#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'HP Chang'
SITENAME = u'HP Chang'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'en'

CSS_FILE = 'main-6.css'
#Profile information
NAME = 'HP Chang 張惠普'
TAGLINE = 'Happy hacking!'
PIC = 'hp_profile.png'
FAVICON = '/theme/images/favicon.jpg'

#sidebar links
EMAIL = 'contact@hpchang.com'
#PHONE = 'N/C'
WEBSITE = 'blog.hpchang.com'
INSTAGRAM='taiwan.go'
LINKEDIN = 'hpchang'
GITHUB = 'hpchang'
TWITTER = '@hpc_techbar'
FACEBOOK = 'hpchangconsole'

CAREER_SUMMARY = 'Over a decade\'s experience in firmware development and its mobile applications of human interface. Constructed 1st touch and display driver integration (TDDI) solution and prototyped smallest optical image stabilization (O.I.S) camera for smartphone. Proven track record of superior on-site ODM support over 30% of the DSC market, shipping into almost every camera brand.'

SKILLS = [
	{
		'title': 'Embedded RTOS',
   		'level': '90'
   	},
  	{
  		'title': 'C/C++, python, Matlab',
   		'level': '95'
   	},
    {
  		'title': 'Touch screen algorithm',
  		'level': '95'
  	},
  	{
  		'title': 'Peripheral driver, HW/AFE',
  		'level': '90'
  	},
  	{
  		'title': 'GNU gcc, make',
  		'level': '85'
  	},
  	{
  		'title': 'Chip bring up & Automated CI regression',
  		'level': '85'
  	}
]

# PROJECT_INTRO = 'You can list your side projects or open source libraries in this section. '

PROJECTS = [
	{
		'title': 'Synaptics Awards 2017',
		'tagline': '"Exhilarating and Rewarding Environment" for achievement for initial release to MP of tire-one OEM with A0 silicon.'
	},
	{
		'title': 'Synaptics Awards 2016',
		'tagline': '"Innovation to Win" for overcoming a tremendous deal of challenges throughout silicon development w/ new fabrication.'
	},
	{
		'title': 'US Patents',
		'tagline': '<a href="https://www.google.com/patents/US20130054155" target="_blank" title="Digital programmable load measurement device (2011)">Digital programmable load measurement device (2011)</a>'
	},
	{
		'title': 'Thesis',
		'tagline': '<a href="https://goo.gl/5DQAuA" target="_blank" title="A new on-line battery state-of-charge estimation and monitoring system (2007)">A new on-line battery state-of-charge estimation and monitoring system (2007)</a>'
	},
]

LANGUAGES = [
	{
		'name': 'Mandarin',
		'description': 'Native'
	},
	{
		'name': 'English',
		'description': 'Professional'
	}
]

INTERESTS = [
	'Reading',
	'Running',
	'Travel'
]

EXPERIENCES = [
	{
		'job_title': 'Team Lead <sub>for industrial AI inspection solutions</sub>',
		'time': 'Jul 2018 - Present',
                'company': '開必拓數據 Kapito Inc, Taiwan',
		'details': "Provided fast and stable AI inspection solution<br>" 
	},
        {

		'job_title': 'Sr. Firmware Engineer <sub>for Touch&Display driver integration(TDDI)</sub>',
		'time': 'May 2014 - Jun 2018',
		'company': 'Synaptics, Taiwan',
		'details': "Worked on developing TDDI from 0 to 100Mu shipments in 3yrs with exceptional cross-geography teamwork<br>" 
		           "&minus; Led 1st TDDI XL display ASIC to MP with A0 silicon for 9 customers.<br>" 
				   "&minus; Led 1st TDDI Gen2 ASIC to MP, 3 months ahead of original target.<br>"
				   "&minus; Constructed TDDI Gen1 for world's first TDDI single-chip solution.<br>"
                   "&minus; Implemented an auto-notify FW build validation of continuous integration(CI). Focused on cloud-based automated regression testing"
	},
	{
		'job_title': 'Firmware Engineer <sub>for digital still camera soc</sub>',
		'time': 'Nov 2010 - Mar 2014',
		'company': 'CSR Plc. (via acquisition of Zoran Corporation), Taiwan',
		'details': 
		           "Led and supported in 10+ ODM projects from design-in to massproduction, accounting for millions of shipped cameras. And brought up SOCs drivers (CMOS sensor, LCD, Audio Codec...) connecting through common interface (LVDS, I2C, SPI, UART...) and debugging and developing features in image signal processing pipeline&software flow.<br>"
	},
	{
		'job_title': 'Control System Leader <sub>for mobile phoen camera actuator</sub>',
		'time': 'Feb 2009 - Nov 2010',
		'company': 'TDK Corporation, Taiwan',
		'details': "In one year, built the smallest 2-axes anti-shake O.I.S system for mobile phone camera in collaboration with Japanese engineering colleagues, and implemented camera module system with H.264 video recording in WinCE platform."
	}
]

EDUCATIONS = [
	{
		'degree': 'M.S. Opto-Mechatronics Engineering',
		'meta': 'National Central University',
		'time': '2005 - 2007'
	},
	{
		'degree': 'B.S. Mechanical Engineering',
		'meta': 'National Central University',
		'time': '2001 - 2004'
	}
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = "./pelican-themes/resume_hp"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
