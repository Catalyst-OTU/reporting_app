from typing import Any,Dict,Generic,Type,TypeVar,Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, UUID4
from sqlalchemy.orm import Session
from . import schemas
from . import models





# Define custom types for SQLAlchemy model, and Pydantic schemas
ModelType = TypeVar("ModelType", bound=models.Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)





class BaseActions(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        """Base class that can be extend by other action classes.
           Provides basic CRUD and listing operations.

        :param model: The SQLAlchemy model
        :type model: Type[ModelType]
        """
        self.model = model



    def get_all(self, db: Session, *, skip: int = 0, limit: int = 100):
        return db.query(self.model).offset(skip).limit(limit).all()
    


    def get(self, db: Session, id: UUID4):
        return db.query(self.model).filter(self.model.id == id).first()

    def create(self, db: Session, *, obj_in: CreateSchemaType):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ):
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: UUID4):
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
    








#SituationReportCategory BaseActions
class SituationReportCategoryActions(BaseActions[models.SituationReportCategory, schemas.CreateSituationReportCategory, schemas.UpdateSituationReportCategory]):

    pass



#SituationReport BaseActions
class SituationReportActions(BaseActions[models.SituationReport, schemas.CreateSituationReport, schemas.UpdateSituationReport]):

    pass



#SituationReportAttachment BaseActions
class SituationReportAttachmentActions(BaseActions[models.SituationReportAttachment, schemas.CreateSituationReportAttachment, schemas.UpdateSituationReportAttachment]):

    pass



#SituationReportComment BaseActions
class SituationReportCommentActions(BaseActions[models.SituationReportComment, schemas.CreateSituationReportComment, schemas.UpdateSituationReportComment]):

    pass




#SiteReportCommentFile BaseActions
class SiteReportCommentFileActions(BaseActions[models.SiteReportCommentFile, schemas.CreateSiteReportCommentFile, schemas.UpdateSiteReportCommentFile]):

    pass




#SiteReportTask BaseActions
class SiteReportTaskActions(BaseActions[models.SiteReportTask, schemas.CreateSiteReportTask, schemas.UpdateSiteReportTask]):

    pass




#SiteReportActivity BaseActions
class SiteReportActivityActions(BaseActions[models.SiteReportActivity, schemas.CreateSiteReportActivity, schemas.UpdateSiteReportActivity]):

    pass




#ReportTeam BaseActions
class ReportTeamActions(BaseActions[models.ReportTeam, schemas.CreateReportTeam, schemas.UpdateReportTeam]):

    pass




#ReportStaff BaseActions
class ReportStaffActions(BaseActions[models.ReportStaff, schemas.CreateReportStaff, schemas.UpdateReportStaff]):

    pass




#Memorandum BaseActions
class MemorandumActions(BaseActions[models.Memorandum, schemas.CreateMemorandum, schemas.UpdateMemorandum]):

    pass



#MemorandumComment BaseActions
class MemorandumCommentActions(BaseActions[models.MemorandumComment, schemas.CreateMemorandumComment, schemas.UpdateMemorandumComment]):

    pass




#Task BaseActions
class TaskActions(BaseActions[models.Task, schemas.CreateTask, schemas.UpdateTask]):

    pass





#Activities BaseActions
class ActivitiesActions(BaseActions[models.Activities, schemas.CreateActivities, schemas.UpdateActivities]):

    pass


