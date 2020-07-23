import sqlite3

# Connect to databse
conn = sqlite3.connect('HorizonDrive.db')

# Create a cursor 
# Need to pick the units
c.execute("""CREATE TABLE HD (
	    time_in_ms INTEGER PRIMARY KEY,
	    displacement_in_unit REAL,
	    force_in_unit REAL,
	    current_in_unit REAL,
	    voltage_measurement_in_unit REAL,
	    voltage_output_in_unit REAL,
	    pressure_in_unit REAL,
	    temperature_in_unit REAL,
	
	)""")

print("Command executed successfully...")
# INTEGER REAL TEXT BLOB

# Commit the command
conn.commit()

# Close the connection
conn.close()