import googleapiclient.discovery
import googleapiclient.errors
import csv

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBdzAfHlGUdkudF5jYAuGwHonDF1GwoezI"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

video_ids = ["PvlhJPtEstA", "WDk0jy-CiLs", "YSoc5kR0RP8", "g1fdVs3uJnA", "xzIKCYl4z38", "c7b74Ex-kCA", "zPRIW50IYGU", "wNU59vgr6mk", "zpMKoC-B7w4", ]

def fetch_and_write_comments(video_id, csv_writer):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100, 
        textFormat="plainText"
    )
    while request:
        response = request.execute()

        for item in response['items']:
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            csv_writer.writerow([video_id, author, comment]) 

        request = youtube.commentThreads().list_next(request, response)

with open('youtube_comments.csv', 'a', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    if csv_file.tell() == 0:
        csv_writer.writerow(['Video ID', 'Author', 'Comment'])

    for video_id in video_ids:
        fetch_and_write_comments(video_id, csv_writer)
