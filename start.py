import requests, json

from os import system

# AuthorBy: RyoDev
# Facebook: bit.ly/YtRyoFb
# Instagram: bit.ly/YtRyoIg
# Website: bit.ly/YtRyoWeb

# Get a free API token at https://afara.my.id

Token = json.load(open('token.json'))['token']

def main():
    system('clear')
    try:
        print('[+] Bot Nulis [+]')
        print('')
        text = input('Text: ')
        res = requests.get('https://afara.my.id/api/writing-bot', data = '{"text":"' + str(text) + '"}', headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Authorization": "Bearer " + Token
        }).json()
        if 'error' in res:
            print(res['error'])
        elif 'message' in res:
            print('Invalid API token, get a free API token at "https://afara.my.id"')
        else:
            print('')
            print('Berhasil, buka url ini untuk melihat hasilnya: ' + res['url'])
            print('')
    except KeyboardInterrupt:
        print('Exit.')

if __name__ == "__main__":
    main()