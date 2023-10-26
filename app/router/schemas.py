from pydantic import BaseModel,UUID4
from typing import Optional
from enum import Enum





class Roles(str, Enum):
    admin = "admin"
    user = "user"







# Shared  SituationReportCategory properties
class SituationReportCategoryBase(BaseModel):
    category: Optional[str] = None


# Properties to receive via API on creation
class CreateSituationReportCategory(SituationReportCategoryBase):
    category: str


# Properties to receive via API on update
class UpdateSituationReportCategory(SituationReportCategoryBase):
    pass



class SituationReportCategoryInDBBase(SituationReportCategoryBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class SituationReportCategory(SituationReportCategoryInDBBase):
    pass












# Shared properties
class SituationReportBase(BaseModel):
    report_category_id: Optional[UUID4] = None
    classification: Optional[str] = None
    confidential: Optional[str] = None
    file_number : Optional[str] = None
    date : Optional[str] = None
    primary_heading : Optional[str] = None
    secondary_heading : Optional[str] = None
    conclusion : Optional[str] = None
    recomendation : Optional[str] = None
    reference : Optional[str] = None
    sent_to : Optional[str] = None





# Properties to receive via API on creation
class CreateSituationReport(SituationReportBase):
    report_category_id: Optional[UUID4] = None
    classification : Optional[str] = None
    confidential : Optional[str] = None
    file_number : Optional[str] = None
    date : Optional[str] = None
    primary_heading : Optional[str] = None
    secondary_heading : Optional[str] = None
    conclusion : Optional[str] = None
    recomendation : Optional[str] = None
    reference : Optional[str] = None
    sent_to : Optional[str] = None


# Properties to receive via API on update
class UpdateSituationReport(SituationReportBase):
    pass



class SituationReportInDBBase(SituationReportBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class SituationReport(SituationReportInDBBase):
    pass















# Shared properties
class SituationReportAttachmentBase(BaseModel):
    situation_report_id: Optional[UUID4] = None
    file_name : Optional[str] = None
    file_type : Optional[str] = None
    file_url : Optional[str] = None
    description : Optional[str] = None
    keywords : Optional[str] = None
    tags : Optional[str] = None




# Properties to receive via API on creation
class CreateSituationReportAttachment(SituationReportAttachmentBase):
    situation_report_id: Optional[UUID4] = None
    file_name : Optional[str] = None
    file_type : Optional[str] = None
    file_url : Optional[str] = None
    description : Optional[str] = None
    keywords : Optional[str] = None
    tags : Optional[str] = None


# Properties to receive via API on update
class UpdateSituationReportAttachment(SituationReportAttachmentBase):
    pass



class SituationReportAttachmentInDBBase(SituationReportAttachmentBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class SituationReportAttachment(SituationReportAttachmentInDBBase):
    pass














# Shared properties
class SituationReportCommentBase(BaseModel):
    situation_report_id: Optional[UUID4] = None
    comment : Optional[str] = None
    commented_by : Optional[str] = None





# Properties to receive via API on creation
class CreateSituationReportComment(SituationReportCommentBase):
    situation_report_id: Optional[UUID4] = None
    comment : Optional[str] = None
    commented_by : Optional[str] = None


# Properties to receive via API on update
class UpdateSituationReportComment(SituationReportCommentBase):
    pass



class SituationReportCommentInDBBase(SituationReportCommentBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class SituationReportComment(SituationReportCommentInDBBase):
    pass










# Shared properties
class SiteReportCommentFileBase(BaseModel):
    situation_report_id: Optional[UUID4] = None
    comment_id: Optional[UUID4] = None
    comment : Optional[str] = None
    commented_by : Optional[str] = None




# Properties to receive via API on creation
class CreateSiteReportCommentFile(SiteReportCommentFileBase):
    situation_report_id: Optional[UUID4] = None
    comment_id: Optional[UUID4] = None
    comment : Optional[str] = None
    commented_by : Optional[str] = None


# Properties to receive via API on update
class UpdateSiteReportCommentFile(SiteReportCommentFileBase):
    pass



class SiteReportCommentFileInDBBase(SiteReportCommentFileBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class SiteReportCommentFile(SiteReportCommentFileInDBBase):
    pass











# Shared properties
class SiteReportTaskBase(BaseModel):
    situation_report_id: Optional[UUID4] = None
    name : Optional[str] = None
    description : Optional[str] = None
    note : Optional[str] = None



# Properties to receive via API on creation
class CreateSiteReportTask(SiteReportTaskBase):
    situation_report_id: Optional[UUID4] = None
    name : Optional[str] = None
    description : Optional[str] = None
    note : Optional[str] = None


# Properties to receive via API on update
class UpdateSiteReportTask(SiteReportTaskBase):
    pass



class SiteReportTaskInDBBase(SiteReportTaskBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class SiteReportTask(SiteReportTaskInDBBase):
    pass








# Shared SiteReportActivity properties
class SiteReportActivityBase(BaseModel):
    situation_report_id: Optional[UUID4] = None
    situation_report_task_id: Optional[UUID4] = None
    work_done : Optional[str] = None
    note : Optional[str] = None



# Properties to receive via API on creation
class CreateSiteReportActivity(SiteReportActivityBase):
    situation_report_id: Optional[UUID4] = None
    situation_report_task_id: Optional[UUID4] = None
    work_done : Optional[str] = None
    note : Optional[str] = None


# Properties to receive via API on update
class UpdateSiteReportActivity(SiteReportActivityBase):
    pass



class SiteReportActivityInDBBase(SiteReportActivityBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class SiteReportActivity(SiteReportActivityInDBBase):
    pass










# Shared ReportTeam properties
class ReportTeamBase(BaseModel):
    situation_report_id: Optional[UUID4] = None
    role : Optional[str] = None



# Properties to receive via API on creation
class CreateReportTeam(ReportTeamBase):
    situation_report_id: Optional[UUID4] = None
    role : Optional[str] = None


# Properties to receive via API on update
class UpdateReportTeam(ReportTeamBase):
    pass



class ReportTeamInDBBase(ReportTeamBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ReportTeam(ReportTeamInDBBase):
    pass







# Shared ReportStaff properties
class ReportStaffBase(BaseModel):
    situation_report_id: Optional[UUID4] = None


# Properties to receive via API on creation
class CreateReportStaff(ReportStaffBase):
    situation_report_id: Optional[UUID4] = None


# Properties to receive via API on update
class UpdateReportStaff(ReportStaffBase):
    pass



class ReportStaffInDBBase(ReportStaffBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ReportStaff(ReportStaffInDBBase):
    pass








# Shared Memorandum properties
class MemorandumBase(BaseModel):
    classification : Optional[str] = None
    file_number : Optional[str] = None
    date : Optional[str] = None
    primary_heading : Optional[str] = None
    secondary_heading : Optional[str] = None
    send_from : Optional[str] = None
    sent_to : Optional[str] = None
    subject : Optional[str] = None
    reference : Optional[str] = None
    introduction : Optional[str] = None
    body : Optional[str] = None




# Properties to receive via API on creation
class CreateMemorandum(MemorandumBase):
    classification : Optional[str] = None
    file_number : Optional[str] = None
    date : Optional[str] = None
    primary_heading : Optional[str] = None
    secondary_heading : Optional[str] = None
    send_from : Optional[str] = None
    sent_to : Optional[str] = None
    subject : Optional[str] = None
    reference : Optional[str] = None
    introduction : Optional[str] = None
    body : Optional[str] = None


# Properties to receive via API on update
class UpdateMemorandum(MemorandumBase):
    pass



class MemorandumInDBBase(MemorandumBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Memorandum(MemorandumInDBBase):
    pass







# Shared MemorandumComment properties
class MemorandumCommentBase(BaseModel):
    memorandum_id: Optional[UUID4] = None
    comment : Optional[str] = None
    commented_by : Optional[str] = None
    remarks : Optional[str] = None



# Properties to receive via API on creation
class CreateMemorandumComment(MemorandumCommentBase):
    memorandum_id: Optional[UUID4] = None
    comment : Optional[str] = None
    commented_by : Optional[str] = None
    remarks : Optional[str] = None


# Properties to receive via API on update
class UpdateMemorandumComment(MemorandumCommentBase):
    pass



class MemorandumCommentInDBBase(MemorandumCommentBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class MemorandumComment(MemorandumCommentInDBBase):
    pass









# Shared Task properties
class TaskBase(BaseModel):
    name : Optional[str] = None
    instructions : Optional[str] = None
    status : Optional[str] = None


# Properties to receive via API on creation
class CreateTask(TaskBase):
    name : Optional[str] = None
    instructions : Optional[str] = None
    status : Optional[str] = None


# Properties to receive via API on update
class UpdateTask(TaskBase):
    pass



class TaskInDBBase(TaskBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Task(TaskInDBBase):
    pass








# Shared Activities properties
class ActivitiesBase(BaseModel):
    task_id: Optional[UUID4] = None
    staff_id: Optional[UUID4] = None
    comment : Optional[str] = None
    commented_by : Optional[str] = None



# Properties to receive via API on creation
class CreateActivities(ActivitiesBase):
    task_id: Optional[UUID4] = None
    staff_id: Optional[UUID4] = None
    comment : Optional[str] = None
    commented_by : Optional[str] = None


# Properties to receive via API on update
class UpdateActivities(ActivitiesBase):
    pass



class ActivitiesInDBBase(ActivitiesBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Activities(ActivitiesInDBBase):
    pass
