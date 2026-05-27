import zmq
import duckdb
import pandas as pd
pd.set_option('display.max_columns', None)
import csv
import time
#setup ZMQ

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:49155")

def getProjects(field, criteria):

    #read data from request and pull info from DB table
    query = f"""
            SELECT *
            FROM read_csv('CData.csv')
            WHERE "{field}" = '{criteria}'
        """
    result_df = duckdb.query(query).df()
    #Save related data to replyData in JSON format so it can be sent
    replyData = result_df.to_json(orient='records')
    #Send Reply to Requester
    socket.send_json(replyData)
def pushUpdates(proj, criteria, targetColumn, newData):
    #get all results from file
    with open('CData.csv', mode="r", encoding="utf-8-sig", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        newFile = []
        for row in reader:
            # find your match and insert your update
            if row[proj] == criteria:
                row[targetColumn] = newData
            newFile.append(row)
    print(newFile)
    # write back to CSV
    with open('CData.csv', mode="w", encoding="utf-8-sig", newline='') as csvfile:
        writer=csv.DictWriter(csvfile, fieldnames=newFile[0].keys())
        writer.writeheader()
        writer.writerows(newFile)
def loadState():
    df=pd.read_csv('CData.csv')
    replyData = df.to_json(orient='records')
    socket.send_json(replyData)

#Listen and reply to request
while True:
    requestData=socket.recv_json()

    #Read data from JSON sent from request file

    if requestData["Action"]=="getProjects":
        getProjects(requestData["Criteria Column"], requestData["Criteria"])
    if requestData["Action"]=="pushUpdates":
        pushUpdates(requestData["Criteria Column"], requestData["Criteria"], requestData["Data Column"], requestData["New Data"])
    if requestData["Action"]=="loadState":
        loadState()
    time.sleep(1)
