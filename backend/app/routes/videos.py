from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.deps import get_database
from app.models.video import Video
from app.schemas.video import VideoCreate, VideoResponse

router = APIRouter(
    prefix="/videos",
    tags=["Videos"]
)


@router.post("/", response_model=VideoResponse)
def create_video(
    video: VideoCreate,
    db: Session = Depends(get_database)
):

    new_video = Video(
        title=video.title,
        description=video.description,
        video_url=video.video_url
    )

    db.add(new_video)
    db.commit()
    db.refresh(new_video)

    return new_video