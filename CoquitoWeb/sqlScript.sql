-- Tabla de personas (empleados)
CREATE TABLE personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    documento VARCHAR(20) NOT NULL,
    nombres VARCHAR(100),
    apellidos VARCHAR(100),
    correo_electronico VARCHAR(100),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO personas (documento, nombres, apellidos, correo_electronico) VALUES
('12345678', 'Juan', 'Pérez', 'juan.perez@email.com'),
('23456789', 'Ana', 'González', 'ana.gonzalez@email.com'),
('34567890', 'Carlos', 'López', 'carlos.lopez@email.com'),
('45678901', 'María', 'Rodríguez', 'maria.rodriguez@email.com'),
('56789012', 'Luis', 'Martínez', 'luis.martinez@email.com'),
('67890123', 'Patricia', 'Sánchez', 'patricia.sanchez@email.com'),
('78901234', 'David', 'Fernández', 'david.fernandez@email.com'),
('89012345', 'Laura', 'García', 'laura.garcia@email.com'),
('90123456', 'Pedro', 'Ruiz', 'pedro.ruiz@email.com'),
('01234567', 'Sofía', 'Díaz', 'sofia.diaz@email.com'),
('11223344', 'Ricardo', 'Gómez', 'ricardo.gomez@email.com'),
('22334455', 'Marta', 'Jiménez', 'marta.jimenez@email.com'),
('33445566', 'José', 'Vázquez', 'jose.vazquez@email.com'),
('44556677', 'Elena', 'Paredes', 'elena.paredes@email.com'),
('55667788', 'Oscar', 'Castro', 'oscar.castro@email.com'),
('66778899', 'Inés', 'Alvarez', 'ines.alvarez@email.com'),
('77889900', 'Fernando', 'Molina', 'fernando.molina@email.com'),
('88990011', 'Cristina', 'Morales', 'cristina.morales@email.com'),
('99001122', 'Raúl', 'Cruz', 'raul.cruz@email.com');




-- Tabla de dimensiones (como la rueda de la vida, por ejemplo, salud, familia, etc.)
CREATE TABLE dimensiones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT
);

INSERT INTO dimensiones (nombre, descripcion) VALUES
('Trabajo', 'Satisfacción con el entorno laboral y las condiciones de trabajo.'),
('Salud', 'Bienestar físico y emocional de la persona.'),
('Familia', 'Relaciones familiares y la vida en el hogar.'),
('Finanzas', 'Situación económica y estabilidad financiera.'),
('Social', 'Relaciones y actividades sociales fuera del entorno laboral.'),
('Crecimiento Personal', 'Desarrollo personal y profesional.'),
('Tiempo Libre', 'Tiempo dedicado a actividades recreativas y descanso.'),
('Educación', 'Nivel educativo y oportunidades de aprendizaje.'),
('Vivienda', 'Condiciones de la vivienda y el entorno físico.'),
('Comunidad', 'Nivel de satisfacción con la comunidad y entorno social.'),
('Espiritualidad', 'Satisfacción con la vida espiritual o creencias religiosas.'),
('Cultura', 'Involucramiento en actividades culturales y artísticas.'),
('Transporte', 'Satisfacción con las opciones y condiciones del transporte.'),
('Seguridad', 'Nivel de seguridad y protección en el entorno social y personal.'),
('Tecnología', 'Acceso y uso de la tecnología en la vida diaria.'),
('Liderazgo', 'Percepción sobre las capacidades de liderazgo en el entorno laboral.'),
('Autocuidado', 'Prácticas y hábitos de autocuidado personal.'),
('Diversión', 'Nivel de disfrute y satisfacción con actividades recreativas.'),
('Propósito de Vida', 'Sentimiento de tener un propósito claro en la vida.');



-- Tabla de encuestas (respuestas de cada empleado)
CREATE TABLE encuestas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    persona_id INT,
    dimension_id INT,
    puntuacion INT, -- Puntuación de satisfacción de 1 a 5
    fecha_encuesta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (persona_id) REFERENCES personas(id),
    FOREIGN KEY (dimension_id) REFERENCES dimensiones(id)
);

INSERT INTO encuestas (persona_id, dimension_id, puntuacion) VALUES
(1, 1, 4), (1, 2, 3), (1, 3, 4), (1, 4, 5), (1, 5, 3),
(2, 1, 5), (2, 2, 5), (2, 3, 3), (2, 4, 4), (2, 5, 2),
(3, 1, 2), (3, 2, 4), (3, 3, 3), (3, 4, 5), (3, 5, 4),
(4, 1, 3), (4, 2, 2), (4, 3, 5), (4, 4, 3), (4, 5, 5),
(5, 1, 4), (5, 2, 3), (5, 3, 4), (5, 4, 2), (5, 5, 3),
(6, 1, 3), (6, 2, 5), (6, 3, 4), (6, 4, 5), (6, 5, 2),
(7, 1, 4), (7, 2, 3), (7, 3, 3), (7, 4, 5), (7, 5, 4),
(8, 1, 5), (8, 2, 4), (8, 3, 3), (8, 4, 3), (8, 5, 5),
(9, 1, 2), (9, 2, 3), (9, 3, 4), (9, 4, 4), (9, 5, 2),
(10, 1, 3), (10, 2, 2), (10, 3, 5), (10, 4, 3), (10, 5, 4),
(11, 1, 4), (11, 2, 4), (11, 3, 2), (11, 4, 3), (11, 5, 3),
(12, 1, 5), (12, 2, 5), (12, 3, 4), (12, 4, 2), (12, 5, 3),
(13, 1, 3), (13, 2, 3), (13, 3, 4), (13, 4, 5), (13, 5, 5),
(14, 1, 2), (14, 2, 3), (14, 3, 2), (14, 4, 5), (14, 5, 4),
(15, 1, 4), (15, 2, 5), (15, 3, 3), (15, 4, 4), (15, 5, 2),
(16, 1, 3), (16, 2, 4), (16, 3, 5), (16, 4, 2), (16, 5, 4),
(17, 1, 5), (17, 2, 4), (17, 3, 3), (17, 4, 4), (17, 5, 5),
(18, 1, 3), (18, 2, 3), (18, 3, 4), (18, 4, 3), (18, 5, 2),
(19, 1, 4), (19, 2, 2), (19, 3, 5), (19, 4, 4), (19, 5, 3),
(20, 1, 5), (20, 2, 3), (20, 3, 4), (20, 4, 3), (20, 5, 4);
