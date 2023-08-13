import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6132728857:AAHX16VnWQl1fqto91_7M4H8eQ6IxCkI9cs")
    
    API_ID = int(os.environ.get("API_ID", "20244111"))
    
    API_HASH = os.environ.get("API_HASH","b76d27da2a4220fe109fe9ef0e866530")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5572938538"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://gasofe1633:Jobijobi@1@cluster0.taf0uzx.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
