from django.db import models

class Nation(models.Model):
    # Основная информация
    name = models.CharField(max_length=100, verbose_name="Название народа")
    flag_emoji = models.CharField(max_length=10, default='🏳️', verbose_name="Флаг (эмодзи)")
    
    # Короткое описание для главной (не обязательно)
    short_description = models.CharField(max_length=200, blank=True, verbose_name="Краткое описание")
    
    # История (основной текст)
    history_text = models.TextField(verbose_name="История народа")
    
    # Особенности языка
    language_features = models.TextField(verbose_name="Особенности языка", 
                                         help_text="Напишите про грамматику, интересные факты, алфавит и т.д.")
    
    # Фото (можно загружать несколько)
    photo1 = models.ImageField(upload_to='peoples/photos/', blank=True, null=True, verbose_name="Фото 1")
    photo2 = models.ImageField(upload_to='peoples/photos/', blank=True, null=True, verbose_name="Фото 2")
    photo3 = models.ImageField(upload_to='peoples/photos/', blank=True, null=True, verbose_name="Фото 3")
    
    # Видео (YouTube или любое другое)
    video_url = models.URLField(blank=True, verbose_name="Ссылка на видео", 
                                help_text="Вставьте ссылку на YouTube или Vimeo")
    
    # Дополнительно: аудио (если захочешь)
    audio_file = models.FileField(upload_to='peoples/audio/', blank=True, null=True, verbose_name="Аудио (песня/речь)")
    
    class Meta:
        verbose_name = "Народ"
        verbose_name_plural = "Народы"
    
    def __str__(self):
        return self.name