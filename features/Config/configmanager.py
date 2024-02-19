import os
import time
import yaml

class ConfigurationManager:
    """
    This class manages the global configurations like connections param with Databases, Snowflakes,
    SSH etc
    """
    str_parent_node = 'env'


    def __init__(self):

        global str_environment
        global str_environment_type
        self.obj_config=self.read_base_config_file()



    def get_config_filepath(self):
        """
        Description:
            |  This method fetches path of config.yml

        :return: String
        """
        try:
            str_filepath = self.get_project_path() + os.path.sep + "config.yml"
            return str_filepath
        except Exception as e:
            print("Error in get_config_filepath method-->" + str(e))

    def get_project_path(self):
        """
        Description:
            |  This method fetches path of the root Project folder

        :return: String
        """
        try:
            current_directory = os.getcwd()

            # Get the parent directory
            parent_directory = os.path.dirname(current_directory)
            parent_directory = os.path.dirname(parent_directory)
            parent_directory_main = os.path.dirname(parent_directory)
            parent_directory_proj = os.path.dirname(parent_directory_main)

            return parent_directory_proj
        except Exception as e:
            print("Error in get_project_path method-->" + str(e))
    def read_base_config_file(self):
        """
        Description:
            |  This method reads base config.yml file and loads the content into a dictionary object.

        :return: Dictionary
        """
        try:
            count = 0
            config = None
            while config is None and count < 30:
                try:
                    with open(self.get_config_filepath(), 'r') as config_yml:
                        config = yaml.safe_load(config_yml)





                except Exception as e:
                    pass
                count = count + 1
                time.sleep(1)
            if config is None:
                raise Exception("Error Occurred while reading a config file")
            return config
        except Exception as e:
            print("Error in read_base_config_file method-->" + str(e))
            return None
    def get_features_dirpath(self):
        """
        Description:
            |  This method fetches path of the features directory

        :return: String
        """
        try:
            str_currentdir_path = self.current_path
            str_currentdir_name = os.path.basename(str_currentdir_path)
            while not str_currentdir_name == "features":
                if os.sep + "features" in str_currentdir_path:
                    str_currentdir_path = os.path.dirname(os.path.abspath(str_currentdir_path))
                    str_currentdir_name = os.path.basename(str_currentdir_path)

                else:
                    str_currentdir_path = os.path.abspath(str_currentdir_path) + os.sep + "features"
                    str_currentdir_name = os.path.basename(str_currentdir_path)

            return str_currentdir_path
        except Exception as e:
          print("Error in get_features_dirpath method-->" + str(e))