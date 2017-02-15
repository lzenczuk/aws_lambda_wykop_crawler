import boto3


def generate_pages_range_handler(event, context):
    print("Processing request: " + str(event))

    validation_errors = []

    start = -1
    stop = -1

    if 'from' not in event:
        validation_errors.append("Missing from parameter.")
    else:
        try:
            start = int(event['from'])

            if start < 0:
                validation_errors.append("Expected form parameter bigger then 0, was " + str(start))

        except ValueError:
            validation_errors.append("Expected form parameter as number, was " + event['from'])

    if 'to' not in event:
        validation_errors.append("Missing to parameter.")
    else:
        try:
            stop = int(event['to'])

            if stop < 0:
                validation_errors.append("Expected to parameter bigger then 0, was " + str(stop))

        except ValueError:
            validation_errors.append("Expected to parameter as number, was " + event['to'])

    if len(validation_errors) != 0:
        return {'errors': validation_errors}

    if start > stop:
        validation_errors.append(
            "Expected to parameter bigger or equal from parameter, was from:  " + str(start) + " to: " + str(stop))

    if len(validation_errors) != 0:
        return {'errors': validation_errors}

    topic_arn = "arn:aws:sns:eu-west-1:039898779445:WykopPagesToFetchTopic"

    client = boto3.client('sns')

    for id in range(start, stop):
        response = client.publish(TopicArn=topic_arn, Message=str(id))
        print (response)

    return {'from': start, 'to': stop}


def fetch_page_by_id_handler(event, context):
    page_id = -1

    if 'Records' in event:
        if len(event['Records']) == 1:
            if 'Sns' in event['Records'][0]:
                if 'Message' in event['Records'][0]['Sns']:
                    try:
                        page_id = int(event['Records'][0]['Sns']['Message'])
                    except ValueError:
                        print("Error parsing page id. Expected number, was " + str(event['Records'][0]['Sns']['Message']))
                        return
    else:
        print("Error, expecting event: Records -> [0] -> Sns -> Message, was " + str(event))
        return

    if page_id < 0:
        print("Error, incorrect page id. Expected bigger then 0, was " + str(page_id))
        return

    print("------------> fetching page: " + str(page_id))
    return
