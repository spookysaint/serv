import requests
import os, time
import subprocess
from imgurpython import ImgurClient
import moviepy.editor as mp
try:
    rda = requests.get('https://paste.ee/r/DGbgR/0')
    open('/tmp/rclone.conf', 'wb').write(rda.content)
    os.system('rm video-watermark1.jpg video-watermark.jpg')
    os.system('wget https://github.com/rishabh-modi2/unsudo-apt/raw/master/video-watermark.jpg https://github.com/rishabh-modi2/unsudo-apt/raw/master/video-watermark1.jpg')
except:
    pass
from urllib.parse import urlparse, parse_qs
from contextlib import suppress
# from embeddify import Embedder
# plugin_config = {
#     'youtube': {'width' : 360},
# }
# embedder = Embedder(plugin_config = plugin_config, autoplay=False)
done = []
auth_manushya = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEzMTQsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MDI2MTYzNn0.M7V0oQ9vdZv86ryXqLDmmqw16A3SS8M5jaM8R055yiU'
auth_placebot01 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEzMzYsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MDI2MjY2M30.JgxIvbZX_uT-TziDu4rj1oEhsnA_m-qa_Nsu0JZxTLc'
auth_Baaphutera = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEzMzcsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MDI3Mjg4M30.YXBPXLQZkv1kZDQ_yLiJEJavISKJEN1MBTMxmFY9NUs'
auth_Comedy_cex = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEzMzgsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MDI3Mjk1M30.YLoOws55w6HXaeJps9t4Y9OG1bA_oPn1UPshlr3saVw'
auth_Dangerous_bhaiya = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEzMzksImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MDI3MzAzOH0.vzOa9zlOxFzTqh2KlG_As3tZdjHuvqNsPr0SJ_zTP6Q' 
client_id = 'ce3bb9f42a67e47'
client_secret = 'ccdb03913348f7c7849ec76479db8e52bd00df41'
access_token = '8109acf04770d700a58f8b3ab641e39efb4905da'
refresh_token = '4157cdd8407322e47daf95589dd2dcefc640f66d'
client = ImgurClient(client_id, client_secret, refresh_token)
client.set_user_auth(access_token, refresh_token)
auth_embed = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE2MzEsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MTc0Mjg4OX0.0xUekcGXPTdrDevD56p01xhEn-f5ArpuNuISTGXwFqY'
auth = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE2MzEsImlzcyI6ImJha2Nob2RpLm9yZyIsImlhdCI6MTY1MTc0Mjg4OX0.0xUekcGXPTdrDevD56p01xhEn-f5ArpuNuISTGXwFqY'
#client = ImgurClient(client_id, client_secret, access_token, refresh_token)
a = 0
log_file = open("postscheduler.log", "a+")
# for a in open("done.txt","r").read().splitlines():
#     done.append(a)
# Credential
def get_yt_id(url, ignore_playlist=False):
    # Examples:
    # - http://youtu.be/SA2iWivDJiE
    # - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    # - http://www.youtube.com/embed/SA2iWivDJiE
    # - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    query = urlparse(url)
    if query.hostname == 'youtu.be': return query.path[1:]
    if query.hostname in {'www.youtube.com', 'youtube.com', 'music.youtube.com'}:
        if not ignore_playlist:
        # use case: get playlist id not current video in playlist
            with suppress(KeyError):
                return parse_qs(query.query)['list'][0]
        if query.path == '/watch': return parse_qs(query.query)['v'][0]
        if query.path[:7] == '/watch/': return query.path.split('/')[1]
        if query.path[:7] == '/embed/': return query.path.split('/')[2]
        if query.path[:3] == '/v/': return query.path.split('/')[2]


http_base_url = "https://bakchodi.org/api/v3"
username = os.environ.get("username")
password = os.environ.get("password")
def send_post_request(location, json_data):
    r = requests.post(f"{http_base_url}{location}", json=json_data)
    return r
def Comment(id, content):
    try:
        global auth
        postcomm1 = {"content": content, "post_id": int(id), "auth": auth}
        postcomm = {k: v for k, v in postcomm1.items() if v}
        createComment = send_post_request("/comment", json_data=postcomm)
    except:
        print("comment failed")
        pass
