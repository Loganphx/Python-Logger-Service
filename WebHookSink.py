import json
import sys
import traceback
from enum import Enum

import requests

from LogLevels import LogLevels
from LoggerSink import LoggerSink


class WebHookSink(LoggerSink):
    webhook_url: str

    def __init__(self, requiredLogLevel: LogLevels, webhook_url: str):
        super().__init__(requiredLogLevel)
        self.webhook_url = webhook_url

    def serialize_to_json(self):
        data = super().serialize_to_json()
        data["webhook_url"] = self.webhook_url
        return data

    def post_to_webhook(self, message: str):
        json_data = {"content": message}

        result = requests.post(
            self.webhook_url, data=json.dumps(json_data),
            headers={'Content-Type': 'application/json'}
        )
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))

    def post_to_webhook_exception(self, exception: Exception, trace: traceback, fields: []):

        json_data = {"content": f"{str(exception)}"}

        result = requests.post(
            self.webhook_url, data=json.dumps(json_data),
            headers={'Content-Type': 'application/json'}
        )
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))

    def handle_log(self, message: str):
        if not super().handle_log(message):
            return

        self.post_to_webhook(message)

    def handle_warning(self, message: str):
        if not super().handle_warning(message):
            return

        self.post_to_webhook(message)

    def handle_error(self, message: str):
        if not super().handle_error(message):
            return

        self.post_to_webhook(message)

    def handle_exception(self, exception: Exception, trace: traceback, fields: []):
        if not super().handle_exception(exception, trace, fields):
            return

        self.post_to_webhook_exception(exception, trace, fields)

    def __str__(self):
        return str(self.serialize_to_json())
