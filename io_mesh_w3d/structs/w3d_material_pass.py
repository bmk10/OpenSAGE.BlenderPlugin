# <pep8 compliant>
# Written by Stephan Vedder and Michael Schnabel
# Last Modification 11.2019

from io_mesh_w3d.structs.struct import Struct, HEAD
from io_mesh_w3d.structs.w3d_rgba import RGBA
from io_mesh_w3d.io_binary import *
from io_mesh_w3d.import_utils_w3d import skip_unknown_chunk


W3D_CHUNK_TEXTURE_STAGE = 0x00000048
W3D_CHUNK_TEXTURE_IDS = 0x00000049
W3D_CHUNK_STAGE_TEXCOORDS = 0x0000004A
W3D_CHUNK_PER_FACE_TEXCOORD_IDS = 0x0000004B


class TextureStage(Struct):
    tx_ids = []
    per_face_tx_coords = []
    tx_coords = []

    @staticmethod
    def read(io_stream, chunk_end):
        result = TextureStage(
            tx_ids=[],
            per_face_tx_coords=[],
            tx_coords=[])

        while io_stream.tell() < chunk_end:
            (chunk_type, chunk_size, subchunk_end) = read_chunk_head(io_stream)

            if chunk_type == W3D_CHUNK_TEXTURE_IDS:
                result.tx_ids = read_array(io_stream, subchunk_end, read_long)
            elif chunk_type == W3D_CHUNK_STAGE_TEXCOORDS:
                result.tx_coords = read_array(
                    io_stream, subchunk_end, read_vector2)
            elif chunk_type == W3D_CHUNK_PER_FACE_TEXCOORD_IDS:
                result.per_face_tx_coords = read_array(
                    io_stream, subchunk_end, read_vector)
            else:
                skip_unknown_chunk(None, io_stream, chunk_type, chunk_size)
        return result

    def tx_ids_size(self, include_head=True):
        size = len(self.tx_ids) * 4
        if include_head:
            size += HEAD
        return size

    def per_face_tx_coords_size(self, include_head=True):
        size = len(self.per_face_tx_coords) * 12
        if include_head:
            size += HEAD
        return size

    def tx_coords_size(self, include_head=True):
        size = len(self.tx_coords) * 8
        if include_head:
            size += HEAD
        return size

    def size(self, include_head=True):
        size = 0
        if include_head:
            size += HEAD
        if self.tx_ids:
            size += self.tx_ids_size()
        if self.tx_coords:
            size += self.tx_coords_size()
        if self.per_face_tx_coords:
            size += self.per_face_tx_coords_size()
        return size

    def write(self, io_stream):
        write_chunk_head(io_stream, W3D_CHUNK_TEXTURE_STAGE,
                         self.size(False), has_sub_chunks=True)

        if self.tx_ids:
            write_chunk_head(io_stream, W3D_CHUNK_TEXTURE_IDS,
                             self.tx_ids_size(False))
            write_array(io_stream, self.tx_ids, write_long)

        if self.tx_coords:
            write_chunk_head(io_stream, W3D_CHUNK_STAGE_TEXCOORDS,
                             self.tx_coords_size(False))
            write_array(io_stream, self.tx_coords, write_vector2)

        if self.per_face_tx_coords:
            write_chunk_head(io_stream, W3D_CHUNK_PER_FACE_TEXCOORD_IDS,
                             self.per_face_tx_coords_size(False))
            write_array(io_stream, self.per_face_tx_coords, write_vector)


W3D_CHUNK_MATERIAL_PASS = 0x00000038
W3D_CHUNK_VERTEX_MATERIAL_IDS = 0x00000039
W3D_CHUNK_SHADER_IDS = 0x0000003A
W3D_CHUNK_DCG = 0x0000003B
W3D_CHUNK_DIG = 0x0000003C
W3D_CHUNK_SCG = 0x0000003E
W3D_CHUNK_SHADER_MATERIAL_ID = 0x0000003F


