CREATE TABLE HD (
    time_in_ms INT NOT NULL AUTO_INCREMENT,
    displacement_in_unit DECIMAL(10, 4),
    force_in_unit DECIMAL(8, 4),
    current_in_unit DECIMAL(5, 3),
    voltage_measurement_in_unit DECIMAL(5, 3),
    voltage_output_in_unit DECIMAL(5, 3),
    pressure_in_unit DECIMAL(8, 4),
    temperature_in_unit DECIMAL(4, 2),
    PRIMARY KEY (time_in_ms)
);

DESCRIBE HD;

SELECT * FROM HD;