def Like(id, auth):
    postlike1 = {"score": int(1), "post_id": int(id), "auth": auth}
    postlike = {k: v for k, v in postlike1.items() if v}
    createLike = send_post_request("/post/like", json_data=postlike)
def LikeComment(id, content):
    global auth
    postlike1 = {"score": int(1), "post_id": int(id), "auth": auth}
    postlike = {k: v for k, v in postlike1.items() if v}
    createLike = send_post_request("/post/like", json_data=postlike)
    postcomm1 = {"content": content, "post_id": int(id), "auth": auth}
    postcomm = {k: v for k, v in postcomm1.items() if v}
    createComment = send_post_request("/comment", json_data=postcomm)


def mp4(id, url):
    global auth
    content = " ::: spoiler Video \n`<iframe src='https://videoplayer.rishabh.ml/v/?url=" + url + "' height='360' width=100% allowfullscreen=True></iframe>`\n::: spoiler DownloadLink \n" + url + "\n:::  Copy The Embed code and Post"
    # print(content)
    LikeComment(id, content)
    time.sleep(10)

def imagewatermark(url, id):
    try:
        Like(id, auth_embed)
        file = 'img-raw.jpg' 
        with open(file, 'wb') as image:
            image.write(requests.get(url).content)
            image.close()
        os.system("convert 'img-raw.jpg' 'video-watermark1.jpg' -gravity SouthEast -geometry +50+300 -define compose:args=30,1 -compose dissolve -composite 'img.jpg'")
        a2 = client.upload_from_path('img.jpg', config=None, anon=False)
        content = "::: spoiler watermark\nImage Link:" + a2['link'] + "![](" + a2['link'] + ")\n:::\nI am a Bot\nI watermark all photos in Shitpost and funny\nVisit https://collection.rishabh.ml/txt/Video/raw/Chodi_vid+perma.html For Chodi Video Collection of 8900 videos and https://collection.rishabh.ml/IndianDankMemes/image/IndianDankMemes1000__image.html For some top idm memes images\nfor any issue or complaint msg to mod"
        Comment(id, content)
    except Exception as e:
        print(e)
def download(id, url):
    try:
        global auth
        Like(id, auth_embed)

        if 'v.red' in url:
            subprocess.check_output("wget " + url  + "/DASH_audio.mp4 " + url + "/DASH_480.mp4", shell=True)
            subprocess.call("ffmpeg -i DASH_480.mp4 -i DASH_audio.mp4 -c:v copy -c:a aac"  + id + "video.mp4" + " -y", shell=True, stdout=subprocess.PIPE)
        else:
        #    id = str(r.json()['posts'][i]['post']['id'])
            # print(id)
            os.system('./yt-dlp -o' + id + 'video.mp4 ' + url, shell=True)
        time.sleep(5)
        os.system("./rclone copy " + id + "video.mp4 onedrive:public --config /tmp/rclone.conf --ignore-existing", shell=True)
        os.remove(id + "video.mp4")
        os.system("ls")
#        drive_id = subprocess.Popen("./rclone lsf --format 'i' m:" + id + "video.mp4", shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0].replace('\n', '')
        content = "::: spoiler Video code \n`<iframe src=https://videoplayer.rishabh.ml/v/?url=?load=metadata&url=https://vid.rishabh.ml/api/raw/?path=/" + id + "video.mp4" + " scrolling='no' width='100%' height='320px' allowfullscreen></iframe>`\n::: spoiler How to Use\nJust Copy the highlight code given above and edit post and paste in body of post\n:::\n ::: spoiler DownloadLink\nhttps://vid.rishabh.ml/api/raw/?path=/" + id + "video.mp4" + "\n:::"
        Comment(id, content)
    except Exception as e:
        print(e)
        conte = "post id " + id + " error " + e + "  [@Rishabhmoodi@bakchodi.org](https://bakchodi.org/u/Rishabhmoodi) error found"
        Comment(id, conte)

