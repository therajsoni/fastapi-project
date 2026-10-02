from pydantic import BaseModel


class VideoCreate(BaseModel):
    title: str
    description: str | None = None
    video_url: str


class VideoResponse(VideoCreate):
    id: int

    model_config = {
        "from_attributes": True
    }