from typing import Any, List, Union
from fastapi import Depends,APIRouter,HTTPException,status
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED,HTTP_404_NOT_FOUND
from core.database import get_db
from . import crud, models, schemas





# APIRouter creates path operations for all report
report_app = APIRouter(
    prefix="/report",
    responses={404: {"description": "Not found"}},
)



                        # Situation Report Category crud operations


#function to list all Situation Report Categories
@report_app.get("/situation_report_category/all", response_model=List[schemas.SituationReportCategory], tags=["Situation Report Category"])
def list_situation_report_category(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    list_all = crud.situationReportCategory.get_all(db=db, skip=skip, limit=limit)
    return list_all


                    

#function to create Situation Report Category
@report_app.post(
    "/situation_report_category/create",response_model=schemas.SituationReportCategory, status_code=HTTP_201_CREATED, tags=["Situation Report Category"])
def create_situation_report_category(*, db: Session = Depends(get_db), payload:schemas.CreateSituationReportCategory):
    create = crud.situationReportCategory.create(db=db, obj_in=payload)
    return create







#function to get Situation Report Category by id
@report_app.get("/situation_report_category/id/{id}", response_model=schemas.SituationReportCategory, tags=["Situation Report Category"])
def get_situation_report_category(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.situationReportCategory.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Situation Report Category not found")
    return get





## function to update Situation Report Category base on id
@report_app.put("/situation_report_category/update/{id}",response_model=schemas.SituationReportCategory, tags=["Situation Report Category"])
def update_situation_report_category(*, db: Session = Depends(get_db), id: UUID4, obj_in: schemas.UpdateSituationReportCategory):
    update = crud.situationReportCategory.get(db=db, id=id)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Situation Report Category not found")
    update = crud.situationReportCategory.update(db=db, db_obj=update, obj_in=obj_in)
    return update





## function to delete Situation Report Category base on id
@report_app.delete("/situation_report_category/delete/{id}", response_model=schemas.SituationReportCategory,tags=["Situation Report Category"])
def delete_situation_report_category(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.situationReportCategory.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Situation Report Category not found")
    delete = crud.situationReportCategory.remove(db=db, id=id)
    return delete















                        # Situation Report crud operations


#function to list all Situation Reports
@report_app.get("/situation_report/all", response_model=List[schemas.SituationReport], tags=["Situation Report"])
def list_situation_report(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    list_all = crud.situationReport.get_all(db=db, skip=skip, limit=limit)
    return list_all




#function to create Situation Report
@report_app.post(
    "/situation_report/create",response_model=Union[schemas.SituationReport, List[schemas.SituationReport]], status_code=HTTP_201_CREATED, tags=["Situation Report"])
def create_situation_report(*, db: Session = Depends(get_db), payload:Union[schemas.CreateSituationReport, List[schemas.CreateSituationReport]]):
    create = crud.situationReport.create(db=db, obj_in=payload)
    return create




#function to get Situation Report by id
@report_app.get("/situation_report/id/{id}", response_model=schemas.SituationReport, tags=["Situation Report"])
def get_situation_report(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.situationReport.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Situation Report not found")
    return get





## function to update Situation Report base on id
@report_app.put("/situation_report/update/{id}",response_model=schemas.SituationReport, tags=["Situation Report"])
def update_situation_report(*, db: Session = Depends(get_db), id: UUID4, obj_in: schemas.UpdateSituationReport):
    update = crud.situationReport.get(db=db, id=id)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Situation Report not found")
    update = crud.situationReport.update(db=db, db_obj=update, obj_in=obj_in)
    return update





## function to delete Situation Report base on id
@report_app.delete("/situation_report/delete/{id}", response_model=schemas.SituationReport,tags=["Situation Report"])
def delete_situation_report(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.situationReport.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Situation Report not found")
    delete = crud.situationReport.remove(db=db, id=id)
    return delete


















                        # Situation Report Attachment crud operations


#function to list all Situation Report Attachments
@report_app.get("/situation_report_attachment/all", response_model=List[schemas.SituationReportAttachment], tags=["Situation Report Attachment"])
def list_situation_report_attachment(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    list_all = crud.situationReportAttachment.get_all(db=db, skip=skip, limit=limit)
    return list_all




#function to create Situation Report Attachment
@report_app.post(
    "/situation_report_attachment/create",response_model=Union[schemas.SituationReportAttachment, List[schemas.SituationReportAttachment]], status_code=HTTP_201_CREATED, tags=["Situation Report Attachment"])
def create_situation_report_attachment(*, db: Session = Depends(get_db), payload:Union[schemas.CreateSituationReportAttachment, List[schemas.CreateSituationReportAttachment]]):
    create = crud.situationReportAttachment.create(db=db, obj_in=payload)
    return create




#function to get Situation Report Attachment by id
@report_app.get("/situation_report_attachment/id/{id}", response_model=schemas.SituationReportAttachment, tags=["Situation Report Attachment"])
def get_situation_report_attachment(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.situationReportAttachment.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Situation Report Attachment not found")
    return get





## function to update Situation Report Attachment base on id
@report_app.put("/situation_report_attachment/update/{id}",response_model=schemas.SituationReportAttachment, tags=["Situation Report Attachment"])
def update_situation_report_attachment(*, db: Session = Depends(get_db), id: UUID4, obj_in: schemas.UpdateSituationReportAttachment):
    update = crud.situationReportAttachment.get(db=db, id=id)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Situation Report Attachment not found")
    update = crud.situationReportAttachment.update(db=db, db_obj=update, obj_in=obj_in)
    return update





## function to delete Situation Report Attachment base on id
@report_app.delete("/situation_report_attachment/delete/{id}", response_model=schemas.SituationReportAttachment,tags=["Situation Report Attachment"])
def delete_situation_report_attachment(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.situationReportAttachment.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Situation Report Attachment not found")
    delete = crud.situationReportAttachment.remove(db=db, id=id)
    return delete






















                        # Situation Report Comment crud operations


#function to list all Situation Report Comments
@report_app.get("/situation_report_comment/all", response_model=List[schemas.SituationReportComment], tags=["Situation Report Comment"])
def list_situation_report_comment(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    list_all = crud.situationReportComment.get_all(db=db, skip=skip, limit=limit)
    return list_all




#function to create Situation Report Comment
@report_app.post(
    "/situation_report_comment/create",response_model=Union[schemas.SituationReportComment, List[schemas.SituationReportComment]], status_code=HTTP_201_CREATED, tags=["Situation Report Comment"])
def create_situation_report_comment(*, db: Session = Depends(get_db), payload:Union[schemas.CreateSituationReportComment, List[schemas.CreateSituationReportComment]]):
    create = crud.situationReportComment.create(db=db, obj_in=payload)
    return create




#function to get Situation Report Comment by id
@report_app.get("/situation_report_comment/id/{id}", response_model=schemas.SituationReportComment, tags=["Situation Report Comment"])
def get_situation_report_comment(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.situationReportComment.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Situation Report Comment not found")
    return get





## function to update Situation Report Comment base on id
@report_app.put("/situation_report_comment/update/{id}",response_model=schemas.SituationReportComment, tags=["Situation Report Comment"])
def update_situation_report_comment(*, db: Session = Depends(get_db), id: UUID4, obj_in: schemas.UpdateSituationReportComment):
    update = crud.situationReportComment.get(db=db, id=id)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Situation Report Comment not found")
    update = crud.situationReportComment.update(db=db, db_obj=update, obj_in=obj_in)
    return update





## function to delete Situation Report Comment base on id
@report_app.delete("/situation_report_comment/delete/{id}", response_model=schemas.SituationReportComment,tags=["Situation Report Comment"])
def delete_situation_report_comment(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.situationReportComment.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Situation Report Comment not found")
    delete = crud.situationReportComment.remove(db=db, id=id)
    return delete













                        # Site Report Comment File crud operations


#function to list all Site Report Comment Files
@report_app.get("/site_report_comment_file/all", response_model=List[schemas.SiteReportCommentFile], tags=["Site Report Comment File"])
def list_site_report_comment_file(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    list_all = crud.siteReportCommentFile.get_all(db=db, skip=skip, limit=limit)
    return list_all




#function to create Site Report Comment File
@report_app.post(
    "/site_report_comment_file/create",response_model=Union[schemas.SiteReportCommentFile, List[schemas.SiteReportCommentFile]], status_code=HTTP_201_CREATED, tags=["Site Report Comment File"])
def create_site_report_comment_file(*, db: Session = Depends(get_db), payload:Union[schemas.CreateSiteReportCommentFile, List[schemas.CreateSiteReportCommentFile]]):
    create = crud.siteReportCommentFile.create(db=db, obj_in=payload)
    return create




#function to get Site Report Comment File by id
@report_app.get("/site_report_comment_file/id/{id}", response_model=schemas.SiteReportCommentFile, tags=["Site Report Comment File"])
def get_site_report_comment_file(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.siteReportCommentFile.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Site Report Comment File not found")
    return get





## function to update Site Report Comment File base on id
@report_app.put("/site_report_comment_file/update/{id}",response_model=schemas.SiteReportCommentFile, tags=["Site Report Comment File"])
def update_site_report_comment_file(*, db: Session = Depends(get_db), id: UUID4, obj_in: schemas.UpdateSiteReportCommentFile):
    update = crud.siteReportCommentFile.get(db=db, id=id)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Site Report Comment File not found")
    update = crud.siteReportCommentFile.update(db=db, db_obj=update, obj_in=obj_in)
    return update





## function to delete Site Report Comment File base on id
@report_app.delete("/site_report_comment_file/delete/{id}", response_model=schemas.SiteReportCommentFile,tags=["Site Report Comment File"])
def delete_site_report_comment_file(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.siteReportCommentFile.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Site Report Comment File not found")
    delete = crud.siteReportCommentFile.remove(db=db, id=id)
    return delete













                        # Site Report Task crud operations


#function to list all Site Report Tasks
@report_app.get("/site_report_task/all", response_model=List[schemas.SiteReportTask], tags=["Site Report Task"])
def list_site_report_task(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    list_all = crud.siteReportTask.get_all(db=db, skip=skip, limit=limit)
    return list_all




#function to create Site Report Task
@report_app.post(
    "/site_report_task/create",response_model=Union[schemas.SiteReportTask, List[schemas.SiteReportTask]], status_code=HTTP_201_CREATED, tags=["Site Report Task"])
def create_site_report_task(*, db: Session = Depends(get_db), payload:Union[schemas.CreateSiteReportTask, List[schemas.CreateSiteReportTask]]):
    create = crud.siteReportTask.create(db=db, obj_in=payload)
    return create




#function to get Site Report Task by id
@report_app.get("/site_report_task/id/{id}", response_model=schemas.SiteReportTask, tags=["Site Report Task"])
def get_site_report_task(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.siteReportTask.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Site Report Task not found")
    return get





## function to update Site Report Task base on id
@report_app.put("/site_report_task/update/{id}",response_model=schemas.SiteReportTask, tags=["Site Report Task"])
def update_site_report_task(*, db: Session = Depends(get_db), id: UUID4, obj_in: schemas.UpdateSiteReportTask):
    update = crud.siteReportTask.get(db=db, id=id)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Site Report Task not found")
    update = crud.siteReportTask.update(db=db, db_obj=update, obj_in=obj_in)
    return update





## function to delete Site Report Task base on id
@report_app.delete("/site_report_task/delete/{id}", response_model=schemas.SiteReportTask,tags=["Site Report Task"])
def delete_site_report_task(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.siteReportTask.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Site Report Task not found")
    delete = crud.siteReportTask.remove(db=db, id=id)
    return delete


















                # Site Report Activity crud operations


#function to list all Site Report Activitys
@report_app.get("/site_report_activity/all", response_model=List[schemas.SiteReportActivity], tags=["Site Report Activity"])
def list_site_report_activity(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    list_all = crud.siteReportActivity.get_all(db=db, skip=skip, limit=limit)
    return list_all




#function to create Site Report Activity
@report_app.post(
    "/site_report_activity/create",response_model=Union[schemas.SiteReportActivity, List[schemas.SiteReportActivity]], status_code=HTTP_201_CREATED, tags=["Site Report Activity"])
def create_site_report_activity(*, db: Session = Depends(get_db), payload:Union[schemas.CreateSiteReportActivity, List[schemas.CreateSiteReportActivity]]):
    create = crud.siteReportActivity.create(db=db, obj_in=payload)
    return create




#function to get Site Report Activity by id
@report_app.get("/site_report_activity/id/{id}", response_model=schemas.SiteReportActivity, tags=["Site Report Activity"])
def get_site_report_activity(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.siteReportActivity.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Site Report Activity not found")
    return get





## function to update Site Report Activity base on id
@report_app.put("/site_report_activity/update/{id}",response_model=schemas.SiteReportActivity, tags=["Site Report Activity"])
def update_site_report_activity(*, db: Session = Depends(get_db), id: UUID4, obj_in: schemas.UpdateSiteReportActivity):
    update = crud.siteReportActivity.get(db=db, id=id)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Site Report Activity not found")
    update = crud.siteReportActivity.update(db=db, db_obj=update, obj_in=obj_in)
    return update





## function to delete Site Report Activity base on id
@report_app.delete("/site_report_activity/delete/{id}", response_model=schemas.SiteReportActivity,tags=["Site Report Activity"])
def delete_site_report_activity(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.siteReportActivity.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Site Report Activity not found")
    delete = crud.siteReportActivity.remove(db=db, id=id)
    return delete














                # Report Team crud operations


#function to list all Report Teams
@report_app.get("/report_team/all", response_model=List[schemas.ReportTeam], tags=["Report Team"])
def list_report_team(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    list_all = crud.reportTeam.get_all(db=db, skip=skip, limit=limit)
    return list_all




#function to create Report Team
@report_app.post(
    "/report_team/create",response_model=Union[schemas.ReportTeam, List[schemas.ReportTeam]], status_code=HTTP_201_CREATED, tags=["Report Team"])
def create_report_team(*, db: Session = Depends(get_db), payload:Union[schemas.CreateReportTeam, List[schemas.CreateReportTeam]]):
    create = crud.reportTeam.create(db=db, obj_in=payload)
    return create




#function to get Report Team by id
@report_app.get("/report_team/id/{id}", response_model=schemas.ReportTeam, tags=["Report Team"])
def get_report_team(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.reportTeam.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report Team not found")
    return get





## function to update Report Team base on id
@report_app.put("/report_team/update/{id}",response_model=schemas.ReportTeam, tags=["Report Team"])
def update_report_team(*, db: Session = Depends(get_db), id: UUID4, obj_in: schemas.UpdateReportTeam):
    update = crud.reportTeam.get(db=db, id=id)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report Team not found")
    update = crud.reportTeam.update(db=db, db_obj=update, obj_in=obj_in)
    return update





## function to delete Report Team base on id
@report_app.delete("/report_team/delete/{id}", response_model=schemas.ReportTeam,tags=["Report Team"])
def delete_report_team(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.reportTeam.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report Team not found")
    delete = crud.reportTeam.remove(db=db, id=id)
    return delete














                # Report Staff crud operations


#function to list all Report Staffs
@report_app.get("/report_staff/all", response_model=List[schemas.ReportStaff], tags=["Report Staff"])
def list_report_staff(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    list_all = crud.reportStaff.get_all(db=db, skip=skip, limit=limit)
    return list_all




#function to create Report Staff
@report_app.post(
    "/report_staff/create",response_model=Union[schemas.ReportStaff, List[schemas.ReportStaff]], status_code=HTTP_201_CREATED, tags=["Report Staff"])
def create_report_staff(*, db: Session = Depends(get_db), payload:Union[schemas.CreateReportStaff, List[schemas.CreateReportStaff]]):
    create = crud.reportStaff.create(db=db, obj_in=payload)
    return create




#function to get Report Staff by id
@report_app.get("/report_staff/id/{id}", response_model=schemas.ReportStaff, tags=["Report Staff"])
def get_report_staff(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.reportStaff.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report Staff not found")
    return get





## function to update Report Staff base on id
@report_app.put("/report_staff/update/{id}",response_model=schemas.ReportStaff, tags=["Report Staff"])
def update_report_staff(*, db: Session = Depends(get_db), id: UUID4, obj_in: schemas.UpdateReportStaff):
    update = crud.reportStaff.get(db=db, id=id)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report Staff not found")
    update = crud.reportStaff.update(db=db, db_obj=update, obj_in=obj_in)
    return update





## function to delete Report Staff base on id
@report_app.delete("/report_staff/delete/{id}", response_model=schemas.ReportStaff,tags=["Report Staff"])
def delete_report_staff(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.reportStaff.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report Staff not found")
    delete = crud.reportStaff.remove(db=db, id=id)
    return delete


















                # Memorandum crud operations


#function to list all Memorandums
@report_app.get("/memorandum/all", response_model=List[schemas.Memorandum], tags=["Memorandum"])
def list_memorandum(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    list_all = crud.memorandum.get_all(db=db, skip=skip, limit=limit)
    return list_all




#function to create Memorandum
@report_app.post(
    "/memorandum/create",response_model=Union[schemas.Memorandum, List[schemas.Memorandum]], status_code=HTTP_201_CREATED, tags=["Memorandum"])
def create_memorandum(*, db: Session = Depends(get_db), payload:Union[schemas.CreateMemorandum, List[schemas.CreateMemorandum]]):
    create = crud.memorandum.create(db=db, obj_in=payload)
    return create




#function to get Memorandum by id
@report_app.get("/memorandum/id/{id}", response_model=schemas.Memorandum, tags=["Memorandum"])
def get_memorandum(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.memorandum.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Memorandum not found")
    return get





## function to update Memorandum base on id
@report_app.put("/memorandum/update/{id}",response_model=schemas.Memorandum, tags=["Memorandum"])
def update_memorandum(*, db: Session = Depends(get_db), id: UUID4, obj_in: schemas.UpdateMemorandum):
    update = crud.memorandum.get(db=db, id=id)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Memorandum not found")
    update = crud.memorandum.update(db=db, db_obj=update, obj_in=obj_in)
    return update





## function to delete Memorandum base on id
@report_app.delete("/memorandum/delete/{id}", response_model=schemas.Memorandum,tags=["Memorandum"])
def delete_memorandum(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.memorandum.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Memorandum not found")
    delete = crud.memorandum.remove(db=db, id=id)
    return delete



















                # Memorandum Comment crud operations

#function to list all Memorandum Comments
@report_app.get("/memorandum_comment/all", response_model=List[schemas.MemorandumComment], tags=["Memorandum Comment"])
def list_memorandum_comment(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    list_all = crud.memorandumComment.get_all(db=db, skip=skip, limit=limit)
    return list_all




#function to create Memorandum Comment
@report_app.post(
    "/memorandum_comment/create",response_model=Union[schemas.MemorandumComment, List[schemas.MemorandumComment]], status_code=HTTP_201_CREATED, tags=["Memorandum Comment"])
def create_memorandum_comment(*, db: Session = Depends(get_db), payload:Union[schemas.CreateMemorandumComment, List[schemas.CreateMemorandumComment]]):
    create = crud.memorandumComment.create(db=db, obj_in=payload)
    return create




#function to get Memorandum Comment by id
@report_app.get("/memorandum_comment/id/{id}", response_model=schemas.MemorandumComment, tags=["Memorandum Comment"])
def get_memorandum_comment(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.memorandumComment.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Memorandum Comment not found")
    return get





## function to update Memorandum Comment base on id
@report_app.put("/memorandum_comment/update/{id}",response_model=schemas.MemorandumComment, tags=["Memorandum Comment"])
def update_memorandum_comment(*, db: Session = Depends(get_db), id: UUID4, obj_in: schemas.UpdateMemorandumComment):
    update = crud.memorandumComment.get(db=db, id=id)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Memorandum Comment not found")
    update = crud.memorandumComment.update(db=db, db_obj=update, obj_in=obj_in)
    return update





## function to delete Memorandum Comment base on id
@report_app.delete("/memorandum_comment/delete/{id}", response_model=schemas.MemorandumComment,tags=["Memorandum Comment"])
def delete_memorandum_comment(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.memorandumComment.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Memorandum Comment not found")
    delete = crud.memorandumComment.remove(db=db, id=id)
    return delete

















                # Task crud operations

#function to list all Tasks
@report_app.get("/task/all", response_model=List[schemas.Task], tags=["Task"])
def list_task(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    list_all = crud.task.get_all(db=db, skip=skip, limit=limit)
    return list_all




#function to create Task
@report_app.post(
    "/task/create",response_model=Union[schemas.Task, List[schemas.Task]], status_code=HTTP_201_CREATED, tags=["Task"])
def create_task(*, db: Session = Depends(get_db), payload:Union[schemas.CreateTask, List[schemas.CreateTask]]):
    create = crud.task.create(db=db, obj_in=payload)
    return create




#function to get Task by id
@report_app.get("/task/id/{id}", response_model=schemas.Task, tags=["Task"])
def get_task(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.task.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return get





## function to update Task base on id
@report_app.put("/task/update/{id}",response_model=schemas.Task, tags=["Task"])
def update_task(*, db: Session = Depends(get_db), id: UUID4, obj_in: schemas.UpdateTask):
    update = crud.task.get(db=db, id=id)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    update = crud.task.update(db=db, db_obj=update, obj_in=obj_in)
    return update





## function to delete Task base on id
@report_app.delete("/task/delete/{id}", response_model=schemas.Task,tags=["Task"])
def delete_task(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.task.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    delete = crud.task.remove(db=db, id=id)
    return delete
















                # Activities crud operations

#function to list all Activitiess
@report_app.get("/activities/all", response_model=List[schemas.Activities], tags=["Activities"])
def list_activities(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    list_all = crud.activities.get_all(db=db, skip=skip, limit=limit)
    return list_all




#function to create Activities
@report_app.post(
    "/activities/create",response_model=Union[schemas.Activities, List[schemas.Activities]], status_code=HTTP_201_CREATED, tags=["Activities"])
def create_activities(*, db: Session = Depends(get_db), payload:Union[schemas.CreateActivities, List[schemas.CreateActivities]]):
    create = crud.activities.create(db=db, obj_in=payload)
    return create




#function to get Activities by id
@report_app.get("/activities/id/{id}", response_model=schemas.Activities, tags=["Activities"])
def get_activities(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.activities.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activities not found")
    return get





## function to update Activities base on id
@report_app.put("/activities/update/{id}",response_model=schemas.Activities, tags=["Activities"])
def update_activities(*, db: Session = Depends(get_db), id: UUID4, obj_in: schemas.UpdateActivities):
    update = crud.activities.get(db=db, id=id)
    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activities not found")
    update = crud.activities.update(db=db, db_obj=update, obj_in=obj_in)
    return update





## function to delete Activities base on id
@report_app.delete("/activities/delete/{id}", response_model=schemas.Activities,tags=["Activities"])
def delete_activities(*, db: Session = Depends(get_db), id: UUID4):
    get = crud.activities.get(db=db, id=id)
    if not get:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Activities not found")
    delete = crud.activities.remove(db=db, id=id)
    return delete
