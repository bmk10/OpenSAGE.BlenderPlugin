# <pep8 compliant>
# Written by Stephan Vedder and Michael Schnabel
# Last Modification 11.2019

from mathutils import Vector

from io_mesh_w3d.structs.struct import Struct, HEAD
from io_mesh_w3d.import_utils_w3d import skip_unknown_chunk
from io_mesh_w3d.io_binary import *


W3D_CHUNK_AABBTREE_HEADER = 0x00000091


class AABBTreeHeader(Struct):
    node_count = 0
    poly_count = 0  # num tris of mesh

    @staticmethod
    def read(io_stream):
        result = AABBTreeHeader(
            node_count=read_ulong(io_stream),
            poly_count=read_ulong(io_stream))

        io_stream.read(24)  # padding
        return result

    @staticmethod
    def size(include_head=True):
        size = 8
        if include_head:
            size += HEAD
        return size

    def write(self, io_stream):
        write_chunk_head(io_stream, W3D_CHUNK_AABBTREE_HEADER,
                         self.size(False))
        write_ulong(io_stream, self.node_count)
        write_ulong(io_stream, self.poly_count)

        for pad in range(24):
            write_ubyte(io_stream, 0)  # padding


class AABBTreeNode(Struct):
    min = Vector((0.0, 0.0, 0.0))
    max = Vector((0.0, 0.0, 0.0))
    front_or_poly_0 = 0
    back_or_poly_count = 0

    @staticmethod
    def read(io_stream):
        return AABBTreeNode(
            min=read_vector(io_stream),
            max=read_vector(io_stream),
            front_or_poly_0=read_long(io_stream),
            back_or_poly_count=read_long(io_stream))

    @staticmethod
    def size():
        return 32

    def write(self, io_stream):
        write_vector(io_stream, self.min)
        write_vector(io_stream, self.max)
        write_long(io_stream, self.front_or_poly_0)
        write_long(io_stream, self.back_or_poly_count)


W3D_CHUNK_AABBTREE = 0x00000090
W3D_CHUNK_AABBTREE_POLYINDICES = 0x00000092
W3D_CHUNK_AABBTREE_NODES = 0x00000093


class AABBTree(Struct):
    header = AABBTreeHeader()
    poly_indices = []
    nodes = []

    @staticmethod
    def read(context, io_stream, chunk_end):
        result = AABBTree()

        while io_stream.tell() < chunk_end:
            (chunk_type, chunk_size, subchunk_end) = read_chunk_head(io_stream)

            if chunk_type == W3D_CHUNK_AABBTREE_HEADER:
                result.header = AABBTreeHeader.read(io_stream)
            elif chunk_type == W3D_CHUNK_AABBTREE_POLYINDICES:
                result.poly_indices = read_array(
                    io_stream, subchunk_end, read_long)
            elif chunk_type == W3D_CHUNK_AABBTREE_NODES:
                result.nodes = read_array(
                    io_stream, subchunk_end, AABBTreeNode.read)
            else:
                skip_unknown_chunk(context, io_stream, chunk_type, chunk_size)
        return result

    def poly_indices_size(self, include_head=True):
        size = len(self.poly_indices) * 4
        if include_head:
            size += HEAD
        return size

    def nodes_size(self, include_head=True):
        size = 0
        if include_head:
            size += HEAD
        for node in self.nodes:
            size += node.size()
        return size

    def size(self, include_head=True):
        size = 0
        if include_head:
            size += HEAD
        size += self.header.size()
        if self.poly_indices:
            size += self.poly_indices_size()
        if self.nodes:
            size += self.nodes_size()
        return size

    def write(self, io_stream):
        write_chunk_head(io_stream, W3D_CHUNK_AABBTREE,
                         self.size(False), has_sub_chunks=True)
        self.header.write(io_stream)

        if self.poly_indices:
            write_chunk_head(io_stream, W3D_CHUNK_AABBTREE_POLYINDICES,
                             self.poly_indices_size(False))
            write_array(io_stream, self.poly_indices, write_long)
        if self.nodes:
            write_chunk_head(
                io_stream, W3D_CHUNK_AABBTREE_NODES, self.nodes_size(False))
            for node in self.nodes:
                node.write(io_stream)
