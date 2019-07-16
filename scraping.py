# -*- coding: utf-8 -*-


import requests
import settings



class Youtube:
    
    
    def __init__(self, video_id, n=10):
        self.URL = 'https://www.googleapis.com/youtube/v3/'
        
        self.video_id = video_id
        self.resource = self._get_video(n)
        
        
        
        self.comments = self._get_comments()
        self.eval_response = self._get_eval()
        
    def _get_video(self, n=10):
        API_KEY = settings.AP
        params = {
            'key': API_KEY,
            'part': 'snippet',
            'videoId': self.video_id,
            'order': 'time',
            'textFormat': 'plaintext',
            'maxResults': n,
        }
        
        response = requests.get(self.URL + 'commentThreads', params=params)
        
        return response.json()
        
        
    def _get_comments(self):
        text_lists = []
        for comment_info in self.resource['items']:
            #名前
            name = comment_info['snippet']['topLevelComment']['snippet']['authorDisplayName']
            # コメント
            text = comment_info['snippet']['topLevelComment']['snippet']['textDisplay']
            text = text.replace('\n','')
            text_lists.append(text)
            # グッド数
#            like_cnt = comment_info['snippet']['topLevelComment']['snippet']['likeCount']
            # 返信数
#            reply_cnt = comment_info['snippet']['totalReplyCount']
        return text_lists
    
    def _get_eval(self):
        
        comments = "\n".join(self.comments)
        
        #APIキーを入力
        key = settings.AP
        #APIのURL
        url = 'https://language.googleapis.com/v1/documents:analyzeSentiment?key=' + key
         
        #基本情報の設定 JAをENにすれば英語のテキストを解析可能
        header = {'Content-Type': 'application/json'}
        body = {
            "document": {
                "type": "PLAIN_TEXT",
                "language": "JA",
                "content": comments
            },
            "encodingType": "UTF8"
        }
         
        #json形式で結果を受け取る。
        return requests.post(url, headers=header, json=body).json()
    
    def get_eval(self, log=False):
        
        total = {"total_magnitude": self.eval_response["documentSentiment"]["magnitude"],
                "total_score": self.eval_response["documentSentiment"]["score"]}
        
        if log:
            total["log"] = []
            for sentence in self.eval_response["sentences"]:
                total["log"].append(
                        {
                        "content": sentence["text"]["content"],
                        "magnitude": sentence["sentiment"]["magnitude"],
                        "score:": sentence["sentiment"]["score"]
                        }
                  )
        
        return total
        

    def get_youbou(self):
        b=0
        c=0
        for comment in self.comments:
            
            ins_f = lambda word: word in comment
            b+=1
            if any(map(ins_f,("ほしい", "いいな", "いいなぁ"))):
                c+=1
                print(comment)
        return b, c



#youtube_page = Youtube('YSefF0u1Vb0', 50)
#text = youtube_page.get_youbou()

#for comment in youtube_page.comments:
#    
#    ins_f = lambda word: word in comment
#    if any(map(ins_f,("ほしい", "いいな", "いいなぁ"))):
#        print(comment)
    
