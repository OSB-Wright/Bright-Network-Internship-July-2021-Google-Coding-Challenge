"""A video player class."""
#import random module
import random
from .video_playlist import Playlist
from .video_library import VideoLibrary

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.video_playing = False #attribute tells stores data about the video that is currently playing. Set to false when nothing is playing
        self.video_paused = False #attribute tells us if the current video playing is paused or not.
        self.playlists = [] #attribute stores playlists as a list.

    def find_video_data_from_title(self, video_title):
        #This method finds and returns the data (video_id and tags attributes) of a video using its title attribute

        video_list = self._video_library.get_all_videos()
        ids = ""
        tag = ""
        for video in video_list:
            if video_title == video.title:
                ids = video.video_id
                tag = video.tags
        return ids, tag

    def format_tag(self, video_tag):
        #This method formats the tags attribute for the videos by removing the brackets, comma and apostrophes.

        tag = str(video_tag)
        tag = tag.replace("(","")
        tag = tag.replace(")","")
        tag = tag.replace("'","")
        tag = tag.replace(",","")
        return tag

    def find_video_info_using_id(self, video_id):
        #This method finds and returns the data (title and tags attributes) of a video using its id attribute

        video_list = self._video_library.get_all_videos()
        video_found = False
        title = ""
        tag = ""
        for video in video_list:
            if video_id == video.video_id:
                video_found = True
                title = video.title
                tag = video.tags
                break
        
        return video_found, title, tag

    def check_playlist_exists(self, playlist_name):
        #This method checks whether a playlist exists and returns a boolean value and the index of the playlist in playlists attribute
        
        playlist_name_exists = False
        position = 0
        for index in range(len(self.playlists)):
                   if str(playlist_name).upper() == str(self.playlists[index].name).upper():
                       playlist_name_exists = True
                       position = index
                       break
        return playlist_name_exists, position

    def check_video_id_exists_in_playlist(self, video_id, playlist_index):
        #This method checks if a video id exists withing a playlist and returns a boolean value
        
        video_in_playlist = False
        for playlist_video_id in self.playlists[playlist_index].playlist_video_ids:
            if playlist_video_id == video_id:
                video_in_playlist = True
                break
        return video_in_playlist
        

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        video_list = self._video_library.get_all_videos() #stores videos as objects in a list
        video_data = []
        for video in video_list: #loops through each object and extracts attributes
            tag = self.format_tag(video.tags)#formats tags attribute of video
            video_data.append(str(video.title) + " (" + str(video.video_id) + ") " + "[" + str(tag) + "]")
        video_data.sort() #sorts videos by title
        print("Here's a list of all available videos:")
        for video in video_data: #prints video data from sorted list
            print("  " + video)
            
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        [video_found, title, raw_tag] = self.find_video_info_using_id(video_id) #checks if video exists and retrieves data

        if video_found == True: #code below only executed if video exists

            if self.video_playing != False:#message below is printed if a video is currently playing
                    print("Stopping video: " + self.video_playing[0])

            print("Playing video: " + str(title))
            tag = self.format_tag(raw_tag)
            self.video_paused = False #set to false as new video is playing
            self.video_playing = [str(title), str(video_id), str(tag)] #stores data of video currently playing

        else:
            print("Cannot play video: Video does not exist") 
       

    def stop_video(self):
        """Stops the current video."""
        #method checks if there is a video currently playing
        if self.video_playing == False:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: " + self.video_playing[0])
            self.video_playing = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        video_list = self._video_library.get_all_videos()
        random_video = random.choice(video_list) #random module allows us to select random element from the list of videos
        if self.video_playing != False:
            print("Stopping video: " + self.video_playing[0])
        print("Playing video: " + random_video.title)
        tag = self.format_tag(random_video.tags)
        self.video_paused = False
        self.video_playing = [str(random_video.title), str(random_video.video_id), str(tag)]

    def pause_video(self):
        """Pauses the current video."""
        #checks if theres a video playing, then if the video playing is already paused
        if self.video_playing == False:
            print("Cannot pause video: No video is currently playing")
        elif self.video_paused == True:
            print("Video already paused: " + self.video_playing[0])
        else:
            print("Pausing video: " + self.video_playing[0])
            self.video_paused = True

    def continue_video(self):
        """Resumes playing the current video."""
        #checks if theres a video playing and then if the video playing is paused or not
        if self.video_playing == False:
            print("Cannot continue video: No video is currently playing")
        elif self.video_paused == False:
            print("Cannot continue video: Video is not paused" + self.video_playing[0])
        else:
            print("Continuing video: " + self.video_playing[0])
            self.video_paused = True

    def show_playing(self):
        """Displays video currently playing."""
        if self.video_playing == False: #line checks if a video is playing
            print("No video is currently playing")
        else:
            #prints data from video_playing attribute and whether its paused or not
            if self.video_paused == True:
                print("Currently playing: " + str(self.video_playing[0]) + " (" + str(self.video_playing[1]) + ") " + "[" +str(self.video_playing[2] + "]") + " - PAUSED")
            else:
                print("Currently playing: " + str(self.video_playing[0]) + " (" + str(self.video_playing[1]) + ") " + "[" + str(self.video_playing[2]) + "]")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        [playlist_name_exists, position] = self.check_playlist_exists(playlist_name) #checks if playlist name exists already
        
        if playlist_name_exists == True:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            #adds the new playlist to the playlists attribute
            new_playlist = Playlist(playlist_name)
            self.playlists.append(new_playlist)
            print("Successfully created new playlist: " + new_playlist.name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        [playlist_name_exists, position] = self.check_playlist_exists(playlist_name) #checks the requested playlist exists and finds its index in playlists attribute
        [video_found, title, raw_tag] = self.find_video_info_using_id(video_id)#checks if the video exist and returns its data (attributes)
    
        if video_found == True and playlist_name_exists == True: 
            video_in_playlist = self.check_video_id_exists_in_playlist(video_id, position) #if the playlist and video exist this line checks if the video is already in the playlist
            if video_in_playlist == True:
                print("Cannot add video to " + playlist_name + ": Video already added")
            else:
                self.playlists[position].playlist_video_ids.append(video_id)#video's id is added to the playlist_video_ids attribute in playlist class
                print("Added video to " + playlist_name + ": " + title)

        elif playlist_name_exists == False: #error messages displayed if playlist or video doesnt exist
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")
        else:
            print("Cannot add video to " + playlist_name + ": Video does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self.playlists) == 0: #checks if playlist is empty or not
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            playlist_names = []
            for playlist in self.playlists: #loops through playlists attribute and displays each playlist alphabetically 
                playlist_names.append(playlist.name)
            playlist_names.sort()
            for names in playlist_names:
                print("  " + names)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        [playlist_name_exists, position] = self.check_playlist_exists(playlist_name)#this line checks the playlist exists and returns its index in playists
        if playlist_name_exists == False:
            print("Cannot show playlist " + playlist_name + ": Playlist does not exist")
        else:
            print("Showing playlist: " + playlist_name)
            if len(self.playlists[position].playlist_video_ids) == 0: #this line prints if the playlist is empty (no elements stored in playlist_video_id attributes)
                print("  No videos here yet")
            else:
                for video_id in self.playlists[position].playlist_video_ids: 
                    [video_found, title, raw_tag] = self.find_video_info_using_id(video_id)#for each id in a playlist, this method is used to find its title and tags which are displayed
                    tag = self.format_tag(raw_tag)
                    print(str(title) + " (" + str(video_id) + ") " + "[" + str(tag) + "]")
            
        
        

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        
        [video_found, title, raw_tag] = self.find_video_info_using_id(video_id)#checks video exists 
        [playlist_name_exists, position] = self.check_playlist_exists(playlist_name)#checks playlist exists and returns its idndex
        
        if playlist_name_exists == False:
            print("Cannot remove video from " + playlist_name + ": Playlist does not exist")
        elif video_found == False:
            print("Cannot remove video from " + playlist_name + ": Video does not exist")
        else:
            video_in_playlist = self.check_video_id_exists_in_playlist(video_id, position)
            if video_in_playlist == False:
                print("Cannot remove video from " + playlist_name + ": Video is not in playlist")
            else:
                self.playlists[position].playlist_video_ids.remove(video_id)#removes specified id from the playlist
                print("Removed video from " + playlist_name + ": " + title)
                
        

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        [playlist_name_exists, position] = self.check_playlist_exists(playlist_name)#checks playlist exists and returns its index
        if playlist_name_exists == False:
            print("Cannot clear playlist " + playlist_name + ": Playlist does not exist")
        else:
            for id_index in range(len(self.playlists[position].playlist_video_ids)):
                self.playlists[position].playlist_video_ids.pop(id_index)#removes all ids stored in a playlists playlist_video_id attribute
            print("Successfully removed all videos from " + playlist_name)
            

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        [playlist_name_exists, position] = self.check_playlist_exists(playlist_name) #check if playlist exists
        if playlist_name_exists == False:
            print("Cannot delete playlist " + playlist_name + ": Playlist does not exist")
        else:
            self.playlists.pop(position)#deletes a playlist from playlists attribute
            print("Deleted playlist: " + playlist_name)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        video_list = self._video_library.get_all_videos()
        video_data = []
        video_titles = []
        no_results = True
        integer_input = False
        for video in video_list: #compares search term with video titles ignoring case sensitivity
            if str(search_term).upper() in str(video.title).upper():
                no_results = False
                video_titles.append(video.title)
                tag = self.format_tag(video.tags)
                video_data.append(str(video.title) + " (" + str(video.video_id) + ") " + "[" + str(tag) + "]")
                video_data.sort()
                video_titles.sort()
        if no_results == True: #prints message below if no matches could be found
            print("No search results for " + str(search_term))
        else:
            label = 1 # used to list and index the videos
            print("Here are the results for " + str(search_term) + ":")
            for video in video_data:
                print(str(label) + ") " + str(video))
                label = label + 1
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            user_choice = str(input())# asks for user to input their choice
            try:
                user_choice = int(user_choice)#tests user input is an integer
                integer_input = True
            except:
                ()
            if integer_input == True and int(user_choice) <= label and int(user_choice) > 0: #checks users input is within the specified range
                index = user_choice - 1
                [video_id, video_tag] = self.find_video_data_from_title(video_titles[index]) #finds the data for the selected video and calls the play_video() method
                self.play_video(video_id)
            else:
                ()

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        video_list = self._video_library.get_all_videos()
        video_data = []
        video_titles = []
        no_results = True
        integer_input = False
        for video in video_list:#compares search term with video tags ignoring case sensitivity
            tag = self.format_tag(video.tags)
            if str(video_tag).upper() in str(tag).upper():
                no_results = False
                video_titles.append(video.title)
                video_data.append(str(video.title) + " (" + str(video.video_id) + ") " + "[" + str(tag) + "]")
                video_data.sort()
                video_titles.sort()
        if no_results == True: #prints message below if no matches could be found
            print("No search results for " + str(video_tag))
        else:
            label = 1 # used to list and index the videos
            print("Here are the results for " + str(video_tag) + ":")
            for video in video_data:
                print(str(label) + ") " + str(video))
                label = label + 1
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            user_choice = str(input())
            try:
                user_choice = int(user_choice) #checks if user input is an integer
                integer_input = True 
            except:
                ()
            if integer_input == True and int(user_choice) <= label and int(user_choice) > 0: #checks users input is within the specified range
                index = user_choice - 1
                [video_id, video_tag] = self.find_video_data_from_title(video_titles[index]) #finds the data for the selected video and calls the play_video() method
                self.play_video(video_id)
            else:
                ()

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """

        print("allow_video needs implementation")
        
    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
