import sys
import os

# STEP 1: Comment the main() function
# STEP 2: Complete the code for the eight class methods below that have no code.
#           Note: in this program we are keeping track of types and token separately for each song, and then also
#           creating a type and token summary number for the artist that combines all of their songs together.
#           Feel free to refer back to our code from earlier weeks. But you will probably need to adapt it slightly
#           If you want to test yourself, coding it from scratch again is good practice.
#           HINT: you dont need to count freqs, types, and tokens twice.
#           Do it for the songs
#           Then, combine the freq dictionaries for each song to create one summary freq dictionary for the artist
#           Then you can count the artist's overall types and tokens from that summary dictionary

class Artist:

    def __init__(self, name, directory_location):#this sets up the parameters for the class artist
        self.name = name
        self.directory_location = directory_location
        self.num_songs = 0
        self.song_list = []
        self.lyric_freq_dict = {}
        self.num_tokens = 0
        self.num_types = 0

    def get_freq_dict(self):#place holders
        for song in self.song_list:
            a = counter(self.lyric_freq_dict)
            b = counter(song.lyric_freq_dict)
            c=a+b

    def get_word_type_sum(self):
        for song in self.song_list:    
            self.num_types += len(song.lyric_freq_dict)

    def get_word_token_sum(self):
        for song in self.song_list:
            self.num_tokens += len(song.lyric_list)

class Song:

    def __init__(self, title, file_location):#sets up stuff for the class song
        self.title = title
        self.file_location = file_location
        self.lyric_list = []
        self.lyric_freq_dict = {}
        self.num_tokens = 0
        self.num_types = 0

    def get_lyrics(self):#also place holders
        file = open(self.file_location)
        self.lyric_list= file.read().split(' ')

    def get_freq_dict(self):
        for word in self.lyric_list:
            if word in self.lyric_freq_dict:
                self.lyric_freq_dict[word] +=1
            else:
                self.lyric_freq_dict[word] =1

    def get_word_type_sum(self):
        for lyric_key in self.lyric_freq_dict:
            self.num_types += self.lyric_freq_dict[lyric_key]

    def get_word_token_sum(self):
        self.num_tokens= len(self.lyric_list)


def remove_hidden_files(input_list):# this creates the function, there is a list in it
    output_list = []
    for item in input_list:
        if item[0] != '.':# if the first item isnt a period then you can append it to the output list
            output_list.append(item)
    return output_list#then prints the output


def main():
    artist_object_list = []
    input_directory = sys.argv[1]
    artist_directory_list = os.listdir(input_directory)
    artist_list = remove_hidden_files(artist_directory_list)

    for artist_name in artist_list:#creates instances, goes through kanye and taylors stuff 10 times each bc 10 songs

        artist_directory = input_directory+artist_name
        new_artist_instance = Artist(artist_name, artist_directory)#this instanciates artists for the class, and we are assigning a class, the parameters are being extracted form out input
        song_directory_list = os.listdir(artist_directory)#creating a list of artist songs from artist directory
        song_filename_list = remove_hidden_files(song_directory_list)

        for song_filename in song_filename_list:#goes through each song in our song file list and goes into anye, looks at all its songs, and the title will be the songfile name
            song_title = song_filename[:-4]# just the song title will print not a .txt
            song_location = artist_directory + "/" + song_title+ ".txt"#goes into each artist directory
            new_song_instance = Song(song_title, song_location)#creates an instance and with each instance it neds a title and a location
            new_artist_instance.song_list.append(new_song_instance)
            new_song_instance.get_lyrics()
            new_song_instance.get_freq_dict()
            new_song_instance.get_word_type_sum()
            new_song_instance.get_word_token_sum()
            new_artist_instance.song_list.append(new_song_instance)

        artist_object_list.append(new_artist_instance)

    for i in range(len(artist_object_list)):
        artist = artist_object_list[i]
        print("{}     Types: {}      Tokens: {}".format(artist.name, artist.num_types, artist.num_tokens))
        for j in range(artist.num_songs):
            song = artist.song_list[j]
            print("     {}      Types: {}      Tokens: {}".format(song.title, song.num_types, song.num_tokens))


main()

