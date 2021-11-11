import settings
from services import CoronaService

corona_service = CoronaService()
corona_brazil_info = corona_service.get_info('brazil')
corona_world_info = corona_service.get_info()

print(corona_brazil_info)
print(corona_world_info)