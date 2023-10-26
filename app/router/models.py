from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import ForeignKey,TIMESTAMP,Column,String,text,Enum,Boolean
from sqlalchemy.orm import relationship
from typing import Any
from pydantic import UUID4
import uuid
from .schemas import Roles


@as_declarative()
class Base:
    id: Any







class Admin(Base):
    __tablename__='admin'
    #Generate a random UUID.
    id = Column(String(255), primary_key=True,index=True, nullable=False, default=uuid.uuid4)
    name = Column(String(255), nullable=True)
    contact = Column(String(255), nullable=True, unique=True)
    email = Column(String(255), nullable=True, unique=True)
    password = Column(String(255), nullable=True)
    role = Column(Enum(Roles), nullable=True)
    reset_password_token = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    logs = relationship("Logs", back_populates="admin")







class Logs(Base):
    __tablename__ = "logs"
    id = Column(String(255), primary_key=True,index=True, nullable=False, default=uuid.uuid4)
    user_id = Column(String(255), ForeignKey("admin.id"))
    login_time = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    admin = relationship("Admin", back_populates="logs")





class SituationReportCategory(Base):
    __tablename__ = "situation_report_category"
#Generate a random UUID.
    id = Column(String(255), primary_key=True, index=True, default=uuid.uuid4)
    category = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    situation_report = relationship("SituationReport", back_populates="situation_report_category")








class SituationReport(Base):
    __tablename__ = "situation_report"
#Generate a random UUID.
    id = Column(String(255), primary_key=True, index=True, default=uuid.uuid4)
    report_category_id = Column(String(255), ForeignKey('situation_report_category.id'), nullable=True)
    classification = Column(String(255), nullable=True)
    confidential = Column(String(255), nullable=True)
    file_number = Column(String(255), nullable=True)
    date = Column(String(255), nullable=True)
    primary_heading = Column(String(255), nullable=True)
    secondary_heading = Column(String(255), nullable=True)
    conclusion = Column(String(255), nullable=True)
    recomendation = Column(String(255), nullable=True)
    reference = Column(String(255), nullable=True)
    sent_to = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    situation_report_category = relationship("SituationReportCategory", back_populates="situation_report")
    situation_report_attachment = relationship("SituationReportAttachment", back_populates="situation_report")
    situation_report_comment = relationship("SituationReportComment", back_populates="situation_report")
    site_report_comment_file = relationship("SiteReportCommentFile", back_populates="situation_report")
    site_report_task = relationship("SiteReportTask", back_populates="situation_report")
    report_team = relationship("ReportTeam", back_populates="situation_report")
    report_staff = relationship("ReportStaff", back_populates="situation_report")
    site_report_activity = relationship("SiteReportActivity", back_populates="situation_report")






class SituationReportAttachment(Base):
    __tablename__ = "situation_report_attachment"
#Generate a random UUID.
    id = Column(String(255), primary_key=True, index=True, default=uuid.uuid4)
    situation_report_id = Column(String(255), ForeignKey('situation_report.id'), nullable=True)
    file_name = Column(String(255), nullable=True)
    file_type = Column(String(255), nullable=True)
    file_url = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    keywords = Column(String(255), nullable=True)
    tags = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    situation_report = relationship("SituationReport", back_populates="situation_report_attachment")





class SituationReportComment(Base):
    __tablename__ = "situation_report_comment"
#Generate a random UUID.
    id = Column(String(255), primary_key=True, index=True, default=uuid.uuid4)
    situation_report_id = Column(String(255), ForeignKey('situation_report.id'), nullable=True)
    comment = Column(String(255), nullable=True)
    commented_by = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    situation_report = relationship("SituationReport", back_populates="situation_report_comment")
    site_report_comment_file = relationship("SiteReportCommentFile", back_populates="situation_report_comment")






class SiteReportCommentFile(Base):
    __tablename__ = "site_report_comment_file"
