import sys #allows us to access the traceback
import logging

def error_handling():
    return "{}. {}, line: {}".format(sys.exc_info()[0],
                                           sys.exc_info()[2],
                                           sys.exc_info()[2].tb_lineno)

try:
    a+b
except Exception as e:
    logging.error(error_handling())
    #dont assign them to variables because exceptions within them will be bad
##    print sys.exc_info()[0] #type
##    print sys.exc_info()[1] #name
##    print sys.exc_info()[2].tb_lineno #traceback
    
    


