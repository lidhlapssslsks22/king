from flask import Flask, request, jsonify
import pycountry
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/tiktok_info', methods=['GET'])
def get_tiktok_info():
    user = request.args.get('user')
    if user:
        patre = {
            "Host": "www.tiktok.com",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "accept-language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr;q=0.6,hu;q=0.5,zh-CN;q=0.4,zh;q=0.3"
        }

        tikinfo = requests.get(f'https://www.tiktok.com/@{user}', headers=patre).text
        by = '@maho_s9'

        try:
            getting = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
            try:
                id = str(getting.split('id":"')[1]).split('",')[0]
            except:
                id = ""
            try:
                name = str(getting.split('nickname":"')[1]).split('",')[0]
            except:
                name = ""
            try:
                bio = str(getting.split('signature":"')[1]).split('",')[0]
            except:
                bio = ""
            try:
                country = str(getting.split('region":"')[1]).split('",')[0]
            except:
                country = ""
            try:
                private = str(getting.split('privateAccount":')[1]).split(',"')[0]
            except:
                private = ""
            try:
                followers = str(getting.split('followerCount":')[1]).split(',"')[0]
            except:
                followers = ""
            try:
                following = str(getting.split('followingCount":')[1]).split(',"')[0]
            except:
                following = ""
            try:
                like = str(getting.split('heart":')[1]).split(',"')[0]
            except:
                like = ""
            try:
                video = str(getting.split('videoCount":')[1]).split(',"')[0]
            except:
                video = ""
            try:
                secid = str(getting.split('secUid":"')[1]).split('"')[0]
            except:
                secid = ""
            try:
                countryn = str(pycountry.countries.get(alpha_2=country)).split("name='")[1].split("'")[0]
            except:
                countryn = ""
            try:
                countryf = str(pycountry.countries.get(alpha_2=country)).split("flag='")[1].split("'")[0]
            except:
                countryf = ""
            binary = "{0:b}".format(int(id))
            i = 0
            bits = ""
            while i < 31:
                bits += binary[i]
                i += 1
            timestamp = int(bits, 2)
            try:
                cdt = datetime.fromtimestamp(timestamp)
            except:
                cdt = ""

            return jsonify({
                'id': id,
                'name': name,
                'bio': bio,
                'country': country,
                'private': private,
                'followers': followers,
                'following': following,
                'like': like,
                'video': video,
                'secid': secid,
                'country_name': countryn,
                'country_flag': countryf,
                'created': cdt,
                'BY': by                
            })

        except Exception as e:
            return jsonify({'error': str(e)})

    return jsonify({'error': 'BY: @maho_s9'})

if __name__ == '__main__':
    app.run(debug=True)
