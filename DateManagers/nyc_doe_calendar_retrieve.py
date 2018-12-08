"""
Description: get NYC DOE calendar using url
             Note: need to get additional modules/update
                pip install pytest-runner
                pip install --upgrade pands
                pip install pdftotree
                pip install pdf2text
                pip install textract>

                <if port outofdate:
                    <update: Command Line Tools>
                    sudo port selfupdate
                >
                sudo port install ImageMagick
"""
import urllib2
import textract
import pdftotree


class NycDoeCalendarRetriever(object):
    def __init__(self, url):
        """

        :param url: str, get Central Calendar link
                    eg: http://proxy.nycboe.org/NR/rdonlyres/3F3B1473-ED7F-4FA9-9616-5C1F83B828B3/0
                    /201819CentralCalendar.pdf
        """
        self.url = url
        self.pdfText = None


if __name__ == "__main__":
    pass