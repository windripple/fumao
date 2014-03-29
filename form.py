# -*- coding: utf-8 -*-  
import os
from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.ext import ndb
from datetime import datetime, timedelta
import jinja2
import webapp2
import uuid
import urllib
import urllib2



JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


    



class MainPage(webapp2.RequestHandler):
    
    def get(self):
    
    
    

        template_values = {
          
           
           
           
        }

        template = JINJA_ENVIRONMENT.get_template('fumao.html')
        self.response.write(template.render(template_values)) 
        
    


       
     
application = webapp2.WSGIApplication([
    ('/', MainPage),
   


    
], debug=True)