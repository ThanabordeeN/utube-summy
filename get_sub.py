from youtube_transcript_api import YouTubeTranscriptApi 
  
# assigning srt variable with the list 
# of dictionaries obtained by the get_transcript() function
def get_transcript(link):
    video_id = link.split("v=")[1]
    try:
        srt = YouTubeTranscriptApi.get_transcript(video_id)
        return srt

    except: 
        return "There are no transcripts for this Video"
        
  
# prints the result
