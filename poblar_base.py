# poblar_base.py
from configuracion import SessionLocal
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

def poblar():
    session = SessionLocal()
    try:
        # 1) Institución
        utpl = Institucion(nombre="UTPL", ciudad="Loja", pais="Ecuador")
        session.add(utpl)
        session.flush()  # asegura id disponible

        # 2) Departamentos
        dsti = Departamento(nombre="Depto. Sistemas y TI", codigo="DSTI", institucion_id=utpl.id)
        dcii = Departamento(nombre="Depto. Ciencias de la Info", codigo="DCII", institucion_id=utpl.id)
        session.add_all([dsti, dcii])
        session.flush()

        # 3) Investigadores
        inv1 = Investigador(
            nombre="Omar",
            apellido="Arevalo",
            email="omar.arevalo@utpl.edu.ec",
            area_investigacion="Redes y Seguridad",
            departamento_id=dsti.id,
        )
        inv2 = Investigador(
            nombre="David",
            apellido="Yanqui",
            email="david.yanqui@utpl.edu.ec",
            area_investigacion="Bases de Datos y ORMs",
            departamento_id=dcii.id,
        )
        session.add_all([inv1, inv2])
        session.flush()

        # 4) Publicaciones
        pub1 = Publicacion(
            titulo="Segmentación de redes seguras en entornos institucionales",
            fecha_publicacion="2024-11-15",
            doi="10.1234/seg-redes-2024",
            tipo_publicacion="Artículo",
            investigador_id=inv1.id,
        )
        pub2 = Publicacion(
            titulo="Buenas prácticas ORM con SQLAlchemy",
            fecha_publicacion="2025-05-03",
            doi="10.5678/orm-sqlalchemy-2025",
            tipo_publicacion="Conferencia",
            investigador_id=inv2.id,
        )
        pub3 = Publicacion(
            titulo="Modelado de datos relacional en proyectos académicos",
            fecha_publicacion="2025-06-20",
            doi=None,
            tipo_publicacion="Tesis",
            investigador_id=inv2.id,
        )
        session.add_all([pub1, pub2, pub3])

        session.commit()
        print("✅ Datos insertados correctamente.")
    except Exception as e:
        session.rollback()
        print("❌ Error insertando datos:", e)
    finally:
        session.close()

if __name__ == "__main__":
    poblar()
