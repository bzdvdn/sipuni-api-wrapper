import requests
from json import JSONDecodeError
from datetime import datetime
from hashlib import md5
from urllib.parse import urlencode

from .exceptions import SipuniException


class Sipuni(object):
    API_URL = 'https://sipuni.com/api/'

    def __init__(self, user: str, token: str = '') -> None:
        """
        :param user: str (user id)
        :param token: str (api key)
        """
        self.user = user
        self.token = token
        self._session = requests.session()

    def _generate_hash(self, query_params: list) -> str:
        """
        :param query_params: list ()
        :return: str
        """
        hash_str = "+".join(str(query).lower() for query in query_params)
        return md5(hash_str.encode('utf-8')).hexdigest()

    def _create_query_params(self, params: dict) -> str:
        hash_ = self._generate_hash(list(params.values()))
        params.pop('secret', None)
        params['hash'] = hash_
        return urlencode(params)

    def _send_api_request(self, method: str, url: str, data: dict = {},
                          headers: dict = {}, csv=False, file=False) -> any:
        """
        :param method: str (get, post, put, delete, head)
        :param url: str
        :param data: dict
        :param headers: dict
        :param csv: bool (True in statistic)
        :param file: bool (True in record)
        :return: any
        """
        self._session.headers.update(headers)
        try:
            response = self._session.__getattribute__(method)(url=url, json=data)
            if response.status_code > 204:
                raise SipuniException(response.status_code, response.reason, response.text)
            if csv:
                return response.content.decode('utf-8')
            if file:
                return response.content
            return response.json()
        except (requests.ConnectionError, JSONDecodeError):
            raise SipuniException(500,
                                  'Server not answer or Cant decoded to json',
                                  'Server not answer or Cant decoded to json'
                                  )

    def make_call(self, phone: str, sipnumber: str, reverse: int = 0, antion: int = 0) -> dict:
        """
        :param phone: str
        :param sipnumber: str
        :param reverse: int
        :param antion: int
        :return: dict
        """
        params = {
            'antion': antion,
            'phone': phone,
            'reverse': reverse,
            'sipnumber': sipnumber,
            'user': self.user,
            'secret': self.token
        }
        query_params = self._create_query_params(params)
        url = f'{self.API_URL}callback/call_number?{query_params}'
        return self._send_api_request('post', url)

    def get_call_stats(self, from_date: datetime, to_date: datetime, type_: int = 0,
                       state: int = 0, tree: str = '', from_number: str = '',
                       to_number: str = 0, to_answer: str = '', anonymous: int = 1,
                       first_time: int = 0) -> str:
        """
        :param from_date: str
        :param to_date: str
        :param type_: int
        :param state: int
        :param tree: str
        :param from_number: str
        :param to_number: str
        :param to_answer: str
        :param anonymous: int
        :param first_time: int
        :return: str (csv data or raise SupiniException)
        """
        params = {
            'anonymous': anonymous,
            'firstTime': first_time,
            'from': from_date.strftime('%d.%m.%Y'),
            'fromNumber': from_number,
            'state': state,
            'to': to_date.strftime('%d.%m.%Y'),
            'toAnswer': to_answer,
            'toNumber': to_number,
            'tree': tree,
            'type': type_,
            'user': self.user,
            'secret': self.token,
        }
        query_params = self._create_query_params(params)
        url = f'{self.API_URL}statistic/export?{query_params}'
        print(url)
        return self._send_api_request('post', url, csv=True)

    def get_record(self, id_: str) -> bytes:
        """
        :param id_: str
        :return: bytes
        """
        params = {
            'id': id_,
            'user': self.user,
            'secret': self.token
        }
        query_params = self._create_query_params(params)
        url = f'{self.API_URL}statistic/record?{query_params}'
        return self._send_api_request('post', url, file=True)

    def get_managers(self) -> str:
        """
        :return: str (csv data or raise SupiniException)
        """
        params = {
            'user': self.user,
            'secret': self.token,
        }
        query_params = self._create_query_params(params)
        url = f'{self.API_URL}statistic/operators?{query_params}'
        return self._send_api_request('post', url, csv=True)

    def make_tree_call(self, phone: str, sipnumber: str, tree: str, reverse: int = 0) -> dict:
        """
        :param phone: str
        :param sipnumber: str
        :param tree: str
        :param reverse: int
        :return: dict (call data or or raise SupiniException)
        """
        params = {
            'phone': phone,
            'reverse': reverse,
            'sipnumber': sipnumber,
            'tree': tree,
            'user': self.user,
            'secret': self.token
        }
        query_params = self._create_query_params(params)
        url = f'{self.API_URL}callback/call_tree?{query_params}'
        return self._send_api_request('post', url)

    def make_external_call(self, from_phone: str, to_phone, first_sipnumber: str,
                           second_sipnumber: str) -> dict:
        """
        :param from_phone: str
        :param to_phone: str
        :param first_sipnumber: str
        :param second_sipnumber: str
        :return: dict
        """
        params = {
            'phoneFrom': from_phone,
            'phoneTo': to_phone,
            'sipnumber': first_sipnumber,
            'sipnumber2': second_sipnumber,
            'user': self.user,
            'secret': self.token
        }
        query_params = self._create_query_params(params)
        url = f'{self.API_URL}callback/call_external?{query_params}'
        return self._send_api_request('post', url)

    def hangup_call(self, call_id: str) -> dict:
        """
        :param call_id: str
        :return: dict
        """
        params = {
            'callId': call_id,
            'user': self.user,
            'secret': self.token
        }
        query_params = self._create_query_params(params)
        url = f'{self.API_URL}events/call/hangup?{query_params}'
        return self._send_api_request('post', url)

    def make_voice_call(self, phone: str, message: str, voice_type: str, sipnumber: str) -> dict:
        """
        :param phone: str
        :param message: str
        :param voice_type: str (like Vladimir, Alexandr, Anna, Maria, Victoria)
        :param sipnumber:
        :return:
        """
        params = {
            'message': message,
            'phone': phone,
            'sipnumber': sipnumber,
            'voice': voice_type,
            'user': self.user,
            'secret': self.token
        }
        query_params = self._create_query_params(params)
        url = f'{self.API_URL}voicecall/call?{query_params}'
        return self._send_api_request('post', url)
