import os
import yaml

class YamlUtil:
     #读取extract.yaml文件
    def read_extract_yaml(self):
        # 获取根目录下的yaml文件，读取并打开
        # python通过open方式读取文件数据，再通过load函数将数据转化为列表或字典
        with open(os.getcwd()+"/extract.yaml",mode='r',encoding='UTF-8') as f:
           value= yaml.load(stream=f,Loader=yaml.FullLoader)
           return value;


    #写入extract.yaml文件
    def write_extract_yaml(self,data):

         with open(os.getcwd()+'/extract.yaml',mode='w',encoding='UTF-8') as f:
             value=yaml.dump(data=data,stream=f,allow_unicode=True  )
             return value;


    # 清除yamlw文件
    def clean_extract_yaml(self):
        with open(os.getcwd()+'/extract.yaml',mode='w',encoding='UTF-8') as f:
            f.truncate()