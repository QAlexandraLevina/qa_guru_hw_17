import requests
from schemas import post_user_create_schema, get_single_user_schema, put_update_user_schema, patch_update_user_schema, post_unsuccessful_login_schema
from jsonschema import validate
from constants import URL, API_KEY



"""Позитивные проверки с разными схемами"""
def test_assert_post_method_create_user():
  post_method = requests.post(f'{URL}users', data={"name":"morpheus", "job":"leader"}, headers=API_KEY)
  assert post_method.status_code == 201
  validate(post_method.json(), post_user_create_schema)


def test_assert_get_method_single_user():
  get_method = requests.get(f'{URL}users/2', headers=API_KEY)
  assert get_method.status_code == 200
  validate(get_method.json(), get_single_user_schema)


def test_assert_put_method_update_user():
  name = "morpheus"
  job = "zion resident"
  put_method = requests.put(f'{URL}users/2', data={"name":name, "job":job}, headers=API_KEY)
  body = put_method.json()
  assert put_method.status_code == 200
  assert body["name"] == name
  assert body["job"] == job
  validate(body, put_update_user_schema)


def test_assert_patch_method_update_user():
  patch_method = requests.patch(f'{URL}users/2', data={"name":"morpheus", "job":"zion resident"}, headers=API_KEY)
  assert patch_method.status_code == 200
  validate(patch_method.json(), patch_update_user_schema)


def test_assert_delete_method_user():
  delete_method = requests.delete(f'{URL}users/2', headers=API_KEY)
  assert delete_method.status_code == 204
  assert  delete_method.text == ""



"""Негативные проверки"""
def test_assert_get_method_single_user_not_found():
  get_method = requests.get(f'{URL}users/23', headers=API_KEY)
  assert get_method.status_code == 404
  assert  get_method.json() == {}


def test_assert_post_method_login_unsuccessful():
  post_method = requests.post(f'{URL}login', data={"email": "peter@klaven"}, headers=API_KEY)
  assert post_method.status_code == 400
  validate(post_method.json(), post_unsuccessful_login_schema)