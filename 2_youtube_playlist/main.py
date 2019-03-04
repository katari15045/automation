from requests import get
from youtube_dl import YoutubeDL

''' Task: Given a youtube playlist, download mp3 version of each song; filename of a downloaded .mp3 version of a song - 
should start with "song's position number in playlist" 
'''

class Main:

	api_key = "AIzaSyA8mzVl3pFTu_d-ak5Gtp1WjGn9hV13cPg"
	playlist_id = "PLfRGVFjiprOwnKFo_38f6-_exN5gZMGof" # punjabi
	#playlist_id = "PLfRGVFjiprOzs2awqwuO5KeagE36Ub0FG" # english
	max_results = "50"

	@staticmethod
	def main():
		url_api = "https://www.googleapis.com/youtube/v3/playlistItems"
		params_g_api = {"part":"snippet", "maxResults":Main.max_results, "playlistId":Main.playlist_id, 'key':Main.api_key}		
		next_page_token = "dummy"
		song_num = 1
		while(next_page_token != None):
			response = get(url=url_api, params=params_g_api)
			response = response.json()
			ind = 0
			while(ind < len(response["items"])):
				video_id = response["items"][ind]["snippet"]["resourceId"]["videoId"]
				video_title = response["items"][ind]["snippet"]["title"]
				video_title = video_title.replace(" ", "_")
				video_title = str(song_num) + "_" + video_title
				url_video = "https://www.youtube.com/watch?v=" + video_id
				params_y_api = {'format':'bestaudio', 'outtmpl': video_title + '.%(ext)s'}
				with YoutubeDL(params_y_api) as ydl:
					print("Song " + str(song_num) + " ...")
					ydl.download([url_video])
				song_num = song_num+1
				ind = ind+1
			next_page_token = response.get("nextPageToken")
			if(next_page_token != None):
				params_g_api["pageToken"] = next_page_token
Main.main()