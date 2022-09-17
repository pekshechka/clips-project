# clips-project

# Описание датасета

root
 <br />|-- clip_id: integer - уникальный айди клипа
 <br />|-- owner_id: integer - уникальный айди автора
 <br />|-- clipContentCategory: string - категория клипа (лейбл)
 <br />|-- date: string - дата создания
 <br />|-- contentAudioEmbedding: array - вектор клипа по нарезке кадров, размерность 1024
 <br />|    |-- element: float 
 <br />|-- contentEmbedding: array - вектор клипа по аудио (используется для определения трека), размерность 128
 <br />|    |-- element: float 
 <br />|-- AUTOTAG_max_proba_sum: map - автотэггер: классы с максимальной суммой вероятностей по всем кадрам (топ-10 при условии >= 0.1)
 <br />|    |-- key: string
 <br />|    |-- value: double 
 <br />|-- AUTOTAG_most_frequent: map - автотэггер: классы с максимальной частотой встречаемости на фрейме (кадре), value - сколько кадров
 <br />|    |-- key: string
 <br />|    |-- value: long 
 <br />|-- AUTOTAG_top_50_precentage_frames: map автотэггер: средняя вероятность класса на топ-50% фреймов по вероятности этого класса
 <br />|    |-- key: string
 <br />|    |-- value: double 
 <br />|-- description: string описание клипа от автора
 <br />|-- asr: string распознанные субтитры клипа (null - asr не работал для этого клипа)
 <br />|-- confidence_asr: double уровень "уверенности" модели в субтитрах (низкое значение может означать отсутствие произносимых слов). Субъективно считаю хорошими субтитры с >0.18
 
 
 Классы и датасет для автотеггера можно посмотреть здесь https://www.kaggle.com/competitions/youtube8m-2019/data
 
 
 
 
