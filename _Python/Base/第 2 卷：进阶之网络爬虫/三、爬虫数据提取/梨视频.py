# https://video.pearvideo.com/mp4/third/20211127/cont-1746656-10305425-084402-hd.mp4  真链接
# srcUrl: "https://video.pearvideo.com/mp4/third/20211127/1638154872214-10305425-084402-hd.mp4" 假连接
# https://www.pearvideo.com/video_1746656
import requests
url ='https://www.pearvideo.com/video_1746656'
cont_=url.split('_')[1]
# print(cont_)
videp_url=f'https://www.pearvideo.com/videoStatus.jsp?contId={cont_}'
# print(videp_url)
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'referer':url
}
response=requests.get(videp_url,headers=headers)
data=response.json()
srcurl=data['videoInfo']['videos']['srcUrl']
# print(srcurl)
systemTime=data['systemTime']
# print(systemTime)
# print
srcurl=srcurl.replace(systemTime,f'conf-{cont_}')
r=requests.get(srcurl,headers=headers).content
with open('./shenzhen.mp4','wb')as f:
    f.write(r)
print('ok')