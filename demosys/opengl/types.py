

class BufferFormat:

    def __init__(self, format_string: str, components: int, bytes_per_component: int):
        """
        :param format_string: moderngl format string
        :param components: components
        :param byte_size: byte per component
        """
        self.format = "{}{}".format(components, format_string)
        self.components = components
        self.bytes_per_component = bytes_per_component

    def pad_str(self) -> str:
        return "{}x{}".format(self.components, self.bytes_per_component)

    def __str__(self) -> str:
        return "<BufferFormat {} {} {}>".format(self.format, self.components, self.bytes_per_component)

    def __repr__(self) -> str:
        return str(self)


def buffer_format(frmt: str) -> BufferFormat:
    """
    Look up info about a buffer format
    :param frmt: format string such as '3f'
    :return: BufferFormat instance
    """
    try:
        return BUFFER_FORMATS[frmt]
    except KeyError:
        raise ValueError("Buffer format '{}' unknown. Valid formats: {}".format(
            frmt, BUFFER_FORMATS.keys()
        ))


BUFFER_FORMATS  = {
    # f4 32 bit float - short version
    '1f': BufferFormat('f4', 1, 4),
    '2f': BufferFormat('f4', 2, 4),
    '3f': BufferFormat('f4', 3, 4),
    '4f': BufferFormat('f4', 4, 4),

    # u4 unsigned int - short version
    '1u': BufferFormat('u4', 1, 4),
    '2u': BufferFormat('u4', 2, 4),
    '3u': BufferFormat('u4', 3, 4),
    '4u': BufferFormat('u4', 4, 4),

    # i4 signed 32bit integer - short version
    '1i': BufferFormat('i4', 1, 4),
    '2i': BufferFormat('i4', 2, 4),
    '3i': BufferFormat('i4', 3, 4),
    '4i': BufferFormat('i4', 4, 4),

    # f1 unsigned byte - short version
    '1f1': BufferFormat('f1', 1, 1),
    '2f1': BufferFormat('f1', 2, 1),
    '3f1': BufferFormat('f1', 3, 1),
    '4f1': BufferFormat('f1', 4, 1),

    # f2 half float (16 bit)
    '1f2': BufferFormat('f2', 1, 2),
    '2f2': BufferFormat('f2', 2, 2),
    '3f2': BufferFormat('f2', 3, 2),
    '4f2': BufferFormat('f2', 4, 2),

    # f4 32 bit float
    '1f4': BufferFormat('f4', 1, 4),
    '2f4': BufferFormat('f4', 2, 4),
    '3f4': BufferFormat('f4', 3, 4),
    '4f4': BufferFormat('f4', 4, 4),

    # u1 unsigned byte
    '1u1': BufferFormat('u1', 1, 1),
    '2u1': BufferFormat('u1', 2, 1),
    '3u1': BufferFormat('u1', 3, 1),
    '4u1': BufferFormat('u1', 4, 1),

    # u2 unsigned short
    '1u2': BufferFormat('u2', 1, 2),
    '2u2': BufferFormat('u2', 2, 2),
    '3u2': BufferFormat('u2', 3, 2),
    '4u2': BufferFormat('u2', 4, 2),

    # u4 unsigned int
    '1u4': BufferFormat('u4', 1, 4),
    '2u4': BufferFormat('u4', 2, 4),
    '3u4': BufferFormat('u4', 3, 4),
    '4u4': BufferFormat('u4', 4, 4),

    # i1 signed byte
    '1i1': BufferFormat('i1', 1, 1),
    '2i1': BufferFormat('i1', 2, 1),
    '3i1': BufferFormat('i1', 3, 1),
    '4i1': BufferFormat('i1', 4, 1),

    # i2 signed short
    '1i2': BufferFormat('i2', 1, 2),
    '2i2': BufferFormat('i2', 2, 2),
    '3i2': BufferFormat('i2', 3, 2),
    '4i2': BufferFormat('i2', 4, 2),

    # i4 signed 32bit integer
    '1i4': BufferFormat('i4', 1, 4),
    '2i4': BufferFormat('i4', 2, 4),
    '3i4': BufferFormat('i4', 3, 4),
    '4i4': BufferFormat('i4', 4, 4),
}


# --- Texture internal format from DataType.cpp

# static int f1_internal_format[5] = {0, GL_R8, GL_RG8, GL_RGB8, GL_RGBA8};
# static int f2_internal_format[5] = {0, GL_R16F, GL_RG16F, GL_RGB16F, GL_RGBA16F};
# static int f4_internal_format[5] = {0, GL_R32F, GL_RG32F, GL_RGB32F, GL_RGBA32F};
# static int u1_internal_format[5] = {0, GL_R8UI, GL_RG8UI, GL_RGB8UI, GL_RGBA8UI};
# static int u2_internal_format[5] = {0, GL_R16UI, GL_RG16UI, GL_RGB16UI, GL_RGBA16UI};
# static int u4_internal_format[5] = {0, GL_R32UI, GL_RG32UI, GL_RGB32UI, GL_RGBA32UI};
# static int i1_internal_format[5] = {0, GL_R8I, GL_RG8I, GL_RGB8I, GL_RGBA8I};
# static int i2_internal_format[5] = {0, GL_R16I, GL_RG16I, GL_RGB16I, GL_RGBA16I};
# static int i4_internal_format[5] = {0, GL_R32I, GL_RG32I, GL_RGB32I, GL_RGBA32I};
