from django.contrib import admin
from tiendaApp.models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'nombre', 
        'get_apellido_completo',
        'email', 
        'get_departamento_cargo',
        'get_salario_total',
        'fecha_contratacion'
    )
    list_filter = ('departamento', 'cargo', 'fecha_contratacion')
    search_fields = ('nombre', 'apellido', 'paterno', 'email', 'run')
    ordering = ('id',)  # Cambiado de ('-id',) a ('id',) para orden ascendente 1, 2, 3...
    list_per_page = 20
    
    fieldsets = (
        ('Información de Identificación', {
            'fields': ('run',)
        }),
        ('Información Personal', {
            'fields': ('nombre', 'apellido', 'paterno', 'email', 'telefono', 'fotografia')
        }),
        ('Información Laboral', {
            'fields': ('departamento', 'cargo', 'salario', 'sueldo', 'fecha_contratacion')
        }),
    )
    
    def get_apellido_completo(self, obj):
        """Muestra apellido o paterno"""
        return obj.apellido or obj.paterno or '-'
    get_apellido_completo.short_description = 'Apellido'
    
    def get_departamento_cargo(self, obj):
        """Muestra departamento y cargo"""
        depto = obj.departamento or '-'
        cargo = obj.cargo or '-'
        return f"{depto} / {cargo}"
    get_departamento_cargo.short_description = 'Depto/Cargo'
    
    def get_salario_total(self, obj):
        """Muestra el salario total"""
        salario = obj.salario or obj.sueldo or 0
        return f"${salario:,.0f}"
    get_salario_total.short_description = 'Salario'
    
    # Acciones personalizadas
    actions = ['marcar_activos', 'exportar_empleados']
    
    def marcar_activos(self, request, queryset):
        """Acción personalizada de ejemplo"""
        updated = queryset.count()
        self.message_user(request, f'{updated} empleados procesados.')
    marcar_activos.short_description = "Marcar empleados seleccionados"
    
    def exportar_empleados(self, request, queryset):
        """Acción para exportar empleados"""
        from django.http import HttpResponse
        import csv
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="empleados.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['ID', 'Nombre', 'Apellido', 'Email', 'Departamento', 'Salario'])
        
        for emp in queryset:
            writer.writerow([
                emp.id,
                emp.nombre,
                emp.apellido or emp.paterno,
                emp.email,
                emp.departamento or emp.cargo,
                emp.salario or emp.sueldo or 0
            ])
        
        return response
    exportar_empleados.short_description = "Exportar empleados a CSV"