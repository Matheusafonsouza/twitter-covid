from services import CoronaService

corona_service = CoronaService()
corona_info = corona_service.get_info()

print(corona_info)