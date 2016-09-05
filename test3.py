import jenkins
jenkins_server_url='localhost:8080'
user_id='xjiang-ext'
api_token='ddceca17aee7b0af56249c8160c02781'
server=jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
server.build_job(job_name)
server.build_job(Test11, parameters=param_dict)
server.get_job_info(Test11)
server.get_job_info(Test11)['lastBuild']['1']

