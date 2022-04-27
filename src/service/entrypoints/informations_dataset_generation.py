from src.application.interfaces.report_generator import ReportGenerator
from src.infra.data import data_handler


def generate_reports(topic: str, info_request: ReportGenerator):
    dataframe = data_handler.get_dataframe(topic)
    info_request.generate_info_dataset(dataframe, topic)

        
        


