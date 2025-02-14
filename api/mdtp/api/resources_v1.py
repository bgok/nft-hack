import datetime
from typing import Dict
from typing import Optional

from core.s3_manager import S3PresignedUpload
from pydantic import BaseModel

from mdtp.model import GridItem, NetworkSummary
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

class ApiNetworkSummary(BaseModel):
    marketCapitalization: float
    totalSales: int
    averagePrice: float

    @classmethod
    def from_model(cls, model: NetworkSummary):
        return cls(
            marketCapitalization=model.marketCapitalization,
            totalSales=model.totalSales,
            averagePrice=model.averagePrice,
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
    url: str
    generatedDate: datetime.datetime

    @classmethod
    def from_model(cls, model: BaseImage):
        return cls(
            baseImageId=model.baseImageId,
            network=model.network,
            url=model.url,
            generatedDate=model.generatedDate,
        )
