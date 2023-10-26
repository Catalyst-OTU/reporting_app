from . import models,actions


situationReportAttachment = actions.SituationReportAttachmentActions(models.SituationReportAttachment)

situationReportCategory = actions.SituationReportCategoryActions(models.SituationReportCategory)

situationReportComment = actions.SituationReportCommentActions(models.SituationReportComment)

siteReportCommentFile = actions.SiteReportCommentFileActions(models.SiteReportCommentFile)

siteReportActivity = actions.SiteReportActivityActions(models.SiteReportActivity)

memorandumComment = actions.MemorandumCommentActions(models.MemorandumComment)

situationReport = actions.SituationReportActions(models.SituationReport)

siteReportTask = actions.SiteReportTaskActions(models.SiteReportTask)

reportStaff = actions.ReportStaffActions(models.ReportStaff)

reportTeam = actions.ReportTeamActions(models.ReportTeam)

memorandum = actions.MemorandumActions(models.Memorandum)

activities = actions.ActivitiesActions(models.Activities)

task = actions.TaskActions(models.Task)