class MaterialPass(Struct):
    vertex_material_ids = []
    shader_ids = []
    dcg = []
    dig = []
    scg = []
    shader_material_ids = []
    tx_stages = []
    tx_coords = []

    @staticmethod
    def read(io_stream, chunk_end):
        result = MaterialPass(
            vertex_material_ids=[],
            shader_ids=[],
            dcg=[],
            dig=[],
            scg=[],
            shader_material_ids=[],
            tx_stages=[],
            tx_coords=[])

        while io_stream.tell() < chunk_end:
            (chunk_type, chunk_size, subchunk_end) = read_chunk_head(io_stream)

            if chunk_type == W3D_CHUNK_VERTEX_MATERIAL_IDS:
                result.vertex_material_ids = read_array(
                    io_stream, subchunk_end, read_ulong)
            elif chunk_type == W3D_CHUNK_SHADER_IDS:
                result.shader_ids = read_array(
                    io_stream, subchunk_end, read_ulong)
            elif chunk_type == W3D_CHUNK_DCG:
                result.dcg = read_array(io_stream, subchunk_end, RGBA.read)
            elif chunk_type == W3D_CHUNK_DIG:
                result.dig = read_array(io_stream, subchunk_end, RGBA.read)
            elif chunk_type == W3D_CHUNK_SCG:
                result.scg = read_array(io_stream, subchunk_end, RGBA.read)
            elif chunk_type == W3D_CHUNK_SHADER_MATERIAL_ID:
                result.shader_material_ids = read_array(
                    io_stream, subchunk_end, read_ulong)
            elif chunk_type == W3D_CHUNK_TEXTURE_STAGE:
                result.tx_stages.append(
                    TextureStage.read(io_stream, subchunk_end))
            elif chunk_type == W3D_CHUNK_STAGE_TEXCOORDS:
                result.tx_coords = read_array(
                    io_stream, subchunk_end, read_vector2)
            else:
                skip_unknown_chunk(None, io_stream, chunk_type, chunk_size)
        return result

    def vertex_material_ids_size(self, include_head=True):
        size = len(self.vertex_material_ids) * 4
        if include_head:
            size += HEAD
        return size

    def shader_ids_size(self, include_head=True):
        size = len(self.shader_ids) * 4
        if include_head:
            size += HEAD
        return size

    def dcg_size(self, include_head=True):
        size = len(self.dcg) * 4
        if include_head:
            size += HEAD
        return size

    def dig_size(self, include_head=True):
        size = len(self.dig) * 4
        if include_head:
            size += HEAD
        return size

    def scg_size(self, include_head=True):
        size = len(self.scg) * 4
        if include_head:
            size += HEAD
        return size

    def shader_material_ids_size(self, include_head=True):
        size = len(self.shader_material_ids) * 4
        if include_head:
            size += HEAD
        return size

    def tx_stages_size(self):
        size = 0
        for stage in self.tx_stages:
            size += stage.size()
        return size

    def tx_coords_size(self, include_head=True):
        size = len(self.tx_coords) * 8
        if include_head:
            size += HEAD
        return size

    def size(self, include_head=True):
        size = 0
        if include_head:
            size += HEAD
        if self.vertex_material_ids:
            size += self.vertex_material_ids_size()
        if self.shader_ids:
            size += self.shader_ids_size()
        if self.dcg:
            size += self.dcg_size()
        if self.dig:
            size += self.dig_size()
        if self.scg:
            size += self.scg_size()
        if self.shader_material_ids:
            size += self.shader_material_ids_size()
        if self.tx_stages:
            size += self.tx_stages_size()
        if self.tx_coords:
            size += self.tx_coords_size()
        return size

    def write(self, io_stream):
        write_chunk_head(io_stream, W3D_CHUNK_MATERIAL_PASS,
                         self.size(False), has_sub_chunks=True)

        if self.vertex_material_ids:
            write_chunk_head(io_stream, W3D_CHUNK_VERTEX_MATERIAL_IDS,
                             self.vertex_material_ids_size(False))
            write_array(io_stream, self.vertex_material_ids, write_ulong)

        if self.shader_ids:
            write_chunk_head(io_stream, W3D_CHUNK_SHADER_IDS,
                             self.shader_ids_size(False))
            write_array(io_stream, self.shader_ids, write_ulong)

        if self.dcg:
            write_chunk_head(io_stream, W3D_CHUNK_DCG, self.dcg_size(False))
            for dat in self.dcg:
                dat.write(io_stream)

        if self.dig:
            write_chunk_head(io_stream, W3D_CHUNK_DIG, self.dig_size(False))
            for dat in self.dig:
                dat.write(io_stream)

        if self.scg:
            write_chunk_head(io_stream, W3D_CHUNK_SCG, self.scg_size(False))
            for dat in self.scg:
                dat.write(io_stream)

        if self.shader_material_ids:
            write_chunk_head(io_stream, W3D_CHUNK_SHADER_MATERIAL_ID,
                             self.shader_material_ids_size(False))
            write_array(io_stream, self.shader_material_ids, write_ulong)

        if self.tx_stages:
            for tx_stage in self.tx_stages:
                tx_stage.write(io_stream)

        if self.tx_coords:
            write_chunk_head(io_stream, W3D_CHUNK_STAGE_TEXCOORDS,
                             self.tx_coords_size(False))
            write_array(io_stream, self.tx_coords, write_vector2)