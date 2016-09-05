import jenkinsapi
from jenkinsapi.jenkins import Jenkins
jenkins_server_url='http://localhost:8080'
user_id='xjiang-ext'
api_token='ddceca17aee7b0af56249c8160c02781'
job_name='Test11'
server=Jenkins(jenkins_server_url, username=user_id, password=api_token)
job = server[job_name]
lgb = job.get_last_good_build()
print lgb.get_revision()


