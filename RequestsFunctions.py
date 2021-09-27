import requests
import json


def get_pets_by_status(status):
    """
    Gets all pets by status
    :param status: string - new status that will be updated (e.g. sold, pending, available)
    :return: JSON - request response
    """
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available'
    response = requests.get(url=url)
    data = response.json()

    if response.status_code != 200:
        print(f'get_pets_by_status {status}: {response.status_code}')

    return data


def add_new_pet(name, unique_id):
    """
    Send POST request to add a new pet by name and id
    :param name: string, the name of the pet to add
    :param unique_id: int - the id of the pet to add (should be unique)
    :return: JSON - request response
    """
    url = "https://petstore.swagger.io/v2/pet"

    body = {
      "id": unique_id,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": name,
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }

    headers = {"Content-Type": "application/json",
               "Accept": "*/*",
               "Accept-Encoding": "gzip, deflate, br",
               "Connection": "keep-alive"}

    response = requests.post(url=url, data=json.dumps(body), headers=headers)
    if response.status_code != 200:
        print(f'add_new_pet status code: {response.status_code}')

    return response.json()


def update_pet(pet_id, name, status):
    """
    Update status of existing pet
    :param pet_id: int - id of existing pet
    :param name: string - name that will be updated
    :param status: string - new status that will be updated (e.g. sold, pending, available)
    :return: JSON - request response
    """
    url = "https://petstore.swagger.io/v2/pet"
    body = {
      "id": pet_id,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": name,
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": status
    }

    headers = {"Content-Type": "application/json",
               "Accept": "*/*",
               "Accept-Encoding": "gzip, deflate, br",
               "Connection": "keep-alive"}

    response = requests.put(url=url, data=json.dumps(body), headers=headers)
    if response.status_code != 200:
        print(f'update_pet status code: {response.status_code}')

    return response.json()


def delete_pet(pet_id):
    """
    Delete a pet by id
    :param pet_id:
    :return: JSON - request response
    """
    url = f"https://petstore.swagger.io/v2/pet/{pet_id}"

    response = requests.delete(url=url)

    if response.status_code != 200:
        print(f'delete_pet status code: {response.status_code}')

    return response.json()


def get_pet_by_id(pet_id):
    """
    Get single pet by id
    :param pet_id: int: The id of the pet to get
    :return: JSON - request response if status code is 200, else: None
    """
    url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
    response = requests.get(url=url)

    if response.status_code == 200:
        return_value = response.json()
    else:
        return_value = None

    return return_value
