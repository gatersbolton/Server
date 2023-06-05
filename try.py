import json
txt='123123'
filename = 'try.json'  #文件路径   一般文件对象类型为json文件
with open(filename,"w") as f_obj:#打开模式为可写
	json.dump(txt, f_obj)