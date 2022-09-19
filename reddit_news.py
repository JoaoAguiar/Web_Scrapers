import requests
import pandas
import warnings
import csv
import smtplib
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

while(True):
    warnings.filterwarnings("ignore")

    # authenticate API
    client_auth = requests.auth.HTTPBasicAuth('', '')
    data = { 'grant_type': 'password', 'username': '', 'password': '' }
    headers = {'User-Agent': 'mining/0.0.1'}

    # send authentication request for OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=client_auth, data=data, headers=headers)

    # extract token from response and format correctly
    token = res.json()['access_token']
    # update API headers with authorization (bearer token)
    headers['Authorization'] = f'bearer {token}'

    # initialize dataframe and parameters for pulling data in loop
    dataframe = pandas.DataFrame()
    params = { 'limit': 100 }

    # subreddit
    #subreddit = input("Subreddit: ")
    subreddit = "https://oauth.reddit.com/r/" + "portugal" + "/hot"
    # keyword
    #keyword = input("Keyword: ")
    keyword = "portugal"

    # make a request for the most recent posts
    res = requests.get(subreddit, headers=headers, params=params)

    # loop through each post retrieved from GET request
    for post in res.json()['data']['children']:
        # append relevant data to dataframe
        dataframe = dataframe.append({
            'title': post['data']['title'],
            'permalink': post['data']['permalink']
        }, ignore_index=True)

    elements_list = dataframe.values.tolist()

    for element in elements_list:
        element[1] = 'https://www.reddit.com' + element[1]

    i = 0

    while i in range(len(elements_list)+1):
        try:
            if keyword not in elements_list[i][0]: 
                elements_list.remove(elements_list[i])
            else:
                i = i + 1
        except:
            if i == len(elements_list):
                break
            else:
                print("Error in element")
                elements_list.remove(elements_list[i])

    # email address
    email = "" 
    password = ""

    message = MIMEMultipart('alternative')
    message['To'] = email
    message['From'] = email
    message['Subject'] = "SubReddit"

    html = " <h4> %s links you might find interesting today:</h4> " % len(elements_list)

    for element in elements_list:
        html = html + element[0] + " <br> " + element[1] + "<br><br>"

    mime = MIMEText(html, 'html')

    message.attach(mime)

    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(email, password)
        mail.sendmail(email, email, message.as_string())
        mail.quit()
        print('Email sent!')
    except Exception as e:
        print('Something went wrong... %s' % e)

    # After 4h go search for new news
    time.sleep(14400)
