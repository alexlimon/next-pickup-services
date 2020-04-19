from ..helpers.provider import provide_db_connection
from ...models.notification_recipient import NotificationRecipient
from ..helpers import constants, parameter_validation_async
import datetime
import os
import logging
import asyncio
import pymongo
from typing import List


notification_recipients = provide_db_connection().notification_recipients


async def get_all_recipients() -> List[NotificationRecipient]:
    loop = asyncio.get_running_loop()

    raw_recipients = await loop.run_in_executor(None, notification_recipients.find)

    if raw_recipients is None:
        return None

    recipient_list = []
    encode_tasks = []

    for raw_recipient in raw_recipients:
        encode_tasks.append(
            asyncio.create_task(parameter_validation_async.dict_to_custom_objects(
                raw_recipient, recipient_list))
        )

    await asyncio.gather(*encode_tasks)

    return recipient_list


async def insert_recipient(new_recipient: NotificationRecipient) -> str:
    loop = asyncio.get_running_loop()

    dict_encoded_recipient = await parameter_validation_async.custom_object_to_dict(new_recipient)

    created_recipient_result = await loop.run_in_executor(None, notification_recipients.insert_one, dict_encoded_recipient)

    if created_recipient_result.acknowledged is None:
        raise RuntimeError("Could not insert: " +
                           NotificationRecipient.phone_number)

    return created_recipient_result


async def update_recipient(updated_recipient: NotificationRecipient):
    loop = asyncio.get_running_loop()

    dict_encoded_recipient = await parameter_validation_async.custom_object_to_dict(updated_recipient)

    updated_recipient_result = await loop.run_in_executor(None, notification_recipients.insert_one, dict_encoded_recipient)

    if updated_recipient_result.acknowledged is None:
        raise RuntimeError("Could not update: " +
                           NotificationRecipient.phone_number)

    return updated_recipient_result


async def delete_recipient(phone_number_to_delete: NotificationRecipient) -> str:

    loop = asyncio.get_running_loop()


    deleted_recipient_result = await loop.run_in_executor(None, notification_recipients.delete_one, {"phone_number": phone_number_to_delete})

    if deleted_recipient_result.acknowledged is None:
        raise RuntimeError("Could not update: " +
                           NotificationRecipient.phone_number)

    return deleted_recipient_result


def get_recipients_to_notify() -> List[NotificationRecipient]:
    loop = asyncio.get_running_loop()
    return


async def get_recipient(existing_recipient_number) -> NotificationRecipient:
    loop = asyncio.get_running_loop()

    raw_recipient = await loop.run_in_executor(None, notification_recipients.find_one, {"phone_number": existing_recipient_number})

    if raw_recipient is None:
        return None

    return await parameter_validation_async.dict_to_custom_objects(raw_recipient)