#Generate a random UUID.
    id = Column(String(255), primary_key=True, index=True, default=uuid.uuid4)
    situation_report_id = Column(String(255), ForeignKey('situation_report.id'), nullable=True)
    comment_id = Column(String(255), ForeignKey('situation_report_comment.id'), nullable=True)
    comment = Column(String(255), nullable=True)
    commented_by = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    situation_report = relationship("SituationReport", back_populates="site_report_comment_file")
    situation_report_comment = relationship("SituationReportComment", back_populates="site_report_comment_file")






class SiteReportTask(Base):
    __tablename__ = "site_report_task"
#Generate a random UUID.
    id = Column(String(255), primary_key=True, index=True, default=uuid.uuid4)
    situation_report_id = Column(String(255), ForeignKey('situation_report.id'), nullable=True)
    name = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    note = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    situation_report = relationship("SituationReport", back_populates="site_report_task")
    site_report_activity = relationship("SiteReportActivity", back_populates="site_report_task")






class SiteReportActivity(Base):
    __tablename__ = "site_report_activity"
#Generate a random UUID.
    id = Column(String(255), primary_key=True, index=True, default=uuid.uuid4)
    situation_report_id = Column(String(255), ForeignKey('situation_report.id'), nullable=True)
    situation_report_task_id = Column(String(255), ForeignKey('site_report_task.id'), nullable=True)
    work_done = Column(String(255), nullable=True)
    note = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    situation_report = relationship("SituationReport", back_populates="site_report_activity")
    site_report_task = relationship("SiteReportTask", back_populates="site_report_activity")







class ReportTeam(Base):
    __tablename__ = "report_team"
#Generate a random UUID.
    team_id = Column(String(255), primary_key=True, index=True, default=uuid.uuid4)
    situation_report_id = Column(String(255), ForeignKey('situation_report.id'), nullable=True)
    role = Column(String(255), nullable=True)
    situation_report = relationship("SituationReport", back_populates="report_team")




class ReportStaff(Base):
    __tablename__ = "report_staff"
#Generate a random UUID.
    staff_id = Column(String(255), primary_key=True, index=True, default=uuid.uuid4)
    situation_report_id = Column(String(255), ForeignKey('situation_report.id'), nullable=True)
    situation_report = relationship("SituationReport", back_populates="report_staff")
    activities = relationship("Activities", back_populates="report_staff")










class Memorandum(Base):
    __tablename__ = "memorandum"
#Generate a random UUID.
    id = Column(String(255), primary_key=True, index=True, default=uuid.uuid4)
    classification = Column(String(255), nullable=True)
    file_number = Column(String(255), nullable=True)
    date = Column(String(255), nullable=True)
    primary_heading = Column(String(255), nullable=True)
    secondary_heading = Column(String(255), nullable=True)
    send_from = Column(String(255), nullable=True)
    sent_to = Column(String(255), nullable=True)
    subject = Column(String(255), nullable=True)
    reference = Column(String(255), nullable=True)
    introduction = Column(String(255), nullable=True)
    body = Column(String(255), nullable=True)
    comments_recomendations = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    memorandum_comment = relationship("MemorandumComment", back_populates="memorandum")










class MemorandumComment(Base):
    __tablename__ = "memorandum_comment"
#Generate a random UUID.
    id = Column(String(255), primary_key=True, index=True, default=uuid.uuid4)
    memorandum_id = Column(String(255), ForeignKey('memorandum.id'), nullable=True)
    comment = Column(String(255), nullable=True)
    commented_by = Column(String(255), nullable=True)
    remarks = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    memorandum = relationship("Memorandum", back_populates="memorandum_comment")









class Task(Base):
    __tablename__ = "task"
#Generate a random UUID.
    id = Column(String(255), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(255), nullable=True)
    instructions = Column(String(255), nullable=True)
    status = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    activities = relationship("Activities", back_populates="task")








class Activities(Base):
    __tablename__ = "activities"
#Generate a random UUID.
    activity_id = Column(String(255), primary_key=True, index=True, default=uuid.uuid4)
    task_id = Column(String(255), ForeignKey('task.id'), nullable=True)
    staff_id = Column(String(255), ForeignKey('report_staff.staff_id'), nullable=True)
    comment = Column(String(255), nullable=True)
    commented_by = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    task = relationship("Task", back_populates="activities")
    report_staff = relationship("ReportStaff", back_populates="activities")
