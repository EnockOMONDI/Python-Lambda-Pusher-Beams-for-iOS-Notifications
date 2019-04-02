from pusher_push_notifications import PushNotifications
import requests

def lambda_handler(event, context):
    beams_client = PushNotifications(
                instance_id='YOUR_INSTANCE_ID',
                secret_key='YOUR_SECRET_KEY',
                )

    response = beams_client.publish_to_interests(interests=['hello'],
                                             publish_body={
                                             'apns': {
                                                'aps': {
                                                    'alert': {
                                                        'title': event['title'],
                                                        'body': event['message']
                                                        },
                                                    },
                                                },
                                             },
                                             )
    print(response['publishId'])
