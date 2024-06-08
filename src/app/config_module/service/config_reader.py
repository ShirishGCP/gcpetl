import os
import configparser

class ConfigReader:
    def __init__(self,file_path):
        self.config=configparser.ConfigParser()
        self.config.read(file_path)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Configuration file not found: {file_path}")

        if not self.config.sections():
            raise ValueError(f"No sections found in the configuration file: {file_path}")



        self.config_dict=self._config_to_dict()

    def _config_to_dict(self):
        config_dict={}
        for section in self.config.sections():
            print(section)
            config_dict[section]=dict(self.config.items(section))
        return config_dict
    
    def get_config(self):
        return self.config_dict
    
    def get_group_config(self,group):
        print("group:"+group)
        return self.config_dict.get(group,None)
    
# Initialize the config reader
configdir="D:\\GCPLearning\\codebase\\gcpetl\\"
config_file_path = os.path.join(os.path.dirname(configdir), 'config', 'gcpetl.param')
config_reader = ConfigReader(config_file_path)  




