

class DeclaracionModel:
    _mes = None
    _anio = None
    _periodicidad = None
    _codigo_version = None  # referencia al XML con widgets del formulario
    _version = None  # referencia a los XMLs de calculos y validaciones
    _contribuyente = None
    _anticipada = False
    _original = 'O'
    _sustituye = ''
    _alias_formulario = ''
    _archivo = None  # ruta del archivo de la declaracion

    def __init__(self):
        pass

    def set_mes(self, mes):
        self._mes = mes

    def set_anio(self, anio):
        self._anio = anio

    def set_periodicidad(self, periodicidad):
        self._periodicidad = periodicidad

    def set_codigo_version(self, codigo_version):
        self._codigo_version = codigo_version

    def set_version(self, version):
        self._version = version

    def set_contribuyente(self, contribuyente):
        self._contribuyente = contribuyente

    def set_anticipada(self, anticipada):
        self._anticipada = anticipada

    def set_original(self, original):
        self._original = original

    def set_sustituye(self, sustituye):
        self._sustituye = sustituye

    def set_alias_formulario(self, alias_formulario):
        self._alias_formulario = alias_formulario

    def set_archivo(self, archivo):
        self._archivo = archivo

    def get_mes(self):
        return self._mes

    def get_anio(self):
        return self._anio

    def get_codigo_version(self):
        return self._codigo_version

    def get_version(self):
        return self._version

    def get_contribuyente(self):
        return self._contribuyente

    def get_anticipada(self):
        return self._anticipada

    def get_original(self):
        return self._original

    def get_sustituye(self):
        return self._sustituye

    def get_alias_formulario(self):
        return self._alias_formulario

    def get_periodicidad(self):
        return self._periodicidad

    def get_archivo(self):
        return self._archivo

    # retorna la fecha de declaracion en formato yyyy-mm-dd
    # La fecha de declaracion NO es la fecha actual,
    # sino el periodo ANIO-MES del documento
    def get_fecha_declaracion(self):
        if self._mes is not None:
            return self._anio + '-' + self._mes.zfill(2) + '-01'
        else:
            return self._anio + '-01-01'

    def cargar_declaracion_guardada(self, xml, contribuyentes, ref_data):
        cabecera = xml.find('cabecera')

        if cabecera is None:
            raise Exception("No se pudo cargar la cabecera")

        codigo_version_formulario = cabecera.find('codigo_version_formulario').text
        ruc = cabecera.find('ruc').text
        anio = xml.find('detalle/campo[@numero="102"]').text
        if xml.find('detalle/campo[@numero="101"]') is not None:
            mes = xml.find('detalle/campo[@numero="101"]').text
        else:
            mes = '01'
        original = xml.find('detalle/campo[@numero="31"]').text
        sustituye = xml.find('detalle/campo[@numero="104"]').text

        if sustituye is None:
            sustituye = ""

        contribuyente = contribuyentes.find_by_ruc(ruc)

        if contribuyente is None:
            raise Exception("No existe el contribuyente: " + ruc)

        declaracion = ref_data.get_objeto_declaracion(codigo_version_formulario)
        declaracion.set_contribuyente(contribuyente)
        declaracion.set_anio(anio)
        declaracion.set_mes(mes)
        declaracion.set_original(original)
        declaracion.set_sustituye(sustituye)

        return declaracion

# EOF