def yt(id, url):
    try:
        global auth
    #    id = str(r.json()['posts'][i]['post']['id'])
        # print(id)
        Like(id, auth_embed)
        result = get_yt_id(url, ignore_playlist=False)
        if result is None:
            os.system('./yt-dlp -f 18 -o' + id + 'video.mp4 ' + url)                       
            time.sleep(5)
            os.system("./rclone copy " + id + 'video.mp4 m: --ignore-existing')
            os.remove(id + 'video.mp4')
            time.sleep(20)
            content = "::: spoiler Server Code `<iframe src='https://videoplayer.rishabh.ml/v/?url=https://backend.rishabh.ml/1:/serv/" + id + "video.mp4' height='360' width=100% allowfullscreen=True></iframe>`\n::: spoiler DownloadLink\nhttps://backend.rishabh.ml/1:/serv/" + id + "video.mp4\n:::" 
            Comment(id, content)
        else:
            content = "::: spoiler Server Direct code \n`<div style='position:relative; padding-bottom:calc(90.00%)'><iframe src='https://videoplayer2.rishabh.ml/videoapi/?url=" + result +  "' frameborder='0' scrolling='no' width='100%' height='100%' style='position:absolute;top:0;left:0;' allowfullscreen></iframe></div>`\n:::\n + ::: spoiler Invidious Embed code \n`<iframe src='https://invidious.snopyta.org/embed/" + result +  "' height='300' width=95% allowfullscreen=True></iframe>`\n:::\n" + "::: spoiler Youtube Code \n<iframe width=95% height='300' src='https://www.youtube-nocookie.com/embed/" + result + "' title='bakchodi.org' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>\n\n`<iframe width=95% height='300' src='https://www.youtube-nocookie.com/embed/" + result + "' title='bakchodi.org' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>`\n:::" 
            LikeComment(id, content)
    except Exception as e:
        print(e)
        conte = "post id " + id + " error " + e + "  [@Rishabhmoodi@bakchodi.org](https://bakchodi.org/u/Rishabhmoodi) error found"
        Comment(id, conte)

def ytshort(id, url):
#    #try:
        global auth
    #    id = str(r.json()['posts'][i]['post']['id'])
        # print(id)
        os.system('./yt-dlp -f 18 -o ' + id + 'video.mp4 ' + url)                       
        time.sleep(5)
        os.system("./rclone copy " + id + 'video.mp4 m: --ignore-existing')
        os.remove(id + 'video.mp4')
        time.sleep(20)
        # ytembed = get_yt_id(url, ignore_playlist=False)
        # result = embedder(url)
        Like(id, auth_embed)
        content = "::: spoiler Youtube Provided Embed Codes \nThis msg is sent because a defined video link is found in url " + url + "  `<iframe src='https://videoplayer.rishabh.ml/v/?url=https://backend.rishabh.ml/1:/serv/" + id + "video.mp4' height='360' width=100% allowfullscreen=True></iframe>` <iframe src='https://videoplayer.rishabh.ml/v/?url=https://backend.rishabh.ml/1:/serv/" + id + "video.mp4' height='360' width=100% allowfullscreen=True></iframe>\n:::" 
        Comment(id, content)
def videowatermark(id, url):
    try:
        Like(id, auth_embed)
        os.system('./yt-dlp -o' + id + 'video1.mp4 ' + url)                       
        time.sleep(5)
        os.system("ffmpeg -i " + id + "video1.mp4 -i video-watermark.jpg -filter_complex 'overlay=main_w-overlay_w-50:main_h-overlay_h-250' -codec:a copy " + id + "video.mp4 -y")
        os.system("./rclone copy " + id + 'video.mp4 m: --ignore-existing')
        os.remove(id + 'video.mp4')
        time.sleep(20)
        content = "::: spoiler Server Code \n`::: spoiler Video`\n\n`<iframe src='https://videoplayer.rishabh.ml/v/?url=https://backend.rishabh.ml/1:/serv/" + id + "video.mp4' height='360' width=100% allowfullscreen=True></iframe>`\n\n`:::`\n:::" 
        Comment(id, content)
    except Exception as e:
        print(e)
        conte = "post id " + id + " error " + e + "  [@Rishabhmoodi@bakchodi.org](https://bakchodi.org/u/Rishabhmoodi) error found"
        Comment(id, conte)
    # print(content)

