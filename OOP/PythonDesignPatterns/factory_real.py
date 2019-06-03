### FACTORY Method (Creational Pattern)


# Instead of using complex (if/elif/else) conditional structure
# for determiningtthe concrete implementation a class can
# delegate this decision to another component (class)


import json
import xml.etree.ElementTree as et


class Song:

    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

class SongSerializer:
    """  convert a song object into its string representation
    according to the value of the format parameter
    """
    
    def serialize(self, song, format):
        """ song : instane of SONG class """
        
        if format == 'JSON':
            song_info = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            }
            return json.dumps(song_info)
        
        elif format == 'XML':
            song_info = et.Element('song', attrib={'id': song.song_id})
            title = et.SubElement(song_info, 'title')
            title.text = song.title
            artist = et.SubElement(song_info, 'artist')
            artist.text = song.artist
            return et.tostring(song_info, encoding='unicode')

        elif format =="YML":
            raise NotImplementedError
        
        else:
            raise ValueError(format)


if __name__ == "__main__":

    #create song obj
    s = Song(1,"Dance","Chris Brown")

    SongSerializer().serialize(s,"JSON")
    SongSerializer().serialize(s,"XML")

     
