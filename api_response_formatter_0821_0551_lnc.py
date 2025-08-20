# 代码生成时间: 2025-08-21 05:51:28
import json

class ApiResponseFormatter:
    """
    A class to format API responses in a standardized way.
    """

    def __init__(self, status_code, data, message):
        """
        Initializes the ApiResponseFormatter with a status code, data, and message.
        
        :param status_code: HTTP status code
        :param data: Data payload of the response
        :param message: A message describing the status of the response
        """
        self.status_code = status_code
        self.data = data
        self.message = message

    def format_response(self):
        """
        Formats the API response into a JSON object.
        
        :return: A JSON formatted string of the response
        """
        try:
            response = {
                "status": self.status_code,
                "data": self.data,
                "message": self.message
            }
            return json.dumps(response, indent=4)
        except (TypeError, ValueError) as e:
            # Handle errors related to JSON serialization
            return json.dumps(
                {
                    "status": 500,
                    "data": None,
                    "message": f"Internal Server Error: {str(e)}"
                },
                indent=4
            )

    def set_status_code(self, status_code):
        """
        Sets the HTTP status code of the response.
        
        :param status_code: The new status code
        """
        self.status_code = status_code

    def set_data(self, data):
        """
        Sets the data payload of the response.
        
        :param data: The new data payload
        """
        self.data = data

    def set_message(self, message):
        """
        Sets the message describing the response status.
        
        :param message: The new message
        """
        self.message = message

# Example usage:
if __name__ == '__main__':
    # Create an instance of ApiResponseFormatter
    formatter = ApiResponseFormatter(200, {"user": "John Doe"}, "Success")

    # Format the response
    formatted_response = formatter.format_response()
    print(formatted_response)
    # Output:
    # {
    #     "status": 200,
    #     "data": {"user": "John Doe"},
    #     "message": "Success"
    # }