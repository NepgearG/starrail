import os

from onepush import get_notifier

WEBHOOK = os.environ['WEBHOOK']
with open('output.log', 'r', encoding='utf-8') as f:
    log_content = f.read()


    #if "Message: OK" not in log_content:
    n = get_notifier(discord)
    print(n.params)  
    
    response = n.notify(webhook=WEBHOOK)
    print(response.text)  
