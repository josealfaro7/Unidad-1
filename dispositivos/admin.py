from django.contrib import admin


from .models import Category, Zone, Device, Organization, Measurement, Alert


class BaseModelAdmin(admin.ModelAdmin): #clase padre para todos los modelos 
    #para poder ocultar el campo del soft delete en el panel de admin de django
    exclude = ("deleted_at",)
    # setearlo para dejarlo en readonly 
    readonly_fields = ("created_at", "updated_at")


@admin.register(Category)
class CategoryAdmin(BaseModelAdmin):
    pass


@admin.register(Zone)
class ZoneAdmin(BaseModelAdmin):
    pass


@admin.register(Organization)
class OrganizationAdmin(BaseModelAdmin):
    pass


@admin.register(Device)
class DeviceAdmin(BaseModelAdmin):
    pass


@admin.register(Measurement)
class MeasurementAdmin(BaseModelAdmin):
    pass


@admin.register(Alert)
class AlertAdmin(BaseModelAdmin):
    pass

