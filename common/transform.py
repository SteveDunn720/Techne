
import maya.cmds as mc

class Transform:
    def __init__(self, input):
        if not mc.objExists(input):
            raise ValueError(f"{input} does not exist")
        self.input = input
        if isinstance(input, list):
            print('vert list not supported yet')
        else:
            self.type = mc.nodeType(input)

    def get_all_transform_data(self, world_space=True):
        '''
        gets all transform data

        input: Strig or List // What you want to get the translate of / use an string for an object in your scene, then a list for a series of verts, cvs, etc.
        WS_translate:bool // Worldspace or Local translation
        WS_orientation:bool // Worldspace or Local orientation

        returns 
        self.pos // postion of the input
        self.rot // oreint of the input
        '''
        self.get_translation(world_space=world_space)
        self.get_orientation(world_space=world_space)
        return self.pos, self.rot,

    def get_translation(self, world_space:bool=True):
        '''
        gets translation data

        input: Strig or List // What you want to get the translate of / use an string for an object in your scene, then a list for a series of verts, cvs, etc.
        world_space:bool // Worldspace or Local translation

        returns 
        self.pos // postion of the inputs
        '''

        if world_space:
            self.pos = mc.xform(self.input, query=True, translation=True, worldSpace=True)
        else:
            self.pos = list(mc.getAttr(f"{self.input}.translate")[0])

        return self.pos

    def get_orientation(self, world_space:bool=True):
        '''
        gets orientation data

        input: Strig or List // What you want to get the orient of / use an string for an object in your scene, then a list for a series of verts, cvs, etc.
        world_space:bool // Worldspace or Local translation

        returns 
        self.rot // postion of the input
        '''

        if world_space:
            self.rot = mc.xform(self.input, query=True, rotation=True, worldSpace=True)
        else:
            self.rot = list(mc.getAttr(f"{self.input}.rotate")[0])

        return self.rot
    
    def get_matrix(self, world_space=True):
        return mc.xform(self.node, q=True, m=True, ws=world_space)

    def set_translation(self, target:str=None, freeze:bool=False):
        pass

    def set_orientation(self, target:str=None, freeze:bool=False, type:bool=False):
        pass

    def match(self, target:str=None, translate:bool=True, oreint:bool=True, input_type:bool=False, freeze=False):
        pass

    
    