# https://medium.com/@neonforge/an-amazingly-simple-way-to-store-and-retrieve-numpy-arrays-in-mysql-database-via-png-conversion-in-14901125fbbf
# Steps: Numpy array -> PNG image -> save locally -> convert to binary -> upload to MySQL

import mysql.connector
import os
import numpy as np
from imgarray import save_array_img, load_array_img
from os import fsync

# make sure that data is written to disk, so that buffering doesn’t influence the timings
def sync(fh):
   fh.flush()
   fsync(fh.fileno())
   return True

# convert any given Numpy data set into PNG image. 
# parameters: numpy array name and save path where the new image will be stored
def save_array_to_PNG(numpy_array, save_path):
    with open(save_path, 'wb+') as fh:
        save_array_img(numpy_array, save_path, img_format='png')
        sync(fh)

    return save_path

# convert the image file into binary format, which will be needed for future processing in SQL
def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

# handle the image upload to MySQL database
# but bf this we need to set up the database table with a column for image storage (column type = Blob)
def insertBLOB(png_image):
    try:
        connection = mysql.connector.connect(
            user='Your_user_name',
            password='Your_MySQL_password',
            host='host_address',
            database='database_name')

        sql_table = 'your_table_name'
        image_column_name = 'your_blob_column_name'

        file = convertToBinaryData(png_image)

        cursor = connection.cursor()
        sql_insert_blob_query = "INSERT INTO " + sql_table + " (" + image_column_name + ") VALUES (" + file + ")"
        result = cursor.execute(sql_insert_blob_query)
        connection.commit()

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# write Numpy array into MySQL database
my_numpy_array = np.ones(150,150)
insertBLOB(save_array_to_PNG(my_numpy_array, 'image.png'))