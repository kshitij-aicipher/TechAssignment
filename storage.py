import json

class FileStorage:
    """
    A class to handle file-based storage operations using JSON format.

    Attributes:
        filename (str): The name of the file to store data.
    """

    def __init__(self, filename):
        """
        Initialize FileStorage object with a specified filename.

        Args:
            filename (str): The name of the file to store data.
        """
        self.filename = filename

    def save_data(self, data):
        """
        Save data to the file in JSON format.

        Args:
            data (list or dict): The data to be saved.

        Notes:
            If the file does not exist, it will be created.
        """
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        """
        Load data from the file in JSON format.

        Returns:
            list or dict: The loaded data from the file.

        Notes:
            If the file does not exist, an empty list is returned.
        """
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                #print('Loaded data:', data)
        except FileNotFoundError:
            data = []
        return data
    
