#coding:utf-8
import jenkins

jenkins_server_url='http://10.0.2.2:8080'
user_id='xjiang-ext'
api_token='ddceca17aee7b0af56249c8160c02781'
job_name='test112'
build_number=2
server=jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
#info=server.get_job_info(job_name)
#dif=server.get_build_info(job_name,build_number)['building']
#print dif
#user=server.get_whoami()
#version=server.get_version()
#print 'hello %s from jenkins %s' %(user['fullname'],version)
#server.create_job('empty', jenkins.EMPTY_CONFIG_XML)
#jobs = server.get_jobs()
#print jobs
#server.build_job('empty')
#server.disable_job('empty')
#server.copy_job('test112', 'empty_copy')
#server.enable_job('empty')
#server.reconfig_job('empty_copy', jenkins.RECONFIG_XML)
#server.delete_job('test1123')
server.delete_job('empty_copy')

