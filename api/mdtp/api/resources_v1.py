import datetime
from typing import Dict
from typing import Optional

from core.s3_manager import S3PresignedUpload
from pydantic import BaseModel

from mdtp.model import GridItem
from mdtp.model import StatItem
from mdtp.model import BaseImage

class ApiGridItem(BaseModel):
    gridItemId: int
    updatedDate: datetime.datetime
    network: str
    tokenId: int
    title: str
    description: Optional[str]
    imageUrl: str
    resizableImageUrl: Optional[str]
    ownerId: str

    @classmethod
    def from_model(cls, model: GridItem, shouldCompact: bool = False):
        return cls(
            gridItemId=model.gridItemId,
            updatedDate=model.updatedDate,
            network=model.network,
            tokenId=model.tokenId,
            title=model.title,
            description=model.description if not shouldCompact else None,
            imageUrl=model.imageUrl,
            resizableImageUrl=model.resizableImageUrl,
            ownerId=model.ownerId,
        )

class ApiStatItem(BaseModel):
    statItemId: int
    title: str
    data: str

    @classmethod
    def from_model(cls, model: StatItem):
        return cls(
            statItemId=model.statItemId,
            title=model.title,
            data=model.data,
        )

class ApiPresignedUpload(BaseModel):
    url: str
    params: Dict[str, str]

    @classmethod
    def from_model(cls, model: S3PresignedUpload):
        return cls(
            url=model.url,
            params={field.name: field.value for field in model.fields},
        )

class ApiBaseImage(BaseModel):
    baseImageId: int
    network: str
    updatedDate: datetime.datetime
    url: str

    @classmethod
    def from_model(cls, model: BaseImage):
        return cls(
            baseImageId=model.baseImageId,
            network=model.network,
            updatedDate=model.updatedDate,
            url=model.url,
        )
