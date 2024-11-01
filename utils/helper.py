import json
import allure
from allure_commons.types import AttachmentType
from requests import Response


class Helper:
    @staticmethod
    def attach_response(response: Response):
        formatted_response = json.dumps(response, indent=4)
        allure.attach(body=formatted_response, name='API Response', attachment_type=AttachmentType.JSON)
