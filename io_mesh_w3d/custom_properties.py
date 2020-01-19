# <pep8 compliant>
# Written by Stephan Vedder and Michael Schnabel

import bpy
from bpy.props import *
from bpy.types import Panel, Object, Material, PropertyGroup

##########################################################################
# Object
##########################################################################

Object.userText = StringProperty(
    name="User Text",
    description="This is a text defined by the user",
    default="")

Object.object_type = EnumProperty(
    name="Type",
    description="Attributes that define the type of this object",
    items=[
        ('NORMAL', 'Normal', 'desc: just a normal mesh'),
        ('BOX', 'Box', 'desc: this object defines a boundingbox'),
        ('DAZZLE', 'Dazzle', 'desc: todo')],
    default='NORMAL')


class OBJECT_PANEL_PT_w3d(Panel):
    bl_label = "W3D Properties"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(context.active_object, "object_type")
        col = layout.column()
        col.prop(context.active_object, "userText")


##########################################################################
# Material
##########################################################################


Material.attributes = EnumProperty(
    name="attributes",
    description="Attributes that define the behaviour of this material",
    items=[
        ('DEFAULT', 'Default', 'desc: todo', 0),
        ('USE_DEPTH_CUE', 'UseDepthCue', 'desc: todo', 1),
        ('ARGB_EMISSIVE_ONLY', 'ArgbEmissiveOnly', 'desc: todo', 2),
        ('COPY_SPECULAR_TO_DIFFUSE', 'CopySpecularToDiffuse', 'desc: todo', 4),
        ('DEPTH_CUE_TO_ALPHA', 'DepthCueToAlpha', 'desc: todo', 8)],
    default={'DEFAULT'},
    options={'ENUM_FLAG'})

Material.surface_type = EnumProperty(
    name='Surface type',
    description='Describes the surface type for this material',
    items=[
        ('0', 'LightMetal', 'desc: todo'),
        ('1', 'HeavyMetal', 'desc: todo'),
        ('2', 'Water', 'desc: todo'),
        ('3', 'Sand', 'desc: todo'),
        ('4', 'Dirt', 'desc: todo'),
        ('5', 'Mud', 'desc: todo'),
        ('6', 'Grass', 'desc: todo'),
        ('7', 'Wood', 'desc: todo'),
        ('8', 'Concrete', 'desc: todo'),
        ('9', 'Flesh', 'desc: todo'),
        ('10', 'Rock', 'desc: todo'),
        ('11', 'Snow', 'desc: todo'),
        ('12', 'Ice', 'desc: todo'),
        ('13', 'Default', 'desc: todo'),
        ('14', 'Glass', 'desc: todo'),
        ('15', 'Cloth', 'desc: todo'),
        ('16', 'TiberiumField', 'desc: todo'),
        ('17', 'FoliagePermeable', 'desc: todo'),
        ('18', 'GlassPermeable', 'desc: todo'),
        ('19', 'IcePermeable', 'desc: todo'),
        ('20', 'ClothPermeable', 'desc: todo'),
        ('21', 'Electrical', 'desc: todo'),
        ('22', 'Flammable', 'desc: todo'),
        ('23', 'Steam', 'desc: todo'),
        ('24', 'ElectricalPermeable', 'desc: todo'),
        ('25', 'FlammablePermeable', 'desc: todo'),
        ('26', 'SteamPermeable', 'desc: todo'),
        ('27', 'WaterPermeable', 'desc: todo'),
        ('28', 'TiberiumWater', 'desc: todo'),
        ('29', 'TiberiumWaterPermeable', 'desc: todo'),
        ('30', 'UnderwaterDirt', 'desc: todo'),
        ('31', 'UnderwaterTiberiumDirt', 'desc: todo')],
    default='13')


Material.translucency = FloatProperty(
    name="Translucency",
    default=0.0,
    min=0.0, max=1.0,
    description="Translucency property")

Material.vm_args_0 = StringProperty(
    name="vm_args_0",
    description="Vertex Material Arguments 0",
    default="")

