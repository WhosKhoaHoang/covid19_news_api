import os
from apiclient.discovery import build
from dotenv import load_dotenv
load_dotenv()



class Covid19YouTube:
    """
    A class that retrieves and processes YouTube videos
    about COVID-19 using the YouTube Data API.
    """

    def __init__(self, api_key=os.getenv("YT_API_KEY")):
        """
        Initializes an instance of Covid19YouTube.
        @api_key: The API key to use for the YouTube
                  Data API
        type api_key: str
        return: None
        rtype: None
        """
        self._youtube = build("youtube", "v3", developerKey=api_key)


    def get_videos(self, region):
        """
        Gets YouTube video information associated with the provided region.
        @region: The region to retrieve COVID-19 related videos for
        type region: str
        return: A list of dicts containing information about COVID-19
                videos associated with the provided region
        rtype: [dict]
        """
        # Note that the default number of search results is 5. You
        # can tweak the value by setting the parameter maxResults
        req = self._youtube.search().list(q=f"coronavirus update {region}",
                                          part="snippet", type="video",
                                          order="date")
        result = req.execute()

        # FOR REFERENCE:
        #for item in result["items"]:
        #    print(item["snippet"]["title"])

        return result["items"]


if __name__ == "__main__":
    c_youtube = Covid19YouTube()
    lst = c_youtube.get_videos("japan")
    print(lst[0])