def RedditDownloader(id, url):
    Like(id, auth_embed)
    print('reddit url found')
    # rvid = requests.get(url + '/DASH_360.mp4')
    # if rvid.status_code == 404:
    #     rvid = requests.get(url + '/DASH_360')
    # open('rvideo.mp4', 'wb').write(rvid.content)
    # raud = requests.get(url + '/DASH_audio.mp4')
    # if raud.status_code == 404:
    #     raud = requests.get(url + '/audio')
    # open('raudio.mp4', 'wb').write(raud.content)
    # # subprocess.check_output("ffmpeg -i rvideo.mp4 -i raudio.mp4 -c:v copy -c:a aac rvid" + id + "video1.mp4", shell=True)
    # # subprocess.check_output("ffmpeg -i rvid" + id + "video1.mp4 -i video-watermark.jpg -filter_complex 'overlay=main_w-overlay_w-50:main_h-overlay_h-250' -codec:a copy rvid" + id + "video.mp4 -y", shell=True)
    # file = "rvid" + id + "video.mp4"
    # watermark(file)
    # subprocess.check_output("./rclone copy rvid" + id + "video.mp4 m: --ignore-existing", shell=True)
    # os.remove("rvid" + id + "video.mp4")
    # drive_id = subprocess.Popen("./rclone lsf --format 'i' m:rvid" + id + "video.mp4", shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0].replace('\n', '')
    content = "::: spoiler New Video code\n`<div class='embed-responsive embed-responsive-16by9'><iframe src='https://videoplayer2.rishabh.ml/rvideo2/?url=" + url + "' scrolling='0' allowfullscreen></iframe></div>`\n:::" #+ "\n\n::: spoiler Video code \n`<iframe src=https://videoplayer.rishabh.ml/stream/?load=none&url=" + drive_id + " scrolling='no' width='100%' height='320px' allowfullscreen></iframe>`\n::: spoiler How to Use\nJust Copy the highlight code given above and edit post and paste in body of post\n :::" + "\n::: spoiler DownloadLink \nhttps://videoplayer.rishabh.ml/stream/?load=metadata&url=" + drive_id
    Comment(id, content)

def watermark(filename,):
    video = mp.VideoFileClip("rvideo.mp4")                                                                                                                              
    audioclip = mp.AudioFileClip("raudio.mp4")                                                                                                                        
                                                                                                                                                                          
    new_audioclip = mp.CompositeAudioClip([audioclip])                                                                                                                    
    video.audio = new_audioclip                                                                                                                                           
#videoclip.write_videofile("new_filename.mp4")                                                                                                                        
#    video = mp.VideoFileClip(rawfile)
    logo = (mp.ImageClip("video-watermark.jpg")
              .set_duration(video.duration - 5)
              .resize(height=20) # if you need to resize...
              .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
              .set_pos(("right","center"))
              .set_start(t=5))
    final = mp.CompositeVideoClip([video, logo])
    final.write_videofile(filename=filename, threads=3, verbose=False, progress_bar=False)

for a1 in open("a.txt","r").read():
    a = int(a1)