Material.vm_args_1 = StringProperty(
    name="vm_args_1",
    description="Vertex Material Arguments 1",
    default="")

Material.technique = IntProperty(
    name="Technique",
    description="Dont know yet",
    default=0,
    min=0,
    max=1)

Material.ambient = FloatVectorProperty(
    name="Ambient",
    subtype='COLOR',
    size=4,
    default=(1.0, 1.0, 1.0, 0.0),
    min=0.0, max=1.0,
    description="Ambient color")

Material.emission = FloatVectorProperty(
    name="Emission",
    subtype='COLOR',
    size=4,
    default=(1.0, 1.0, 1.0, 0.0),
    min=0.0, max=1.0,
    description="Emission color")

Material.opacity = FloatProperty(
    name="Opacity",
    default=0.0,
    min=0.0, max=1.0,
    description="Opacity property")

Material.alpha_test = BoolProperty(
    name="Alpha test",
    description="Enable the alpha test",
    default=False)

Material.blend_mode = IntProperty(
    name="Blend mode",
    description="Which blend mode should be used",
    default=0,
    min=0,
    max=5)

Material.bump_uv_scale = FloatVectorProperty(
    name="Bump UV Scale",
    subtype='TRANSLATION',
    size=2,
    default=(0.0, 0.0),
    min=0.0, max=1.0,
    description="Bump uv scale")

Material.edge_fade_out = IntProperty(
    name="Edge fade out",
    description="TODO",
    default=0,
    min=0,
    max=5)

Material.depth_write = BoolProperty(
    name="Depth write",
    description="Todo",
    default=False)

Material.sampler_clamp_uv_no_mip_0 = FloatVectorProperty(
    name="Sampler clamp UV no MIP 0",
    subtype='TRANSLATION',
    size=3,
    default=(0.0, 0.0, 0.0),
    min=0.0, max=1.0,
    description="Sampler clampU clampV no mipmap 0")

Material.sampler_clamp_uv_no_mip_1 = FloatVectorProperty(
    name="Sampler clamp UV no MIP 1",
    subtype='TRANSLATION',
    size=3,
    default=(0.0, 0.0, 0.0),
    min=0.0, max=1.0,
    description="Sampler clampU clampV no mipmap 1")

Material.num_textures = IntProperty(
    name="NumTextures",
    description="TODO",
    default=0,
    min=0,
    max=5)

Material.texture_0 = StringProperty(
    name="Texture 0",
    description="TODO",
    default="")

Material.texture_1 = StringProperty(
    name="Texture 1",
    description="TODO",
    default="")

Material.secondary_texture_blend_mode = IntProperty(
    name="Secondary texture blend mode",
    description="TODO",
    default=0,
    min=0,
    max=5)

Material.tex_coord_mapper_0 = IntProperty(
    name="TexCoord mapper 0",
    description="TODO",
    default=0,
    min=0,
    max=5)

Material.tex_coord_mapper_1 = IntProperty(
    name="TexCoord mapper 1",
    description="TODO",
    default=0,
    min=0,
    max=5)

Material.tex_coord_transform_0 = FloatVectorProperty(
    name="TexCoord transform 0",
    subtype='TRANSLATION',
    size=4,
    default=(0.0, 0.0, 0.0, 0.0),
    min=0.0, max=1.0,
    description="TODO")

Material.tex_coord_transform_1 = FloatVectorProperty(
    name="TexCoord transform 1",
    subtype='TRANSLATION',
    size=4,
    default=(0.0, 0.0, 0.0, 0.0),
    min=0.0, max=1.0,
    description="TODO")

Material.environment_texture = StringProperty(
    name="Environment texture",
    description="TODO",
    default="")

Material.environment_mult = FloatProperty(
    name="Environment mult",
    default=0.0,
    min=0.0, max=1.0,
    description="Todo")

Material.recolor_texture = StringProperty(
    name="Recolor texture",
    description="TODO",
    default="")

Material.recolor_mult = FloatProperty(
    name="Recolor mult",
    default=0.0,
    min=0.0, max=1.0,
    description="Todo")

