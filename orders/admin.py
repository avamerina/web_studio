from django.contrib import admin, messages

from orders.models import Order, File
from orders.tasks import process_order as task_process


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["slug", "description", "status", "user"]
    ordering = ["status"]
    actions = ["send_to_process"]
    search_fields = ['slug', 'description', 'user__phone']
    list_filter = ['user', 'status']

    @admin.action(description="Send selected orders to process")
    def send_to_process(self, request, queryset):
        updated = queryset.update(status="TO_PROCESS")

        self.message_user(
            request,
            f"{updated} successfully sent to be processed",
            messages.SUCCESS
        )

        for instance in queryset:
            order_slug = instance.slug
            task_process.apply_async(args=(order_slug,), countdown=10)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ["id", "url", "order"]

