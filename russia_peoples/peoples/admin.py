from django.contrib import admin
from .models import Nation

class NationAdmin(admin.ModelAdmin):
    list_display = ['name', 'flag_emoji', 'video_url']
    list_filter = ['name']
    search_fields = ['name']
    
    # Группировка полей для удобства
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'flag_emoji', 'short_description')
        }),
        ('История', {
            'fields': ('history_text',),
            'classes': ('wide',)
        }),
        ('Язык', {
            'fields': ('language_features',),
            'classes': ('wide',)
        }),
        ('Медиа - Фото (максимум 3)', {
            'fields': ('photo1', 'photo2', 'photo3'),
            'description': 'Загрузите фото в формате JPG/PNG'
        }),
        ('Медиа - Видео и Аудио', {
            'fields': ('video_url', 'audio_file'),
            'description': 'Для видео: вставьте полную ссылку с YouTube (например: https://www.youtube.com/watch?v=... )'
        }),
    )

admin.site.register(Nation, NationAdmin)