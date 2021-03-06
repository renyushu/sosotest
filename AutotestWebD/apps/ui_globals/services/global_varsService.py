import apps.common.func.InitDjango
from all_models_for_ui.models import Tb3UIGlobalVars
from django.db import connection
from django.forms.models import model_to_dict
from apps.common.func.CommonFunc import *
from all_models.models.A0011_version_manage import TbVersionGlobalVars

class global_varsService(object):

    @staticmethod
    def delVar(id):
        delResult = Tb3UIGlobalVars.objects.get(id=id)
        delResult.state = 0
        delResult.save()

    @staticmethod
    def delVersionVar(id):
        delResult = TbVersionGlobalVars.objects.get(id=id)
        delResult.state = 0
        delResult.save()

    @staticmethod
    def getVar(id):
        return Tb3UIGlobalVars.objects.filter(id=id)[0]

    @staticmethod
    def getVersionVar(id):
        return TbVersionGlobalVars.objects.filter(id=id)[0]

    @staticmethod
    def addVar(varData):
        return Tb3UIGlobalVars.objects.create(**varData)

    @staticmethod
    def addVersionVar(varData,versionName):
        varData['versionName_id'] = versionName
        varData['addTime'] = datetime.datetime.now()
        varData['modTime'] = datetime.datetime.now()
        return TbVersionGlobalVars.objects.create(**varData)

    @staticmethod
    def editVar(varData):
        varDBData = Tb3UIGlobalVars.objects.get(id=varData["id"])
        varDBData.varDesc = varData["varDesc"]
        varDBData.varValue = varData["varValue"]
        varDBData.save()

    @staticmethod
    def editVersionVar(varData,versionName):
        varDBData = TbVersionGlobalVars.objects.get(id=varData["id"])
        varDBData.varDesc = varData["varDesc"]
        varDBData.varValue = varData["varValue"]
        varDBData.save()

if __name__ == "__main__":
    # print((HTTP_test_caseService.getTestCaseForIdToDict("23")))
    # print(UserService.getUserByLoginname(UserService.getUsers()[0].loginname))
    # HTTP_test_caseService.testCaseAdd("")
    pass

