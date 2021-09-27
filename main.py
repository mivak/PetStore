import random
import unittest
import time

import Functions
import RequestsFunctions


class TestPets(unittest.TestCase):
    pet_id = Functions.get_unique_pet_id()

    def test_001_available_pets_count(self):
        status = 'available'
        actual_pets_count = Functions.get_pets_count(status)
        expected_pets_count = 656
        message = f"Pets count is {actual_pets_count} instead of {expected_pets_count}"
        self.assertEqual(expected_pets_count, actual_pets_count, message)

    def test_002_adding_new_pet(self):
        status = 'available'
        # initial_count = Functions.get_available_pets_count(status)
        name = "my_dog" + str(random.randint(0, 1000))
        RequestsFunctions.add_new_pet(name, self.pet_id)

        pet = RequestsFunctions.get_pet_by_id(self.pet_id)
        seconds = 0
        while pet is None:
            time.sleep(1)
            pet = RequestsFunctions.get_pet_by_id(self.pet_id)
            seconds += 1

            if seconds > 10:
                print(f'Pet with id {self.pet_id} was not found after added')
                break

        added_pet_name = pet["name"]
        added_pet_status = pet["status"]

        # actual_count = Functions.get_pets_count(status)

        message_name = f'Name of created pet with id {self.pet_id} is {added_pet_name} instead of {name}'
        message_status = f'Status of created pet with id {self.pet_id} is {added_pet_status} instead of {status}'
        # message_count = f'Count is {actual_count} instead of {initial_count + 1}'

        self.assertEqual(name, added_pet_name, message_name)
        self.assertEqual(status, added_pet_status, message_status)
        # self.assertEqual(initial_count + 1, actual_count, message_count)

    def test_003_updating_pet_status_to_sold(self):
        status = 'sold'
        pet = RequestsFunctions.get_pet_by_id(self.pet_id)
        name = pet["name"]

        RequestsFunctions.update_pet(self.pet_id, name, status)

        updated_pet = RequestsFunctions.get_pet_by_id(self.pet_id)
        updated_status = updated_pet["status"]

        seconds = 0
        while updated_status != status:
            time.sleep(1)
            updated_pet = RequestsFunctions.get_pet_by_id(self.pet_id)
            updated_status = updated_pet["status"]
            seconds += 1

            if seconds > 10:
                print(f'Status of pet with id {self.pet_id} was not updated to {status}')
                break

        message = f'Status is {updated_status} instead of {status}'
        self.assertEqual(status, updated_status, message)

    def test_004_deleting_pet(self):
        RequestsFunctions.delete_pet(self.pet_id)
        pet_to_check = RequestsFunctions.get_pet_by_id(self.pet_id)

        seconds = 0
        while pet_to_check is not None:
            time.sleep(1)
            pet_to_check = RequestsFunctions.get_pet_by_id(self.pet_id)
            seconds += 1

            if seconds > 10:
                print(f'Pet with id {self.pet_id} was not deleted')
                break

        message = f'Pet with id {self.pet_id} was not deleted'

        self.assertTrue(pet_to_check is None, message)


if __name__ == '__main__':
    unittest.main()
