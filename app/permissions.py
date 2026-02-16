from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # padrão que queremos:
        # f'{app_label}.{action_name}_{model_name}'   
        model_permission_codname = self.__get_model_permission_codname(
            method=request.method,
            view=view,
        )

        if not model_permission_codname:
            return False        
        return request.user.has_perm(model_permission_codname)
    

    def __get_model_permission_codname(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action_name = self.__get_action_sufix(method)
            # vai retornar , algo assim: 'genres.delete_genre'/'genres.view_genre'
            return f'{app_label}.{action_name}_{model_name}'
        except AttributeError:
            return None            
        
    def __get_action_sufix(self,method):
        method_action = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTION': 'view',
            'HEAD': 'view',            
        }
        return method_action.get(method, '')
    