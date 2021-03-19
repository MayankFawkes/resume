from json import loads
from typing import Union
from requests import get

RAW = "https://raw.githubusercontent.com/{}/resume/master/RESUME.json"

def get_user(username:str=None) -> Union[None, loads]:
	req = get(RAW.format(username), params={"flush_cache": "True"})
	if req.status_code == 200:
		return req.json()
