from rest_framework import permissions

FULL_ACCESS = ['GET','DELETE','PUT','PATCH','HEAD','OPTIONS']
ACCOUNTANT = ['GET','HEAD','OPTIONS']
READ_ONLY = ['GET','HEAD','OPTIONS']

class SettingsPermission(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):

        if self.user.user_choice == "FULL_ACCESS":
            if (request.method in FULL_ACCESS):
                return True
        # elif obj.user.user_choice == "ACCOUNTANT":
        #     print('medium')
        #
        #     if (request.method in ACCOUNTANT
        #         ):
        #         return True
        # elif obj.user.user_choice == "READ_ONLY":
        #     print('Top')
        #
        #     if (request.method in READ_ONLY
        #         ):
        #         return True
