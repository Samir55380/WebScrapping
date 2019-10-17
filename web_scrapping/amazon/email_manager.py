import smtplib

URL = 'https://www.amazon.com/Yeelight-Dimmable-Changing-Equivalent-Compatible/dp/B077GCYCT7/ref=nav_signin?crid' \
      '=2CHRQZC7E10IJ&keywords=yeelight&qid=1571256850&sprefix=yee%2Caps%2C241&sr=8-5& '


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('replay351@gmail.com', 'fawyomfwjaedxiij')

    subject = 'Price fell down'

    body = 'Hurry up and buy. Open link: {}'.format(URL)

    msg = f"Subject: {subject}\n\n {body}"

    addrs_list = ('indirasanches@hotmail.com', 'samir21101993@hotmail.com')

    server.sendmail(
        'replay351@gmail.com',
        addrs_list,
        msg
    )
    print('EMAIL SENT WERE SENT TO')

    server.quit()
