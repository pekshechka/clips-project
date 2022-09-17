# clips-project

# Описание датасета

root
 |-- clip_id: integer - уникальный айди клипа
 |-- owner_id: integer - уникальный айди автора
 |-- clipContentCategory: string - категория клипа (лейбл)
 |-- date: string - дата создания
 |-- contentAudioEmbedding: array - вектор клипа по нарезке кадров, размерность 1024
 |    |-- element: float 
 |-- contentEmbedding: array - вектор клипа по аудио (используется для определения трека), размерность 128
 |    |-- element: float 
 |-- AUTOTAG_max_proba_sum: map - автотэггер: классы с максимальной суммой вероятностей по всем кадрам (топ-10 при условии >= 0.1)
 |    |-- key: string
 |    |-- value: double 
 |-- AUTOTAG_most_frequent: map - автотэггер: классы с максимальной частотой встречаемости на фрейме (кадре), value - сколько кадров
 |    |-- key: string
 |    |-- value: long 
 |-- AUTOTAG_top_50_precentage_frames: map автотэггер: средняя вероятность класса на топ-50% фреймов по вероятности этого класса
 |    |-- key: string
 |    |-- value: double 
 |-- description: string описание клипа от автора
 |-- asr: string распознанные субтитры клипа (null - asr не работал для этого клипа)
 |-- confidence_asr: double уровень "уверенности" модели в субтитрах (низкое значение может означать отсутствие произносимых слов). Субъективно считаю хорошими субтитры с >0.18
 
 
 Классы и датасет для автотеггера можно посмотреть здесь https://www.kaggle.com/competitions/youtube8m-2019/data
 
 
 
 
