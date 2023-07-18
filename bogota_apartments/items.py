# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import numpy as np
from itemloaders.processors import TakeFirst, MapCompose
from unidecode import unidecode

def normalize_text_upper(text):
    return unidecode(text.replace('\n', ' ')).upper().strip()

def normalize_text_lower(text):
    return unidecode(text.replace('\n', ' ')).lower().strip()

def replace_zero_with_nan(value):
    return np.nan if value == 0 else value

def has_feature(value):
    return 1 if value else 0

class ApartmentsItem(scrapy.Item):
    codigo = scrapy.Field(output_processor = TakeFirst())

    tipo_propiedad = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )

    tipo_operacion = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )

    precio_venta = scrapy.Field(
        input_processor = MapCompose(int, replace_zero_with_nan),
        output_processor = TakeFirst()
    )

    precio_arriendo = scrapy.Field(
        input_processor = MapCompose(int, replace_zero_with_nan),
        output_processor = TakeFirst()
    )

    area = scrapy.Field(
        input_processor = MapCompose(float),
        output_processor = TakeFirst()
    )

    habitaciones = scrapy.Field(
        input_processor = MapCompose(int),
        output_processor = TakeFirst()
    )

    banos = scrapy.Field(
        input_processor = MapCompose(int),
        output_processor = TakeFirst()
    )

    administracion = scrapy.Field(
        input_processor = MapCompose(int, replace_zero_with_nan),
        output_processor = TakeFirst()
    )

    parqueaderos = scrapy.Field(
        input_processor = MapCompose(int),
        output_processor = TakeFirst()
    )

    sector = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )

    estrato = scrapy.Field(
        input_processor = MapCompose(int),
        output_processor = TakeFirst()
    )

    estado = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )

    antiguedad = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )

    latitud = scrapy.Field(
        input_processor = MapCompose(float, replace_zero_with_nan),
        output_processor = TakeFirst()
    )

    longitud = scrapy.Field(
        input_processor = MapCompose(float, replace_zero_with_nan),
        output_processor = TakeFirst()
    )

    featured_interior = scrapy.Field(output_processor = MapCompose(normalize_text_upper))
    featured_exterior = scrapy.Field(output_processor = MapCompose(normalize_text_upper))
    featured_zona_comun = scrapy.Field(output_processor = MapCompose(normalize_text_upper))
    featured_sector = scrapy.Field(output_processor = MapCompose(normalize_text_upper))

    descripcion = scrapy.Field(
        input_processor = MapCompose(normalize_text_lower),
        output_processor = TakeFirst()
    )

    compañia = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )

    imagenes = scrapy.Field()

    datetime = scrapy.Field(output_processor = TakeFirst())

class HabiApartmentsItem(ApartmentsItem):
    # agregar campos de habitaclia
    address = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )