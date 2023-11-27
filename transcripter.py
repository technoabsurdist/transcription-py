from langchain.document_loaders import YoutubeLoader

def transcription(url: str):
    loader = YoutubeLoader.from_youtube_url(
        url, add_video_info=True
    )
    documents = loader.load()
    print(documents)
    text = [doc.page_content for doc in documents][0]
    metadata = [doc.metadata for doc in documents][0]
    return text, metadata