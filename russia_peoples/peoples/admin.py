from django.contrib import admin
from .models import Nation

class NationAdmin(admin.ModelAdmin):
    list_display = ['name', 'flag_emoji', 'video_url']
    list_filter = ['video_host', 'name']
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
        ('Видеоматериалы', {
            'fields': ('video_host', 'video_url', 'video_embed_code'),
            'description': '''
                <div style="background: #e8f0fe; padding: 15px; border-radius: 10px; margin: 10px 0;">
                    <strong>📌 Инструкция:</strong><br><br>
                    
                    <strong>Для ВКонтакте:</strong><br>
                    1. Откройте видео VK<br>
                    2. Нажмите "Поделиться" → "Код для вставки на сайт"<br>
                    3. Скопируйте полный iframe код в поле "Код для вставки"<br><br>
                    
                    <strong>Для RUTUBE:</strong><br>
                    1. Откройте видео на RUTUBE<br>
                    2. Нажмите "Поделиться" → "Встроить"<br>
                    3. Скопируйте ссылку или iframe код<br>
                    4. Вставьте ссылку в поле "Ссылка на видео"<br>
                    <br>
                    <strong>Примеры:</strong><br>
                    • RUTUBE ссылка: https://rutube.ru/video/123abc456/<br>
                    • VK embed код: &lt;iframe src="https://vk.com/video_ext.php?oid=-123&id=456"&gt;...&lt;/iframe&gt;
                </div>
            ''',
        }),
        ('Аудио (опционально)', {
            'fields': ('audio_file',),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Nation, NationAdmin)