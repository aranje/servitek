from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'ticket_type', 'created_at')
    list_filter = ('ticket_type',)
    search_fields = ('user__username', 'title')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Ticket, TicketAdmin)