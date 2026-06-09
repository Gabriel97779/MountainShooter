from code.Background import Background
from code.Const import WIN_WIDTH


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'blue1':
                list_blue = []
                for i in range(1, 6):
                    list_blue.append(Background(f'blue1 ({i})', (0,0)))
                    list_blue.append(Background(f'blue1 ({i})', (WIN_WIDTH,0)))
                return list_blue