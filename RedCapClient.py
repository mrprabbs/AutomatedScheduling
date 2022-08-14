from redcap import Project


def setup_client(api_key, api_url):
    """
    Static method to initialize the REDCap project with the api key/url. Utilizes the Pycap python wrapper

    Parameters
    ---------
    api_url: str
        url for REDCap API that is required to access that API
    api_key: str
        key for REDCAP API that is required to access that API
    """
    project = Project(api_key, api_url)
    return project


class RedCapClient:
    """
    Client class to interact with REDCap API
    """
    def __init__(self, api_url, api_key):
        """
        construct REDCap project object using Pycap python wrapper

        Parameters
        ----------
        calendar_id: str
           Identification code for specific calendar that has interviewer availability
       """
        self.project = setup_client(api_url, api_key)

    def getGeneralAvailability(self):
        """
        Function to export General Availability report from REDCap project
        """
        # pd.set_option("display.max_columns", 1000)
        # report id: 20033 = general availability
        data = self.project.export_report(report_id="20033", format_type="json")
        return data

    # def exportInterviewRecord(self):
    #     # report id: 20011 = "Scheduled Interviews"
    #     data = self.project.export_report(report_id="20011", format_type="json")
    #     return data