Material.use_recolor = BoolProperty(
    name="Use recolor colors",
    description="Todo",
    default=False)

Material.house_color_pulse = BoolProperty(
    name="House color pulse",
    description="Todo",
    default=False)

Material.scrolling_mask_texture = StringProperty(
    name="Scrolling mask texture",
    description="TODO",
    default="")

Material.tex_coord_transform_angle = FloatProperty(
    name="Texture coord transform angle",
    default=0.0,
    min=0.0, max=1.0,
    description="Todo")

Material.tex_coord_transform_u_0 = FloatProperty(
    name="Texture coord transform u 0",
    default=0.0,
    min=0.0, max=1.0,
    description="Todo")

Material.tex_coord_transform_v_0 = FloatProperty(
    name="Texture coord transform v 0",
    default=0.0,
    min=0.0, max=1.0,
    description="Todo")

Material.tex_coord_transform_u_1 = FloatProperty(
    name="Texture coord transform u 0",
    default=0.0,
    min=0.0, max=1.0,
    description="Todo")

Material.tex_coord_transform_v_1 = FloatProperty(
    name="Texture coord transform v 0",
    default=0.0,
    min=0.0, max=1.0,
    description="Todo")

Material.tex_coord_transform_u_2 = FloatProperty(
    name="Texture coord transform u 0",
    default=0.0,
    min=0.0, max=1.0,
    description="Todo")

Material.tex_coord_transform_v_2 = FloatProperty(
    name="Texture coord transform v 0",
    default=0.0,
    min=0.0, max=1.0,
    description="Todo")

Material.tex_ani_fps_NPR_lastFrame_frameOffset_0 = FloatVectorProperty(
    name="TextureAnimation FPS NumPerRow LastFrame FrameOffset 0",
    subtype='TRANSLATION',
    size=4,
    default=(0.0, 0.0, 0.0, 0.0),
    min=0.0, max=1.0,
    description="TODO")

class MATERIAL_PROPERTIES_PANEL_PT_w3d(Panel):
    bl_label = "W3D Properties"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(context.object.active_material, "attributes")
        col = layout.column()
        col.prop(context.object.active_material, "surface_type")
        col = layout.column()
        col.prop(context.object.active_material, "translucency")
        col = layout.column()
        col.prop(context.object.active_material, "vm_args_0")
        col = layout.column()
        col.prop(context.object.active_material, "vm_args_1")
        col = layout.column()
        col.prop(context.object.active_material, "technique")
        col = layout.column()
        col.prop(context.object.active_material, "ambient")
        col = layout.column()
        col.prop(context.object.active_material, "opacity")
        col = layout.column()
        col.prop(context.object.active_material, "alpha_test")
        col = layout.column()
        col.prop(context.object.active_material, "blend_mode")
        col = layout.column()
        col.prop(context.object.active_material, "bump_uv_scale")
        col = layout.column()
        col.prop(context.object.active_material, "edge_fade_out")
        col = layout.column()
        col.prop(context.object.active_material, "depth_write")
        col = layout.column()
        col.prop(context.object.active_material, "sampler_clamp_uv_no_mip_0")
        col = layout.column()
        col.prop(context.object.active_material, "sampler_clamp_uv_no_mip_1")
        col = layout.column()
        col.prop(context.object.active_material, "num_textures")
        col = layout.column()
        col.prop(context.object.active_material, "texture_0")
        col = layout.column()
        col.prop(context.object.active_material, "texture_1")
        col = layout.column()
        col.prop(context.object.active_material, "secondary_texture_blend_mode")
        col = layout.column()
        col.prop(context.object.active_material, "tex_coord_mapper_0")
        col = layout.column()
        col.prop(context.object.active_material, "tex_coord_mapper_1")
        col = layout.column()
        col.prop(context.object.active_material, "tex_coord_transform_0")
        col = layout.column()
        col.prop(context.object.active_material, "tex_coord_transform_1")
        col = layout.column()
        col.prop(context.object.active_material, "environment_texture")
        col = layout.column()
        col.prop(context.object.active_material, "environment_mult")
        col = layout.column()
        col.prop(context.object.active_material, "recolor_texture")
        col = layout.column()
        col.prop(context.object.active_material, "recolor_mult")
        col = layout.column()
        col.prop(context.object.active_material, "use_recolor")
        col = layout.column()
        col.prop(context.object.active_material, "house_color_pulse")
        col = layout.column()
        col.prop(context.object.active_material, "scrolling_mask_texture")
        col = layout.column()
        col.prop(context.object.active_material, "tex_coord_transform_angle")
        col = layout.column()
        col.prop(context.object.active_material, "tex_coord_transform_u_0")
        col = layout.column()
        col.prop(context.object.active_material, "tex_coord_transform_v_0")
        col = layout.column()
        col.prop(context.object.active_material, "tex_coord_transform_u_1")
        col = layout.column()
        col.prop(context.object.active_material, "tex_coord_transform_v_1")
        col = layout.column()
        col.prop(context.object.active_material, "tex_coord_transform_u_2")
        col = layout.column()
        col.prop(context.object.active_material, "tex_coord_transform_v_2")
        col = layout.column()
        col.prop(context.object.active_material, "tex_ani_fps_NPR_lastFrame_frameOffset_0")


