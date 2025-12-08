"""
URL configuration for NegocioModel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL configuration for NegocioModel project.
Versión fusionada con todas las implementaciones de API
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# Base Imports (tiendaApp/tiendaApi)
from tiendaApp import views as vistas # Web + DRF function views (empleado_listado/detalle)
from tiendaApi import views as vistasApi # Basic JSON view (empleadosApi)

# DRF Demo Imports (apiDemo apps)
from apiApp import views as api_demo_views
from serialApp import views as serial_demo_views
from cbvApp import views as cbv_demo_views
from mixinsApp import views as mixins_demo_views
from genericsApp import views as generics_demo_views
from viewsetApp import views as viewset_demo_views

# ============================================
# CONFIGURAR ROUTER PARA VIEWSETS
# ============================================
router = DefaultRouter()
# El ViewSet utiliza el EmpleadoViewSets
router.register(r'api/demo/viewset-employees', viewset_demo_views.EmpleadoViewSets, basename='employee-viewset')

# ============================================
# TODAS LAS URLS DEL PROYECTO
# ============================================

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ==========================================
    # RUTAS WEB TRADICIONALES (tiendaApp - Tarea 11)
    # ==========================================
    path('', vistas.inicio, name='inicio'),
    path('empleadoAdd/', vistas.crear_empleado, name='crearEmpleados'),
    path('empleadoEdit/<int:empleado_id>/', vistas.cargar_editar_empleado, name='editarEmpleado'),
    path('empleadoEditado/<int:empleado_id>/', vistas.editar_empleado, name='empleadoEditado'),
    path('empleadoDel/<int:empleado_id>/', vistas.eliminar_empleado, name='eliminarEmpleado'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # API Simple con JsonResponse (tiendaApi - Tarea 11)
    path('empleadosApi/', vistasApi.empleadosApi, name='empleadosApi'),
    
    # ==========================================
    # API RESTful DRF (tiendaApp - Tarea 12)
    # ==========================================
    path('api/empleados/', vistas.empleado_listado, name='empleado_listado'),
    path('api/empleados/<int:pk>/', vistas.empleado_detalle, name='empleado_detalle'),
    
    # ==========================================
    # RUTAS DE DRF DEMO (apiDemo - Fusionadas)
    # ==========================================
    
    # 1️⃣ apiApp - Django Puro (Solo lista desde BD - Renombrado para evitar conflicto con /api/empleados/)
    path('api/demo/employees-raw/', api_demo_views.employeeView_2, name='api-employees-raw'),

    # 2️⃣ serialApp - DRF con @api_view (Funciones)
    path('api/demo/serial-employees/', serial_demo_views.employee_list, name='serial-employee-list'),
    path('api/demo/serial-employees/<int:pk>/', serial_demo_views.employee_detail, name='serial-employee-detail'),
    
    # 3️⃣ cbvApp - DRF con APIView (Clases)
    path('api/demo/cbv-employees/', cbv_demo_views.EmployeeList.as_view(), name='cbv-employee-list'),
    path('api/demo/cbv-employees/<int:pk>/', cbv_demo_views.EmployeeDetail.as_view(), name='cbv-employee-detail'),
    
    # 4️⃣ mixinsApp - DRF con Mixins + GenericAPIView
    path('api/demo/mixins-employees/', mixins_demo_views.EmployeeList.as_view(), name='mixins-employee-list'),
    path('api/demo/mixins-employees/<int:pk>/', mixins_demo_views.EmployeeDetail.as_view(), name='mixins-employee-detail'),
    
    # 5️⃣ genericsApp - DRF con Generic Views
    path('api/demo/generics-employees/', generics_demo_views.EmployeeList.as_view(), name='generics-employee-list'),
    path('api/demo/generics-employees/<int:pk>/', generics_demo_views.EmployeeDetail.as_view(), name='generics-employee-detail'),
    
    # 6️⃣ viewsetApp - DRF con ViewSets (Router)
    path('', include(router.urls)),
]

# Configuración para servir archivos media y static en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)