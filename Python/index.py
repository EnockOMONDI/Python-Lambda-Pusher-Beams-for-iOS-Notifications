from pusher_push_notifications import PushNotifications
import requests


def lambda_handler(event, context):
    beams_client = PushNotifications(
                instance_id='0fb4a756-8780-4425-b393-3c7855470d99',
                secret_key='7A57DBC7C435D04039C301492C05F75F9AD65835D5DCF41F50FC901F68AA93C2',
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
