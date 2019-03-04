from requests import get

class Main:

	api_key = "AIzaSyA8mzVl3pFTu_d-ak5Gtp1WjGn9hV13cPg"
	playlist_id = "PLfRGVFjiprOwnKFo_38f6-_exN5gZMGof" # punjabi
	#playlist_id = "PLfRGVFjiprOzs2awqwuO5KeagE36Ub0FG" # english
	max_results = "50"

	@staticmethod
	def main():
		url_api = "https://www.googleapis.com/youtube/v3/playlistItems"
		params_api = {"part":"snippet", "maxResults":Main.max_results, "playlistId":Main.playlist_id, 'key':Main.api_key}		
		url_videos = []
		next_page_token = "dummy"
		while(next_page_token != None):
			response = get(url=url_api, params=params_api)
			response = response.json()
			ind = 0
			while(ind < len(response["items"])):
				video_id = response["items"][ind]["snippet"]["resourceId"]["videoId"]
				url_video = "https://www.youtube.com/watch?v=" + video_id
				url_videos.append(url_video)
				ind = ind+1
			next_page_token = response.get("nextPageToken")
			if(next_page_token != None):
				params_api["pageToken"] = next_page_token
		print(url_videos)
		print(len(url_videos))

Main.main()