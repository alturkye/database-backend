import zmq
import time


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:49155")

#this is an example of pushing an update
#testPackage={"Action": "pushUpdates", "Criteria Column": "ProjID", "Criteria": "2","Data Column": "Scope", "New Data": "More updates? YES"}

#this is an example of getting a row based on criteria
#testPackage={"Action": "getProjects", "Criteria Column": "Project Name", "Criteria": "Paint Doors"}

#this is an example of loadstate
testPackage={"Action": "loadState"}

socket.send_json(testPackage)

requestData=socket.recv_json()
print(requestData)