# print(done)
# print('starting' + 'a ' + str(a) + 'i ')
# lobal done
#   global i
aans = 2
while aans == 2:
    try:
        for page in range(1, 2):
            r = requests.get('https://bakchodi.org/api/v3/post/list?sort=New&page=' + str(page) +'&auth=' + auth)
            print('getting data...')
            for i in range(0,10):
                    id = str(r.json()['posts'][i]['post']['id'])
                    url = r.json()['posts'][i]['post']['url']
                    name = r.json()['posts'][i]['post']['name']
                    print(id)
                    if str(id) not in done:
                        if r.json()['posts'][i]['my_vote'] is None:
                          Like(id, auth_manushya)
                          Like(id, auth_placebot01)
                          Like(id, auth_Baaphutera)
                        #   Like(id, auth_Comedy_cex)
                        #   Like(id, auth_Dangerous_bhaiya)
                          if url:
                                Link = {'mp4', 'youtu', 'youtube.com/shorts', 'kapwing', 'rumble.com', 'instagram.com', 'https://videoplayer2.rishabh.ml/rvideo'}
                                Video = {'[video]', '[Video]'}
                            # if url in Link or r.json()['posts'][i]['post']['name'] in Video:
                                if r.json()['posts'][i]['post']['community_id'] == 18 or r.json()['posts'][i]['post']['community_id'] == 8:
                                    if '.jpg' in url or '.png' in url or '.jpeg' in url:
                                        imagewatermark(url, id)
                                if 'youtu' in url:
                                    # print('starting' + 'a ' + str(a) + 'i ' + str(i))
                                        yt(id, url)
                                        done.append(id)
                                
                                elif 'youtube.com/shorts' in url:

                                    # print('starting' + 'a ' + str(a) + 'i ' + str(i))
                                    ## try:
                                        result = url.replace('https://www.youtube.com/shorts/', '')
                                        content = "::: spoiler Invidious Embed code \n`::: spoiler Video` \n`<iframe src='https://invidious.snopyta.org/embed/" + result +  "' height='315' width=90% allowfullscreen=True></iframe>`\n`:::`\n:::\n" + "::: spoiler Youtube Code \n`::: spoiler Video` \n`<iframe width=90% height='315' src='https://www.youtube-nocookie.com/embed/" + result + "' title='bakchodi.org' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>`\n`:::`\n:::\n\n`::: spoiler Video `\n`<iframe width=90% height='315' src='https://www.youtube-nocookie.com/embed/" + result + "' title='bakchodi.org' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>`\n`:::`\n:::"
                                        Like(id, auth_embed)
                                        Comment(id, content)
                                        ytshort(id, url)
                                        done.append(id)
                                
                                if 'kapwing' in url or 'rumble.com' in url or 'instagram.com' in url or "[video]" in r.json()['posts'][i]['post']['name'] or "[Video]" in r.json()['posts'][i]['post']['name']:
                                    # print('starting' + 'a ' + str(a) + 'i ' + str(i))
                                    try:
                                        download(id, url)
                                        done.append(id)
                                        # with open ("done.txt", "a") as f:
                                        #     f.write(str(r.json()['private_messages'][i]['private_message']['id']) + '\n')
                                        time.sleep(10)
                                    except Exception as e:
                                        print(e)
                                        conte = "post id " + id + " error " + e + "  [@Rishabhmoodi@bakchodi.org](https://bakchodi.org/u/Rishabhmoodi) error found"
                                        Comment(id, conte)
                                elif 'mp4' in url:
                                    # print('starting' + 'a ' + str(a) + 'i ' + str(i))
                                    try:
                                        url = url
                                        mp4(id, url)
                                        done.append(str(id)) 
                                    except Exception as e:
                                        print(e)
                                        pass
                                
                                if 'https://videoplayer2.rishabh.ml/rvideo' in url:
                                    if 'https://videoplayer2.rishabh.ml/rvideo2/?url=' in url:
                                        # dl1 = url.replace("<div class='embed-responsive embed-responsive-16by9'><iframe src='https://videoplayer2.rishabh.ml/rvideo2/?url=", 'https://v.redd.it/')
                                        # dl2 = dl1.replace("' scrolling='0' allowfullscreen></iframe></div>", '')
                                        url1 = url.replace('https://videoplayer2.rishabh.ml/rvideo/?url=', '')
                                        download(id, url.replace("https://videoplayer2.rishabh.ml/rvideo2/?url=", 'https://v.redd.it/'))
                                        RedditDownloader(id, url1)
                                    if 'https://videoplayer2.rishabh.ml/rvideo/?url=' in url:
                                        url1 = url.replace('https://videoplayer2.rishabh.ml/rvideo2/?url=', '')
                                        RedditDownloader(id, url1)
                                    if 'https://videoplayer2.rishabh.ml/rvideo3/?url=' in url:
                                        url1 = url.replace('https://videoplayer2.rishabh.ml/rvideo3/?url=', '')
                                        RedditDownloader(id, url1)

                            # elif 'reddit.com' in r.json()['posts'][i]['post']['url']:
                            #     try:
                            #         red = requests.get(url + '.json')
                            #         if 'v.redd.it' in :
                            #             content("Reddit player build is under process....")
                            #             #content("`<iframe src='https://videoplayer2.rishabh.ml/rvideo/?url=" + red.json()[0].get('data').get('children')[0].get('data').get('url_overridden_by_dest') + "' height='260' width=100% allowfullscreen=True></iframe>`" + "<iframe src='https://videoplayer2.rishabh.ml/rvideo/?url=" + red.json()[0].get('data').get('children')[0].get('data').get('url_overridden_by_dest') + "' height='260' width=100% allowfullscreen=True></iframe>")
                            #             Comment(id, content)
                            #             done.append(id)
                            #     except Exception as e:
                            #         print(e)
                            #         conte = "post id " + id + " error " + e + "  [@Rishabhmoodi@bakchodi.org](https://bakchodi.org/u/Rishabhmoodi) error found"
                            #         Comment(id, conte)
                            

                            #elif '.com' in url:

                                    
                            #Body detect
                            
                          elif r.json()['posts'][i]['post']['body']:
                              body = r.json()['posts'][i]['post']['body']
                              if 'iframe' not in body:
                                if 'watermark' in body:
                                    if '.jpg' in url or '.png' in url:
                                        imagewatermark(url, id)
                                    else:
                                        videowatermark(id, url)
                                if 'youtu' in body:
                                # print('starting' + 'a ' + str(a) + 'i ' + str(i))
                                    yt(id, body)
                                    done.append(id)
                            
                                elif 'youtube.com/shorts' in body:

                                    # print('starting' + 'a ' + str(a) + 'i ' + str(i))
                                    ## try:
                                        result = body.replace('https://www.youtube.com/shorts/', '')
                                        content = "::: spoiler Invidious Embed code \n`::: spoiler Video` \n`<iframe src='https://invidious.snopyta.org/embed/" + result +  "' height='315' width=90% allowfullscreen=True></iframe>`\n`:::`\n:::\n" + "::: spoiler Youtube Code \n`::: spoiler Video` \n`<iframe width=90% height='315' src='https://www.youtube-nocookie.com/embed/" + result + "' title='bakchodi.org' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>`\n`:::`\n:::\n\n`::: spoiler Video `\n`<iframe width=90% height='315' src='https://www.youtube-nocookie.com/embed/" + result + "' title='bakchodi.org' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>`\n`:::`\n:::"
                                        Like(id, auth_embed)
                                        Comment(id, content)
                                        ytshort(id, body)
                                        done.append(id)
                                
                                if 'kapwing' in body or 'rumble.com' in body or 'instagram.com' in body or "[video]" in r.json()['posts'][i]['post']['name'] or "[Video]" in r.json()['posts'][i]['post']['name']:
                                    # print('starting' + 'a ' + str(a) + 'i ' + str(i))
                                    try:
                                        download(id, body)
                                        done.append(id)
                                        # with open ("done.txt", "a") as f:
                                        #     f.write(str(r.json()['private_messages'][i]['private_message']['id']) + '\n')
                                        time.sleep(10)
                                    except Exception as e:
                                        print(e)
                                        conte = "post id " + id + " error " + e + "  [@Rishabhmoodi@bakchodi.org](https://bakchodi.org/u/Rishabhmoodi) error found"
                                        Comment(id, conte)
                                elif 'mp4' in body:
                                    # print('starting' + 'a ' + str(a) + 'i ' + str(i))
                                    try:
                                        body = body
                                        mp4(id, body)
                                        done.append(str(id)) 
                                    except Exception as e:
                                        print(e)
                                        pass
                                
                                elif "iframe" not in body:
                                  if 'https://videoplayer2.rishabh.ml/rvideo' in body:
                                    if 'https://videoplayer2.rishabh.ml/rvideo/?url=' in body:
                                        body1 = body.replace('https://videoplayer2.rishabh.ml/rvideo/?url=', '')
                                        RedditDownloader(id, body1)
                                    if 'https://videoplayer2.rishabh.ml/rvideo2/?url=' in body:
                                        body1 = body.repplace('https://videoplayer2.rishabh.ml/rvideo2/?url=', '')
                                        RedditDownloader(id, body1)
                                    if 'https://videoplayer2.rishabh.ml/rvideo3/?url=' in body:
                                        body1 = body.replace('https://videoplayer2.rishabh.ml/rvideo3/?url=', '')
                                        RedditDownloader(id, body1)

                                    if 'https://videoplayer2.rishabh.ml/rvideo/?url=' in body:
                                        body1 = body.replace('https://videoplayer2.rishabh.ml/rvideo/?url=', '')
                                        RedditDownloader(id, body1)
                                        # elif '1watermark' in r.json()['posts'][i]['post']['body']:
                                #     try:
                                #         Like(id, auth_embed)
                                #         os.system('./yt-dlp -o' + id + 'video1.mp4 ' + url)                       
                                #         time.sleep(5)
                                #         os.system("ffmpeg -i " + id + "video1.mp4 -i video-watermark1.jpg -filter_complex 'overlay=main_w-overlay_w-50:main_h-overlay_h-250' -codec:a copy " + id + "video.mp4 -y")
                                #         os.system("./rclone copy " + id + 'video.mp4 m: --ignore-existing')
                                #         time.sleep(20)
                                #         content = "::: spoiler Server Code \n`::: spoiler Video`\n\n`<iframe src='https://videoplayer.rishabh.ml/v/?url=https://backend.rishabh.ml/1:/serv/" + id + "video.mp4' height='360' width=100% allowfullscreen=True></iframe>`\n\n`:::`\n:::" 
                                #         Comment(id, content)
                                #     except Exception as e:
                                #         print(e)
                                #         conte = "post id " + id + " error " + e + "  [@Rishabhmoodi@bakchodi.org](https://bakchodi.org/u/Rishabhmoodi) error found"
                                #         Comment(id, conte)
                                # elif r.json()['posts'][i]['post']['community_id'] == 18 or r.json()['posts'][i]['post']['community_id'] == 8:
                                #     if '.jpg' in url or '.png' in url or '.jpeg' in url:
                                #         imagewatermark(url, id)
                                # elif ' watermark' in name:
                                #     if '.jpg' in url or '.png' in url or '.jpeg' in url:
                                #         imagewatermark(url, id)
                                #     else:
                                #         videowatermark()
                            #elif '.com' in url:
                            #     # print('starting' + 'a ' + str(a) + 'i ' + str(i))
                            #     # try:
                            #         id = str(r.json()['private_messages'][i]['private_message']['id'])
                            #         # print(id)
                            #         a += 1
                            #         # print('downloading')
                            #         os.system('./yt-dlp -o' + id + 'video.mp4 ' + r.json()['private_messages'][i]['private_message']['content'])                       
                            #         time.sleep(10)
                            #         # print('uploading')
                            #         os.system("./rclone copy " + id + 'video.mp4 m: --ignore-existing')
                            #         time.sleep(20)
                            #         recipient_id = r.json()['private_messages'][i]['creator']['id']
                            #         content = r.json()['private_messages'][i]['private_message']['content'] + " `<iframe src='https://videoplayer.rishabh.ml/v/?url=https://backend.rishabh.ml/1:/serv/" + id + "video.mp4' loading=lazy height='360' width='360' allowfullscreen=True></iframe>`  Copy The Embed code and Post"
                            #         # print(content)
                            #         private_message_id = r.json()['private_messages'][i]['private_message']['id']
                            #         postread1 = {"private_message_id": int(private_message_id), "read": True, "auth": auth}
                            #         postread = {k: v for k, v in postread1.items() if v}
                            #         createreadResponse = send_post_request("/private_message/mark_as_read", json_data=postread)
                            #         postData1 = {"content": content, "recipient_id": int(recipient_id), "auth": auth}
                            #         postData = {k: v for k, v in postData1.items() if v}
                            #         createPostResponse = send_post_request("/private_message", json_data=postData)
                            #         # print('response sent')
                            #         done.append(str(r.json()['private_messages'][i]['private_message']['id']))
                            #         # with open ("done.txt", "a") as f:
                            #         #     f.write(str(r.json()['private_messages'][i]['private_message']['id']) + '\n')
                            #         time.sleep(10)
                            #     except Exception as e:
                            #         print(e)
                            #         pass
                        #else:
                            

        time.sleep(120)
            # print(done)
    except Exception as e:
       time.sleep(100)
       print(e)
       print(done)


