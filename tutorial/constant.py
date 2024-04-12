from database.db import conn
from tutorial.write import display_content_write
from tutorial.write_stream  import display_content_write_stream
from tutorial.magic  import display_content_magic
from tutorial.text_element import display_text_element
from tutorial.dataframe import display_dataframe

class  Tutorial():
    def display_content_write(self):
        display_content_write(conn)

    def display_content_write_stream(self):
        display_content_write_stream(conn)

    def display_content_magic(self):
        display_content_magic(conn)

    def display_text_element(self):
        display_text_element()

    def display_dataframe(self):
        display_dataframe(conn)
