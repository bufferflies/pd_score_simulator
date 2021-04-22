import requests
import json

class Prometheus:
    host=""
    port=""
    path=""
    start=''
    end=''
    
    def __init__(self,host,start,end,port="3000"):
        self.host=host
        self.port=port
        self.path="api/v1/query_range"
        self.start=start
        self.end=end

    def GetRecords(self,promql,step="15s"):
        url="http://{}:{}/{}".format(self.host,self.port,self.path) 
        query="query={}&start={}&end={}&step={}".format(promql,self.start,self.end,step)
        rsp=requests.get(url,query)
        data=json.loads(rsp.text)
        if rsp.status_code !=200:
            return   data.get("data")
        result=data.get("data").get("result")
        return result
   


# p=Prometheus("172.16.4.3","33401")
# query="pd_scheduler_store_status{type='store_available_deviation'}"
# start="2021-04-19T13:39:30.781Z"
# end="2021-04-19T17:50:00.781Z"
# data=p.GetRecords(query,start,end)           
# print(data)