from os import listdir, rename

'''Task: You have 2 folders - english_songs and new_english_songs; files in new_english_songs are numbered as follows: 1_song_1.mp3, 2_song_2.mp3 ... 25_song_25.mp3; 
files in english_songs are names as follows: 1_song_1.mp3, 2_song_2.mp3 ... 100_song_100.mp3; you need to rename the songs in english_songs such that 
the final names would be 26_song_1.mp3, 27_song_2.mp3 ... 125_song_100.mp3. Why? after renaming, songs in new_english_songs are moved to english_songs'''

class Main:

	path = "D:\Saketh\Google Drive to Local\Mars\ent\Music\english_songs"

	@staticmethod
	def main():
		content = listdir(Main.path)
		ind = 0
		while(ind < len(content)):
			if("_" in content[ind] and ".mp3" in content[ind]):
				old_name = content[ind]
				word_arr = old_name.split("_")
				word_arr[0] = str(int(word_arr[0]) + 25)
				ind_2 = 0
				new_name = ""
				while(ind_2 < len(word_arr)):
					if(ind_2 != 0):
						new_name = new_name + "_"
					new_name = new_name + word_arr[ind_2]
					ind_2 = ind_2+1
				old_path = Main.path + "\\" + old_name
				new_path = Main.path + "\\" + new_name
				rename(old_path, new_path)
			ind = ind+1

Main.main()