##########################################################################
# Material.Shader
##########################################################################


class ShaderProperties(PropertyGroup):
    depth_compare: bpy.props.IntProperty(min=0, max=255)
    depth_mask: bpy.props.IntProperty(min=0, max=255)
    color_mask: bpy.props.IntProperty(min=0, max=255)
    dest_blend: bpy.props.IntProperty(min=0, max=255)
    fog_func: bpy.props.IntProperty(min=0, max=255)
    pri_gradient: bpy.props.IntProperty(min=0, max=255)
    sec_gradient: bpy.props.IntProperty(min=0, max=255)
    src_blend: bpy.props.IntProperty(min=0, max=255)
    texturing: bpy.props.IntProperty(min=0, max=255)
    detail_color_func: bpy.props.IntProperty(min=0, max=255)
    detail_alpha_func: bpy.props.IntProperty(min=0, max=255)
    shader_preset: bpy.props.IntProperty(min=0, max=255)
    alpha_test: bpy.props.IntProperty(min=0, max=255)
    post_detail_color_func: bpy.props.IntProperty(min=0, max=255)
    post_detail_alpha_func: bpy.props.IntProperty(min=0, max=255)


bpy.utils.register_class(ShaderProperties)
Material.shader = PointerProperty(type=ShaderProperties)


class MATERIAL_SHADER_PROPERTIES_PANEL_PT_w3d(Panel):
    bl_label = "W3D Shader Properties"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(context.object.active_material.shader, "depth_compare")
        col = layout.column()
        col.prop(context.object.active_material.shader, "depth_mask")
        col = layout.column()
        col.prop(context.object.active_material.shader, "color_mask")
        col = layout.column()
        col.prop(context.object.active_material.shader, "dest_blend")
        col = layout.column()
        col.prop(context.object.active_material.shader, "fog_func")
        col = layout.column()
        col.prop(context.object.active_material.shader, "pri_gradient")
        col = layout.column()
        col.prop(context.object.active_material.shader, "sec_gradient")
        col = layout.column()
        col.prop(context.object.active_material.shader, "src_blend")
        col = layout.column()
        col.prop(context.object.active_material.shader, "texturing")
        col = layout.column()
        col.prop(context.object.active_material.shader, "detail_color_func")
        col = layout.column()
        col.prop(context.object.active_material.shader, "detail_alpha_func")
        col = layout.column()
        col.prop(context.object.active_material.shader, "shader_preset")
        col = layout.column()
        col.prop(context.object.active_material.shader, "alpha_test")
        col = layout.column()
        col.prop(context.object.active_material.shader,
                 "post_detail_color_func")
        col = layout.column()
        col.prop(context.object.active_material.shader,
                 "post_detail_alpha_func")