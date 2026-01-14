import json

app_info={"name":"demoApp","service":"homeApp","port":4590,"version":[1.0],
          "authors":{"K1":"Mr.AB","K2":"SAB"}}

print(type(app_info))

jd = json.dumps(app_info) # from python --> to json 
##
print(type(jd))
python_data = json.loads(jd) # from json to python
print(type(python_data))