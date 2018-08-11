import moderngl
from demosys.resources.meta import ProgramDescription
from demosys import context

VERTEX_SHADER = 'VERTEX_SHADER'
GEOMETRY_SHADER = 'GEOMETRY_SHADER'
FRAGMENT_SHADER = 'FRAGMENT_SHADER'
TESS_CONTROL_SHADER = 'TESS_CONTROL_SHADER'
TESS_EVALUATION_SHADER = 'TESS_EVALUATION_SHADER'
COMPUTE_SHADER = 'COMPUTE_SHADER'


class ProgramShaders:
    """Helper class preparing shader source strings for a program"""

    def __init__(self, meta: ProgramDescription):
        self.meta = meta
        self.vertex_source = None
        self.geometry_source = None
        self.fragment_source = None

    @property
    def ctx(self) -> moderngl.Context:
        """The moderngl context"""
        return context.ctx()

    @classmethod
    def from_single(cls, meta: ProgramDescription, source: str):
        """Initialize a single glsl string containing all shaders"""
        instance = cls(meta)
        instance.vertex_source = ShaderSource(
            VERTEX_SHADER,
            meta.path or meta.vertex_shader,
            source
        )

        if GEOMETRY_SHADER in source:
            instance.geometry_source = ShaderSource(
                GEOMETRY_SHADER,
                meta.path or meta.geometry_shader,
                source,
            )

        if FRAGMENT_SHADER in source:
            instance.fragment_source = ShaderSource(
                FRAGMENT_SHADER,
                meta.path or meta.fragment_shader,
                source,
            )

        return instance

    @classmethod
    def from_separate(cls, meta: ProgramDescription, vertex_source, geometry_source=None, fragment_source=None):
        """Initialize multiple shader strings"""
        instance = cls(meta)
        instance.vertex_source = ShaderSource(
            VERTEX_SHADER,
            meta.path or meta.vertex_shader,
            vertex_source,
        )

        if geometry_source:
            instance.geometry_source = ShaderSource(
                GEOMETRY_SHADER,
                meta.path or meta.geometry_shader,
                geometry_source,
            )

        if fragment_source:
            instance.fragment_source = ShaderSource(
                FRAGMENT_SHADER,
                meta.path or meta.fragment_shader,
                fragment_source,
            )

        return instance

    def create(self):
        """Return create arguments to the Contex.program function in moderngl"""
        # Get out varyings
        out_attribs = []

        # If no fragment shader is present we are doing transform feedback
        if not self.fragment_source:
            # Out attributes is present in geometry shader if present
            if self.geometry_source:
                out_attribs = self.geometry_source.find_out_attribs()
            # Otherwise they are specified in vertex shader
            else:
                out_attribs = self.vertex_source.find_out_attribs()


        return self.ctx.program(
            vertex_shader=self.vertex_source.source,
            geometry_shader=self.geometry_source.source if self.geometry_source else None,
            fragment_shader=self.fragment_source.source if self.fragment_source else None,
            varyings=out_attribs,
        )


class ShaderSource:
    """
    Helper class representing a single shader type
    """
    def __init__(self, shader_type: str, name: str, source: str):
        self.type = shader_type
        self.name = name
        self.source = source.strip()
        self.lines = self.source.split('\n')

        # Make sure version is present
        if not self.lines[0].startswith("#version"):
            self.print()
            raise ShaderError(
                "Missing #version in {}. A version must be defined in the first line".format(self.name),
            )

        # Add preprocessors to source VERTEX_SHADER, FRAGMENT_SHADER etc.
        self.lines.insert(1, "#define {} 1".format(self.type))

        self.source = '\n'.join(self.lines)

    def find_out_attribs(self):
        """
        Get all out attributes in the shader source.

        :return: List of attribute names
        """
        names = []
        for line in self.lines:
            if line.strip().startswith("out "):
                names.append(line.split()[2].replace(';', ''))
        return names

    def print(self):
        """Print the shader lines"""
        print("---[ START {} ]---".format(self.name))

        for i, line in enumerate(self.lines):
            print("{}: {}".format(str(i).zfill(3), line))

        print("---[ END {} ]---".format(self.name))


class ShaderError(Exception):
    pass
