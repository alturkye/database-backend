# Database Backend Microservice

## Description
This services serves as a lasting memory for applications. 
Data, save states and updates can be written and read from a file

## Communication
### Requesting Data
#### This is an example of pushing an update
testPackage={"Action": "pushUpdates", "Criteria Column": "ProjID", "Criteria": "2","Data Column": "Scope", "New Data": "More updates? YES"}
socket.send_json(testPackage)

#### This is an example of getting a row based on criteria
#testPackage={"Action": "getProjects", "Criteria Column": "Project Name", "Criteria": "Paint Doors"}
socket.send_json(testPackage)

#### This is an example of asking for data from loadstate
testPackage={"Action": "loadState"}
socket.send_json(testPackage)

### Receive Data
requestData=socket.recv_json()
**pushUpdates does not generate any data response**

### UML Diagram

![img.png](img.png)


