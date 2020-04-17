from .clients import notification_collection_client
from ..models.notification_recipient import NotificationRecipient

async def manage_recipient(phone_number, name, zipcode, http_method):

    result = None

    recipient_request = NotificationRecipient(phone_number = phone_number, name = name, zipcode = zipcode)
    await recipient_request.validate_properties_async()

    existing_recipient = await notification_collection_client.get_recipient(recipient_request.phone_number)

    if http_method == "GET":
        result = existing_recipient

    if http_method == "POST":
        if existing_recipient:
            recipient_request._id = existing_recipient._id
            recipient_request.created = existing_recipient.created
            recipient_request.last_notified = existing_recipient.last_notified
            recipient_request.verified = existing_recipient.verified
             
            result = await notification_collection_client.update_recipient(recipient_request)
        else:
            result = await notification_collection_client.insert_recipient(recipient_request)
    
    if http_method == "DELETE":
        result = await notification_collection_client.delete_recipient(recipient_request.phone_number)
    
    if result == None:
        result = {"result": "The record for: " + recipient_request.name + " and number : "+ recipient_request.phone_number + " do not exist." }

    return result


